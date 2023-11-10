print('Enter the lengths of 3 sides of a triangle:')
a = float(input(''))
b = float(input(''))
c = float(input(''))

if (a + b > c) and (a + c > b) and (b + c > a) and (a> 0) and (b > 0) and (c > 0) :
    if a == b and a != c or b == c and b != a or c == a and c != b:
        print('Isosceles triangle')
    elif a == b and b == c:
        print('Equilateral triangle')
    else:
        print('Scalene triangle')
else :
    print('Error!')