import requests

resp = requests.post(
    "http://localhost:5000/form",
    params={"a": "b"},
    data={"c": "d"}
)
# resp = requests.get("http://localhost:5000/echo", params={"a": "b"})
data = resp.json()
print(data)
