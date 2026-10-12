from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(title="🛡️ NIDS Threat Scorer")

@app.get("/")
def read_root():
    return {"status": "online", "system": "XGBoost-IDS"}
