import pandas as pd


def convert_to_numeric(value):
    try:
        # Check if value contains a comma
        if ',' in str(value):
            return float(value.replace(',', ''))
        else:
            return float(value)
    except ValueError:
        return value  # Return unchanged if conversion fails
    

# Load df1 from file1.csv
df1 = pd.read_csv('GCPriceData.csv')
df1['Close'] = df1['Close'].apply(convert_to_numeric)

# Load df2 from file2.csv
df2 = pd.read_csv('DXY.csv')

df3 = pd.read_csv('CHINA.csv')
df4 = pd.read_csv('RUSSIA.csv')
df5 = pd.read_csv('AUSTRALIA.csv')
df6 = pd.read_csv('VIX.csv')
df7 = pd.read_csv('CANADA.csv')
# Merge df1 and df2 on 'common_column', keeping all rows from df1
merged_df = pd.merge(df1, df2, on='Date', how='left')
merged_df = pd.merge(merged_df, df3, on='Date', how='left')
merged_df = pd.merge(merged_df, df4, on='Date', how='left')
merged_df = pd.merge(merged_df, df5, on='Date', how='left')
merged_df = pd.merge(merged_df, df6, on='Date', how='left')
merged_df = pd.merge(merged_df, df7, on='Date', how='left')
# Write merged_df to a new CSV file
merged_df.to_csv('GCandDXY.csv', index=False)
