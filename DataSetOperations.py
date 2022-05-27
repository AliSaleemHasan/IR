from pkgutil import get_data
from pydoc import doc
from typing_extensions import Self
import pandas as pd
class DataSetOperations:
    documents = {}
    queries = {}
    relations = {}

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
                doc_id = line.split(' ')[1]
                docs[doc_id] = {}
                
            elif line.startswith('.') and line.startswith('.X') == False:
                stripped_line = line.lstrip('.').split(' ')
                docs[doc_id][stripped_line[0]] =' '.join(stripped_line[1:])
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
    


 




            
     


        

        