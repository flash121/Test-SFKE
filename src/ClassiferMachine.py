'''
Created on 2013-11-5

@author: yfeng
'''
import json
import gensim
from gensim import corpora
from numpy import array

class ClassiferMachine(object):
    '''
    This is the main class for classification a document, which tag is most accuarcy to describe it
    Usage:
          1. x=ClassiferMachine()
          2. x=ClassiferMachine(doc)
          3. x=ClassiferMachine()
             x.load_corpora(corpora)
    Extract Process:
          x.extract() #take a lot of time
    Display:
          print x
    '''
    def __init__(self,doc=None,n=5,dirs="D:\\Stack Flow\\data\\"):
        '''
        Constructor: input a document, return the target, if the doc is None, then it just initalized all paramters for classification
        '''
        self.doc=None if doc is None else doc
        self.n=n
        self.dir=dirs
        self.stopword=self.stopword=open(dirs+"stopword.txt",'r').read().split('\n')
        self.dict=corpora.Dictionary.load(dirs+"facebook.dict")
        self.corpora=self.doc2cor()
        self.fin=0
        self.tag=corpora.Dictionary.load(dirs+"Keyword.dict")
        
    def load_corpora(self,cor):
        self.corpora=cor
    def put(self,doc):
        '''
        put function  input is document, and it will store this document in the class
        '''
        self.doc=doc
        self.corpora=self.doc2cor(self.doc)
    def extract(self):
        '''
        get function is the main function to extract tag
        '''
        self.points={}
        for i in range(0,42048):
            point=0
            if(self.tag[i]=="json"):
                point=point
            with open(self.dir+"json\\"+str(i)+".json") as f:
                data=json.load(f)
            for u,v in self.corpora:
                try: 
                    point=point+data[str(u)]*v
                except:
                    point=point+20000*v
            self.points[i]=(point+0.0)/len(self.corpora)
            if(i%100==0): 
                print i
    def getdoc(self):
        '''
        to return document
        '''
        return self.doc if self.doc is not None else {}
    def doc2cor(self):
        '''
        Convert document into corpora with id in the whole dictionary
        '''
        if self.doc is None:
            #print "[Error] document do not exist"
            return []
        else:
            return self.dict.doc2bow([w for w in self.doc.split() if w not in self.stopword and w[0].isalpha() == True])
    def __getitem__(self,doc):
        pass
    def __str__(self):
        return  "" % () if self.fin==1 else "" % ()
    def show(self):
        temp=array(sorted(self.points,key=self.points.get,reverse=False))
        print [(self.tag[u],u) for u in temp[0:self.n]]


'''
Test Code: 
Case 1: __init__
Status: S 
'''

x=ClassiferMachine()
x=ClassiferMachine("I have found that when the following is run python json module included since converts int dictionary keys to string Is there any easy way to preserve the key as an int without needing to parse the string on dump and load. I believe it would be possible using the hooks provided by the json module but again this still requires parsing Is there possibly an argument I have overlooked cheers chaz")
'''
Test Code:
Case 2: extract()
Status: W
'''    
x.extract()
x.show()