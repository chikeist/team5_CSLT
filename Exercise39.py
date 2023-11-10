level = int(input('Enter decibel level (dB): '))

if level == 130:
    noise = 'Jackhammer'
elif level == 106:
    noise = 'Gas lawnmower'
elif level == 70:
    noise = 'Alarm clock'
elif level == 40:
    noise = 'Quiet room'
elif 106 < level < 130:
    noise = 'The level is between Jackhammer va Gas lawnmower'
elif 70 < level < 106:
    noise = 'The level is between Gas lawnmower va Alarm clock'
elif 40 < level < 70:
    noise = 'The level is between Alarm clock va Quiet room'
elif level > 130: 
    noise = 'Larger than Jackhammer'
else:
    noise = 'Smaller than Quiet room'

print(noise)
