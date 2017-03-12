import sqlite3
conn = sqlite3.connect('factbook.db')

import pandas as pd

facts = pd.read_sql_query("select * from facts",conn)
print(facts.info())

facts = facts.dropna(axis=0)
print("-------------")
print("-------------")
print(facts.info())

import math

def estimpop(df):
    estpop = df["population"]*(math.e**((df["population_growth"]/100)*35))
    return round(estpop,0)

facts["estimated_pop"] = facts.apply(estimpop,axis=1)
facts = facts.sort_values("estimated_pop",ascending=False)
print(facts[["name","estimated_pop","population"]][0:10])