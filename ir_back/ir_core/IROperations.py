from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy as np
nlp = spacy.load("en_core_web_sm")

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
    
    def word_embedding(self,data,query):
            docs_as_string =[value for value in data.values()]
            v = [nlp(s).vector for s in docs_as_string]
            q_v = nlp(query).vector
            cosines={};count=0
            print("start")
            for i in v:
                sim = cosine_similarity([i,q_v])[0][1]
                cosines[count] = sim
                count = count +1

            cosines = {k: v for k, v in sorted(cosines.items(), key=lambda item: item[1],reverse=True)}
            return cosines

    def get_semelarity(self,data,query):
        query_tfidf= self.tfidf.transform([query])
        cosines={}
        for index in range(data.shape[0]):
            cosine= cosine_similarity(query_tfidf,data[index])
            cosines[index+1] = cosine

        cosines = {k: v for k, v in sorted(cosines.items(), key=lambda item: item[1],reverse=True)}

        return cosines
    
    
    def precision(self,relavant,retrival):
        right=0;avg_p=[];count=0;rr=0;all_rr=[]
        for i in retrival:
            count = count +1
            if str(i) in relavant:
                right = right +1
                rr = 1 / (retrival.index(i) + 1)  
                all_rr.append(rr)
                avg_p.append(right/count)
        c=0;r=0
        for i in retrival[:10]:
            c=c+1
            if str(i) in relavant:
                r=r+1
        p_10 = r / 10
        precision = right/len(retrival)
        recall = right/len(relavant)
        if(len(all_rr) != 0):
            mrr = np.mean(all_rr[0])
        else:
            mrr = 0
        if(len(avg_p) != 0):
            MAP = sum(avg_p)/len(avg_p)
        else:
            MAP = 0
        return precision,p_10,recall,MAP,mrr