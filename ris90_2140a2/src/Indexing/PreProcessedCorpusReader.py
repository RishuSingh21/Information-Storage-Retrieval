import Classes.Path as Path


class PreprocessedCorpusReader:

    def __init__(self, type):
        self.doc = open(Path.ResultHM1 +type, 'r')
        return

    # Read a line for docNo from the corpus, read another line for the content, and return them in [docNo, content].
    def nextDocument(self):
        doc_no = self.doc.readline().strip()
        #print(doc_no)
        #if the end of document then close the document
        if(doc_no == ""):
            self.doc.close()
        
        #Return Doc_no and Content of a Document
        else:
            doc_content = self.doc.readline().strip()
            return [doc_no,doc_content]
    