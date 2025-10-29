import pandas as pd

df = pd.read_csv('/var/lib/mysql-files/sample.csv')

print(df.head())

df.fillna({'price':0, 'quantity':0, 'category':'Unknown'}, inplace=True)

df.drop_duplicates(inplace=True)

df.columns = [col.strip().lower() for col in df.columns]

df.to_csv('sample_cleaned.csv', index=False)
print("Data cleaned and saved!")
