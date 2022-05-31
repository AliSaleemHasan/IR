from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
# import spacy
# nlp = spacy.load("en_core_web_sm")
class IROperations:
    def __init__(self,data):
        self.tfidf = TfidfVectorizer()
        self.cosine=cosine_similarity
        self.docs_tfidf = []
        self.docs_vectors = []
        self.data = data

    # def get_spacy_vector(self):
    #     query = 'm interest mechan commun disjoint process , possibl , exclus , distribut environ . would rather see descript complet mechan , without implement , oppos theoret work abstract problem . remot procedur call message-pass exampl interest . 4. pavel curti ( comm mech disjoint process )'
    #     vectors = [nlp(sentence).vector for sentence in self.data]
    #     self.docs_vectors= vectors
    #     return vectors


    def transform_to_tfidf(self,query):
        docs_as_string =[query]+ [value for value in self.data.values()]

        data = self.tfidf.fit_transform(docs_as_string)
        self.docs_tfidf= data

        return data

    def get_tfidf_semelarity(self,data):
        cosines={}
        for index in range(data.shape[0]):
            cosine= cosine_similarity(data[0],data[index])
            cosines[index] = cosine

        cosines = {k: v for k, v in sorted(cosines.items(), key=lambda item: item[1],reverse=True)}

        return cosines
    
            
    # def get_vector_semelarity(self,vectors,query):
    #     query_vector = nlp(query).vector
    #     vectors.insert(0,query_vector)
    #     return cosine_similarity(vectors)
        


    


    
