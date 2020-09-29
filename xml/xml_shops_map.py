import xmltodict
#открываем файл и считываем его. Задаем словарь.
fin = open('map1.osm', 'r', encoding='utf8')
text = fin.read()
fin.close()

shops = 0
dct = xmltodict.parse(text)
count1 = 0  #счетчик тэг в ноде (нод - тэг, описывающий некоторую точку на карте)
count2 = 0  #счетчик тэг не в ноде
for node in dct['osm']['node']:
    if 'tag' in node:
        count1 += 1
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'shop':
                    shops += 1
                    print(tag)
    else:
        count2 += 1
print(shops)
print(count1)
print(count2)