import requests


resp_1 = requests.get(url="http://127.0.0.1:3000/api/courses/0")
print(resp_1.json())

resp_2 = requests.post(url="http://localhost:3000/api/courses/4", json={"name": "Golang", "videos": 5})
print(resp_2.json())


resp_3 = requests.delete("http://127.0.0.1:3000/api/courses/2")
print(resp_3.json())