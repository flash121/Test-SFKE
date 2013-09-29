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
    def Query(self):
        #Create file set:
        f={}
        k=1
        for key in self.keyword:
            k+=1
            f[key]=open("D:\\Stack Flow\\test\\keyword\\"+str(k)+'.key','w') # Dictionary
            print key
            if k%500==0:
                num=1
                item=self.source.readline()
                while len(item)!=0:
                    for key in f.keys():
                        if key+' ' in item:
                            f[key].write(str(num)+'\n')
                            continue
                        if ' '+key in item:
                            f[key].write(str(num)+'\n')
                            continue
                    item=self.source.readline()
                    num+=1
                    if num%1000==0:
                        print "Processing "+str(num)+"th Document"
                for r in f.keys():
                    f[r].close() 
                self.source.close()
                self.source=open(self.id,'r')
                f={}
        
        num=1
        item=self.source.readline()
        while len(item)!=0:
            for key in f.keys():
                if key+' ' in item:
                    f[key].write(str(num)+'\n')
                    continue
                if ' '+key in item:
                    f[key].write(str(num)+'\n')
                    continue
            item=self.source.readline()
            num+=1
            if num%1000==0:
                print "Processing "+str(num)+"th Document"
        for r in f.keys():
            f[r].close() 
        self.source.close()    
                
        
