# -*- coding: utf-8 -*-

A =  [-2, 1, -3, 5, -2, 1, 2, -6, 5]

for i in range(1, len(A)):
    A[i] = max(A[i-1] + A[i],A[i])   #keep the sum larger untill A[i] 
       
maxSum= max(A) #the max value in the A
print('Maximum Sum: ', maxSum )  