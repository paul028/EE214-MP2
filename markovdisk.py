# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:15:07 2019

@author: Paul Vincent Nonat
"""
import numpy as np

mat = ([0.95,0.04,0.01],[0.5,0.9,0.5],[0.5,0.5,0.9])
mat1=([0.5, 0.25, 0.25], [0.6666666666666666, 0, 0.3333333333333333], [0.6, 0.4, 0])

def markovdisk(n):
    temp=mat

    for i in range (1,n,1):
        temp = np.dot(temp,mat)
    
    return temp
        

def method2(n):
    d=np.diag(mat)
    c=d
    for i in range(1,n,1):
        c=np.dot(c,d)
        
    ans=np.dot(mat,c)
    ans2=np.dot(ans,np.linalg.inv(mat))
    return ans2