print'YourCalculator'
print 'Enter \n + for addition \n - for subtraction \n * for multiplication \n / for division '
choice = raw_input('Enter choice :')
if choice=='+'or choice=='-'or choice=='*'or choice=='/':
    no1 = int(raw_input('Enter no 1 :'))
    no2 = int(raw_input('Enter no 2 :'))
    if choice=="+":
        s= (no1+no2)
        print 'Addition = ',s
    elif choice=='-':
        s = (no1 - no2)
        print 'Subtraction = ' , s
    elif choice=='*':
        s = (no1 * no2)
        print 'Multiplication = ' , s
    elif choice =='/':
        s = (no1 / no2)
        print 'Division = ' , s
else:
    print 'Wrong option'
