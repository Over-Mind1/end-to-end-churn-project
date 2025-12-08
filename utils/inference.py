import pandas as pd
import numpy as np
from .config import preprocessor, xgb_model, cat_model
from .CustomerData import CustomerData

def predict_churn(data: CustomerData, model_name: str) -> dict:
    """Predict churn using the specified model based on selected feature indices.

    Args:
        data (CustomerData): The customer data for prediction.
        model_name (str): The name of the model to use ('xgb' or 'catboost').

    Returns:
        dict: Predicted churn label and probability.
    """

    # Convert CustomerData to DataFrame
    input_data = pd.DataFrame([data.model_dump()])

    # Preprocess the input data
    processed_data = preprocessor.transform(input_data)

    # Feature indices for each model
    catboost_top = [2, 23, 9, 3, 18, 7, 13, 11, 20, 5]
    xgb_top = [2, 23, 11, 18, 20, 9, 13, 3, 7]
    threshold = .5

    # Select features based on model
    if model_name == 'xgb':
        model = xgb_model
        threshold=.7
        processed_data = processed_data[:, xgb_top].reshape(1, -1)
    elif model_name == 'catboost':
        model = cat_model
        processed_data = processed_data[:, catboost_top]
    else:
        raise ValueError("Invalid model name. Choose 'xgb' or 'catboost'.")

    # Make prediction
    probability = model.predict_proba(processed_data)[:, 1]
    prediction = (probability >= threshold).astype(int)
    return {"prediction": int(prediction[0]), "probability": float(1-probability[0])}