import pandas as pd
import json

df = pd.read_excel('our_data.xlsx')
jsonFile = open("data_sample1.json", "w")

for i in range(1, 5):
    temp = {}
    temp["date"] = str(df.iloc[i][0])
    temp["avg"] = df.iloc[i][1:].mean()
    temp["min"] = df.iloc[i][1:].min()
    temp["max"] = df.iloc[i][1:].max()
    print(i)
    print(temp)
    jsonString = json.dumps(temp)
    jsonFile.write(jsonString)
jsonFile.close()

#print(df.iloc[i][1:].mean())




'''
import requests

from datetime import datetime

url = 'https://reqres.in/api/users'
myobj = {
    "name": "morpheus",
    "job": "leader"
}
ans = []
while len(ans) < 4:
    x = requests.post(url, data = myobj)

    response = x.json()
    dt = response["createdAt"]
    s = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%fZ')
    #print(s.replace(microsecond=0))

    ans.append(response)
    ans[-1]["createdAt"] = s.replace(microsecond=0)

print(ans)
'''
