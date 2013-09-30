'''
Created on 2013-9-29

@author: yfeng

Tags: Pre-processing raw data, eliminate stop-word and useless parts
'''
import logging
import itertools
import gensim

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', filename='web_book.log',level=logging.INFO)

class webbook():
    def __init__(self):
        pass
    def __getitem__(self):
        pass
    def __str__(self):
        pass
    def __len__(self):
        pass
    def back_jobs_translation(self):
        pass
    def index_assign(self,ind):
        '''
        index start from 1
        '''
        return str(ind/1008000+1)+'.dat',ind%1008000
    
    