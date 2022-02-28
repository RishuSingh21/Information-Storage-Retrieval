import re
import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.
        
        #used Findall function of 're' to get the words composed of alphabets (small & capital)
        self.content = re.findall('[a-zA-Z]+',content)
        
        #I created count variable to iter through the word list
        self.count=0
        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        
        #incrementing count to give the next word
        self.count = self.count+1
        word = ""
        
        #Checking for end of the list
        if(self.count >= len(self.content)):
            return None
        
        #else returning next word
        else:
            word = self.content[self.count]
        return word