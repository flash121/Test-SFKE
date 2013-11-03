'''
Created on 2013-9-29

@author: yfeng

Tags: Pre-processing raw data, eliminate stop-word and useless parts
'''
import logging
import itertools
from gensim import *

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', filename='web_book.log',level=logging.INFO)

class webbook():
    def __init__(self,dir='D:\\Stack Flow\\data\\',memory='friendly',maxitem=0):
        self.directory=dir
        self.style=memory
        self.maxitem=maxitem
        self.len=0
        self.set=[open(dir+'1.dat','r'),open(dir+'2.dat','r'),open(dir+'3.dat','r'),open(dir+'4.dat','r'),open(dir+'5.dat','r'),open(dir+'6.dat','r')]
        self.loc=1
        self.keyindcate=open("F:\\tags.csv",'r')
        self.keyindcate.readline()
    def __getitem__(self):
        if(self.style=='friendly'):
            name=self.index_assign(self.doc[self.loc])
            self.loc+=1
            return open(name(0),'r')[name(1)]
        if(self.style=='max_memory'):
            name=self.index_assign(self.doc[self.loc])
            self.loc+=self.maxitem
            return open(name(0),'r')[name(1)]    
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
        """
        read corresponse key_value data
        """
        f=open('D:\\Stack Flow\\test\\key\\'+key+'.key')
        self.doc=f.read().split('\n')
        self.len=len(self.doc)
    def index_assign(self,ind):
        '''
        index start from 1
        '''
        #return [(str(ins/1008000+1)+'.dat', ins%1008000) for ins in ind]
        return str(ind/1008000+1)+'.dat', ind%1008000
    def back_jobs_translation(self):
        pass
    def CreateBigTable(self):
        """
        Write Hash Table         key: id value: responsed word >_< using gensim
        """
        dict=corpora.Dictionary.load("D:\\Stack Flow\\data\\keyword.dict")
        self.BigTable={}
        for x in dict:
            self.BigTable[dict[x]]=x
            
    def WriteBigFile(self):
        """
        New Idea: 0_0 hope Ok...  
                  BigFile is a file document contains all the files (42000 files) with 20G space (so big...) 
        """
        for docs_guide in self.set:
            for spec,doc in enumerate(docs_guide):
                print spec
                keywords=self.keyindcate.readline().replace("\"","").split();
                for word in keywords:
                    f=open(self.directory+"kdoc\\"+str(self.BigTable[word])+".kdoc",'a+')
                    f.write(doc+" ")
                    f.close()
        """
        Work: 2013/9  Forget >_< 
        name=self.index_assign(self.doc[self.loc])
        self.loc+=1
        return open(name(0),'r')[name(1)]
        """
   
    def CleanWord(self):
        pass
"""
Test Case: (CreateBigTable)
"""    
x=webbook();
print "Start Creating Big Table"
x.CreateBigTable();
#print "Successful"
"""
Test Case: (WriteBigFile)
"""    
#x.WriteBigFile()