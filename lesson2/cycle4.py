school  = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '3a', 'scores': [3,4,5,3]}, {'school_class': '2a', 'scores': [3,4,4,5,2,5,5]}, {'school_class': '1a', 'scores': [2,3,3,4,4,4,5,2]}]
all_score =0
cout_ocenki =0
for school_class in school:
	score_class = 0
		for i in school_class['score']:
			score_class += i
			all_score +=i
print("класс {} - средняя оценка {}".format(school_class['school_class'], score_class/ len(school_class['score']))
print("среднее по всей школе {}".format(all_score / count_ocenki))