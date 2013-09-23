'''
Created on 2013-9-22

@author: yfeng

This is the test function for test test_Connect_DB.py

I will try to use example string='php' and a file exaple to do this task
'''

from Read_Raw import KeyWordIndex


#import target test file:


test_model=KeyWordIndex('php','word')
test_model.Query()
