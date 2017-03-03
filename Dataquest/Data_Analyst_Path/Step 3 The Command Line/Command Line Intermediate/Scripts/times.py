import read
import collections
from dateutil.parser import parse

df = read.load_data()

def extract_hour(str):
    date = parse(str)
    return date.hour
    

df["Hour"] = df["submission_time"].apply(extract_hour)
print(df["Hour"].value_counts())

def extract_month(str):
    date = parse(str)
    return date.month

print("-------------")
print("-------------")
df["Month"] = df["submission_time"].apply(extract_month)
print(df["Month"].value_counts())