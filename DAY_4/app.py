
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import joblib
import gradio as gr


class ChurnPreprocessingTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, some_features, mask, X_train_cols, categorical_cols_to_map):
        self.some_features = some_features
        self.mask = mask
        self.X_train_cols = X_train_cols
        self.categorical_cols_to_map = categorical_cols_to_map
        self.median_totalcharges = None

    def fit(self, X, y=None):
        X_copy = X.copy()
        X_copy.columns = X_copy.columns.str.lower().str.replace(' ', '_')

        if 'totalcharges' in X_copy.columns:
            X_copy['totalcharges'] = pd.to_numeric(X_copy['totalcharges'], errors='coerce')
            self.median_totalcharges = X_copy['totalcharges'].median()
        return self

    def transform(self, X, y=None):
        X_transformed = X.copy()
        X_transformed.columns = X_transformed.columns.str.lower().str.replace(' ', '_')

        if 'customerid' in X_transformed.columns:
            X_transformed = X_transformed.drop(columns='customerid')

        general_string_replacements = {
            'no phone service': 'no',
            'no internet service': 'no',
            'month-to-month': 'monthly'
        }

        cols_for_replacements = ['multiplelines', 'contract'] + self.some_features

        for col in cols_for_replacements:
            if col in X_transformed.columns and X_transformed[col].dtype == 'object':
                # Ensure we are only applying to string-like data
                X_transformed[col] = X_transformed[col].astype(str).str.lower().replace(general_string_replacements)

        if 'paymentmethod' in X_transformed.columns and X_transformed['paymentmethod'].dtype == 'object':
            X_transformed['paymentmethod'] = X_transformed['paymentmethod'].astype(str).apply(lambda x: x.split(' ')[0]).replace({'Mailed': 'Mail'})

        if 'totalcharges' in X_transformed.columns:
            X_transformed['totalcharges'] = pd.to_numeric(X_transformed['totalcharges'], errors='coerce')
            X_transformed['totalcharges'] = X_transformed['totalcharges'].fillna(self.median_totalcharges)

        for col in self.categorical_cols_to_map:
            if col in X_transformed.columns and X_transformed[col].dtype == 'object':
                X_transformed[col] = X_transformed[col].map(self.mask).fillna(X_transformed[col])

        for col in self.X_train_cols:
            if col in X_transformed.columns:
                X_transformed[col] = pd.to_numeric(X_transformed[col], errors='coerce')
                X_transformed[col] = X_transformed[col].fillna(0)

        X_final = X_transformed.reindex(columns=self.X_train_cols, fill_value=0)

        return X_final


# Define the variables needed for the transformer (from previous steps)
some_features = ['onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport', 'streamingtv', 'streamingmovies']
mask = {
    'Yes': 1,
    'No': 0,
    'monthly': 0,
    'One year': 1,
    'Two year': 2,
    'Electronic': 0,
    'Bank': 1,
    'Credit': 2,
    'Mail': 3,
    'DSL': 1,
    'Fiber optic': 2,
    'Male': 1,
    'Female': 0
}
categorical_cols_to_map = [
    'gender', 'partner', 'dependents', 'phoneservice', 'multiplelines',
    'internetservice', 'onlinesecurity', 'onlinebackup', 'deviceprotection',
    'techsupport', 'streamingtv', 'streamingmovies', 'contract',
    'paperlessbilling', 'paymentmethod'
]

# Assuming X_train_no_transform.columns is available from the notebook state
X_train_cols_for_pipeline = X_train_no_transform.columns

# Load the saved pipeline
pipeline_filename = 'churn_prediction_pipeline_v2.joblib'
loaded_pipeline = joblib.load(pipeline_filename)

