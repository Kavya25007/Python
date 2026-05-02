#pandas used for data analysis and handling
#numpy used for numerical computation and to find duplicate , missing and infinte values

import pandas as pd
import numpy as np
from pathlib import Path

#loading the dataset
csv_path = Path(__file__).with_name("advanced_dataset.csv")
df = pd.read_csv(csv_path)
print(df.head())

#Convert to numeric
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
df["Salary"] = pd.to_numeric(df["Salary"], errors='coerce')
df["Score"] = pd.to_numeric(df["Score"], errors='coerce')

#checking the missing values
print("Missing values in each column")
print(df.isnull().sum())

#Replace inf → NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

#Calculate  average value of age and filled in it
df["Age"] = df["Age"].fillna(df["Age"].mean())

#Calculate average value of Salary and filled it
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

#Calculating median value of score and filled in it
df["Score"] = df["Score"].fillna(df["Score"].median())

#Replace nan values with average value
df.fillna(df.mean(numeric_only=True), inplace=True)

#Remove duplicate records
df.drop_duplicates(inplace=True)

#Replace negative salaries
df["Salary"] = np.where(df["Salary"] < 0, np.nan, df["Salary"])
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

salary_mean = df["Salary"].mean()
salary_std = df["Salary"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)


#Remove rows where salary is too high or too low
df = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]

df.to_csv("cleaned_advanced_dataset.csv", index=False)

print('Data cleaning completed! Saved as "cleaned_advanced_dataset.csv"')

print(df.isnull().sum())