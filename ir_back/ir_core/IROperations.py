from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
class IROperations:
    def __init__(self,data):
        self.tfidf = TfidfVectorizer()
        self.cosine=cosine_similarity
        self.docs_tfidf = []
        self.docs_vectors = []
        self.data = data

   
    def transform_to_tfidf(self):
        docs_as_string =[value for value in self.data.values()]
        data = self.tfidf.fit_transform(docs_as_string)
        self.docs_tfidf= data
        return data

    def get_semelarity(self,data,query):
        query_tfidf= self.tfidf.transform([query])
        cosines={}
        for index in range(data.shape[0]):
            cosine= cosine_similarity(query_tfidf,data[index])
            cosines[index] = cosine

        cosines = {k: v for k, v in sorted(cosines.items(), key=lambda item: item[1],reverse=True)}

        return cosines
    


    


    
