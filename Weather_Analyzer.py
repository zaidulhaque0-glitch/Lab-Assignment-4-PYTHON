# ==========================================
# Weather Analysis
# Author: Zaidul Haque
# Date: 19 November 2025
# Course: Programming for Problem Solving using Python
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Task 1: Load Dataset

df = pd.read_csv("progm_with_py\Assignment\weather_dataset.csv")

print("\n===== DATA HEAD =====")
print(df.head())

print("\n===== DATA INFO =====")
print(df.info())

print("\n===== DATA SUMMARY =====")
print(df.describe())



# Task 2: Cleaning & Processing

df = df.dropna()   # remove missing values

df['Date'] = pd.to_datetime(df['Date'])   # convert to datetime

weather = df[['Date', 'Temp', 'Humidity', 'Rainfall']]
print("\nCleaned Columns:")
print(weather.head())


# Task 3: NumPy Statistical Analysis

mean_temp = np.mean(weather['Temp'])
max_temp = np.max(weather['Temp'])
min_humidity = np.min(weather['Humidity'])
std_rainfall = np.std(weather['Rainfall'])

print("\n===== NUMPY STATISTICS =====")
print("Mean Temperature:", mean_temp)
print("Max Temperature:", max_temp)
print("Min Humidity:", min_humidity)
print("Std Dev of Rainfall:", std_rainfall)



# Task 4: Visualizations


# Line Chart: Temperature Trend
plt.figure(figsize=(10,5))
plt.plot(weather['Date'], weather['Temp'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temp_trend.png")
plt.show()

# Bar Chart: Monthly Rainfall
weather['Month'] = weather['Date'].dt.month
monthly_rainfall = weather.groupby('Month')['Rainfall'].sum()
plt.figure(figsize=(8,5))
monthly_rainfall.plot(kind='bar')
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("monthly_rainfall.png")
plt.show()

# Scatter Plot: Humidity vs Temperature
plt.figure(figsize=(7,5))
plt.scatter(weather['Temp'], weather['Humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("humidity_temp_scatter.png")
plt.show()



# Task 5: Grouping & Aggregation

monthly_stats = weather.groupby('Month').agg({
    'Temp': ['mean', 'max', 'min'],
    'Rainfall': 'sum',
    'Humidity': 'mean'
})

print("\n===== MONTHLY STATISTICS =====")
print(monthly_stats)



# Task 6: Export Cleaned Data

weather.to_csv("cleaned_weather_data.csv", index=False)
print("\nCleaned data exported as cleaned_weather_data.csv")
