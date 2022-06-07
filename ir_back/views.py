from django.shortcuts import render
from django.http import HttpResponse
from os.path import exists
from .ir_core import DataProcessing,DataSetOperations,IROperations
cacm = {}
cisi = {}


def index(request):
    if exists('ir_back/ir_core/data_sets/processed/cacm_docs.txt') == False or request.session.get('cacm_docs')==None : 
        cacm_files = {'ir_back/ir_core/data_sets/cacm/cacm.all':'docs','ir_back/ir_core/data_sets/cacm/qrels.text':'rel','ir_back/ir_core/data_sets/cacm/query.text':'query'}
        cacm = DataSetOperations.DataSetOperations(files=cacm_files)
        request.session['cacm_docs']=cacm.documents
        request.session['cacm_rel'] = cacm.relations
        request.session['cacm_query']=cacm.queries
        request.session['cacm_query_test']=cacm.queries



        DataProcessing.DataProccessing(data= cacm.documents,to='ir_back/ir_core/data_sets/processed/cacm_docs.txt')
    if exists('ir_back/ir_core/data_sets/processed/cisi_docs.txt') == False  or request.session.get('cisi_docs')==None: 
        cisi_files = {'ir_back/ir_core/data_sets/CISI/CISI.ALL':'docs','ir_back/ir_core/data_sets/CISI/CISI.REL':'rel','ir_back/ir_core/data_sets/CISI/CISI.QRY':'query'}

        cisi = DataSetOperations.DataSetOperations(files=cisi_files)
        request.session['cisi_docs']=cisi.documents
        request.session['cisi_rel'] = cisi.relations
        request.session['cisi_query']=cisi.queries
        request.session['cisi_query_test']=cisi.queries

        DataProcessing.DataProccessing(data= cisi.documents,to='ir_back/ir_core/data_sets/processed/cisi_docs.txt')


    return render(request,'home.html',{"fetched":True,"data":"preProcessed Docuemnents Saved to server"})


def get_documents(request):
    f = open('ir_back/ir_core/data_sets/processed/cacm_docs.txt','r')
    content = f.readlines(0)
    c={};count=0
    for i in content:
        if('.I' not in i):
            if(count == 0):continue
            c[count-1] = i
        else:
            count = count+1

    request.session['cacm_docs'] = c
    rel = request.session.get('cacm_rel')
    q = request.session.get('cacm_query')

    query = request.POST.get('query','')
    docs = c
    for i,v in q.items():
        if query in v:    
            q_number = i

    relavant = rel[str(q_number)]
    request.session['relavant'] = relavant
        
    if query != '':
        request.session['query']= query
            
        DP = DataProcessing.DataProccessing(query)
        data = DP.process_query()
        del DP

        IRO = IROperations.IROperations(data=docs)
        tfidf=IRO.transform_to_tfidf()
        cosines = IRO.get_semelarity(data=tfidf,query=data)

        response_data = []
        index =0
        for key in cosines.keys():
            if index>10:
                break
            response_data.append({
                "doc_num":key,
                "doc":docs[key]
            })
            index +=1
            
        
        retrival = response_data
        request.session['retrival'] = retrival
    return render(request,'home.html',{'fetched':True,'docs':response_data})

        

def get_results(request):
    rel = request.session.get('cacm_rel')
    docs = request.session.get('cacm_docs')
    querys = request.session['cacm_query_test']

    precision= request.session.get('precision')
    all_retrival= request.session.get('all_retrival')
    all_relavant= request.session.get('all_relavant')
    MAP= request.session.get('MAP')
    MRR= request.session.get('MRR')
    

    if(precision== None and all_relavant ==None and all_retrival==None and MAP==None and MRR == None):
        IRO = IROperations.IROperations(data=docs)
        tfidf=IRO.transform_to_tfidf()
        
        all_list={};all_retrival={};all_relavant={};all_ap=[];all_rr=[]
        for q_number,query in querys.items():
            cosines = IRO.get_semelarity(tfidf,query)
            response_data = [];index =0
            for key in cosines.keys():
                if index>9:
                    break
                response_data.append(key)
                index +=1
            
            retrival = response_data
            all_retrival[q_number] =retrival
            if(q_number in rel.keys()):
                relavant = rel[q_number]
            else:
                all_list[q_number] = [0]
                continue
            all_relavant[q_number] = relavant 
            p,p10,recall,AP,rr =  IRO.precision(relavant,retrival)
            all_ap.append(AP)
            all_rr.append(rr)
            listed=[p,p10,recall,AP,rr]
            all_list[q_number] = listed
            listed=[]
        precision = all_list
        MAP = sum(all_ap)/len(all_ap)
        MRR = sum(all_rr)/len(all_rr)
        request.session['precision'] = precision
        request.session['all_retrival'] = all_retrival
        request.session['all_relavant'] = all_relavant
        request.session['MAP'] = MAP
        request.session['MRR'] = MRR
    data=[]
    for i,j in precision.items():
        data.append((i,j))
    return render(request,'results.html',{'fetched':True,'data': data,'querys': querys,'MAP':MAP,'MRR':MRR})


def test1(request):
    precision = request.session['precision']
    querys = request.session['query_test']
    #all_retrival = request.session.get('all_retrival')
    #all_relavant = request.session.get('all_relavant')
    test=[]
    for i,j in precision.items():
        test.append(j)
    return render(request,'test1.html',{'fetched':True,'data': test,'querys': querys})

    
