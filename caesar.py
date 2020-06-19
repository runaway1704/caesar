def code(value, shift):
    c = []
    for letter in value:
        if letter == chr(32):
            letter = chr(ord(letter))
        else:
            letter = chr((ord(letter) - 19 + shift) % 26 + 97)
        c.append(letter)
    return c


def decode(value, shift):
    d = []
    for letter in value:
        if letter == chr(32):
            letter = chr(ord(letter))
        else:
            letter = chr((ord(letter) - 19 - shift) % 26 + 97)
        d.append(letter)
    return d


while True:
    action = input('Code or decode: ').lower()
    value = input("Your value here: ").lower()
    shift = int(input('Enter shift: '))
    if action == 'code':
        print(code(value, shift))
    elif action == 'decode':
        print(decode(value, shift))
