import random

alphabet = {
    'a': ('alfa', 'alpha'),
    'b': ('bravo', ),
    'c': ('charlie', ),
    'd': ('delta', ),
    'e': ('echo', ),
    'f': ('foxtrot', ),
    'g': ('golf', ),
    'h': ('hotel', ),
    'i': ('india', ),
    'j': ('juliett', 'juliet'),
    'k': ('kilo', ),
    'l': ('lima', ),
    'm': ('mike', ),
    'n': ('november', ),
    'o': ('oscar', ),
    'p': ('papa', ),
    'q': ('quebec', ),
    'r': ('romeo', ),
    's': ('sierra', ),
    't': ('tango', ),
    'u': ('uniform', ),
    'v': ('victor', ),
    'w': ('whiskey', ),
    'x': ('x-ray', 'xray'),
    'y': ('yankee', ),
    'z': ('zulu', ),
}

def infinite_shuffle(items):
    while True:
        yield from random.sample(items, len(items))

def check_response(response, answers):
    def normalize(str):
        return str.strip().lower()
    return normalize(response) in map(normalize, answers)

if __name__ == '__main__':
    for letter, code_words in infinite_shuffle(alphabet.items()):
        try:
            response = input(letter.upper() + ': ')
            if check_response(response, code_words):
                print('Right')
            else:
                print('Wrong:', code_words[0].title())
            print()
        except EOFError:
            # quit gracefully
            print()
            break
