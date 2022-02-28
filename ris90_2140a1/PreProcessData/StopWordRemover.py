import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.
        
        #opening and reading stopword.text file
        file = open(Path.StopwordDir,'r')
        
        #used splitlines() function to create a list of stop words
        self.stopwords = file.read().splitlines()
        
        #closing the file
        file.close()
        return

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.
        for entry in self.stopwords:
            
            #Checking word for stop words
            if( word == entry):
                return True
        return False
