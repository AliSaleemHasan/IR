from DataSetOperations import DataSetOperations
from DataProcessing import DataProccessing
from sklearn.feature_extraction.text import TfidfVectorizer 
from IROperations import IROperations
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
from os.path import exists


if exists('./data_sets/processed/cacm_docs.txt') == False : 
    cacm_files = {'./data_sets/cacm/cacm.all':'docs','./data_sets/cacm/qrels.text':'rel','./data_sets/cacm/query.text':'query'}
    cisi_files = {'./data_sets/CISI/CISI.ALL':'docs','./data_sets/CISI/CISI.REL':'rel','./data_sets/CISI/CISI.QRY':'query'}
    cacm = DataSetOperations(files=cacm_files)
    DataProccessing(data= cacm.documents,to='./data_sets/processed/cacm_docs.txt')
    DataProccessing(data= cacm.queries,to='./data_sets/processed/cacm_queries.txt')


preprocessed_data = DataSetOperations({'./data_sets/processed/cacm_docs.txt':'docs'})

IRO = IROperations(data=preprocessed_data.documents)
tfidf = IRO.transform_to_tfidf()
cosines= IRO.get_semelarity(data=tfidf)


index =0
for key in cosines.keys():
    if index>10:
        break
    print(key)
    index +=1




