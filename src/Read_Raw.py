'''
Created on 2013-9-23

@author: yfeng

Tags: Read Process

Idea: Redistributed Files From Raw Data

Input: string, filename -> return every elements' index
'''

__author__ = 'Yifeng Gao'
__email__ = 'gaoyfeng2010@hotmail.com'

class KeyWordIndex():
    def __init__(self,keyword='none',type='word',resource='tag.csv'):
        try: 
            self.id="..//data//"+resource
            self.source=open(self.id,'r')
        except RuntimeError:
            print "Can not open resource"
            
        if(type=='word'):
            try:
                self.keyword=keyword.split()
            except ValueError:
                print "keyword Read failure from string"
        if(type=='file'):
            try:
                self.keyword=open(keyword,'r').read().split()
            except ValueError:
                print "keyword Read failure from file"
    def AllQuery(self):
        #Create file set:
        f={}
        k=1
        for key in self.keyword:
            k+=1
            '''
            if(k<=2000):
                continue
            if(k>2508):
                continue
            '''
             
            print key
            f[key]=open("D:\\Stack Flow\\test\\keyword\\"+str(k)+'.key','w') # Dictionary
            if k%500==0:
                num=1
                item=self.source.readline()
                while len(item)!=0:
                    items=item.split()
                    for key in f.keys():
     #                   if key+' ' in item:
     #                       f[key].write(str(num)+'\n')
     #                       continue
     #                   if ' '+key in item:
     #                       f[key].write(str(num)+'\n')
     #                       continue
                        for it in items:
                            if it == key:
                                f[key].write(str(num)+'\n')
                    item=self.source.readline()
                    num+=1
                    if num%1000==0:
                        print "Processing "+str(num)+"th Document"
                for r in f.keys():
                    f[r].close() 
                self.source.close()
                self.source=open(self.id,'r')
                f={}
        self.source.close()
    def Check(self):
        #self.dict={}
        #for i,key in enumerate(self.keyword):
        #    self.dict[i+2]=key
        err=[]
        for i in range(2,42050):
            s=open("D:\\Stack Flow\\test\\keyword\\"+str(i)+'.key','r').read()
            if(len(s)==0):
                print str(i)+"Broken"+"  "+self.keyword[i-2]
                err.append(i)
        return err
    def Query(self,sets=[]):
        #Create file set:
        f={}
        
        words=[self.keyword[s-2] for s in sets] 
        for i,key in enumerate(words):
            print sets[i]
            f[key]=open("D:\\Stack Flow\\test\\keyword\\"+str(sets[i])+'.key','w') # Dictionary
        num=1
        item=self.source.readline()
        while len(item)!=0:
            items=item.split()
            for key in f.keys():
                for it in items:
                    if it == key:
                        f[key].write(str(num)+'\n')
            item=self.source.readline()
            num+=1
            if num%1000==0:
                print "Processing "+str(num)+"th Document"
        for r in f.keys():
            f[r].close() 
        self.source.close()
            
        
