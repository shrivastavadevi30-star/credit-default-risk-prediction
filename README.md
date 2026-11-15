# Credit Default Risk Prediction System Using Machine Learning

## 1. Project Overview
This project develops a Machine Learning-based system to predict the possibility of credit card payment default using customer financial and repayment information.

The system uses historical credit card data and classification algorithms to estimate whether a customer may default on their next payment.

## 2. Objectives
- To analyze credit card customer data.
- To perform data cleaning and preprocessing.
- To train Machine Learning classification models.
- To compare model performance.
- To develop a simple web application for prediction.

## 3. Dataset
The project uses the **Default of Credit Card Clients Dataset** from the UCI Machine Learning Repository.

- Total records after cleaning: 29,965
- Input features: 23
- Target variable: Y
- Target classes:
  - 0: No default
  - 1: Default

**Note:** The dataset represents credit card clients in Taiwan. The model is developed for educational purposes and is not validated for real-world credit decisions.

## 4. Technologies Used
- Python
- Google Colab
- Pandas and NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib
- GitHub

## 5. Machine Learning Algorithms
1. Logistic Regression
2. Random Forest Classifier

Logistic Regression was selected as the final model because it achieved better recall and F1-score for the default class.

## 6. Model Performance

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 68.26% | 81.09% |
| Default Precision | 37% | 64% |
| Default Recall | 63% | 33% |
| Default F1-score | 47% | 44% |

## 7. Project Files
- `Credit_Default_Risk_Prediction.ipynb` – Machine Learning notebook
- `app.py` – Streamlit web application
- `best_credit_default_model.pkl` – Trained model
- `requirements.txt` – Required Python packages

## 8. Conclusion
The project demonstrates how Machine Learning can be used to estimate credit card default risk. Two classification algorithms were trained and compared. Logistic Regression was selected based on its ability to identify a greater proportion of actual default cases.

## 9. Disclaimer
This project is developed for academic and educational purposes only. Predictions should not be used as the sole basis for real financial or credit decisions.
