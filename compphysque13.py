import numpy as np
import pygsl
# Given data
A = np.array([[3,-1,1],
             [3,6,2],
             [3,3,7]])
lu = pygsl.linalg.LU(A)                            
L = lu.L().copy()
U = lu.U().copy()
# To verify we can reconstruct the matrix
A1 = np.dot(L, U)
# Print the factors
print("\n Original matrix A :")
print(A)
print("\n L factor :")
print(L)
print("\n U factor :")
print(U)
print("\n Reconstructed A (L * U) :")
print(A1)
A=np.array([[10,-1,0],
            [-1,10,-2],
            [0,-2,10]])
lu = pygsl.linalg.LU(A)                            
L = lu.L().copy()
U = lu.U().copy()
# To verify we can reconstruct the matrix
A1 = np.dot(L, U)
# Print the factors
print("\n Original matrix A :")
print(A)
print("\n L factor :")
print(L)
print("\n U factor :")
print(U)
print("\n Reconstructed A (L * U) :")
print(A1)
A=np.array([[10,5,0,0],
            [5,10,-4,0],
            [0,-4,8,-1],
            [0,0,-1,5]])
lu = pygsl.linalg.LU(A)                            
L = lu.L().copy()
U = lu.U().copy()
# To verify we can reconstruct the matrix
A1 = np.dot(L, U)
# Print the factors
print("\n Original matrix A :")
print(A)
print("\n L factor :")
print(L)
print("\n U factor :")
print(U)
print("\n Reconstructed A (L * U) :")
print(A1)
A=np.array([[4,1,1,0,1],
            [-1,-3,1,1,0],
            [2,1,5,-1,-1],
            [-1,-1,-1,4,0],
            [0,2,-1,1,4]])

lu = pygsl.linalg.LU(A)                            
L = lu.L().copy()
U = lu.U().copy()
# To verify we can reconstruct the matrix
A1 = np.dot(L, U)
# Print the factors
print("\n Original matrix A :")
print(A)
print("\n L factor :")
print(L)
print("\n U factor :")
print(U)
print("\n Reconstructed A (L * U) :")
print(A1)


