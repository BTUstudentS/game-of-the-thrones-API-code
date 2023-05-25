import requests
import json

# 1. requests მოდულის 4 ფუნქცია/ატრიბუტი: get(), status_code, headers, text

# resp = requests.get('https://thronesapi.com/')
# print(resp.status_code)
# print(resp.headers)
# print(resp.text)

# 2. სამეფო კარის თამაშების აპიდან მომაქვს პერსონაჟების სია, რომელსაც ვინახავ json ფაილში სტრუქტურირებულად (dump ფუნქციით).

# url = 'https://thronesapi.com/api/v2/Characters'
# resp = requests.get(url)
#
# if resp.status_code == 200:
#     characters = resp.json()
#     for character in characters:
#         with open('thrones.json', 'w') as file:
#             json.dump(characters, file, indent=4)
# else:
#     print('Error occurred:', resp.status_code)


# 3. json/dict ობიექტთან სამუშაო ფუნქციები: load, loads, dumps

# url = 'https://thronesapi.com/api/v2/Characters'
# resp = requests.get(url)

# result = resp.json()
# print(type(result))
# print(json.dumps(result, indent=4))

# result = json.loads(resp.text)
# print(result)
# print(type(result))

# with open('thrones.json', 'r') as file:
#     result = json.load(file)
#     print(result)


# 4. sqlite მონაცემთა ბაზაში სამეფო კარის პერსონაჟების სიის ჩაწერა.

# url = 'https://thronesapi.com/api/v2/Characters'
# resp = requests.get(url)
# characters = resp.json()
#
# print(characters)
# print(type(characters))


# import sqlite3
#
# conn = sqlite3.connect("thronesdb.sqlite")
# conn.row_factory = sqlite3.Row
# cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS Characters
#             (id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name VARCHAR(20),
#             lastname VARCHAR(30),
#             fullname VARCHAR(50),
#             title VARCHAR(50),
#             family VARCHAR(30),
#             image BLOB,
#             imageUrl TEXT(50))
#             ''')

# for character in characters:
#     cur.execute('''
#         INSERT INTO Characters (name, lastname, fullname, title, family, image, imageUrl)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     ''', (
#         character['firstName'],
#         character['lastName'],
#         character['fullName'],
#         character['title'],
#         character['family'],
#         character['image'],
#         character['imageUrl']
#     ))

# conn.commit()
# conn.close()

# 5. win10toast მოდულით notification-ის მიღება სამეფო კარის თამაშების აპის შესახებ.

# from win10toast import ToastNotifier
#
# resp = requests.get('https://thronesapi.com/api/v2/Characters')
# characters = resp.json()
#
# toaster = ToastNotifier()
# for character in characters:
#     name = character['fullName']
#     title = character['title']
#     message = f"Name: {name}\nTitle: {title}"
#
#     toaster.show_toast("Game of Thrones Character", message, duration=5)
#     toaster.notification_active()
#
# toaster.notification_active()

