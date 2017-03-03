import read
import collections

df = read.load_data()

print(df.head())

print(df["url"].value_counts(sort=True, ascending=False)[0:100])