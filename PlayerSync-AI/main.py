import joblib
import numpy as np
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="PlayerSync AI Engine")

# Updated input data validator to expect 4 features
class PlayerFeatures(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float

try:
    kmeans_model = joblib.load("player_cluster_model.pkl")
    print("Success: player_cluster_model.pkl loaded flawlessly using joblib!")
except Exception as e:
    kmeans_model = None
    print(f"Error loading model file: {str(e)}")

@app.get("/")
def home():
    return {"status": "healthy", "model_loaded": kmeans_model is not None}

@app.post("/predict")
def predict_cluster(player: PlayerFeatures, db: Session = Depends(get_db)):
    if kmeans_model is None:
        raise HTTPException(status_code=500, detail="Machine learning model is not initialized.")
    
    try:
        # Pass all 4 features to the model array
        input_data = np.array([[player.feature_1, player.feature_2, player.feature_3, player.feature_4]])
        predicted_cluster = int(kmeans_model.predict(input_data)[0])
        
        new_prediction = models.PlayerPrediction(
            feature_1=player.feature_1,
            feature_2=player.feature_2,
            feature_3=player.feature_3,
            feature_4=player.feature_4, # Logged 4th feature
            assigned_cluster=predicted_cluster
        )
        
        db.add(new_prediction)
        db.commit()
        db.refresh(new_prediction)
        
        return {
            "success": True,
            "prediction_id": new_prediction.id,
            "assigned_cluster": predicted_cluster,
            "msg": "Data saved permanently to the local cloud database!"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")