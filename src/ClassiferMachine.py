'''
Created on 2013-11-5

@author: yfeng
'''

class ClassiferMachine(object):
    '''
    This is the main class for classification a document, which tag is most accuarcy to describe it
    '''


    def __init__(self,doc=None,n=5):
        '''
        Constructor: input a document, return the target, if the doc is None, then it just initalized all paramters for classification
        '''
        self.doc=None if doc is None else doc
        self.n=n
    def load_corpora(self,cor):
        pass 
    def put(self,doc):
        '''
        put function  input is document, and it will store this document in the class
        '''
        self.doc=doc
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
        pass
    def __getitem__(self,doc):
        pass
    def __str__(self):
        pass
    def show(self):
        pass