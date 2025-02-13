# Medicine Detector Code
import pandas as pd
df = pd.read_csv(r"C:\Users\ayush\Desktop\medicine_detector1\medicine_data.csv")
print(df.head())
print(df.isnull().sum())
df['Expiry'] = pd.to_datetime(df['Expiry'], dayfirst=True)
expired_meds = df[df['Expiry'] < '2025-01-01']
print("Expired Medicine:\n", expired_meds)
