#Text of challenge: "If we list all the natural numbers below 10 that are multiples
#of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
#all the multiples of 3 or 5 below 1000."


numbers = []
newlist = []

for i in range(1, 1000):
    numbers.append(i)

for number in numbers:
    if number % 3 == 0 or number % 5 == 0:
        newlist.append(number)

total = sum(newlist)

print total
