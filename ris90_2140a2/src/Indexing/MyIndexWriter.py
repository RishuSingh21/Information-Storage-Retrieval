#for referencing the path of the files
import Classes.Path as Path

#to write a dictionary in a file
import json

# Efficiency and memory cost should be paid with extra attention.
class MyIndexWriter:
    doc_id = 1
    
    def __init__(self, type):
        self.type = type
        self.doc = open(Path.ResultHM1 + self.type, 'r')
        self.term_index={}
        self.doc_index={}
        return

    # This method build index for each document.
	# NT: in your implementation of the index, you should transform your string docno into non-negative integer docids,
    # and in MyIndexReader, you should be able to request the integer docid for each docno.
    def index(self, docNo, content):
        #creating index to keep a record of doc_id and docNo
        self.doc_index[docNo] = self.doc_id
        
        #Creating term index {term:{doc_id:freq}}
        doc_content = content.split(" ")
        for i in range(0,len(doc_content)-1):
            term = doc_content[i]
            
            #Case1: term is in Index
            if self.term_index.get(term)!=None:
                
                #Case1.1: term is in Index & Doc_id is in Index
                #Action: Increase the term frequency by 1
                if self.doc_id in self.term_index[term].keys(): 
                    self.term_index[term][self.doc_id] += 1
                
                #Case1.2: term is in Index & Doc_id is not in Index
                #Action: Add doc_id with the term frequency set as 1
                else:
                    self.term_index[term][self.doc_id] = 1   
            
            #Case2: term is not in the Index
            #Action: Add the term in the dictionary with the corresponding doc_id and term frequency set as 1
            else:    
                self.term_index[term]={}
                self.term_index[term][self.doc_id] = 1
        
        #Incrementing doc_id for the next document
        self.doc_id += 1    
        return





    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):

        #for writing term index and posting index for the data type trectext
        if self.type == 'trectext':
            #Writing Term Index
            with open(Path.IndexTextDir+"TextTermIndex.txt",'w+') as file:
                file.writelines(json.dumps(self.term_index))
 
            #Writing posting index
            with open(Path.IndexTextDir+"TextDocIndex.txt","w+") as file1:
                file1.writelines(json.dumps(self.doc_index))
        
        #for writing term index and posting index for the data type trectext
        else:
            #Writing Term Index
            with open(Path.IndexWebDir+"WebTermIndex.txt",'w+') as file:
                file.writelines(json.dumps(self.term_index))
            
            #Writing posting index
            with open(Path.IndexWebDir+"WebDocIndex.txt","w+") as file1:
                file1.writelines(json.dumps(self.doc_index))
         
        return
