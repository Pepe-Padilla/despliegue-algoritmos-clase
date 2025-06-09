from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional
from classes_values import Identity


app = FastAPI()

@app.get('/Saluda')
def roout(name: str): 
    return {'Message': f'Hola soy {name}'}

@app.post('/test')
def testing(info: Identity): 
    return {'Message': f'Hola me llamo {info.name} y mi telefono es {info.phone_number}'}