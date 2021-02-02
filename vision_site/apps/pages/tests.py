import pandas as pd
from pandas import DataFrame as dtf
import numpy as np
from collections import Counter
from datetime import datetime as dt

import json
from django_pandas.io import read_frame

"""

data = [",id,date_time,amount,account,comments", "0,1,2021-01-01 00:00:00+00:00,100.00,,", "1,2,2021-01-02 00:00:00+00:00,200.00,,"]
data = [item.strip().split(',')[1:] for item in data]

d1 = pd.DataFrame(data=data[1:], index=None,  columns=data[0])
print(d1)
print(list(d1.iloc[0]))


s = '{"id":{"0":1,"1":2},"date_time":{"0":1609459200000,"1":1609545600000},"amount":{"0":100.0,"1":200.0},"account":{"0":null,"1":null},"comments":{"0":null,"1":null}}'

d2 = pd.read_json(s)
print(d2)
print(np.cumsum(d2['amount']))
"""

d1 = dtf({'add_datetime': [dt(2020, 12, 11),
                           dt(2020, 12, 11),
                           dt(2020, 12, 11),
                           dt(2020, 12, 12),
                           dt(2021, 1, 11),
                           dt(2021, 1, 11),
                           ]}, dtype='datetime64[ns, UTC]')
fields = ['date_time', 'amount']
time_range = pd.date_range('2020-12-1', '2020-12-31')
time_range = time_range.astype('datetime64[ns, UTC]')
re = dtf([], columns=fields)

add_datetimes = d1['add_datetime']
counts = Counter(np.searchsorted(time_range, add_datetimes))

re.at[:, 'date_time'] = time_range
re = re.fillna(0)

for key in counts.keys():
    if key < len(re):
        re.at[key, 'amount'] = counts[key]

re['amount'] = np.cumsum(re['amount'])

print(re)


