# Customer Churn Prediction Dashboard - Day 4

## Project Overview

This project presents a comprehensive solution for predicting customer churn using advanced machine learning techniques combined with interactive data visualization. The primary objective is to identify customers at risk of discontinuing their services, enabling proactive retention strategies.

## Executive Summary

The **Customer Churn Prediction** initiative integrates predictive analytics with business intelligence to transform raw customer data into actionable insights. By analyzing key behavioral and demographic patterns, this system provides accurate churn predictions that empower data-driven decision-making across the organization.

### Key Project Components

- **Dataset**: Customer Churn Dataset containing ~7,000+ customer records with 20+ attributes
- **Predictive Model**: Gradient Boosting Classifier with optimized hyperparameters
- **Technology Stack**: Python, scikit-learn, Pandas, NumPy, Gradio
- **Visualization**: Interactive Power BI dashboard for comprehensive analytics

---

## Dashboard Insights & Analysis Report

### Customer Base Composition

Based on the dashboard analytics:

- **Total Active Customers**: ~7,000+ accounts tracked
- **Churn Rate**: Approximately 26-27% of customers show churn indicators
- **Retention Rate**: 73-74% of customers remain loyal to the service

### Key Performance Metrics

#### Demographic Patterns
- **Gender Distribution**: Relatively balanced between male and female customers
- **Senior Citizens**: Represent ~16% of the customer base, with higher churn propensity
- **Partner Status**: Customers with partners show 20% lower churn rates compared to singles
- **Dependents**: Family status significantly impacts retention rates

#### Service Utilization Insights
- **Tenure Impact**: 80% of churned customers leave within their first 12 months
- **Internet Service Type**: 
  - Fiber Optic users show 42% churn rate (highest)
  - DSL users maintain 19% churn rate (more stable)
- **Contract Type**: 
  - Month-to-month contracts: 42% churn rate
  - One-year contracts: 11% churn rate
  - Two-year contracts: 3% churn rate

#### Revenue Patterns
- **Monthly Charges**: Higher-tier customers ($65+/month) display increased churn
- **Total Charges**: Cumulative spend correlates inversely with churn probability
- **Payment Method**: Electronic check payment holders show 45% higher churn vs. automatic methods

#### Support Engagement
- **Tech Support Service**: Adoption reduces churn by 29%
- **Admin Tickets**: High ticket volumes indicate dissatisfaction and predict churn
- **Online Security Features**: Adoption correlates with 40% lower churn rates

---

## Technical Architecture

### Data Pipeline

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Predictions
```

### Custom Preprocessing Transformer

The `ChurnPreprocessingTransformer` class handles:
- Column name normalization (lowercase, underscore formatting)
- String value standardization across categorical features
- Missing value imputation using statistical methods
- Categorical encoding for model consumption
- Feature alignment with training data specifications

### Model Specifications

**Algorithm**: Gradient Boosting Classifier
- **Purpose**: Binary classification (Churn / No Churn)
- **Input Features**: 20 customer attributes
- **Output**: Churn probability and prediction label

**Key Parameters**:
- Handles non-linear relationships in customer behavior
- Provides probability estimates for risk stratification
- Optimized for balanced performance across both classes

---

## Usage Instructions

### Running the Interactive Prediction Interface

The application provides a user-friendly Gradio interface for real-time predictions:

```bash
python app.py
```

**Features**:
- Input customer profile information through intuitive controls
- Receive instant churn predictions with confidence scores
- View probability estimates for both outcomes
- No technical expertise required

### Input Parameters

**Customer Demographics**:
- Gender (Female/Male)
- Senior Citizen Status (0/1)
- Partner Status (Yes/No)
- Dependents (Yes/No)

**Service Profile**:
- Tenure in months (0-72)
- Phone Service (Yes/No)
- Multiple Lines (Yes/No/No phone service)
- Internet Service Type (DSL/Fiber optic/No)
- Add-on Services (Security, Backup, Protection, Tech Support, etc.)

**Billing Information**:
- Monthly Charges ($)
- Total Charges ($)
- Contract Type (Month-to-month/One year/Two year)
- Payment Method (Electronic/Bank/Credit/Mail)

**Support Metrics**:
- Number of Admin Tickets
- Number of Tech Tickets

### Output Interpretation

The model returns three predictions:
1. **Churn Status**: Binary prediction (Churn/No Churn)
2. **No-Churn Probability**: Confidence score for retention (0.00-1.00)
3. **Churn Probability**: Confidence score for churn risk (0.00-1.00)

---

## Files & Resources

| File | Description |
|------|-------------|
| `app.py` | Main application with Gradio interface and prediction logic |
| `Customer Churn Dashboard.pbix` | Power BI dashboard for visual analytics |
| `Customer Churn Dashboard.png` | Dashboard screenshot for quick reference |
| `02 Customer Churn-Dataset.xlsx` | Complete customer dataset with all attributes |
| `LICENSE.txt` | MIT License for open-source usage |
| `data/` | Directory for processed data files |
| `model/` | Directory for trained model artifacts |

---

## Key Findings & Recommendations

### High-Risk Churn Indicators
1. **New customers** within first 3 months show 35% higher churn
2. **Fiber Optic internet** subscribers require targeted retention
3. **Month-to-month contracts** need proactive engagement
4. **Electronic check payments** correlate with service dissatisfaction

### Recommended Actions
- Implement 90-day onboarding excellence program for new customers
- Incentivize annual or bi-annual contract upgrades
- Promote automatic payment methods with discount incentives
- Increase tech support availability for high-churn service types
- Develop service bundling strategies to increase customer lifetime value

---

## Technical Requirements

### Dependencies
- Python 3.7+
- pandas
- numpy
- scikit-learn
- joblib
- gradio

### Installation
```bash
pip install pandas numpy scikit-learn joblib gradio
```

---

## Data Privacy & Compliance

This project adheres to data privacy best practices:
- Customer data is processed securely
- Predictions are used solely for service improvement
- No sensitive information is stored unnecessarily
- All processing complies with GDPR and similar standards

---

## Future Enhancements

- Integration of real-time customer data streams
- Advanced feature engineering with customer lifetime value modeling
- Ensemble methods combining multiple algorithms
- Automated alert system for high-risk customer segments
- API deployment for enterprise systems integration

---

## License

This project is released under the **MIT License**. See `LICENSE.txt` for full details.

---

## Contact & Support

For questions, suggestions, or technical support regarding this analysis and predictive model, please reach out to the project maintainers.

---

**Project Developed By**: Mayank Gariya  
**Series**: Asking Great Questions Series  
**Date**: May 2026  
**Status**: Production Ready

*This analysis represents a practical approach to data science and business intelligence, demonstrating how predictive analytics can drive meaningful business outcomes.*

---
