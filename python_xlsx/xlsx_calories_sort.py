import xlrd, xlwt
#открываем файл
rb = xlrd.open_workbook('trekking1.xlsx')

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
        
#записываем в словарь калорийность:продукт. Если в словаре уже есть калорийность - дописываем через ","        
for i in range(1,len(sheet.col_values(0))):
    if sheet.col_values(1)[i] in results:
        results[sheet.col_values(1)[i]] +=(', '+sheet.col_values(0)[i])
    else:
        results[sheet.col_values(1)[i]] = sheet.col_values(0)[i]
        
#сортируем словарь по ключу-калорийности. Из значений по ключу делаем список, который тоже сортируем
for k, v in sorted(results.items(), reverse=True):
    v = sorted(v.split(', '))  
    print(('\n').join(v))