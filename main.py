from fastapi import FastAPI, HTTPException
from Data import Diet
from Data import Exercise
import uvicorn

app = FastAPI()

# Fetch data
diet = Diet.getDiet()
exercise = Exercise.getExercise()

@app.get("/")
def home():
    return {"message": "Welcome to fitconnect api"}

@app.get("/diet")
def get_diet():
    return {"diet": diet}

@app.get("/diet/{id}")
def get_diet_item(id: str):
    for item in diet:
        if item["ID"] == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/exercise")
def get_exercise():
    return {"exercise": exercise}

@app.get("/exercise/{id}")
def get_exercise_item(id: str):
    for item in exercise:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
