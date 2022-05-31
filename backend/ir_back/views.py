from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from os.path import exists
from .ir_core import DataProcessing,DataSetOperations,IROperations
cacm = {}
cisi = {}


@api_view(['GET'])
def index(request):
    if exists('ir_back/ir_core/data_sets/processed/cacm_docs.txt') == False or request.session.get('cacm')==None : 
        cacm_files = {'ir_back/ir_core/data_sets/cacm/cacm.all':'docs','ir_back/ir_core/data_sets/cacm/qrels.text':'rel','ir_back/ir_core/data_sets/cacm/query.text':'query'}
        cacm = DataSetOperations.DataSetOperations(files=cacm_files)
        request.session['cacm']=cacm.documents

        DataProcessing.DataProccessing(data= cacm.documents,to='ir_back/ir_core/data_sets/processed/cacm_docs.txt')
    if exists('ir_back/ir_core/data_sets/processed/cisi_docs.txt') == False  or request.session.get('cisi')==None: 
        cisi_files = {'ir_back/ir_core/data_sets/CISI/CISI.ALL':'docs','ir_back/ir_core/data_sets/CISI/CISI.REL':'rel','ir_back/ir_core/data_sets/CISI/CISI.QRY':'query'}

        cisi = DataSetOperations.DataSetOperations(files=cisi_files)
        request.session['cisi']=cisi.documents

        DataProcessing.DataProccessing(data= cisi.documents,to='ir_back/ir_core/data_sets/processed/cisi_docs.txt')


    return HttpResponse("preProcessed Docuemnents Saved to server")


@api_view(['get'])
def get_documents(request):
    query = request.GET.get('query','')
    doc_type = request.GET.get('doc_type','')
    docs = request.session.get('cacm')
    if doc_type == 'cisi':
        docs = request.session.get('cisi')
    if query != '':
      DP = DataProcessing.DataProccessing(query)
      data = DP.process_query()
      del DP

      IRO = IROperations.IROperations(data=docs)
      tfidf=IRO.transform_to_tfidf(query=data)
      cosines = IRO.get_tfidf_semelarity(tfidf)
      del IRO


    response_data = []
    index =0
    for key in cosines.keys():
        if index>10:
            break
        response_data.append(key)
        index +=1

        
    
    return HttpResponse(response_data)



        

# Create your views here.
