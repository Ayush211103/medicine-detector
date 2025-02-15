# Medicine Detector Code
import pandas as pd

df = pd.read_csv(r"C:\Users\ayush\Desktop\medicine_detector1\medicine_data.csv")

print(df.head())
print(df.isnull().sum())


df['Expiry'] = pd.to_datetime(df['Expiry'], dayfirst=True)

expired_meds = df[df['Expiry'] < '2025-01-01']
print("Expired Medicine:\n", expired_meds)

print(df.info())

print(df.isnull().sum())


df = df.dropna(subset=["Name","Expiry"])

print("missing value after cleaning the data")

print(df.isnull().sum())


df.to_csv("cleaned_medicine_data.csv",index = False)
print(df)
print("Cleaned Data Saved Successfully!")
