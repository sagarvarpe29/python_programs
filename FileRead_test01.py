with open('input.txt') as file:
    #result = file.read()
    #print(result)

    print('-----------------------------')
    #result1 = file.readlines()
    #for myresult in result1:
    #    print(myresult)

# Since this type of loop is very common, we can instead use file object

    for myresult2 in file:
        print(myresult2)

