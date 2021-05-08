# This is the Method 1 for MaxPooling with NumPy

# Import the necessary packages
import numpy as np

#generating a 4x4 matrix with random elements ranging from 0 to 20
large_matrix = np.random.randint(0,20,(4,4))
print(large_matrix)

#This functioin is defined to split the 4x4 matrix to 2x2 smaller matrices
def split(matrix, n_rows, n_cols):
  r, c = matrix.shape
  return (matrix.reshape(c//n_rows, n_rows, -1, n_cols).swapaxes(1,2).reshape(-1,n_rows, n_cols))

#calling the function and storing the matrices to A, B, C, and D
A, B, C, D = split(large_matrix,2,2)
print("\n")
print("A=",A)
print("B=", B)
print("C=", C)
print("D=", D)

#Retrieving the highest value elements from the generated matrices
final = np.array([A.max(), B.max(),C.max(), D.max()])

#generating the matrix with the maximum values 
final_matrix = final.reshape(2,2)
print("final_matrix= \n ",final_matrix)
