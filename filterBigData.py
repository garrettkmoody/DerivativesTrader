import pandas as pd

# Replace 'your_file.csv' with the path to your actual CSV file
input_file = '2006-2015.csv'
output_file = '2006-2009.csv'  # New file to save filtered data

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Split the date string into month, day, and year
df['Month'] = df['Report_Date_as_MM_DD_YYYY'].str.split('/').str[0].astype(int)
df['Day'] = df['Report_Date_as_MM_DD_YYYY'].str.split('/').str[1].astype(int)
df['Year'] = df['Report_Date_as_MM_DD_YYYY'].str.split('/').str[2].astype(int)

# Filter rows where the year is on or before 2009
df_filtered = df[df['Year'] <= 2009]

# Concatenate 'Month', 'Day', and 'Year' back to the original format
df_filtered['Report_Date_as_MM_DD_YYYY'] = df_filtered['Month'].astype(str) + '/' + df_filtered['Day'].astype(str) + '/' + df_filtered['Year'].astype(str)

# Drop temporary columns 'Month', 'Day', and 'Year'
df_filtered = df_filtered.drop(['Month', 'Day', 'Year'], axis=1)

# Write the filtered DataFrame to a new CSV file
df_filtered.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")