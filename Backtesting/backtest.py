from datetime import timedelta
import joblib
import numpy as np
import pandas as pd
import sys
sys.path.append('../Training')
from config import COMMODITY_KEY, COMMODITY_TO_FEATURE_PROFILES_MAP

class Trader:
    def __init__(self, balance=20000):
        self.balance = balance
        self.contractsQueue = []
        self.percentGains = []

class Contract:
    def __init__(self, purchasePrice, type, numContracts):
        self.purchasePrice = purchasePrice
        self.weeksHeld = 0
        self.type = type
        self.numContracts = numContracts


def main():

    # Example start and end dates (replace with your actual dates)
    start_date = '2021-07-02' 
    end_date = '2024-06-14'
    # Load your DataFrame from the CSV file
    df1 = pd.read_csv('../Training/BacktestData/NATURALGAS_Backtest.csv')
    
    df2 = pd.read_csv('../HistoricalData/CommodityPrices/NaturalGasPrices.csv')
    # df2 = pd.read_csv('GCandDXY.csv')

    
    # df2['Close'] = df2['Close'].str.replace(',', '').astype(float)

    df1['Report_Date_as_MM_DD_YYYY'] = pd.to_datetime(df1['Report_Date_as_MM_DD_YYYY'])
    df2['Date'] = pd.to_datetime(df2['Date'])  # Convert 'Date' column to datetime if it's not already

    current_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    loaded_model = joblib.load('../Training/currentModel.pkl')

    trader = Trader()
    previous_month = current_date.month
    currentMonthGains = 0
    monthlyGains = []

    while current_date <= end_date:
        # Lookup rows for current_date in the DataFrame
        if current_date.weekday() == 4:
            rows_for_current_date = df2[df2['Date'] == current_date]
            if rows_for_current_date.empty:
                previous_date = current_date - timedelta(days=1)
                rows_for_current_date = df2[df2['Date'] == previous_date]
            
            for contract in trader.contractsQueue:
                contract.weeksHeld += 1
                # if contract.weeksHeld == 4:
                #     if contract.type == "LONG" and ((rows_for_current_date['Close'].iloc[0] - contract.purchasePrice) / rows_for_current_date['Close'].iloc[0]) * 100 < -1:
                #         trader.balance += (rows_for_current_date['Close'].iloc[0] - contract.purchasePrice) * 10 * contract.numContracts
                #         contract.weeksHeld = 10
                #     elif contract.type == "SHORT" and ((contract.purchasePrice - rows_for_current_date['Close'].iloc[0]) / rows_for_current_date['Close'].iloc[0]) * 100 < -1:
                #         trader.balance += (contract.purchasePrice - rows_for_current_date['Close'].iloc[0]) * 10 * contract.numContracts
                #         contract.weeksHeld = 10
                if contract.weeksHeld == 1:
                    if contract.type == "LONG":
                        percentage_change = ((rows_for_current_date['Close'].iloc[0] - contract.purchasePrice) / rows_for_current_date['Close'].iloc[0]) * 100
                        trader.percentGains.append(percentage_change)
                        trader.balance += (rows_for_current_date['Close'].iloc[0] - contract.purchasePrice) * 1000 * contract.numContracts
                        currentMonthGains += percentage_change
                    else:
                        percentage_change = ((contract.purchasePrice - rows_for_current_date['Close'].iloc[0]) / rows_for_current_date['Close'].iloc[0]) * 100
                        trader.percentGains.append(percentage_change)
                        trader.balance += (contract.purchasePrice - rows_for_current_date['Close'].iloc[0]) * 1000 * contract.numContracts
                        currentMonthGains += percentage_change

            if current_date.month != previous_month:
                print(f"A month has passed: {current_date.strftime('%B %Y')}")
                monthlyGains.append(currentMonthGains)
                currentMonthGains = 0
                previous_month = current_date.month

            previous_month = current_date.month
            cotReport = df1[df1['Report_Date_as_MM_DD_YYYY'] == current_date]
            
            if not cotReport.empty:
            #     newDataDf = cotReport[[
            # 'RSI',
            # 'MACD', 'Signal Line',
            # 'RSI_LONG',
            # 'Change_in_Prod_Merc_Long_All',
            # 'Percent_PMPU_Long', 'Percent_MM_Long']]
                commodityProfile = COMMODITY_TO_FEATURE_PROFILES_MAP[COMMODITY_KEY]
                newDataDf = cotReport[[feature for feature in commodityProfile.keys() if commodityProfile[feature]]]

                probs = loaded_model.predict_proba(newDataDf)
                print("Predictions:")
                print(probs)
                predictions = loaded_model.predict(newDataDf)[0]
                # print(predictions)
                
                if probs[0][0] >= 0.55 or probs[0][0] <= 0.45:
                    if predictions == 1:
                        trader.contractsQueue.append(Contract(rows_for_current_date['Close'].iloc[0], "LONG", trader.balance * 0.5 // 500))
                    else:
                        trader.contractsQueue.append(Contract(rows_for_current_date['Close'].iloc[0], "SHORT", trader.balance * 0.5 // 500))
                print(trader.balance)
        # Move to the next date
        current_date += pd.DateOffset(days=1)  # Increment by one day


    # for gain in trader.percentGains:
    #     print(gain)
    for monthlyGain in monthlyGains:
        print(monthlyGain)
    print(f"TOTAL GAINS: {sum(trader.percentGains)}")
    print(f"TOTAL BALANCE: {trader.balance}")
    print(f"Winning Trade Ratio: {len([x for x in trader.percentGains if x >= 0]) / len(trader.percentGains) * 100}")

    avg_monthly_return = np.mean(monthlyGains[1:-1])

    # Calculate standard deviation of weekly returns
    std_dev_monthly_return = np.std(monthlyGains[1:-1])


    # Calculate Sharpe Ratio
    sharpe_ratio_monthly = (avg_monthly_return) / std_dev_monthly_return
    print(f"SHARPE RATIO: {sharpe_ratio_monthly}")

if __name__ == "__main__":
    main()

