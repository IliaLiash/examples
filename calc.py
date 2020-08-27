a = int(input())
b = int(input())
arifm = str(input())

if arifm == '*':
	print(a * b)
elif arifm =='/' and b == 0:
	print('На ноль делить нельзя!')
elif arifm == '/':
	print(a / b)
elif arifm == '+':
	print(a + b)
elif arifm =='-':
	print(a - b)
else:
	print('Неверная операция')
