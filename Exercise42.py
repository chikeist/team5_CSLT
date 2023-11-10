tanso = float(input("Enter the frequency: "))  

tan_so_note = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88
}

note_gan_nhat = None

if abs(tanso - tan_so_note['C4']) <= 1:
    note_gan_nhat = 'C4'
elif abs(tanso - tan_so_note['D4']) <= 1:
    note_gan_nhat = 'D4'
elif abs(tanso - tan_so_note['E4']) <= 1:
    note_gan_nhat = 'E4'
elif abs(tanso - tan_so_note['F4']) <= 1:
    note_gan_nhat = 'F4'
elif abs(tanso - tan_so_note['G4']) <= 1:
    note_gan_nhat = 'G4'
elif abs(tanso - tan_so_note['A4']) <= 1:
    note_gan_nhat = 'A4'
elif abs(tanso - tan_so_note['B4']) <= 1:
    note_gan_nhat = 'B4'
if note_gan_nhat: 
    print("Frequency", int(tanso), "corresponds to musical notes", note_gan_nhat)
else:
    print("Frequency", int(tanso), "does not correspond to any known musical note!")