import pandas as pd

data = pd.read_csv(".learn/assets/us_baby_names_right.csv")

del data["Unnamed: 0"]

name_count = len(data.groupby("Name").sum())

print(name_count)