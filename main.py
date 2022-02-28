import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")

posts = r.json()
res = []

for post in posts:
    res.append([post.get("email"), post.get("body")])

for r in res:
    print(r)