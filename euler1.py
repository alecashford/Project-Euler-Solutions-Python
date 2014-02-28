numbers = []
newlist = []

for i in range(1, 1000):
    numbers.append(i)

for number in numbers:
    if number % 3 == 0 or number % 5 == 0:
        newlist.append(number)

total = sum(newlist)

print total
