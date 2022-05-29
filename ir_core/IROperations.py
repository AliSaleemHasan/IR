from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
class IROperations:
    def __init__(self,data):
        self.tfidf = TfidfVectorizer()
        self.cosine=cosine_similarity
        self.docs_tfidf = []
        self.data = data

    
    def transform_to_tfidf(self):
        query = 'm interest mechan commun disjoint process , possibl , exclus , distribut environ . would rather see descript complet mechan , without implement , oppos theoret work abstract problem . remot procedur call message-pass exampl interest . 4. pavel curti ( comm mech disjoint process )'
        docs_as_string =[query]+ [value for value in self.data.values()]

        data = self.tfidf.fit_transform(docs_as_string)
        self.docs_tfidf= data

        return data

    def get_semelarity(self,data):
        cosines={}
        for index in range(data.shape[0]):
            cosine= cosine_similarity(data[0],data[index])
            cosines[index] = cosine

        cosines = {k: v for k, v in sorted(cosines.items(), key=lambda item: item[1],reverse=True)}

        return cosines
        
            

        
        

    


    
