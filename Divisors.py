no = int(raw_input('Enter any no : '))
print 'Divisors of ' ,no , 'are'
for i in range(1,no+1):
    if no%i == 0:
        print i