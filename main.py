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

