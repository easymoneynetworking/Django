def get_summ(num_one, num_two):
	try:
		num_one = int(num_one)
		num_two = int(num_two)
		return num_one + num_two
	except ValueError:
		pass
if __name__ == "__main__":	
print(get_summ(1 , 2))