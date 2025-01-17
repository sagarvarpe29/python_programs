number = int(input('Please enter the number you want to make Factorial of it!\n'))

fact = 1
for i in range(1, number+1):
    fact = fact * i

print('Factorial of', number, 'is:', fact)