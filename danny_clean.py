import pandas as pd

df = pd.read_csv('data/churn.csv')

# Dummify the city column and drop 'city'
df[['Astapor', "King's Landing", 'Winterfell']] = pd.get_dummies(df['city'])
df = df.drop(['city'], axis=1)

# Drop rows that have NaN values
df = df[df['avg_rating_by_driver'].notnull()]
df = df[df['avg_rating_of_driver'].notnull()]
