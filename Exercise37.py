number = int(input('Enter number of sides of the shape: '))

if 3 <= number <= 10:
    if number == 3:
        hinh = 'triangle'
    elif number == 4:
        hinh = 'quadrilateral'
    elif number == 5:
        hinh = 'pentagon'
    elif number == 6:
        hinh = 'hexagon'
    elif number == 7:
        hinh = 'heptagon'
    elif number == 8:
        hinh = 'octagon'
    elif number == 9:
        hinh = 'nonagon'
    else:
        hinh = 'decagon'
    print('A shape with', number, 'sides is a', hinh)
else:
    print('Error!') 