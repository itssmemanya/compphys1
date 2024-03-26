import numpy as np
import timeit

# part a
start=timeit.timeit()
A=np.array([[2,1],
            [1,0]])
U, S, Vh = np.linalg.svd(A, full_matrices=True)
end=timeit.timeit()
elapsed=end-start
print(" \n The Singular value matrix is ")
print(S)
print(" \n The time elapsed in this is ",elapsed)

# part b
start=timeit.timeit()
A=np.array([[2,1],
            [1,0],
            [0,1]])
U, S, Vh = np.linalg.svd(A, full_matrices=True)
end=timeit.timeit()
elapsed=end-start
print(" \n The Singular value matrix is ")
print(S)
print(" \n The time elapsed in this is ",elapsed)

# part c
start=timeit.timeit()
A=np.array([[2,1],
            [-1,1],
            [1,1],
            [2,-1]])
U, S, Vh = np.linalg.svd(A, full_matrices=True)
end=timeit.timeit()
elapsed=end-start
print(" \n The Singular value matrix is ")
print(S)
print(" \n The time elapsed in this is ",elapsed)

# part d
start=timeit.timeit()
A=np.array([[1,1,0],
            [-1,0,1],
            [0,1,-1],
            [1,1,-1]])
U, S, Vh = np.linalg.svd(A, full_matrices=True)
end=timeit.timeit()
elapsed=end-start
print(" \n The Singular value matrix is ")
print(S)
print(" \n The time elapsed in this is ",elapsed)

# part e
start=timeit.timeit()
A=np.array([[0,1,1],
            [0,1,1],
            [1,1,0],
            [0,1,0],
            [1,0,1]])
U, S, Vh = np.linalg.svd(A, full_matrices=True)
end=timeit.timeit()
elapsed=end-start
print(" \n The Singular value matrix is ")
print(S)
print(" \n The time elapsed in this is ",elapsed)

# The algorithm is very fast
# Thats why some of the elapsed time is coming negative
# we can seee that the number of seingular values is the same as the
# smaller order of the 2D matrix
