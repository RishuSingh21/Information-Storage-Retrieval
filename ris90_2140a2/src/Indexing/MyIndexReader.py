import Classes.Path as Path
import json
from nltk.stem.snowball import SnowballStemmer

# Efficiency and memory cost should be paid with extra attention.
class MyIndexReader:

    def __init__(self, type):
        
        #Check data type to open relevant files for reading
        self.type = type
        
        #Case1: open files related to trectext for reading
        if self.type == "trectext":
            
            #Open Term Index file
            with open(Path.IndexTextDir+"TextTermIndex.txt",'r') as f:
                self.term_index = f.read()
                self.term_js = json.loads(self.term_index)
        
            #Open Posting/Document Index file
            with open(Path.IndexTextDir+"TextDocIndex.txt",'r') as file:
                self.doc_index = file.read()
                self.js = json.loads(self.doc_index)
        
        #Case2: open files related to trectext for reading
        else:
            
            #Open Term Index file
            with open(Path.IndexWebDir+"WebTermIndex.txt",'r') as f:
                self.term_index = f.read()
                self.term_js = json.loads(self.term_index)
                
            #Open Posting/Document Index file    
            with open(Path.IndexWebDir+"WebDocIndex.txt",'r') as file:
                self.doc_index = file.read()
                self.js = json.loads(self.doc_index)
        print("finish reading the index")

    # Return the integer DocumentID of input string DocumentNo.
    def getDocId(self, docNo):
        for doc_no, doc_id in self.js.items():
            if docNo == doc_no:
                return doc_id

 

    # Return the string DocumentNo of the input integer DocumentID.
    def getDocNo(self, docId):
        for doc_no, doc_id in self.js.items():
            if int(docId) == doc_id:
                return doc_no
 
 
    
    # Return DF.
    def DocFreq(self, token):
        
        #First we will stem the given token word as we have stemmed our words in Index as well
        self.stemmer = SnowballStemmer(language='english')
        token = token.lower()
        token = self.stemmer.stem(token)
        
        #Check for existence of the token word in the Index
        if self.term_js.get(token)!= None:
            
            #Case1: Token word is in the Index. 
            #freq_list will store the dictionary {doc_id:freq}
            freq_list = self.term_js[token].values()
            
            #To count how many documents contain the token word
            freq = len(freq_list)
        
        #Case2: Token word is not in the Index
        #freq = 0 i.e. 0 documents contain the token word
        else:
            freq = 0
        return (freq)

    
    
    # Return the frequency of the token in whole collection/corpus.
    def CollectionFreq(self, token):
        
        #col_freq is a variable to calculate the collection frequency of the token
        col_freq=0
        
        #First we will stem the given token word as we have stemmed our words in Index as well
        self.stemmer = SnowballStemmer(language='english')
        token = token.lower()
        token = self.stemmer.stem(token)
        
        #Case1: if the token word is in the Index
        if self.term_js.get(token)!= None:
            freq_list = self.term_js[token].values()
            for i in freq_list:
                col_freq += i
        return (col_freq)

    
    
    # Return posting list in form of {documentID:frequency}.
    def getPostingList(self, token):
        
        #doc_freq is a dictionary variable: {doc_is: freq}
        doc_freq={}
        
        #First we will stem the given token word as we have stemmed our words in Index as well
        self.stemmer = SnowballStemmer(language='english')
        token = token.lower()
        token = self.stemmer.stem(token)
        
        #Case1: if the token word is in the Index
        if self.term_js.get(token)!= None:
            doc_list = self.term_js[token]
            for k,v in doc_list.items():
                doc_freq[k]=v
        return doc_freq
