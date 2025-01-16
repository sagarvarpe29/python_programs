def remainder_division(a,b):
    if b==0:
        #raise ZeroDivisionError
        raise Exception('Divisor cannot be 0')
    result = a//b
    reminder = a%b
    print(a,'/',b, 'is', result,'remainder',reminder)

remainder_division(10,0)