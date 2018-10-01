def ask_user(dct):
	question=0
	while question not in dct:
		question = input(" Задай вопрос ")
	else:
		return dct[question]

dct = {"Как дела": " Хорошо " , "ЧТо делаешь?": "Программирую"}
print(ask_user(dct))