# fastapi -- framework for building APIs
# uvicorn -- Server to run the API
# pydantic -- validates input data
# joblib -- load our saved model



# step 1 - creating a simple api
from fastapi import FastAPI

# step 2 - create API instance
app = FastAPI(title="Churn Prediction API")

# step 3 create a simple endpoint --- the address of the API
# - www.facebook.com  - an endpoint/address
# - google.com/careers - an endpoint
# google takes you to the career page

# - www.predictions_with_mo/logistic_regression ---
# input name
# input nphone number
# other details
# Model (Logistic reg, Random F or Xgboost) -- process the input data
# Get predictions

# get request ---- user is seeking for information 
# post request ---- user is seeking for information - giving a clue or some input data



@app.get("/")  #get request #facebook.com - sign up and sign up
def home():
    return {"message": "Welcome to Churn prediction API"}

# create health endpoint
@app.get("/health")
def health():
    return {"status": "This solution is healthy"}



