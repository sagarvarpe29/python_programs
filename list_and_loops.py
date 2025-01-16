expenses = [11,90,34,56,32,89,53,21]
sumtest = 0
for x in expenses:
    sumtest = sumtest + x
print('You spent $', sumtest, sep = '')

#or

total = sum(expenses)
print("You spent $", total, sep = '')