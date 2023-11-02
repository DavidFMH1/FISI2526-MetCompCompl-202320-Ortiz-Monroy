import numpy as np

k = 23
m1 = 13
m2 = 13
m3 = 5

A=np.array([[(-2*k)/m1,k/m1,0.],[k/m2,(-2*k)/m2,k/m2,],[0.,k/m3,(-2*k)/m3]])

b = np.array([1.,1.,3.])


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

v1,e1 = eigenvalue(A,b,90)

w1 = np.sqrt(np.abs(e1))

print(v1,e1)

def ptm(w,A):
    wt = w.T
    p = np.dot(wt,A)
    f = np.dot(p,w)
    return f

def eigenvectors(A,b,k):
    
    z = b
       
    for i in range(k):
        w = z/norma(z)  
        mu =  ptm(w,A)
        z = np.matmul(A,w)
    
    return w,mu

v,e = eigenvectors(A,b,10)

w = np.sqrt(np.abs(e))

print(v,w)