note_musical = input("Enter the name of the note musiccal: ")
note = note_musical[0]
interval = int(note_musical[1:5])

if (note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B') and 0 <= interval <= 8:
    if note == 'C':
        frequency = 261.63
    elif note == 'D': 
        frequency = 293.66
    elif note == 'E':
        frequency = 329.63
    elif note == 'F':
        frequency = 349.23
    elif note == 'G':
        frequency = 392.00
    elif note == 'A':
        frequency = 440.00
    elif note == 'B':
        frequency = 493.88
        
    f = frequency / (2 ** (4 - interval))
    print("Frequency of musical notes", note_musical, "is", f, "Hz")
else:
    print("Error!")