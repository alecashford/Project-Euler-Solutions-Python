#Text of challenge: "The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385. The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025. Hence the difference between the sum of the squares
#of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640. Find
#the difference between the sum of the squares of the first one hundred natural numbers
#and the square of the sum."


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
