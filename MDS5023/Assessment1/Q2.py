import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
#file_path = '/mnt/data/iris.csv'
iris_df = pd.read_csv(iris)

# Create two new columns
iris_df['sepal_area'] = iris_df['sepallength'] * iris_df['sepalwidth']
iris_df['petal_area'] = iris_df['petallength'] * iris_df['petalwidth']

# Filter for Iris-setosa
setosa_df = iris_df[iris_df['class'] == 'Iris-setosa']

# Create a plot for the two new columns
plt.figure(figsize=(12, 6))

# Plot sepal area
plt.subplot(2, 1, 1)  # First subplot
plt.plot(setosa_df.index, setosa_df['sepal_area'], label='Sepal Area', color='blue', marker='o')
plt.title('Sepal Area for Iris-setosa')
plt.xlabel('Index')
plt.ylabel('Sepal Area')
plt.grid(True)
plt.legend()

# Plot petal area
plt.subplot(2, 1, 2)  # Second subplot
plt.plot(setosa_df.index, setosa_df['petal_area'], label='Petal Area', color='green', marker='s')
plt.title('Petal Area for Iris-setosa')
plt.xlabel('Index')
plt.ylabel('Petal Area')
plt.grid(True)
plt.legend()

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
