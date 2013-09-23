'''
Created on 2013-9-23

@author: yfeng

tags: gensim, keyword-extract

idea: use gensim to create dictionary and extract keyword write to a file
'''
from gensim import corpora
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class KeywordList():
    def __init__(self,resource='tag.csv'):
        try: 
            self.source=open("..//data//"+resource,'r')
        except RuntimeError:
            print "Can not open resource"
    def GetDict(self):
        print "Processing words"
        texts = [[word for word in document.lower().split()] for document in self.source]
        print "Create Dictionary"
        self.dic= corpora.Dictionary(texts)
        self.dic.save('..//data/Keyword.dict')
        del texts
        token=self.dic.token2id
        self.token=token.keys()
        #Write result into file
        f=open("dict.kw",'w')
        temp=str(self.token)
        #Replace useless string
        temp=temp.replace(',','')
        temp=temp.replace('\'','')
        temp=temp.replace('  ',' ')
        f.write(temp[1:-1])
        f.close()
        return token
    def free(self):
        self.source.close()
        del self.dic
        del self.token
        