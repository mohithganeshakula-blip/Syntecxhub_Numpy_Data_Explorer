import numpy as np

#creation of array
n=np.array([1,2,3,4])
print(f"array:{n},Dimensions:{np.ndim(n)}")

r=np.array([[1,2,3],[4,5,6]])
print(f"array:{r},Dimensions:{np.ndim(r)}")

t=np.array([[3,4,5],[6,7,8],[9,10,11]])
print(f"array:{t},Dimensions:{np.ndim(t)}")

#indexing

print("Indexing")

print(f"The first Element in n:{n[0]}")
print(f"The last element in n:{n[-1]}")

print(f"The middle element in t:{t[1,1]}")

#slicing
print("slicing")

print(f"The 3 elements in n:{n[0:3]}")

print(f"Only last four:{r[0:,1:]}")

print(f"Upper-matrix:{t[1:,1:]}")

print(f"Lower matrix:{t[0:2,:2]}")

#mathemetical operations

print("Mathematical Operations")

print(f"N+5:{n+5}")

print(f"n*5: {n*5}")

print(f"n/5: {n/5}")


p = np.square(n)   # store actual value
print(f"Square of n: {p}")

print(f"Square root: {np.sqrt(p)}")

a=np.array([1,2,3])
b=np.array([4,5,6])
print(f"Dot Product:{np.dot(a,b)}")


#statistics
print(f"Mean of n:{np.mean(n)}")

print(f"Median of n :{np.median(n)}")

print(f"max of n:{np.max(n)}")

print(f"min of n:{np.min(n)}")

print(f"sum of n:{np.sum(n)}")

print(f"Standard for n: {round(np.std(n),2)}")

print(f"varience : {np.var(n)}")

print(f"row-wise-sum:",np.sum(r,axis=0))

print(f"Column-wise-sum",np.sum(r,axis=1))

#re-shaping

print("Re-shaping")

print(f"Rehape of n: {n.reshape(2,2)}")

print(f"Reshape of r:{r.reshape(3,2)}")

print(f"Reshape of t : {t.reshape(3,3)}")

#Broadcasting
print("Broadcasting")

arr=np.array([1,2,3,4,5])
rr=np.array([6,7,8,9,10])
o=arr+rr
print(o)

print(arr+10)

print(f"Adding the 20 to arr:{arr+20}")

e=np.array([[20,21,22],[30,31,32]])
y=np.array([10,20,30])

print(f"Adding e+y:{e+y}")

#saving the array

print("Saving the array")

np.save("my_array.npy",t)
print("Array saved successfully")

#load the array

loaded_array=np.load("my_array.npy")
print(loaded_array)

import time

print("Performance Comparison")

# Large data for comparison
python_list = list(range(1000000))
numpy_array = np.arange(1000000)

# Python list timing
start = time.time()
[x * 2 for x in python_list]
python_time = time.time() - start

# NumPy timing
start = time.time()
numpy_array * 2
numpy_time = time.time() - start

print("Python List Time:", python_time)
print("NumPy Array Time:", numpy_time)
