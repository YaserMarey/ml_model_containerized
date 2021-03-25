import uvicorn
from fastapi import FastAPI

import boston_housing

#
app = FastAPI()
#
@app.get("/")
def index():
    return 'ML Model API is alive!'
#
@app.post("/predict")
def predict(house_to_evalute: list):
    prediction = boston_housing.predict(house_to_evalute)
    return str(prediction)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
