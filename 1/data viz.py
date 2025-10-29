import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sample_cleaned.csv')

plt.figure(figsize=(8,6))
sns.histplot(df['price'], bins=10, kde=True)
plt.title('Price Distribution of Products')
plt.xlabel('Price')
plt.ylabel('Count')
plt.savefig('price_distribution.png')
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(x='category', y='quantity', data=df)
plt.title('Quantity by Category')
plt.savefig('quantity_by_category.png')
plt.show()
