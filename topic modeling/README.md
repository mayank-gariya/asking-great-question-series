# Topic Modeling: A Comprehensive Guide

## Overview

This directory contains a complete implementation of **Topic Modeling**, a powerful natural language processing technique used to discover abstract topics within a collection of documents. This project demonstrates the application of topic modeling on Amazon Fine Food Reviews dataset to identify and extract meaningful topics from customer feedback.

## 📚 Contents

### Files in This Repository

- **`Topic Modeling _ A comprehensive guide.pdf`** - Detailed theoretical documentation covering topic modeling concepts, methodologies, and best practices
- **`topic-modeling.ipynb`** - Jupyter Notebook with end-to-end implementation including:
  - Data loading and exploratory data analysis
  - Text preprocessing and cleaning
  - Dictionary and corpus creation
  - LDA (Latent Dirichlet Allocation) model training
  - Coherence score evaluation
  - Topic extraction and visualization

- **`app.py`** - Streamlit application for interactive topic visualization
- **`amazon_topics_visualization.html`** - Pre-generated interactive visualization of discovered topics

## 🎯 Key Features

### Data Processing
- Handles large-scale Amazon Fine Food Reviews dataset (568,454+ reviews)
- Advanced text preprocessing including:
  - HTML tag removal
  - Lowercasing and tokenization
  - Lemmatization using NLTK WordNetLemmatizer
  - Stopword removal
  
### Topic Modeling
- **Algorithm**: Latent Dirichlet Allocation (LDA)
- **Number of Topics**: 5 topics identified from customer reviews
- **Coherence Score**: 0.40 (C_V metric)
- Topics discovered include:
  - **Topic 0**: Snacks & Chips (flavor, taste, snacks)
  - **Topic 1**: Coffee & Breakfast Items (coffee, pancake, mix)
  - **Topic 2**: General Products (product, price, delivery)
  - **Topic 3**: Chocolate & Hot Beverages (chocolate, hot water)
  - **Topic 4**: Pet Food (dog, food, organic)

### Interactive Visualization
An **interactive Streamlit application** is available for exploring the topic model:
🔗 **Live Demo**: [Machine Learning Practices - Topic Modeling App](https://machinelearningpractices-tin2nnb4i7mtmbw6uduoeg.streamlit.app/)

The app provides:
- Interactive topic exploration
- Word frequency analysis within topics
- Document-topic distributions
- Real-time topic visualization

## 📊 Dataset

**Source**: Amazon Fine Food Reviews  
**Records**: 568,454 reviews  
**Sample Size Used**: 50,000 reviews for modeling  
**Features**:
- Rating (1-5 stars)
- Summary
- Review Text

## 🛠️ Technologies & Libraries

- **Python 3.7+**
- **Data Processing**: Pandas, NumPy
- **NLP**: NLTK, Gensim
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Web App**: Streamlit
- **Machine Learning**: Gensim LdaModel, CoherenceModel

## 📖 Usage

### Running the Jupyter Notebook

```bash
jupyter notebook topic-modeling.ipynb
```

The notebook provides step-by-step implementation with detailed comments and visualizations.

### Running the Streamlit App Locally

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Accessing the Online Demo

Visit: [https://machinelearningpractices-tin2nnb4i7mtmbw6uduoeg.streamlit.app/](https://machinelearningpractices-tin2nnb4i7mtmbw6uduoeg.streamlit.app/)

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Number of Unique Tokens | 3,299 |
| Documents in Corpus | 5,000 |
| Number of Topics | 5 |
| LDA Passes | 10 |
| Coherence Score (C_V) | 0.40 |

## 🔍 Key Insights

1. **Topic Diversity**: The model successfully identified distinct topics across snacks, beverages, and pet food categories
2. **Quality Metrics**: Coherence score of 0.40 indicates good semantic coherence between words within topics
3. **Scalability**: Process can handle large datasets efficiently with sampling strategies
4. **Interpretability**: Topics are highly interpretable with meaningful keyword associations

## 📝 Methodology

### Text Preprocessing Pipeline
1. HTML tag removal
2. Lowercasing and special character removal
3. Tokenization
4. Lemmatization
5. Stopword filtering

### Model Training
- **Algorithm**: Latent Dirichlet Allocation (LDA)
- **Hyperparameters**:
  - Number of topics: 5
  - Training passes: 10
  - Random state: 42 (for reproducibility)

### Evaluation
- **Coherence Model**: Used C_V metric to evaluate topic quality
- **Interpretability**: Manual review of top keywords per topic

## 🎓 Learning Resources

This project demonstrates:
- Advanced NLP techniques
- Large-scale text processing
- Machine learning model evaluation
- Interactive data visualization
- Production-ready web application deployment

## 📧 Contact & Support

For questions, suggestions, or collaborations related to this topic modeling project, please feel free to reach out.

## 📄 License

This project is provided for educational and research purposes.

---

**Last Updated**: June 2026  
**Repository**: [mayank-gariya/asking-great-question-series](https://github.com/mayank-gariya/asking-great-question-series)
