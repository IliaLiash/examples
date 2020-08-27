num = int(input())

if (num > 36) or (num < 0):
	print('ошибка ввода')

if num == 0:
	print('зеленый')

if 1 <= num <= 10:
	if num % 2 != 0:
		print('красный')
	else:
		print('черный')

elif 11 <= num <= 18:
	if num % 2 != 0:
		print('черный')
	else:
		print('красный')

elif 19 <= num <= 28:
	if num % 2 != 0:
		print('красный')
	else:
		print('черный')

elif 29 <= num <= 36:
	if num % 2 != 0:
		print('черный')
	else:
		print('красный')
