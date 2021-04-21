import requests

name = input("Ваше имя: ")

while True:
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json = { 'name': name, 'text': input()}
    )

# response = requests.get(
#     'http://127.0.0.1:5000/status'
# )
#
# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.json())