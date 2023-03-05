import random

"""Word Finder: finds random words from a dictionary."""

    


class WordFinder:
    ...
    def __init__(self):
        self.words = []
    def read_file(self):
        file = open("words.txt", "r")
        for word in file:
            self.words.append(word.rstrip('\n'))
        file.close()
        return f"{len(self.words)} words read"

    def random(self):
        self.read_file()
        rand = random.randrange(0,len(self.words))
        return self.words[rand]

    
