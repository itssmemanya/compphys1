import numpy as np 
  
# Given Dta
A = np.array([[2, -1, 0],
              [-1, 2,-1],
              [0,-1,2]]) 
  
# Guess Vector 
x = np.array([[1,0,0]]).T 
  
tol = 0.01  
max_iter = 100  
lam_prev = 0
   
for i in range(max_iter): 
    Ax=np.dot(A,x)
    x = Ax / np.linalg.norm(Ax)
    xAx=np.dot(x.T,Ax)
    xTx=np.dot(x.T,x)
    lam = xAx / xTx

    if np.abs(lam - lam_prev) < tol: 
        break
    lam_prev = lam 
 
print(" \n The eiigenvalues using power method are ")
print(x)
