stolb1 = int(input())
stroka1 = int(input())
stolb2 = int(input())
stroka2 = int(input())

if (stolb1 - 1 <= stolb2 <= stolb1 + 1) and (stroka1 - 1 <= stroka2 <= stroka1 + 1):
	print('YES')
else:
	print('NO')
