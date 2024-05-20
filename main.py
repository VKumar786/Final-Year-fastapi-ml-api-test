from typing import Union
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

'''
Define a Pydantic model
'''


class Item(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


loaded_model = pickle.load(open("trained_model.sav", "rb"))
data = []


def diabetes_prediction(input_data):
    id_np_arr = np.asarray(input_data)
    id_reshaped = id_np_arr.reshape(1, -1)
    predict = loaded_model.predict(id_reshaped)

    print(predict)
    if predict[0] == 0:
        return 0
    else:
        return 1


@app.get("/")
def read_root():
    return data


@app.post('/')
def create_item(item: Item):
    features = [
        item.Pregnancies,
        item.Glucose,
        item.BloodPressure,
        item.SkinThickness,
        item.Insulin,
        item.BMI,
        item.DiabetesPedigreeFunction,
        item.Age
    ]
    diagnosis = diabetes_prediction(features)
    return {"result": diagnosis}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"message": "Validation error",
                 "status": 422, "detail": exc.errors()}
    )
