import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

A1 = np.array([[5.,-4.,-2.],[5.,-5.,4.],[2.,5.,-4.],[-5.,4.,3.],[3.,-4.,-3.]])
B1 = np.array([5.,-2.,-3.])

A2 = np.array([[0.,-1.,-1.,3.],[5.,-5.,-2.,2.],[1.,0.,4.,5]])
B2 = np.array([[0.,-3.],[-2.,-1.],[3.,-3.]])

A3 = np.array([[2.,-5.,5.,1.],[5.,2.,-7.,6.],[-6.,-1.,7.,-4.],[5.,4.,1.,-5]])
B3 = np.array([[0.,4.,-7.,1.,-6.],[-1.,-6.,-5.,1.,1.],[2.,-1.,-6.,5.,-5],[-3.,-6.,6.,3.,5.]])

def MultiMatAux(A,B):
    
    n,m = (A.shape[0],B.shape[1])
        
    D = np.zeros((n,m))
    
    for i in range(n):
        for j in range(m):
            l = sum(A[i,:]*B[:,j])
            D[i,j] = l
            
    return D

def MultiMat(A,B):     
    if len(B.shape) == 1:
        
        V = B.reshape(B.shape[0],1)
        
        if A.shape[1] != V.shape[0]:
            return 'No cumplen el requisito de dimensiones'
        
        D = MultiMatAux(A,V)
        
    else:
        
        if A.shape[1] != B.shape[0]:
            return 'No cumplen el requisito de dimensiones'
        
        D = MultiMatAux(A,B)
    
    return D

print(MultiMat(A1,B1))
print(MultiMat(A2,B2))
print(MultiMat(A3,B3))

Ac = np.array([[2.,5],[5.,-5]])
Bc = np.array([[-6.,6],[8.,6.]])

print(MultiMat())