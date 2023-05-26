import requests

params = {'email': 'example@mail.ru', 'password': '1234'}
result = requests.post('http://127.0.0.1:5000/register', json=params)
print(result)
