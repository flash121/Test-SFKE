'''
Created on 2013-11-5

@author: yfeng
'''
import json
import ClassiferMachine
from numpy import array
class BasicView(object):
    '''
    A convenient class to view the context of json, store in [home_path]/json/
    '''
    def __init__(self,id,doc=None,n=10,reverse=False):
        '''
        Constructor
        '''
        self.n=n
        self.id=id
        self.reverse=reverse
        self.tar=ClassiferMachine.ClassiferMachine(doc)
        self.name=self.tar.tag[id]
        self.load()
        self.temp=sorted(self.context,key=self.context.get,reverse=False)
        
    def load(self):
        with open(self.dir+"\\json\\"+str(self.id)+'.json') as f:
            self.context=json.load(f)
    def find(self,wid=None):
        '''
        to find a word rank or a id rank
        '''
        print "The value of %s, the word is %s, rank is %s" (self.context[str(wid)],self.tar.tag[wid],self.temp.index(wid))
        return (self.context[str(wid)],self.tar.tag[wid],self.temp.index(wid))
    def selectTop(self,n,flag=True):
        temp=array(self.temp)
        return [self.dict[u] for u in temp[0:n]] if flag else [(self.dict[u],u) for u in temp[0:n]]
    def __str__(self):
        '''
        print top n words in json
        '''
        return str(self.selectTop(self.n))
    