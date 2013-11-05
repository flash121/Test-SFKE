'''
Created on 2013-11-4

@author: yfeng

This is main function to dump cluster feature to a json in json folder
'''
from SelfCluster import SelfCluster 
if __name__ == '__main__':
    dirs="D:\\Stack Flow\\data\\kdoc"
    for i in range(0,42048):
        a=SelfCluster(str(i)+".kdoc",flag=True,n=10)
        print a
        a.save()