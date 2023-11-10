n = int(input('Human year: '))

if n >= 0:
    if n <= 2:
        c =  n*10.5       
    else:
        c = 21 + 4*n - 8
    print('Dog year: ' + str(c))
else:
    print('Error')