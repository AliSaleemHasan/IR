from nltk.stem import WordNetLemmatizer
import datefinder
import datefinder

from pyparsing import Word
class DataProccessing:
    

    def __init__(self,data,stemmer,tokenizer,stop_words,tagger,w_corrector):
        self.stemmer = stemmer
        self.lemmatizer = WordNetLemmatizer() 
        self.stop_words = stop_words
        self.tokenizer = tokenizer
        self.tagger= tagger
        self.w_corrector= w_corrector
        self.data = data

    def tokanize_words(self):
        data = self.tokenizer(self.data.lower())
        self.data = data
        return data


    def stemm_words(self):
        data = [self.stemmer.stem(w) for w in self.data if w not in self.stop_words]
        self.data = data 
        return data
    
    def lemmatize_words(self):
        tagged_data = self.tagger(self.data)
        data = []
        for word,tag in tagged_data:
            if tag.startswith('J'):
                data.append(self.lemmatizer.lemmatize(word,pos='a'))
            elif tag.startswith('V') or tag.startswith('N') or tag.startswith('R'):
                data.append(self.lemmatizer.lemmatize(word,pos=tag[0].lower()))
            else:
                data.append(self.lemmatizer.lemmatize(word))
        self.data=data
        return data 

 
    def parse_dates(self):
        natches = datefinder.find_dates(self.data, source=True)
        for match in natches:
          if len(match[1]) >= 6:
            self.data = self.data.replace(match[1] , str(match[0].date()))
        return self.data


    def correct_words(self):
        data = [self.w_corrector(w) for w in self.data]
        self.data = data 
        return data 
    

    def gather_stirng(self):
        data = ' '.join([w for w in self.data])
        self.data = data 
        return data 
    





    
    



