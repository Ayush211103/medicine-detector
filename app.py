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





# DAY-4

print("Total number of medicine: ", df.shape[0])



print("Medicine Type: \n",df["Type"].value_counts())


print("Price statistic: \n", df["Price"].describe())


medicine_name = input("Enter medicine name: ").strip().lower()

found = df[df["Name"].str.lower() == medicine_name]

if not found.empty:
    print(found)
else:
    print("Medicine not found")

df.drop_duplicates(subset=["Name"],keep="first",inplace=True)
df.to_csv("cleaned_medicine_data.csv",index=False)
print("Cleaned Data Saved Successfully!")