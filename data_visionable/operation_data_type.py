import numpy as np
import random

# Use numpy to generate array and get the type of ndarray
t1 = np.array([1,2,3,])
# print(t1)                 # [1 2 3]
# print(type(t1))           # <class 'numpy.ndarray'>

t2 = np.array(range(10))
# print(t2)
# print(type(t2))

t3 = np.arange(4,10,2)
# print(t3)                 # [4 6 8]
# print(type(t3))           # <class 'numpy.ndarray'>
# Data types in numpy
# print(t3.dtype)           # int32

t4 = np.array(range(1,4),dtype="i1")
# print(t4)                   # [1 2 3]
# print(t4.dtype)             # int8

# numpy: bool
t5 = np.array([1,1,0,1,0,0],dtype=bool)
# print(t5)                   # [ True  True False  True False False]
# print(t5.dtype)             # bool

# Adjust data type
t6 = t5.astype("int8")
# print(t6)               # [1 1 0 1 0 0]
# print(t6.dtype)         # int8

# numpy: float
t7 = np.array([random.random() for i in range(10)])
# print(t7)
# print(t7.dtype)     # float64

# Keep decimal places
t8 = np.round(t7,2)
print(t8)