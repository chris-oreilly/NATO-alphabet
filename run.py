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

def infinite_shuffle(items):
    while True:
        yield from random.sample(items, len(items))

if __name__ == '__main__':
    for letter, code_word in infinite_shuffle(alphabet.items()):
        try:
            answer = input(letter.upper() + ': ')
            if answer.strip().lower() == code_word:
                print('Right')
            else:
                print('Wrong:', code_word.title())
            print()
        except EOFError:
            # quit gracefully
            print()
            break
