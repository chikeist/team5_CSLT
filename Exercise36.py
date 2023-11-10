cc = input('Enter a lowercase letter of the alphabet (a, b, c,...): ')

if cc == 'a' or cc == 'e' or cc == 'i' or cc == 'o' or cc == 'u':
    print(cc, 'entered letter is vowel')
elif cc == 'y':
    print( 'sometimes y is vowel, and sometimes y is a consonant')
else:
    print(cc, 'entered letter is consonant')
    