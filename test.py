from DataSetOperations import DataSetOperations

cacm = DataSetOperations()
cacm.preprocess_docs(filepath='cacm/cacm.all')
cacm.preprocess_docs(filepath='cacm/query.text',type='query')
cacm.preprocess_rel(filepath='cacm/qrels.text')

print(cacm.relations)