day = int(input('Enter day: '))
month = input('Enter month: ')
holiday = 'does not correspond to fixed holidays.'

if day == 1 and month == 'January':
    name = 'is New years day'
elif day == 1 and month == 'July':
    name = 'is Canada day'
elif day == 25 and month == 'December':
    name = 'is Christmas day'
else:
    name = holiday
    
print(month, day, name)