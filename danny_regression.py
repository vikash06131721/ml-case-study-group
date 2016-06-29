from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from master_clean import load_churn
import pandas as pd

df = load_churn()

y = df.pop('churn').as_matrix()
X = df.as_matrix()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

scale = StandardScaler()

scale.fit(X_train)
scale.transform(X_train)
scale.transform(X_test)

model = LogisticRegression(C=0.01)

model.fit(X_train, y_train)

model.predict(X_test)
