'''
Created on 2013-9-22

@author: yfeng

Tags: MongoDB, Read- Like Expression in MongoDB, SELECT and Redistributed file

Idea: Use MongoDB to read tag and redistributed store in the hardware (Space -> Time)

Input: string, filename -> return every elements' index
'''
__author__ = 'Yifeng Gao'
__email__ = 'gaoyfeng2010@hotmail.com'

from uploaddb import connect_c #connect mongodb socket: 


class KeyWordIndex():
    def __init__(self,keyword='none',type='word'):
        try:
            self.db=connect_c('facebook','train','localhost',27017)
        except RuntimeError:
            print "Can not connect to database"
        if(type=='word'):
            try:
                self.keyword=keyword.split()
            except ValueError:
                print "keyword Read failure from string"
        if(type=='file'):
            try:
                self.keyword=open(keyword,'r').read().split('')
            except ValueError:
                print "keyword Read failure from file"
    
    def Query(self):
        print "Processing Query: "
        for key in self.keyword:
            f=open(key,'w')
            docs=self.db.find({"Tags": {"$regex" : key}},{"Id" : 1}).explain()
            print docs
            #k=0
            #if docs.hasNext():
            #    data=docs.next()
            #    f.write(data['Id']+'\n')
            #    k+=1
            #    print k
            #for doc in docs:
            #    print k
            #    if k==100:
            #        k=100
                #if k%1000==0:
                #    print "Prcoessing "+str(k)+"th Document" 
            #    f.write(str(doc['Id'])+'\n')
            #    k+=1
            
   
    



