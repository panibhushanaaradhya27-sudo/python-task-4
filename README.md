# 🚦 Traffic Accident Data Analysis

## 📌 Project Overview
This project focuses on analyzing traffic accident data to identify patterns related to:

- 🌧️ Weather conditions  
- 🛣️ Road conditions  
- 🕒 Time of day  
- 📍 Accident hotspot locations  

The goal is to discover contributing factors behind accidents and visualize trends using Python.

---

## 📂 Dataset
The dataset used contains traffic accident records with attributes such as:

- Severity  
- Start Time  
- Weather Condition  
- Visibility  
- Road Features  
- Latitude & Longitude  
- Sunrise / Sunset  

> Note: Original dataset file was too large to upload on GitHub.

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 📊 Project Workflow

### 1️⃣ Data Cleaning
- Handled missing values  
- Removed unnecessary columns  
- Converted datetime columns  

### 2️⃣ Exploratory Data Analysis
- Accidents by weather condition  
- Accidents by severity level  
- Accidents by hour of day  
- Road feature impact analysis  

### 3️⃣ Data Visualization
- Count plots  
- Bar charts  
- Correlation heatmap  
- Accident hotspot scatter plot  

---

## 📈 Key Insights

✅ Most accidents occurred during rush hours.  
✅ Bad weather conditions increased accident counts.  
✅ Certain road junctions had higher accident frequency.  
✅ Clear hotspot regions were visible using location data.

---

## 📁 Files Included

- `accident.py` → Main Python script  
- `README.md` → Project documentation  
- Output screenshots / charts  

---

## ▶️ How to Run

```bash
pip install pandas matplotlib seaborn
python accident.py
