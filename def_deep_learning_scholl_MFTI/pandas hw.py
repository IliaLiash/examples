import numpy as np
import pandas as pd

data = pd.read_csv('BlackFriday.csv')
#Сколько всего возрастных категорий?  
#print(data['Age'].value_counts())
#Сколько строк с мужчинами из категории города A? (речь не об уникальных ID мужчин, а о количестве строк)
#print(data[data['Gender'] == 'M']['City_Category'].value_counts())
#Сколько женщин от 46 до 50, потративших (столбец Purchase) больше 20000 (условных единиц, в данном случае)?
#print(len(data[(data['Age']=='46-50') & (data['Gender'] == 'F') & (data['Purchase']>20000)]))
#Сколько NaN'ов в столбце Product_Category_3?
#print(data['Product_Category_3'].isna().sum())


a = len(data[(data['Age'] == '26-35') & (data['Gender'] == 'M')])
b = len(data[(data['Age'] > '36') & (data['Gender'] == 'F')])

print((a + b) / len(data))