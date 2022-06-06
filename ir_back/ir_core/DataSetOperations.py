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
        f = open(filepath,"r")
        c =  f.readlines();x=[];first_two={};count=1
        for i in c:
            i = i.split()
            if(int(i[0]) == count):
                x.append(i[1])
            else:
                first_two[count] = x
                x=[]
                count=int(i[0])
                x.append(i[1])

        first_two[int(i[0])] = x
        self.relations= first_two







            
     


        

        