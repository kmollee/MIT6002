def loadWords(PATH_TO_FILE):
    inFile = open(PATH_TO_FILE, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

loadWords('words.txt')


def loadWords2(PATH_TO_FILE):
    try:
        inFile = open(PATH_TO_FILE, 'r')
    except IOError:
        print("The wordlist doesn't exist; using some fruits for now")
        return ['apple', 'orange', 'pear', 'lime', 'lemon',
                'grape', 'pineapple']
    line = inFile.readline()
    wordlist = line.split(',')
    print("  ", len(wordlist), "words loaded.")
    return wordlist

loadWords2('words2.txt')
loadWords2('doesntExist.txt')
