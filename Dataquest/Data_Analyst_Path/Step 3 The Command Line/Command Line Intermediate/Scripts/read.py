import numpy as np
import pandas as pd
def load_data():
    data = pd.read_csv("hn_stories.csv")
    print(data.head())
    print("--------------")
    data.columns = ["submission_time","upvotes", "url", "headline"]
    print(data.head())
    return data

if __name__ == "__main__":
        # This will call load_data if you run the script from the command line.
        load_data()