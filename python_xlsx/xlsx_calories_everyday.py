'''
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с указанием калорийности на 100 грамм,
а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю).
Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой.
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx 

Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и его количества в граммах.
Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел.
'''





import xlrd, xlwt
#открываем файл
rb = xlrd.open_workbook('trekking2.xlsx')
results = {}

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#получаем список значений из всех записей построчно
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

#если в таблице пустая ячейка - записываем в нее 0
for element in vals[1:]:
    for cell in element[1:]:
        if cell == '':
            cell += '0' 
        cell = float(cell)
     
#записываем в словарь продукт:калорийность, белки, жиры, углеводы.        
for i in range(1,len(sheet.col_values(0))):
        results[sheet.col_values(0)[i]] = [sheet.col_values(1)[i], sheet.col_values(2)[i], sheet.col_values(3)[i], sheet.col_values(4)[i]]

#переходим на второй лист
raskladka = rb.sheet_by_index(1)
vals_raskladka = [raskladka.row_values(rownum) for rownum in range(raskladka.nrows)]
raskl_dict = {}

#добавляем в словарь пары продукт:граммы потребления, учитывая повторяющиеся значения
for i in range(1,len(raskladka.col_values(0))):
    if raskladka.col_values(0)[i] in raskl_dict:
        raskl_dict[raskladka.col_values(0)[i]] += float(raskladka.col_values(1)[i]/100)
    else:
        raskl_dict[raskladka.col_values(0)[i]] = float(raskladka.col_values(1)[i]/100)

#готовим ответ, записываем его в ans
ans = [0, 0, 0, 0]

#если ключ в суточной норме потребления - ищем его в таблице калорий и умножаем К, Б. Ж, У на суточную норму потребления
for k in raskl_dict.keys():
    if k in results:
        ans[0] += (results[k][0] * float(raskl_dict[k]))
        ans[1] += (results[k][1] * float(raskl_dict[k])) 
        ans[2] += (results[k][2] * float(raskl_dict[k]))
        ans[3] += (results[k][3] * float(raskl_dict[k]))

#округление вниз до ближайшего целого        
for i in range(len(ans)):
    ans[i] = int(ans[i])
    
print(ans)
