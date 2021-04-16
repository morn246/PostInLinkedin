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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    
   
  
    
  
    


def wordSubset( A, B):       
        dicB={}
        res=[]
        for unit in B:
            temp={}
            for x in unit:
                if x in temp:
                    print(temp)
                    temp[x]+=1
                else:
                    temp[x]=1
                for k, v in temp.items():
                    dicB[k] = max(dicB[k], v) if k in dicB else v                
        fg=False
        for unit in A:
            for (a,b) in dicB.items():
                if dicB[a]<=unit.count(a):            
                    fg=True
                else:
                    fg=False
                    break
            if fg==True:
                res.append(unit)
        return res
    
    
    
    



   
# def Concatenation( S, L):
#         word_size=len(L[0])
#         lists_size=len(L)  
#         total=(lists_size)*(word_size)
#         i=0
#         Points=[]
#         comp=0
#         for w in L:
#             comp+=hash(w)
   
#         while (i+total<=len(S)):
#             x=list(S[i:i+(lists_size)*(word_size)])           
#             flag=0
#             while x!=[]:
#                 k=0
#                 tempword=[]
#                 while k<word_size:
#                     y=x.pop(0)
#                     tempword.append(y)
#                     k+=1 
#                 print(tempword)
#                 flag+=hash("".join(tempword))
#             if comp==flag:
#                 Points.append(i)
#             i+=1
#         print(i) 
#         print(len(S))
#         return Points
    
    
# def Concatenation1( A, B):
#     L = {}
#     num_words = 0
#     Points = []
#     for i in B:
#         if L.get(i):
#             L[i]+=1
#         else:
#             L[i]=1
#         num_words += 1
#     i = 0
#     j = len(B[0])-1
#     temp_num = num_words
#     temp_L = dict(L)
#     while j<len(A):
#         temp_i = i
#         while j<len(A):
#             if temp_L.get(A[i:j+1]) and temp_num>0:
#                 temp_num -=1
#                 temp_L[A[i:j+1]]-=1
#                 i+=len(B[0])
#                 j+=len(B[0])
#                 if temp_num == 0:
#                     Points.append(temp_i)
#                     break
#             else:
#                 break
#         i = temp_i+1
#         j = i+len(B[0])-1
#         temp_num = num_words
#         temp_L = dict(L)
#     return Points



# S="one likehash"
# L=["like", "hash"]
# #output:  [2, 21]
# print ("output: ",Concatenation1(S, L))








# def Concatenation1( A, B):
#     word_len = len(B[0])
#     vocab_size = len(B)
#     Points = []
#     hash_all_words = 0
#     for word in B:
#         hash_all_words += hash(word)
    
#     idx = 0
#     window_size = vocab_size*word_len
    
#     while (idx) < len(A):
#         if A[idx: idx + word_len] in B:
#             temp_hash = 0
#             for pos in range(idx, idx + window_size, word_len):
              
#                 if pos > len(A) :
#                     break
#                 print((A[pos:pos+word_len]))
#                 temp_hash += hash(A[pos:pos+word_len])

#             if temp_hash == hash_all_words:
#                 Points.append(idx)
        
#         idx += 1
#     return Points