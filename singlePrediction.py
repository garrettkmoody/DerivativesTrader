
import joblib
import pandas as pd


loaded_model = joblib.load('currentModel.pkl')

newDataDf = cotReport[['Pct_of_OI_Prod_Merc_Long_All','Pct_of_OI_Prod_Merc_Short_All',
                'Pct_of_OI_M_Money_Long_All','Pct_of_OI_M_Money_Short_All','Pct_of_OI_M_Money_Spread_All',
                'RSI', 'CloseDXY', 'MA', 'CloseCHINA', 'CloseRUSSIA', 'CloseAUS',
                'MACD', 'Signal Line', 'Upper Band', 'Lower Band']]
data = {
    'Pct_of_OI_Prod_Merc_Long_All': [12],
    'Pct_of_OI_Prod_Merc_Short_All': [12],
    'Pct_of_OI_M_Money_Long_All': [12],
    'Pct_of_OI_M_Money_Short_All': [12],
    'Pct_of_OI_M_Money_Spread_All': [12],
    'RSI': [12],
    'CloseDXY': [12],
    'MA': [12],
    'CloseCHINA': [12],
    'CloseRUSSIA': [12],
    'CloseAUS': [12],
    'MACD': [12],
    'Signal Line': [12],
    'Upper Band': [12],
    'Lower Band': [12],
}
df = pd.DataFrame(data)

probs = loaded_model.predict_proba(newDataDf)
print("Predictions:")
print(probs)
predictions = loaded_model.predict(newDataDf)[0]