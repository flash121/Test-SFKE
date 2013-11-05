'''
Created on 2013-11-5

@author: yfeng
'''
import gensim
from gensim import corpora

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
        self.dict=corpora.Dictionary.load(dirs+"facebook.dict")
        self.corpora=self.doc2cor(self.doc)
        self.fin=0
        self.stopword=self.stopword=open(dirs+"stopword.txt",'r').read().split('\n')
    def load_corpora(self,cor):
        pass 
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
        pass
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
        return  "" % () if self.fin==1 else "" % ()
    def __str__(self):
        return 
    def show(self):
        pass