'''
Created on 2013-11-5

@author: yfeng
'''
import json
import ClassiferMachine
from numpy import array
import numpy
class BasicView(object):
    '''
    A convenient class to view the context of json, store in [home_path]/json/
    '''
    def __init__(self,word=None,tag=None,doc=None,wid=None,tagid=None,n=10,reverse=False,dirs="D:\\Stack Flow\\data\\"):
        '''
        Constructor
        '''
        self.n=n
        self.dir=dirs
        self.tar=ClassiferMachine.ClassiferMachine(doc)
        if word is not None:
            self.word=word
            self.tag=tag
            self.tagid=self.convertTag()
            self.wid=self.convertWord()
        else:
            self.tagid=tagid
            self.wid=wid
            self.word=self.tar.dict[wid]
            self.tag=self.tar.tag[tagid]
        
        self.reverse=reverse
        self.load()
        self.temp=sorted(self.context,key=self.context.get,reverse=self.reverse)
        
    def load(self):
        with open(self.dir+"json\\"+str(self.tagid)+'.json') as f:
            self.context=json.load(f)
    def find(self,wid=None):
        '''
        to find a word rank or a id rank
        '''
        print "The value of %s, the word is %s, rank is %s" (self.context[str(wid)],self.tar.tag[wid],self.temp.index(wid))
        return (self.context[str(wid)],self.tar.tag[wid],self.temp.index(wid))
    def selectTop(self,n,flag=True):
        temp=array(self.temp)
        return [self.tar.dict[int(u)] for u in temp[0:n]] if flag else [(self.tar.dict[int(u)],u) for u in temp[0:n]]
    def __str__(self):
        '''
        print top n words in json
        '''
        return "Keyword: "+self.tar.tag[self.tagid]+" "+str(self.selectTop(self.n))
    def convertWord(self):
        return self.tar.dict.doc2bow([self.word])[0][0]
    def convertTag(self):
        return self.tar.tag.doc2bow([self.tag])[0][0]
    def TextkeySort(self, flag=True):
        Text={}
        for a in self.tar.corpora:
            try:
                Text[a[0]]=self.context[str(a[0])]
            except:
                Text[a[0]]=20000
                self.temp.append(str(a[0]))
        temp=sorted(Text,key=Text.get,reverse=self.reverse)
        return [self.tar.dict[int(u)] for u in temp[0:min(len(self.tar.corpora),self.n)]] if flag else [(self.tar.dict[int(u)],Text[u],self.temp.index(str(u))) for u in temp[0:min(len(self.tar.corpora),self.n)]]
        
#x=BasicView(n=6, word="python",tag="json",doc="I have found that when the following is run python json module included since converts int dictionary keys to string Is there any easy way to preserve the key as an int without needing to parse the string on dump and load. I believe it would be possible using the hooks provided by the json module but again this still requires parsing Is there possibly an argument I have overlooked cheers chaz")
#print x.selectTop(100)
#print x.TextkeySort(flag=False)
point=[]
for i in range(0,500):
    if i==38:
        i=38
    x=BasicView(n=6,wid=4173,tagid=i,doc="I have found that when the following is run python json module included since converts int dictionary keys to string Is there any easy way to preserve the key as an int without needing to parse the string on dump and load. I believe it would be possible using the hooks provided by the json module but again this still requires parsing Is there possibly an argument I have overlooked cheers chaz")
    p=x.TextkeySort(flag=False)
    point.append(array([s[2] for s in p]).sum())
    print i
array=array(point)
temp = array.argsort()
ranks = numpy.arange(len(array))[temp.argsort()]
print ranks