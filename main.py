from fastapi import FastAPI
from utils.CustomerData import CustomerData
from utils.inference import predict_churn
from utils.config import VERSION, APP_NAME

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,description="API for predicting customer churn using XGBoost and CatBoost models.",version=VERSION # type: ignore
)
@app.get("/")
def root():
    return {"status": "API is running"}

@app.post("/predict_churn/", tags=["Prediction"])
def predict_churn_endpoint(data: CustomerData, model_name: str) -> dict:
    """
    Predict customer churn using the specified model.

    Args:
        data (CustomerData): Customer features for prediction.
        model_name (str): Model to use, either 'xgb' or 'catboost'.

    Example request body:
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

    Example outputs for this input:
        - CatBoost probability: 0.9535
        - XGBoost probability: 0.9333
        - Both models predict churn (0 ==>not exit, 1 ==> exit)
    """
    result = predict_churn(data, model_name)
    return result
