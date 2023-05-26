import requests

params = {'username': '11111111', 'email': 'example@2223324ьж2дло4д23ж4оч.ru', 'password': '1234'}
result = requests.post('http://127.0.0.1:5000/login', json=params)
print(result.json())
