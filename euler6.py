numberlist = []

def square(list):
    result = [i ** 2 for i in list]
    total = sum(result)
    return total

def sumo(list):
    total = sum(list)
    squaredlist = total ** 2
    return squaredlist

for i in range(1,101):
    numberlist.append(i)

print sumo(numberlist)-square(numberlist)
