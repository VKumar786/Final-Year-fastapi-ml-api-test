from typing import Union
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Define a Pydantic model
class Item(BaseModel):
    pregnancies: int
    glucose: int
    blood_pressure: int
    skin_thickness: int
    insulin: int
    bmi: float
    diabetes_pedigree_function: float
    age: int

# Load the trained model
loaded_model = pickle.load(open("trained_model.sav", "rb"))
data = []

# Function for diabetes prediction
def diabetes_prediction(input_data):
    id_np_arr = np.asarray(input_data)
    id_reshaped = id_np_arr.reshape(1, -1)
    predict = loaded_model.predict(id_reshaped)
    
    if predict[0] == 0:
        return 0
    else:
        return 1

# Define root endpoint
@app.get("/")
def read_root():
    return data

# Define POST endpoint for creating an item
@app.post('/')
def create_item(item: Item):
    features = [
        item.pregnancies,
        item.glucose,
        item.blood_pressure,
        item.skin_thickness,
        item.insulin,
        item.bmi,
        item.diabetes_pedigree_function,
        item.age
    ]
    diagnosis = diabetes_prediction(features)
    return {"result": diagnosis}

# Exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"message": "Validation error", "status": 422, "detail": exc.errors()}
    )

