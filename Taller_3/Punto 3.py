import numpy as np

A=np.array([[-2.,1.,0.],[1.,-2.,1.,],[0.,1.,-2.]])

b = np.array([1.,1.,3.])
c = np.array([2,4,5])


def norma(v):

    s = 0

    for i in range(v.shape[0]):
        s += v[i]**2
    return np.sqrt(s) 

def eigenvalue(A,v,k):

    z = v
    q = z/norma(z)
    Ai= np.linalg.inv(A)

    for i in range(k):
        z = np.dot(Ai,q)
        q = z/norma(z)
        q2 = np.transpose(q)
        sup = np.dot(q2,Ai)
        r = np.dot(q2,sup)
        w=np.sqrt(np.abs(1/r))

    return (-q,w)

print(eigenvalue(A,b,90))

#print(np.dot(A,c))
#print(c*3) 