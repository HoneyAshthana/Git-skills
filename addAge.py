name = raw_input('Enter your good name : ')
age = int(raw_input('Enter your present age : '))
print 'Year in which ' ,name ,' will turn 100 years is' ,(2017 + (100-age))
times = int(raw_input("Enter no times you want to print the above message :"))
for i in range(times):
    print 'Year in which ', name, ' will turn 100 years is', (2017 + (100 - age))