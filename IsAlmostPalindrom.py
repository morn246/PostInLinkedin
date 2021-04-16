# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:17:51 2021

@author: 97252
"""
def isPalindrome(word,first,last):    
    isPalindromeFlag = 1    
    while(first<last):
           if(word[first]==word[last]):
               first=first+1
               last=last-1
           else:
               isPalindromeFlag = 0
               break
    return int(isPalindromeFlag)    
def isAlmostPalindrome(word,first,last):
    if word=="":
        return True
    isAlmostPFlag = 1
    while(first<last):         
        if(word[first]!=word[last]):           
            if(isPalindrome(word,first,last-first)==False 
               and isPalindrome(word,first+1,last-first+1)==False ):                  
                   isAlmostPFlag = 0
            break                      
        first=first+1
        last=last-1
    return int(isAlmostPFlag) 

    
word =[ "k","b","a","y","a","k"]
first = 0
last = len(word) -1 
status= isAlmostPalindrome(word,first,last)
if(status):
    print("It is a almost palindrome ")
else:
    print("It is not almost palindrome")
