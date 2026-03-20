from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI() 
 
model = joblib.load("customer_segmentation_pipline.pkl")

@app.post("/predict")
def predict(recency: float, frequency: float, monetary: float): 
    
    data = pd.DataFrame([[recency, frequency, monetary]], columns=['Recency', 'Frequency', 'Monetary']) 
    
    cluster = model.predict(data)[0] 
    
    return {"cluster": int(cluster)}