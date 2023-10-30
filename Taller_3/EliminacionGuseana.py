import numpy as np

A= np.array([[3.,1.,-1.],[1.,-2.,1.],[4.,-1.,1.]])

b=np.array([2.,0.,3.])

def sustitucion_atras(M):
    
    n= np.shape(M)[0]
    A= np.zeros(shape=(n,n))
    b= np.zeros(n)
    A= M[:,:3]
    b=M[:,n]
    x= np.zeros(n)

    for i in range(n-1,-1,-1):
        sum = b[i]
        for j in range(n-1,i,-1):
            sum -= A[i,j]*x[j]
        x[i]= sum/A[i,i]

    return x

def gaussian_elimitation(A,b):

    n=np.shape(A)[0]
    M= np.zeros(shape=(n,n+1))

    M[:,:n]=A
    M[:,n]=b

    for i in range(n-1):
        Ri=M[i,:]/M[i,i]
        M[i,:]=Ri
        for j in range(i+1,n):
            M[j,:]= M[j,:]-Ri*M[j,i]

    M[-1]=M[-1]/M[-1,n-1]

    return M

def solucion_lineal(A,b):

    B=gaussian_elimitation(A,b)
    Bs=sustitucion_atras(B)

    return Bs