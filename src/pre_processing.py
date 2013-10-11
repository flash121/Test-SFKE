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
        f=open('D:\\Stack Flow\\test\\keyword\\'+str(key)+'.key')
        self.loc=f.read().split('\n')
        self.loc=[int(num) for num in self.loc if num != '']
        self.len=len(self.loc)
        self.key=key
    def index_assign(self,ind):
        '''
        index start from 1
        '''
        return [(str(ins/1008000+1)+'.dat', ins%1008000) for ins in ind]
    def back_jobs_translation(self):
        pass
    def basic_read(self,name,ind):
        f=open(name,'r')
        return [u.split() for i,u in enumerate(f) if(i+1 in ind)]
    def basic_group(self,indx,tar):
        return tar,[u[1] for u in indx if u[0]==tar]
    def read(self):
        read_pack=self.index_assign(self.loc)
        content=[]
        for p in self.dict.keys():
            pack_ind=self.basic_group(read_pack,p)
            content.extend(self.basic_read(self.directory+'\\'+p,pack_ind[1]))
            s="Read data:" + str(len(content))
            logging.info(s)
        d=gensim.corpora.Dictionary(content)
        d.save("D:\\Stack Flow\\data\\dic\\"+str(self.key));
        return d
        
    
s=webbook()
s.read_keyword(14)
s.read()
