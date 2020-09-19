import requests
import json
import operator

client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": '7a627cb3befd350c78da',
                      "client_secret": 'b15aaa3d7d8b8f2b3e8086321a1d4517'
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

#открываем файл и считываем из него строки в список
with open ("dataset_24476_4.txt","r") as f:
    x = f.read()
    x = x.splitlines()
    print(x)

artists = {}
    
for id_name in x:
    
    # инициируем запрос с заголовком    
    r = requests.get("https://api.artsy.net/api/artists/{}".format(id_name), headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)
    
    #добавляем в словарь пару ключ-значение (Художник - Год)
    artists[j['sortable_name']] = j['birthday']  
    
#сортируем словарь по значения ключей, после цикла
sorted_artists = sorted(artists.items(), key=operator.itemgetter(1))    

for artist in sorted_artists:
    print(artist[0])