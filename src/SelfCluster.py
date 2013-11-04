'''
Created on 2013-11-2

@author: yfeng
'''
import gensim
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from numpy import *
#import stopword

class SelfCluster(object):
    '''
    The cluster feature vector for each keyword:
    The key place to store information of context from keyword
    '''
    def __init__(self,name,dirs="D:\\Stack Flow\\data\\",n=200):
        '''
        given a bias -n for extract IDF smallest 200 words
              dir of file
        To return:
              context of whole keyword documents
              n for select model
        '''
        self.n=n
        context=open(dirs+"kdoc\\"+name,'r').read()
        doc=context.split("\n")
        self.context=[word.split() for word in doc if(len(word)>10)]
        self.dict=Dictionary.load(dirs+"facebook.dict")
        self.cod_context=[self.dict.doc2bow(doc) for doc in self.context]
        self.model=TfidfModel(self.cod_context)
    def idfs(self):
        '''
        Compute idf, idf is calucating by model.idfs.get
                if a word does not appear in the context, return None, do not list in idf collection
        '''
        self.idf={}
        for i in range(0,20000):
            u=self.model.idfs.get(i)
            if u is not None:
                self.idf[i]=u
        return self.idf



'''
Test Situation
1st construction function: S
'''
print "Start Test..."
a=SelfCluster("3.kdoc")
print "Success"
print a.model

'''
Test Situation 
2nd Generate idf-sorted collection: S
T-func: a.idfs
'''
didf=a.idfs();
sort_key=array(sorted(didf,key=didf.get,reverse=False));
s=[(a.dict[k],didf[k]) for k in sort_key[0:200]]
for x in s:
    print x
'''
ISSUE NO SORT Solved
'''