import requests
from pathlib import Path
import os

def printElem(el):
    print("{")
    for k in el.keys():
        if type(el.get(k)) is dict:
            print(f"   \"{k}\": ")
            printElem(el.get(k))

        else:
            print(f"   \"{k}\": {el.get(k)}, ")
    print("},")

r1 = requests.get("https://jsonplaceholder.typicode.com/posts")
r2 = requests.get("https://jsonplaceholder.typicode.com/photos")

posts = r1.json()
photos = r2.json()

for post in posts:
    i = 0
    while i < len(photos):
        if photos[i].get("id") == post["id"]:
            post["photos"] = photos[i]
            break
        i += 1

def rmdir(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()

print("Removing...")
for i in range(15, 101):
    rmdir(Path(str(i)))

'''
for post in posts:
    #printElem(post)
    dirName = str(post.get("id"))
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


i = 0
for post in posts:
    i += 1
    printElem(post)
    photo = post.get("photos")
    url1 = photo.get("url")
    url2 = photo.get("thumbnailUrl")
    dirID = post.get("id")
    response1 = requests.get(url1)
    response2 = requests.get(url2)

    file = open(str(dirID) + "/" + str(i) + ".png", "wb")
    file.write(response1.content)
    file.close()

    i += 1

    file = open(str(dirID) + "/" + str(i) + ".png", "wb")
    file.write(response2.content)
    file.close()
'''