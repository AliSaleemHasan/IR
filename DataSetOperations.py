from pydoc import doc
import pandas as pd
class DataSetOperations:
    data = []
    documents= {}
    relations = {}
    queries ={}
   


    def get_data(self,filepath,type = 'text'):
        if type == "csv":
            self.data = pd.read_csv(filepath,sep=' ',header=None,on_bad_lines='skip')
        else :
            data = open(filepath)
            self.data= data
            data.close()
        
        return self
    
    def preprocess_docs(self,type='doc'):

        # remove \n from lines 
        lines = ""
        for line in self.data:
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
        if type == 'doc':
            self.documents=docs
        else :
            self.relations= docs
        return self

    def preprocess_rel(self):
        first_two = self.data.iloc[:,:2]
        first_two.columns=['que_id','doc_id']
        self.queries = first_two
        return self
    

    def get_preprocessed_data(self):
        return (self.documents,self.queries,self.relations)
    
    



            
     


        

        