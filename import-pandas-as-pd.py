import pandas as pd

filename = input("Enter CSV file name: ")
df = pd.read_csv(filename)
print(df.head())
