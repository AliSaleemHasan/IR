from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import word_tokenize
from os.path import exists
from textblob import TextBlob
import string



import datefinder

from pyparsing import Word
class DataProccessing:
    

    def __init__(self,data,to=None):
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer() 
        self.stop_words =open("ir_back/ir_core/data_sets/cacm/common_words",'r').read()
        self.tokenizer = word_tokenize
        self.tagger= pos_tag
        self.data =data
        
        if to != None:
          self.save_to_file(filepath=to)

        

    def tokanize_words(self,data):       
        data = self.tokenizer(data.lower())
        return data
    

    


    def stemm_words(self,data):
        data = [self.stemmer.stem(w) for w in data if w not in self.stop_words ]
        return data 
    
    
    def lemmatize_words(self,data):
        tagged_data = self.tagger(data)
        data = []
        for word,tag in tagged_data:
            if tag.startswith('J'):
                data.append(self.lemmatizer.lemmatize(word,pos='a'))
            elif tag.startswith('V') or tag.startswith('N') or tag.startswith('R'):
                data.append(self.lemmatizer.lemmatize(word,pos=tag[0].lower()))
            else:
                data.append(self.lemmatizer.lemmatize(word))
        return data
    


 
    def parse_dates(self,data):
        natches = datefinder.find_dates(data, source=True)
        for match in natches:
          if len(match[1]) >= 6:
            data =data.replace(match[1] , str(match[0].date()))
        return data


    

    def gather_stirng(self,data):
        data = ' '.join([w for w in data])
        return data 
    

    
    def correct_sentence(self,data):
        sentence = TextBlob(data)
        result = sentence.correct()
        return result



    def save_to_file(self,filepath):
        file_exists = exists(filepath)
        docs = ""
        if(file_exists):
            print("Already Done preprocessing on this data")
            return 
        for key,value in self.data.items():
            data = self.tokanize_words(value)

            data = self.lemmatize_words(data)
            
            data = self.stemm_words(data)

            data = self.gather_stirng(data)

            data = self.parse_dates(data)
            docs += "\n.I " + str(key) + " \n"
            docs += data
        
        f = open(filepath, "w")
        f.write(docs)
        f.close

    def process_query(self):
            data = self.correct_sentence(self.data)
            data = self.tokanize_words(str(data))
            data = self.lemmatize_words(data)
            data = self.stemm_words(data)            
            data = self.gather_stirng(data)
            data = self.parse_dates(data)
            return data



            




        

    




    
    


