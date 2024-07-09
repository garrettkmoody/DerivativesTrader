import pandas as pd
import os
from datetime import timedelta
import pandas as pd
from ta import momentum
from config import COMMODITY_KEY, COMMODITY_TO_COT_NAMES_MAP, COMMODITY_TO_PRICE_FILE_MAP

def calculate_rsi(df, window=7):
    # Calculate RSI using ta library
    reversed_closes = df['Close'][::-1]
    # Calculate RSI
    df['RSI'] = momentum.rsi(reversed_closes, window)
    df['RSI_LONG'] = momentum.rsi(reversed_closes, 14)
    return df

def calculate_ma(df, window=7):
    reversed_closes = df['Close'][::-1]
    df['MA'] = reversed_closes.rolling(window=window, min_periods=1).mean()
    return df

def calculate_ema(df, window=7):
    # Reverse the 'Close' prices to calculate EMA from oldest to newest
    reversed_closes = df['Close'][::-1]
    
    # Calculate EMA using pandas' ewm method
    df['EMA'] = reversed_closes.ewm(span=window, adjust=False).mean()[::-1]
    
    return df

def calculate_stochastic_k(df, n=14, d=3):
    # Ensure the 'Close' column is numeric
    reversed_closes = df['Close'][::-1]
    # Calculate %K
    lowest_low = reversed_closes.rolling(window=n, min_periods=1).min()
    highest_high = reversed_closes.rolling(window=n, min_periods=1).max()
    stochastic_k = ((reversed_closes - lowest_low) / (highest_high - lowest_low)) * 100
    
    # Calculate %D
    stochastic_d = stochastic_k.rolling(window=d, min_periods=1).mean()
    
    # Add %K and %D to the DataFrame
    df['%K'] = stochastic_k
    df['%D'] = stochastic_d
    
    return df

def calculate_macd(df, n_fast=3, n_slow=7, n_signal=9):
    reversed_closes = df['Close'][::-1]
    ema_fast = reversed_closes.ewm(span=n_fast, min_periods=1).mean()
    ema_slow = reversed_closes.ewm(span=n_slow, min_periods=1).mean()
    df['MACD'] = ema_fast - ema_slow
    df['Signal Line'] = df['MACD'].ewm(span=n_signal, min_periods=1).mean()

    n_fast=6
    n_slow=14
    n_signal=18
    ema_fast = reversed_closes.ewm(span=n_fast, min_periods=1).mean()
    ema_slow = reversed_closes.ewm(span=n_slow, min_periods=1).mean()
    df['BIG MACD'] = ema_fast - ema_slow
    df['BIG Signal Line'] = df['BIG MACD'].ewm(span=n_signal, min_periods=1).mean()
    return df

def calculate_bollinger_bands(df, n=7, std=2):
    reversed_closes = df['Close'][::-1]
    sma = reversed_closes.rolling(window=n).mean()
    df['Upper Band'] = sma + (reversed_closes.rolling(window=n).std() * std)
    df['Lower Band'] = sma - (reversed_closes.rolling(window=n).std() * std)
    return df

def calculate_percent_traders(df):
    df['Percent_PMPU_Long'] = df['Traders_Prod_Merc_Long_All'] / df['Traders_Tot_All']
    df['Percent_PMPU_Short'] = df['Traders_Prod_Merc_Short_All'] / df['Traders_Tot_All']
    df['Percent_MM_Long'] = df['Traders_M_Money_Long_All'] / df['Traders_Tot_All']
    df['Percent_MM_Short'] = df['Traders_M_Money_Short_All'] / df['Traders_Tot_All']
    df['Percent_MM_Spread'] = df['Traders_M_Money_Spread_All'] / df['Traders_Tot_All']
    df['Percent_SWAP_Long'] = df['Traders_Swap_Long_All'] / df['Traders_Tot_All']
    df['Percent_SWAP_Short'] = df['Traders_Swap_Short_All'] / df['Traders_Tot_All']
    df['Percent_SWAP_Spread'] = df['Traders_Swap_Spread_All'] / df['Traders_Tot_All']
    df['Percent_OR_Long'] = df['Traders_Other_Rept_Long_All'] / df['Traders_Tot_All']
    df['Percent_OR_Short'] = df['Traders_Other_Rept_Short_All'] / df['Traders_Tot_All']
    df['Percent_OR_Spread'] = df['Traders_Other_Rept_Spread_All'] / df['Traders_Tot_All']
    return df

def find_next_monday(date):
    while date.weekday() != 0:  # 0 corresponds to Monday
        date += pd.DateOffset(days=1)
    return date

def calculate_price_change(current_date, merged_df):
    next_week_date = current_date + timedelta(days=7)
    current_data = merged_df[merged_df['Date'] == current_date]
    next_week_data = merged_df[merged_df['Date'] == next_week_date]

    if pd.isna(current_date):
        return None
    
    if not next_week_data.empty:
        current_close = current_data.iloc[0]['Close']
        next_week_close = next_week_data.iloc[0]['Close']
        price_change = next_week_close - current_close
        return 1 if price_change > 0 else 0
    else:
        # If next_week_data is empty, try finding data on the following Monday
        following_monday_date = find_next_monday(next_week_date)
        following_monday_data = merged_df[merged_df['Date'] == following_monday_date]
        if not following_monday_data.empty:
            current_close = current_data.iloc[0]['Close']
            following_monday_close = following_monday_data.iloc[0]['Close']
            price_change = following_monday_close - current_close
            return 1 if price_change > 0 else 0
        else:
            return None

