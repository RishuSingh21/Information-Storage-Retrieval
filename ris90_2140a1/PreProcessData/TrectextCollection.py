from bs4 import BeautifulSoup
import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class TrectextCollection:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!
        
        #opening and reading trectext file
        with open(Path.DataTextDir, 'r') as f:
            data = f.read() 
            
        #Spliting document on </DOC> and creating a doc list to store and iter through it    
        self.dataList = data.split('</DOC>')
        
        #I created count variable to iter through the doc list 
        self.count=0
        return

    
    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        docNo = ""
        content = ""
        
        #reading a document with BeautifulSoup
        bs_soup = BeautifulSoup(self.dataList[self.count],'xml')
        
        #Checking for end of document list.
        #Case: When no document left
        if(self.count==len(self.dataList)-1):
            return None
        
        #Case: When there are documents to read
        docNo = bs_soup.find('DOCNO').text
        content = bs_soup.find('TEXT').text
        
        #incrementing count to iter through the document list
        self.count = self.count+1
        return [docNo, content]