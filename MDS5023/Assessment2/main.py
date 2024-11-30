import pandas as pd

import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('shopping_trends.csv')

# Display basic information about the DataFrame
print("DataFrame Info:")
print(df.info())

# Display the first few rows of the DataFrame
print("\nFirst 5 Rows:")
print(df.head())

# Display summary statistics of the DataFrame
print("\Column information:")
print(df.columns)

# Display summary statistics of the DataFrame
print("\nSummary Statistics:")
print(df.describe)

'''
# Plotting trends
plt.figure(figsize=(10, 6))

# Assuming the CSV has columns 'Date' and 'Sales'
if 'Age' in df.columns and 'Gender' in df.columns:
    df['Age'] = pd.to_datetime(df['Age'])
    plt.plot(df['Gender'], df['Gender'], label='Gender Trend')
    plt.xlabel('Gender')
    plt.ylabel('Gender')
    plt.title('Gender Trend Over Time')
    plt.legend()
    plt.show()
else:
    print("The CSV file does not contain 'Date' and 'Sales' columns.")
'''
# Additional analysis can be added here

print("\nMissing Column")
print(df.isnull().sum())
