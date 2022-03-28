import pandas as pd
import csv
import urllib3
medals_url = "http://winterolympicsmedals.com/medals.csv"

http = urllib3.PoolManager()
r = http.request('GET',medals_url)

lines = r.data.decode('utf-8').split('\n')
col_names = lines[0].split(',')

counter = 0
main_dict = {}
for col in col_names:
    main_dict[col] = []

for line in lines:
    if counter > 0:
        values = line.strip().split(',')
        for i in range(len(col_names)):
            main_dict[col_names[i]].append(values[i])
    counter +=1
df = pd.DataFrame(main_dict)
print(df.head())

