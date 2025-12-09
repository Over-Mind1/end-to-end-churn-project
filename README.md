````markdown
# 🏦 End-to-End Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![ML](https://img.shields.io/badge/XGBoost-CatBoost-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

This project is a complete **Churn Prediction System** built with **FastAPI**, **XGBoost**, and **CatBoost**. It exposes a REST API endpoint that accepts customer data and returns the probability of the customer exiting the bank (churning).

The system includes a full machine learning lifecycle: from data preprocessing and feature engineering to model tuning and deployment.

---

## 📖 Table of Contents
- [Business Context](#-business-context)
- [Project Architecture](#-project-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Model & Pipeline Details](#-model--pipeline-details)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 Business Context

**The Problem:** Customer churn is a critical metric for banks. Retaining existing customers is often more cost-effective than acquiring new ones. In this project, we treat churn as a **Binary Classification Problem**.

- **Target Variable:** `exited` (1 = Customer left, 0 = Customer stayed).
- **Goal:** Predict customer behaviors and attributes that lead to account closure.
- **Metric:** Due to the imbalanced nature of churn data, we focus primarily on the **F1-Score** to balance precision and recall.

**Dataset Reference:** [Kaggle - Churn Modelling](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)

---

## 🏗 Project Architecture

The pipeline consists of offline training (preprocessing, Optuna tuning, SHAP selection) and online inference (FastAPI validation and prediction).

![Project Architecture](end-to-end-churn-project/assests/arch.png)

---

## 📂 Project Structure

```text
.
├── data
│   ├── raw
│   │   └── churn-data.csv          # Original dataset
│   └── processed
│       └── churn-data-features.csv # Data after feature engineering
│
├── models
│   ├── preprocessor
│   │   └── preprocessor.pkl        # Saved ColumnTransformer
│   ├── catboost
│   │   ├── model.pkl               # Trained CatBoost model
│   │   └── checkpoint.cbs
│   └── xgb
│       ├── model.pkl               # Trained XGBoost model
│       └── checkpoint.json
│
├── utils
│   ├── config.py                   # Configuration variables
│   ├── CustomerData.py             # Pydantic schemas for validation
│   ├── FeatureEngineering.py       # Custom transformation logic
│   ├── inference.py                # Prediction logic
│   └── __init__.py
│
├── Notebooks
│   ├── EDA.ipynb                   # Exploratory Data Analysis
│   └── pipline.ipynb               # Training, Tuning (Optuna), and SHAP
│
├── assests/                        # Images and diagrams
├── main.py                         # FastAPI application entry point
├── README.md
└── requirements.txt                # Project dependencies
````

-----

## ⚙️ Installation

### 1\. Clone the Repository

```bash
git clone [https://github.com/Over-Mind1/end-to-end-churn-project.git](https://github.com/Over-Mind1/end-to-end-churn-project.git)
cd end-to-end-churn-project
```

### 2\. Create a Virtual Environment

**Linux / Mac:**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

-----

## 🚀 Usage

### Running the API Server

To start the FastAPI server locally:

```bash
# If main.py is in the root directory:
uvicorn main:app --reload

# If using the specific app module structure:
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### Accessing Documentation

FastAPI provides automatic interactive documentation. Once the server is running, visit:

  * **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  * **ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

-----

## 🔌 API Documentation

### POST `/predict_churn/`

Receives customer data and returns the churn probability.

#### Request Body Example

```json
{
  "CreditScore": 585,
  "Geography": "France",
  "Gender": "Male",
  "Age": 36,
  "Tenure": 7,
  "Balance": 0.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 0,
  "EstimatedSalary": 94283.09
}
```

#### Response Example

```json
{
  "prediction": {
    "CatBoost_probability": 0.9535,
    "XGBoost_probability": 0.9333,
    "Status": "Exited (Churn)"
  }
}
```

> **Note on Logic:**
>
>   * **XGBoost Threshold:** \> 0.7 is considered Churn.
>   * **CatBoost Threshold:** \> 0.5 is considered Churn.

-----

## 🧪 Model & Pipeline Details

The project utilizes `sklearn.pipeline` to ensure reproducibility between training and production.

1.  **Preprocessing:**
      * **Numerical:** SimpleImputer (Median).
      * **Categorical:** SimpleImputer (Most Frequent) + OneHotEncoder.
2.  **Feature Engineering:** Custom logic applied before the preprocessor.
3.  **Feature Selection:** Top features selected via **SHAP** values.
4.  **Tuning:** Hyperparameters optimized using **Optuna**.

-----

## 🤝 Contributing

Contributions are welcome\! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

-----

## 📝 License

This project is licensed under the **MIT License**.

-----

## ⭐ Acknowledgment

  * Dataset provided by [Shruti\_Iyyer on Kaggle](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling).
  * Special thanks to the open-source communities behind FastAPI, Scikit-Learn, and XGBoost.

<!-- end list -->

```
```