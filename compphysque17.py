import numpy as np

A = np.array([[5, -2],
              [-2, 8]])
tol=0.00001
dim=2

def sumoffdiag(A):
    sum=0
    for i in range(dim):
        for j in range(dim):
            if i!=j:
                sum+=A[i,j]
    return sum

A1=A.copy()
V=np.identity(dim)
sum=100
k=0

while sum>tol:
    Q, R = np.linalg.qr(A1)
    A1=np.dot(R,Q)
    V=np.dot(V,Q)
    sum=sumoffdiag(A1)
    k+=1

print(" \n The eigenvectors obtained by QR decomposition ")
print(V)
print(" \n The number of iterations are ",k)

eigenvalues, eigenvectors = np.linalg.eigh(A)
print(" \n The eigenvectors obtained by numpy.linalg.eigh ")
print(eigenvectors)
