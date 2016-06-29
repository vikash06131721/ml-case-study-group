import pandas as pd

df = pd.read_csv('data/churn.csv')

df = df[df['avg_rating_by_driver'].notnull()]
df = df[df['avg_rating_of_driver'].notnull()]
