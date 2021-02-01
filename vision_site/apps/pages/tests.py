import pandas as pd
import json


data = [",id,date_time,amount,account,comments", "0,1,2021-01-01 00:00:00+00:00,100.00,,", "1,2,2021-01-02 00:00:00+00:00,200.00,,"]
data = [item.strip().split(',')[1:] for item in data]

d1 = pd.DataFrame(data=data[1:], index=None,  columns=data[0])
print(d1.loc[0])
d1.columns = d1[1]

s = d1.to_json()
f = open('../re.txt', 'w+')
f.write(s)
f.close()

f = open('../re.txt', 'r')
re = f.readlines()[0]
print(re)