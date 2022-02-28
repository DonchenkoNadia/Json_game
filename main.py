import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")
print(r.json())
temp_list = r.json()
c = {}
f = open('test5.json', 'w')

for i in temp_list:
    f.write("{\n")
    f.write(f"   \"userID\": {i.get('userId', 0)}, \n")
    f.write(f"   \"id\": {i.get('id', 0)}, \n")
    f.write(f"   \"title\": \"{i.get('title', 0)}\", \n")
    tmp_str = i.get('body', "")
    new_str = tmp_str.replace("\n", " ")

    f.write(f"   \"body\": \"{new_str}\" \n")
    f.write("},\n")
    #print(i[id])
    cur_id = i.get('userId', 0)
    if cur_id not in c:
        c[cur_id] = 1
    else:
        c[cur_id] += 1
f.close()