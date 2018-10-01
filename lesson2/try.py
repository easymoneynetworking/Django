def cut_cake(parts):
    try:
        return 1/ int(parts)
    except (ZeroDivisionError,TypeError ,ValueError):
        return "С ума посходили?"
cake = cut_cake("het")
#print(cake)

def do_something(x):
    try:
        print(x)
    except:
        print('her')

x = 0
while x < 10:
    do_something(x)
x += 1
