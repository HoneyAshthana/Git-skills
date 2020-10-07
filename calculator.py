print'YourCalculator'
print 'Enter \n + for addition \n - for subtraction \n * for multiplication \n / for division '
choice = raw_input('Enter choice :')
if choice == '+' or choice == '-' or choice == '*' or choice == '/' :
    no1 = int(raw_input('Enter no 1 :'))
    no2 = int(raw_input('Enter no 2 :'))
    if choice == "+":
        print 'Addition = ',(no1+no2)
    elif choice == '-':
        print 'Subtraction = ' , (no1 - no2)
    elif choice == '*':
        print 'Multiplication = ' , (no1 * no2)
    elif choice == '/':
        print 'Division = ' ,  (no1 / no2)
else:
    print 'Wrong option'
