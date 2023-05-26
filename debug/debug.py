import requests

# params = {'username': '11111111', 'email': 'example@2223324ьж2дло4д23ж4оч.ru', 'password': '1234', 'age':123, 'is_farmer':False}
# result = requests.post('http://127.0.0.1:5000/register', json=params)
# print(result.json())


# params = {'username': '11111111', 'email': 'example@2223324ьж2дло4д23ж4оч.ru', 'password': '1234', 'age':123, 'is_farmer':False}
# result = requests.post('http://127.0.0.1:5000/login', json=params)
# print(result.json())

# result = requests.get('http://127.0.0.1:5000/products')
# print(result.json())

# params = {'product_id': '11111111',
#           'product_name': 'example@2223324ьж2дло4д23ж4оч.ru',
#           'description': '1234',
#           'image': 'path'}
# result = requests.post('http://127.0.0.1:5000/create_product', json=params)
# print(result.json())

result = requests.get('http://127.0.0.1:5000/delete_product', {'id': 123})
print(result.json())