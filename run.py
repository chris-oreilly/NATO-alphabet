import random

alphabet = {
    'a': 'alfa',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu',
}

if __name__ == '__main__':
    while True:
        letter = random.choice(list(alphabet.keys()))

        try:
            answer = input(letter.upper() + ': ')
        except EOFError:
            # quit gracefully
            print()
            break

        if answer.strip().lower() == alphabet[letter]:
            print('Right')
        else:
            print('Wrong:', alphabet[letter].title())
        print()
