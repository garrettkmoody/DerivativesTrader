
import joblib
import pandas as pd
import sys
sys.path.append('Training')
from config import COMMODITY_TO_FEATURE_PROFILES_MAP

models = {
        "GOLD": joblib.load('Models/goldModel.pkl'),
        "COPPER": joblib.load('Models/copperModel.pkl'),
        "NATURALGAS": joblib.load('Models/naturalGasModel.pkl'),
}

datasets = {
    "GOLD": pd.read_csv('Training/BacktestData/GOLD_Backtest.csv'),
    "COPPER": pd.read_csv('Training/BacktestData/COPPER_Backtest.csv'),
    "NATURALGAS": pd.read_csv('Training/BacktestData/NATURALGAS_Backtest.csv'),
}

for key in ["GOLD","COPPER","NATURALGAS"]:
    currentReport = datasets[key].iloc[[43]]
    commodityProfile = COMMODITY_TO_FEATURE_PROFILES_MAP[key]
    newDataDf = currentReport[[feature for feature in commodityProfile.keys() if commodityProfile[feature]]]
    probs = models[key].predict_proba(newDataDf)
    print(f"Predictions: {key}")
    print(probs)
    predictions = models[key].predict(newDataDf)[0]
    print(predictions)
    print("LONG" if predictions == 1 else "SHORT")