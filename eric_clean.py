import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import seaborn
from datetime import timedelta

df = pd.read_csv('data/churn.csv')
ericdf = df.copy()

cols = np.array(['avg_dist', 'avg_rating_by_driver', 'avg_rating_of_driver',
       'avg_surge', 'city', 'last_trip_date', 'phone', 'signup_date',
       'surge_pct', 'trips_in_first_30_days', 'luxury_car_user',
       'weekday_pct'])

# city
# np.sum(pd.isnull(ericdf.city))
# 0
ericdf.city.unique()
cities = np.array(["King's Landing", 'Astapor', 'Winterfell'])

# last_trip_date
# np.sum(pd.isnull(ericdf.last_trip_date))
# 0
ericdf.last_trip_date = pd.to_datetime(ericdf.last_trip_date)
last = max(ericdf.last_trip_date) - timedelta(days=30)
ericdf['churn'] = np.where(ericdf.last_trip_date >= last, 0, 1)

# phone
# np.sum(pd.isnull(ericdf.phone))
# 396
ericdf.phone = ericdf.phone.fillna('Other')
ericdf.phone.unique()
phones = ['Android', 'Other', 'iPhone']
ericdf[phones] = pd.get_dummies(ericdf['phone'])

# signup_date
# np.sum(pd.isnull(ericdf.signup_date))
# 0
ericdf.signup_date = pd.to_datetime(ericdf.signup_date)

# surge_pct
# np.sum(pd.isnull(ericdf.surge_pct))
# 0
ericdf.surge_pct[ericdf.surge_pct == 0].shape[0]
# 34409

# trips_in_first_30_days
# 0
# np.sum(pd.isnull(ericdf.trips_in_first_30_days))




# scatter_matrix(ericdf, alpha=0.3, diagonal='kde')
