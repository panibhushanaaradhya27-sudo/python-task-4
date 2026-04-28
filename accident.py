# Task 4 - Traffic Accident Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("traffic.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Info
print("\nDataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df.dropna(inplace=True)

# Convert Date column if available
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# -------------------------------
# Accidents by Weather Condition
# -------------------------------
if 'Weather_Condition' in df.columns:
    plt.figure(figsize=(10,5))
    sns.countplot(x='Weather_Condition', data=df)
    plt.title("Accidents by Weather Condition")
    plt.xticks(rotation=45)
    plt.show()

# -------------------------------
# Accidents by Road Condition
# -------------------------------
if 'Road_Condition' in df.columns:
    plt.figure(figsize=(10,5))
    sns.countplot(x='Road_Condition', data=df)
    plt.title("Accidents by Road Condition")
    plt.xticks(rotation=45)
    plt.show()

# -------------------------------
# Accidents by Time of Day
# -------------------------------
if 'Time' in df.columns:
    df['Hour'] = pd.to_datetime(df['Time']).dt.hour
    plt.figure(figsize=(10,5))
    sns.histplot(df['Hour'], bins=24, kde=True)
    plt.title("Accidents by Hour of Day")
    plt.xlabel("Hour")
    plt.show()

# -------------------------------
# Correlation Heatmap
# -------------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=['number']).corr(),
            annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# Accident Hotspots Map
# -------------------------------
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    plt.figure(figsize=(10,6))
    plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5)
    plt.title("Accident Hotspots")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()