# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 08:16:53 2021

@author: 97252
"""

import string
def wordSubset( A, B):          
    res=[]
    for word in A:
        letters = {x:0 for x in string.ascii_lowercase } 
        for w in word:
           letters[w]+=1
        f=True    
        for st in B:
            if(f== False):
                break
            for s in st:
                letters[s]-=1
                if(letters[s]<0):
                    f=False
        if(f==True):
            res.append(word)                       
    return res

    
    
    
    
  
A = ["amazon","apple","facebook","google","intelo"]
B = ["lo","eo"]
print("",wordSubset(A,B) )    
  
# ['intel', 'apple', 'mobileye']     
    
    
    
