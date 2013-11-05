'''
Created on 2013-11-5

@author: yfeng
'''
import json
class BasicView(object):
    '''
    A convenient class to view the context of json, store in [home_path]/json/
    '''
    def __init__(self,name,n=10,reverse=False):
        '''
        Constructor
        '''
        self.n=n
        self.name=name
        self.reverse=reverse
        pass
    def find(self,word=None,id=None):
        '''
        to find a word rank or a id rank
        '''
        pass
    def __str__(self):
        '''
        print top n words in json
        '''
        pass