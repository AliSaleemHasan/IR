from pkgutil import get_data
from pydoc import doc
from typing_extensions import Self
import pandas as pd
class DataSetOperations:

    def __init__(self,files):
        self.documents={}
        self.queries = {}
        self.relations= {}
        for path,type in files.items():
            if type  == 'rel':
              self.preprocess_rel(path)
            else :
                self.preprocess_docs(path,type)
            

            


    def preprocess_docs(self,filepath,type = 'docs'):
        data = open(filepath)        
        # remove \n from lines 
        lines = ""
        for line in data:
            if line.startswith('.'):
                lines = lines + '\n' + line.strip()
            else :
                lines = lines + ' ' + line.strip()
        
        
    
        # removing indecators (.I,.A,.B,.T)
        docs = {}
        doc_id = 0
        for line in lines.split('\n'):
            if line.startswith('.I'):
                line_words = line.split(' ')
                doc_id = line_words[1]
                docs[doc_id] = ' '.join(line_words[1:])
            elif (line.startswith('.') and line.startswith('.X') == False ) :
                stripped_line = line.lstrip('.').split(' ')
                docs[doc_id] +=" " + ' '.join(stripped_line[1:])


        if type == 'docs':
            self.documents= docs
        else :
            self.queries = docs

        data.close()


    def preprocess_rel(self,filepath):
        data = pd.read_csv(filepath,sep=' ',header=None,on_bad_lines='skip')
        first_two = data.iloc[:,:2]
        first_two.columns=['que_id','doc_id']
        self.relations= first_two
    


 




            
     


        

        