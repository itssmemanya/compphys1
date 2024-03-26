import numpy as np

# Given data

xsol=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
A=np.array([[0.2, 0.1, 1 , 1, 0  ],
            [0.1, 4  , 1 , 1, -1 ],
            [1  , -1 , 60, 0, -2 ],
            [1  , 1  , 0 , 8, 4  ],
            [0  , -1 , -2, 4, 700]])
b=np.array([1,2,3,4,5])

def relmaxdiff(xk,xk1):
    diff=xk-xk1
    relmax=0
    for i in range(len(b)):
        temp=abs(diff[i])/abs(xk1[i])
        if temp>relmax:
            relmax=temp
    return relmax;

tol=0.01
max_iter=1000
# Jacobi Method
# A=D-(L+U)=D+R
D=np.zeros((len(b),len(b)))
R=np.zeros((len(b),len(b)))
for i in range(len(b)):
    D[i,i]=A[i,i]
    for j in range(len(b)):
        if i!=j:
            R[i,j]=A[i,j]
Dinv=np.linalg.inv(D)
T=np.dot(Dinv,-R)           # T=D^(-1).(L+U)
c=np.dot(Dinv,b)            # c=D^(-1).b

xk1=np.array([1,0,0,0,0])
diff=1
k=0

while diff>tol:
    xk=np.dot(T,xk1)+c       # x(k)=T.x(k-1)+c
    k+=1
    diff=relmaxdiff(xk,xk1)  # For new iteration
    xk1=xk
print(" \n Solution from the Jacobi method is ")
print(xk)
print(" \n The number of iterations is ",k)

# Gauss-Seidel Method
# A=(D+L)+(U)
D=np.zeros((len(b),len(b)))
U=np.zeros((len(b),len(b)))
for i in range(len(b)):
    for j in range(len(b)):
        if i<=j:
            D[i,j]=A[i,j]
        else:
            U[i,j]=A[i,j]
Dinv=np.linalg.inv(D)
T=np.dot(Dinv,-U)           # T=(D+L)^(-1).(-U)
c=np.dot(Dinv,b)            # c=(D+L)^(-1).b

xk1=np.array([1,0,0,0,0])
diff=1
k=0

while diff>tol:
    xk=np.dot(T,xk1)+c       # x(k)=T.x(k-1)+c
    k+=1
    diff=relmaxdiff(xk,xk1)  # For new iteration
    xk1=xk
print(" \n Solution from the Gauss-Seidel method is ")
print(xk)
print(" \n The number of iterations is ",k)

# Relaxation Method
xk=np.zeros(len(b))
k=0
omega=1.25    
for k in range(max_iter):
    k+=1
    xk1=xk.copy()
        
    #Loop over rows
    for i in range(len(b)):
        xk[i] = xk[i]*(1-omega) + (omega/A[i,i])*(b[i] - np.dot(A[i,:i], xk[:i]) - np.dot(A[i,(i+1):], xk1[(i+1):]))           
    diff=relmaxdiff(xk,xk1)
    if  diff < tol:
        break
    
print(" \n Solution from the Relaxation method is ")
print(xk)
print(" \n The number of iterations is ",k)

#Conjugate Gradient Method

k=0
xk1=np.array([10,0,0,0,0])
diff=1

while diff>tol:
    k+=1
    r = b - np.dot(A, xk)
    p = r
    rmag = np.dot(np.transpose(r), r)
    
    for i in range(len(b)):
        Ap = np.dot(A, p)
        alpha = rmag / np.dot(np.transpose(p), Ap)
        xk = xk1 + np.dot(alpha, p)
        r = r - np.dot(alpha, Ap)
        rsmag = np.dot(np.transpose(r), r)
        p = r + (rsmag/rmag)*p
        rmag = rsmag
        diff=relmaxdiff(xk,xk1)
        xk1=xk

print(" \n Solution from the Conjugate Gradient method is ")
print(xk)
print(" \n The number of iterations is ",k)
