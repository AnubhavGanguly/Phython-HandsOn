from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas : List[Tea] = []   

@app.get("/")
def readRoot():
    return {"Message": "Welcome to chai code"}

@app.get("/teas")
def getAllTeas():
    return teas

@app.post("/teas")
def addTeas(tea:Tea):
    teas.append(tea)
    return {"Tea is added successfully"}

@app.put("/teas/{tea_id}")
def updateTea(tea_id:int, updated_tea :Tea):
    for index, tea in enumerate(teas):
        if(tea.id == tea_id):
            teas[index] = updated_tea
            return {"Tea is updated", updated_tea}
    return{"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def deleteTea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deletedTea = teas.pop(index)
            return ("Tea is succesfully deleted",deletedTea)
    return{"error": "Tea not found"}