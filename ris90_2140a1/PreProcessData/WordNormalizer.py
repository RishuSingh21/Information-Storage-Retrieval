from nltk.stem.snowball import SnowballStemmer

import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordNormalizer:

    def __init__(self):
        #stemmer requires a language parameter
        self.stemmer = SnowballStemmer(language='english')
        return

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        word = word.lower()
        return word

    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        word = self.stemmer.stem(word)
        return word
