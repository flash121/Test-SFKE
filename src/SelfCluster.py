'''
Created on 2013-11-2

@author: yfeng
'''

class SelfCluster(object):
    '''
    The cluster feature vector for each keyword:
    The key place to store information of context from keyword
    '''
    def __init__(self,name,dirs="D:\\Stack Flow\\data\\",n=200):
        '''
        given a bias -n for extract IDF smallest 200 words
              dir of file
        To return:
              context of whole keyword documents
              n for select model
        '''
        self.n=n
        context=open(dirs+name,'r').read()
        doc=context.split("\n")
        self.context=[word.split() for word in doc if(len(word)>10)]
    