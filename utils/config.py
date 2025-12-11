from dotenv import load_dotenv
from utils.FeatureEngineering import FeatureEngineering
import os
import joblib
#load environment variables from a .env file
load_dotenv()

#-- Constants from environment variables --#
APP_NAME = os.getenv('APP_NAME', 'DefaultAppName')
VERSION = os.getenv('VERSION', '1.0.0')


#-- base paths --#
BASE_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
MODELS_PATH = os.path.join(BASE_PATH, 'models')

#-- Models paths --#
preprocessor_path = os.path.join(MODELS_PATH, 'preprocessor', 'preprocessor.pkl')
xgb_model_path = os.path.join(MODELS_PATH, 'xgb', 'model.pkl')
cat_model_path = os.path.join(MODELS_PATH, 'catboost', 'model.pkl')

#--load models--#
preprocessor = joblib.load(preprocessor_path)
xgb_model = joblib.load(xgb_model_path)
cat_model = joblib.load(cat_model_path)

print(f"Configuration loaded: APP_NAME={APP_NAME}, VERSION={VERSION}")