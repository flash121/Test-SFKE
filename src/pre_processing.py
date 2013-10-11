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
    def __init__(self,dir='D:\\Stack Flow\\data',memory='friendly',maxitem=0):
        self.directory=dir
        self.style=memory
        self.maxitem=maxitem
        self.len=0
        self.set=[open(dir+'1.dat','r'),open(dir+'2.dat','r'),open(dir+'3.dat','r'),open(dir+'4.dat','r'),open(dir+'5.dat','r'),open(dir+'6.dat','r')]
        self.loc=1
        self.dict={"1.dat" : [],"2.dat" : [],"3.dat" : [],"4.dat" : [],"5.dat" : [],"6.dat" : []}
    def __getitem__(self):
        if(self.style=='friendly'):
            name=self.index_assign(self.doc[self.loc])
            self.loc+=1
            return open(name(0),'r')[name(1)]
        if(self.style=='max_memory'):
            name=self.index_assign(self.doc[self.loc])
            self.loc+=self.maxitem
            return open(name(0),'r')[name(1)]    
        if(self.style=='heavy'):
            shown_str=shown_str+'Data Directory: '+self.directory+'operation style: '+self.style+'maxmize item: '+'All files'
    def __str__(self):
        shown_str=''
        if(self.style=='friendly'):
            shown_str=shown_str+'Data Directory: '+self.directory+'operation style: '+self.style
        if(self.style=='max_memory'):
            shown_str=shown_str+'Data Directory: '+self.directory+'operation style: '+self.style+'maxmize item: '+str(self.maxitem)
        if(self.style=='heavy'):
            shown_str=shown_str+'Data Directory: '+self.directory+'operation style: '+self.style+'maxmize item: '+'All files'
        return shown_str    
    def __len__(self):
        return self.len
    def read_keyword(self,key):
        f=open('D:\\Stack Flow\\test\\key\\'+key+'.key')
        self.doc=f.read().split('\n')
        self.len=len(self.doc)
    def index_assign(self,ind):
        '''
        index start from 1
        '''
        return [(str(ins/1008000+1)+'.dat', ins%1008000) for ins in ind]
    def back_jobs_translation(self):
        pass
    def read(self):
        name=self.index_assign(self.doc[self.loc])
        self.loc+=1
        return open(name(0),'r')[name(1)]
    
    