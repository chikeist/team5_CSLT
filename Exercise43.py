money = int(input('Enter the dollar denomination ($): '))

if money == 1 or money == 2 or money == 5 or money == 10 or money == 20 or money == 50 or money == 100:
    if money == 1:
        name = 'George Washington'
    elif money == 2:
        name = 'Thomas Jefferson'
    elif money == 5:
        name = 'Abraham Lincoln'
    elif money == 10:
        name = 'Alexander Hamilton'
    elif money == 20:
        name = 'Andrew Jackson'
    elif money == 50:
        name = 'Ulysses S. Grant'
    elif money == 100:
        name = 'Benjamin Franklin'
    print('The character on the banknote ' + str(money) + '$ is', name) 
else:
    print('There is no corresponding character.')
