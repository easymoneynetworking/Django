school  = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '3a', 'scores': [3,4,5,3]}, {'school_class': '2a', 'scores': [3,4,4,5,2,5,5]}, {'school_class': '1a', 'scores': [2,3,3,4,4,4,5,2]}]
for item in otmetki:
    scores = 0
    for i in item[“scores”]:
        scores += i
    print(scores/len(item[“scores”])