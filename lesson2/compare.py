def tt(a,b):
	if type(a) == str() and type(b) == str():
		return 0
	if  a == b:
		return 1
	else:
		if b == "learn":
			return 3
		if len(a) > len(b):
			return 2
a = tt('2','learnr')
print(a)
b = tt('3','learnr')
print(b)