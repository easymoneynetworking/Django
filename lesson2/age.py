def age():
	a = int(input("Сколько вам лет ?"))
	if a in range (0,19):
		print('school')
	elif a <= 23:
		print('univercity')
	else:
		print('work')
age()
