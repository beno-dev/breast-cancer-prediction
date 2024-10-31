from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
#import uvicorn
from os.path import join, dirname

path_to_model = join(dirname(__file__), "../model/breast_cancer.pkl")

# Cargar el modelo y el scaler desde los archivos .pkl
with open(path_to_model, 'rb') as archivo_modelo:
    modelo = pickle.load(archivo_modelo)

# Definir las características esperadas
columnas = [
    "radius_mean",
    "texture_mean",
    "smoothness_mean",
    "compactness_mean",
    "symmetry_mean",
    "fractal_dimension_mean",
    "radius_se",
    "texture_se",
    "smoothness_se",
    "compactness_se",
    "symmetry_se",
    "fractal_dimension_se",
]

# Crear la aplicación FastAPI
app = FastAPI(title="Breast Cancer Detection")

# Definir el modelo de datos de entrada utilizando Pydantic
class RadiologyAttributes(BaseModel):
    radius_mean: float
    texture_mean: float
    smoothness_mean: float
    compactness_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    smoothness_se: float
    compactness_se: float
    symmetry_se: float
    fractal_dimension_se: float


@app.get("/")
async def root():
    return {"message": "Prediction"}

# Definir el endpoint para predicción
@app.post("/prediccion/")
async def predecir_cancer(transaccion: RadiologyAttributes):
    try:
        # Convertir la entrada en un DataFrame
        datos_entrada = pd.DataFrame([transaccion.dict()], columns=columnas)
                
        # Realizar la predicción
        prediccion = modelo.predict(datos_entrada)
#        probabilidad = modelo.predict_proba(datos_entrada)[:, 1]
        
        # Construir la respuesta
        resultado = {
            "has_cancer": bool(prediccion[0]),
#
        }
        
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)