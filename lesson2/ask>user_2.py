def ask_user(dct):
	question=""
	
	while question not in dct:
		try:
			question = input(" Задай вопрос ")
			if question in dct:
				print(dct[question])
		except KeyboardInterrupt:
			print("Пока")
			break


dct = {"Как дела": " Хорошо " , "ЧТо делаешь?": "Программирую"}
print(ask_user(dct))