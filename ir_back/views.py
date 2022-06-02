from django.shortcuts import render
from django.http import HttpResponse
from os.path import exists
from .ir_core import DataProcessing,DataSetOperations,IROperations
cacm = {}
cisi = {}


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


    return render(request,'home.html',{"fetched":True,"data":"preProcessed Docuemnents Saved to server"})


def get_documents(request):

    if request.method == 'POST':
        query = request.POST.get('query','')
        docs = request.session.get('cacm')
        print("ttttttttttttttttttt")
        print(docs)

        if query != '':
            DP = DataProcessing.DataProccessing(query)
            data = DP.process_query()
            del DP

            IRO = IROperations.IROperations(data=docs)
            tfidf=IRO.transform_to_tfidf()
            cosines = IRO.get_semelarity(data=tfidf,query=data)
            del IRO


            response_data = []
            index =0
            for key in cosines.keys():
                if index>10:
                    break
                response_data.append(key)
                index +=1
            
            print(response_data)
        
    
        return render(request,'home.html',{'fetched':True,'docs':response_data})

    return render(request,'home.html',{'fetched':True,'docs':{}})
        



        

# Create your views here.