# Prediction function for Gradio
def predict_churn(
    gender, seniorcitizen, partner, dependents, tenure, phoneservice,
    multiplelines, internetservice, onlinesecurity, onlinebackup,
    deviceprotection, techsupport, streamingtv, streamingmovies, contract,
    paperlessbilling, paymentmethod, monthlycharges, totalcharges,
    numadmintickets, numtechtickets
):
    # Create a DataFrame from the input data, matching the original raw data structure
    input_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [int(seniorcitizen)], # Convert '0'/'1' string to int
        'Partner': [partner],
        'Dependents': [dependents],
        'tenure': [tenure],
        'PhoneService': [phoneservice],
        'MultipleLines': [multiplelines],
        'InternetService': [internetservice],
        'OnlineSecurity': [onlinesecurity],
        'OnlineBackup': [onlinebackup],
        'DeviceProtection': [deviceprotection],
        'TechSupport': [techsupport],
        'StreamingTV': [streamingtv],
        'StreamingMovies': [streamingmovies],
        'Contract': [contract],
        'PaperlessBilling': [paperlessbilling],
        'PaymentMethod': [paymentmethod],
        'MonthlyCharges': [monthlycharges],
        'TotalCharges': [str(totalcharges)], # Keep as string, transformer will convert
        'numAdminTickets': [numadmintickets],
        'numTechTickets': [numtechtickets]
    })

    # Make prediction using the loaded pipeline
    prediction = loaded_pipeline.predict(input_data)[0]
    prediction_proba = loaded_pipeline.predict_proba(input_data)[0]

    churn_status = "Churn" if prediction == 1 else "No Churn"
    confidence_no_churn = f"{prediction_proba[0]:.2f}"
    confidence_churn = f"{prediction_proba[1]:.2f}"

    return f"Prediction: {churn_status}", f"Probability (No Churn): {confidence_no_churn}", f"Probability (Churn): {confidence_churn}"


# Define Gradio Interface inputs
inputs = [
    gr.Radio(["Female", "Male"], label="Gender"),
    gr.Radio(["0", "1"], label="Senior Citizen"),
    gr.Radio(["Yes", "No"], label="Partner"),
    gr.Radio(["Yes", "No"], label="Dependents"),
    gr.Slider(minimum=0, maximum=72, step=1, label="Tenure (months)", value=24),
    gr.Radio(["Yes", "No"], label="Phone Service"),
    gr.Radio(["No phone service", "No", "Yes"], label="Multiple Lines"),
    gr.Radio(["DSL", "Fiber optic", "No"], label="Internet Service"),
    gr.Radio(["Yes", "No", "No internet service"], label="Online Security"),
    gr.Radio(["Yes", "No", "No internet service"], label="Online Backup"),
    gr.Radio(["Yes", "No", "No internet service"], label="Device Protection"),
    gr.Radio(["Yes", "No", "No internet service"], label="Tech Support"),
    gr.Radio(["Yes", "No", "No internet service"], label="Streaming TV"),
    gr.Radio(["Yes", "No", "No internet service"], label="Streaming Movies"),
    gr.Radio(["Month-to-month", "One year", "Two year"], label="Contract"),
    gr.Radio(["Yes", "No"], label="Paperless Billing"),
    gr.Dropdown(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], label="Payment Method"),
    gr.Slider(minimum=18.25, maximum=118.75, step=0.05, label="Monthly Charges", value=70.0),
    gr.Number(label="Total Charges", value=1680.0),
    gr.Slider(minimum=0, maximum=5, step=1, label="Number of Admin Tickets", value=0),
    gr.Slider(minimum=0, maximum=9, step=1, label="Number of Tech Tickets", value=0)
]

# Define Gradio Interface outputs
outputs = [
    gr.Textbox(label="Prediction"),
    gr.Textbox(label="Probability (No Churn)"),
    gr.Textbox(label="Probability (Churn)")
]

# Create and launch the Gradio interface
iface = gr.Interface(
    fn=predict_churn,
    inputs=inputs,
    outputs=outputs,
    title="Customer Churn Prediction",
    description="Enter customer details to predict if they will churn. Uses a Gradient Boosting Classifier model."
)

iface.launch(debug=True, share=True)
