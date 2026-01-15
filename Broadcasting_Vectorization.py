'''
Concept of Broadcasting-> expands smaller arrays to larger to match 
shapes for neglecting errors
it is a numpy way of performing operations on large amount 
of data 
How Numpy handles arrays of different shapes
1. Matching dimentions
2. Expanding single elements :-> [1,2,3] + 10 -> [11,12,13]
3. Incompatible shapes :-> show an error 

'''
import numpy as np
prices = [100,200,300,400]
discount = 10 # 10% dicount on each price

final_prices = []

for price in prices:
    final_price = price-(price*discount/100)
    final_prices.append(final_price)
print(final_prices)

arr = np.array([1,2,3,4])#Broadcasting
result = arr*2
print(result)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = np.array([10,20,30])
addition = matrix+vector
print(addition) # expanding sigle element 

'''
Vectorization:->
applying operations on whole loop
without using loop done by vectorization
Used in AI , ML
'''

arr2 = np.array([10,20,30])
print(arr2*2)

'''
Hndling Missing Vlues-> 
Built in Functions:->
1. np.isnan:-> Detect missing values
2. np.nan_to_num(array,nan = value(default=0)):-> 
Replace missing values to some other number
3. np.isinf() returns Bool value (True,False):-> 
To detect infinite values
np.nan_to_num(arr,posinf = value,neginf= value):- >
to replace infinite values
'''
# nan :- not a number , We can't compare nan values directly

arr3 = np.array([1,2,np.nan ,4,np.nan ,6])
cleaned_array = np.nan_to_num(arr3,nan = 100)
print(cleaned_array)

#infinite values:->i.e = 10^1000 and 1/0 etc
arr4 = np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr4))
cleanedarray = np.nan_to_num(arr4,posinf = 1000,neginf = -1000)
print(cleanedarray)