def convert_to_numeric(value):
    try:
        # Check if value contains a comma
        if ',' in str(value):
            return float(value.replace(',', ''))
        else:
            return float(value)
    except ValueError:
        return value  # Return unchanged if conversion fails

def main():
     # Load df1 from file1.csv
    
    df1 = pd.read_csv(f'../HistoricalData/CommodityPrices/{COMMODITY_TO_PRICE_FILE_MAP[COMMODITY_KEY]}')
    df1['Close'] = df1['Close'].apply(convert_to_numeric)

    # Load indexes
    df2 = pd.read_csv('../HistoricalData/Indexes/DXY.csv')
    df3 = pd.read_csv('../HistoricalData/Indexes/VIX.csv')

    # Load currencies
    df4 = pd.read_csv('../HistoricalData/CurrencyPrices/CHINA.csv')
    df5 = pd.read_csv('../HistoricalData/CurrencyPrices/RUSSIA.csv')
    df6 = pd.read_csv('../HistoricalData/CurrencyPrices/AUSTRALIA.csv')
    df7 = pd.read_csv('../HistoricalData/CurrencyPrices/CANADA.csv')

    # Merge all data
    merged_df = pd.merge(df1, df2, on='Date', how='left')
    merged_df = pd.merge(merged_df, df3, on='Date', how='left')
    merged_df = pd.merge(merged_df, df4, on='Date', how='left')
    merged_df = pd.merge(merged_df, df5, on='Date', how='left')
    merged_df = pd.merge(merged_df, df6, on='Date', how='left')
    merged_df = pd.merge(merged_df, df7, on='Date', how='left')

    cotCsvFiles = ['2024.csv', '2023.csv', '2022.csv', '2021.csv',
                '2020.csv', '2019.csv', '2018.csv', '2017.csv', '2016.csv',
                '2015.csv', '2014.csv', '2013.csv', '2012.csv',
                '2011.csv', '2010.csv', '2006-2009.csv']

    allDfs = [pd.read_csv("../CotReports/" + fileName) for fileName in cotCsvFiles]
    df1 = pd.concat(allDfs, ignore_index=True)

    df1['Report_Date_as_MM_DD_YYYY'] = pd.to_datetime(df1['Report_Date_as_MM_DD_YYYY'])
    merged_df['Date'] = pd.to_datetime(merged_df['Date'])

    df1 = df1[(df1['Market_and_Exchange_Names'].isin(COMMODITY_TO_COT_NAMES_MAP[COMMODITY_KEY]))]
    # df1 = df1[(df1['Market_and_Exchange_Names'] == 'GOLD - COMMODITY EXCHANGE INC.')]
    df1 = df1[df1['Report_Date_as_MM_DD_YYYY'].dt.weekday == 1]
    df1['Report_Date_as_MM_DD_YYYY'] = df1['Report_Date_as_MM_DD_YYYY'] + pd.DateOffset(days=3)

    merged_df = pd.merge(df1, merged_df, how='left', left_on='Report_Date_as_MM_DD_YYYY', right_on='Date')

    for index, row in merged_df[merged_df['Date'].isna()].iterrows():
        next_monday_date = find_next_monday(row['Report_Date_as_MM_DD_YYYY'])
        # Merge merged_df data at the next Monday's date into merged_df
        next_monday_data = merged_df[merged_df['Date'] == next_monday_date]
        if not next_monday_data.empty:
            merged_df.loc[index, merged_df.columns] = next_monday_data.iloc[0]

    price_differences = []
    for index, row in merged_df.iterrows():
        current_date = row['Date']
        price_change = calculate_price_change(current_date, merged_df)
        price_differences.append(price_change)

    # Add 'pricechange' column to merged_df
    merged_df['PriceDifference'] = price_differences

    merged_df = calculate_rsi(merged_df)
    merged_df = calculate_ma(merged_df)
    merged_df = calculate_stochastic_k(merged_df)
    merged_df = calculate_macd(merged_df)
    merged_df = calculate_bollinger_bands(merged_df)
    merged_df = calculate_ema(merged_df)
    merged_df = calculate_percent_traders(merged_df)

    backtestDir = 'BacktestData'
    trainDir = 'TrainData'

    # Ensure the base directory exists, create it if it doesn't
    os.makedirs(backtestDir, exist_ok=True)
    os.makedirs(trainDir, exist_ok=True)
    # Construct the full path for the CSV file
    csv_file_path = os.path.join(backtestDir, f'{COMMODITY_KEY}_Backtest.csv')
    csv_file_path2 = os.path.join(trainDir, f'{COMMODITY_KEY}_Train.csv')
    # Save merged DataFrame to CSV
    merged_df.to_csv(csv_file_path, index=False)

    merged_df = merged_df.dropna(subset=['PriceDifference'])
    # Save or use the updated DataFrame as needed
    merged_df.to_csv(csv_file_path2, index=False)



if __name__ == "__main__":
    main()
