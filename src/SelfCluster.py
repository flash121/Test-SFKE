'''
Created on 2013-11-2

@author: yfeng
'''
import gensim
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from numpy import *
import json
#import stopword

class SelfCluster(object):
    '''
    The cluster feature vector for each keyword:
    The key place to store information of context from keyword
    '''
    def __init__(self,name,dirs="D:\\Stack Flow\\data\\",n=200,flag=False):
        '''
        given a bias -n for extract IDF smallest 200 words
              dir of file
        To return:
              context of whole keyword documents
              n for select model
        '''
        self.n=n
        self.dir=dirs
        self.filename=name
        self.id=name.replace(".kdoc","")
        d=Dictionary.load(dirs+"keyword.dict")
        self.tag=d[int(self.id)]
        context=open(dirs+"kdoc\\"+name,'r').read()
        self.stopword=open(dirs+"stopword.txt",'r').read().split('\n')
        doc=context.split("\n")
        self.raw=context 
        self.context=[[w for w in word.split() if w not in self.stopword and w[0].isalpha() == True ] for word in doc if(len(word)>10)]
        self.dict=Dictionary.load(dirs+"facebook.dict")
        self.cod_context=[self.dict.doc2bow(doc) for doc in self.context]
        self.model=TfidfModel(self.cod_context)
        self.tf=TfidfModel(dictionary=self.dict)
        self.mixture={}
        self.flag=flag
        if(flag):
            self.idfs()
            self.tfs()        
        
    def idfs(self):
        '''
        Compute idf, idf is calucating by model.idfs.get
                if a word does not appear in the context, return None, do not list in idf collection
        result: self.idf key: each word inex, value the rank of this word - idf increase
        '''
        self.idf={}
        for i in range(0,20000):
            u=self.model.idfs.get(i)
            if u is not None:
                self.idf[i]=u
        sort_key=sorted(self.idf,key=self.idf.get,reverse=False);
        self.idf_rank={}
        for u,v in enumerate(sort_key):
            self.idf_rank[v]=u
        return self.idf_rank
    def tfs(self):
        '''
        Compute TF value for the document this is based on whole TrainSet data
        result: self.tf_dict  key: each word index, value: the rank of this word - tf decrease
        '''
        temp=self.dict.doc2bow([w for w in self.raw.split() if w not in self.stopword and w[0].isalpha() == True ])
        self.n=min(self.n,len(temp))
        tf_score=self.tf[temp]
        tf_dict={}
        for u,v in tf_score:
            tf_dict[u]=v
        sort_tf=sorted(tf_dict,key=tf_dict.get,reverse=True);
        self.tf_dict={}
        for u,v in enumerate(sort_tf):
            self.tf_dict[v]=u
        return self.tf_dict
    def deleteContext(self):
        del self.raw
    def mixtureRank(self):
        '''
        Key function of this class, generated mixture rank for each word in the Big dictionary, and we can use it to determine the cluster of a keyword
        '''
        for k in self.idf_rank.keys():
            self.mixture[k]=(self.idf_rank[k]+self.tf_dict[k]+0.0)/2
        return sorted(self.mixture,key=self.mixture.get,reverse=False);
    def __str__(self):
        if self.flag==True:
            return "Keyword: %s Id: %s \n IDFModel(num_docs=%s, num_nnz=%s)\n TFModel(num_docs=%s, num_nnz=%s)\n Dictionary: %s" % (self.tag,self.id,self.model.num_docs, self.model.num_nnz,self.tf.num_docs, self.tf.num_nnz,str(self.get(self.mixtureRank()))) 
        else:
            return "Keyword: %s Id: %s \n IDFModel(num_docs=%s, num_nnz=%s)\n TFModel(num_docs=%s, num_nnz=%s)\n Dictionary: %s" % (self.tag,self.id,self.model.num_docs, self.model.num_nnz,self.tf.num_docs, self.tf.num_nnz,"Unavailable") 
            
    def get(self,t):
        return [self.dict[u] for u in t]
    def save(self):
        with open(self.dir+"\\json\\"+str(self.id)+'.json', 'w') as f:
            json.dump(self.mixture, f)
    def load(self):
        with open(self.dir+"\\json\\"+str(self.id)+'.json') as f:
            json.load(self.mixture, f)
    def show(self):
        temp=array(sorted(self.mixture,key=self.mixture.get,reverse=False))
        print [self.dict[u] for u in temp[0:self.n]]

'''
Test Situation
1st construction function: S
'''
print "Start Test..."
a=SelfCluster("36571.kdoc",flag=False)
print "Success"
print a
'''
Test Situation 
2nd Generate idf-sorted collection: S
T-func: a.idfs
'''
'''
Test Code
didf=a.idfs();
sort_key=array(sorted(didf,key=didf.get,reverse=False));
s=[(a.dict[k],didf[k]) for k in sort_key[0:200]]
for x in s:
    print x
'''
'''
ISSUE NO SORT Solved
'''
'''
3rd Generate tf-idf rank in whole dataset
T-func: a.tfs
'''
'''
Test Code:
print "Start TF-IDF in whole database calucating: "
d=a.tfs()
print d
'''
t1=a.idfs()
t2=a.tfs()
print a.get(a.mixtureRank())
