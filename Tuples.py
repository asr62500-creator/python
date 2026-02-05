# TUPLE; 
# Tuple is a built-in data type in Python that is similar to a list 
# but is immutable(meaning its elements cannot be changed after creation),
# Tuples are defined using parentheses `()` and 
# are ordered, indexed, and allow duplicate elements.

tup1= (1,2,3,4,5,6)
print(type(tup1))

tup=()   # Valid tuple
print(type(tup))

tup2=(1) # Invalid tuple , as it returns an Integer type instead of tuple.
print(type(tup2))

tup3=(1,) # Valid tuple, returns tuple data type
print(type(tup3))

#-----------------------------------------------------------------------------------
# In Python, The Tuples can store elements of different datatypes(integers, floats, strings, etc...) same as List
tup4=("Amit", 25, "CS", 25, "Suman", 100)
print(tup4)

# Slicing
print(tup4[1:4])
print(tup4[-5:-1])  

print(tup4[0]) # return element at that index

#-----------------------------------------------------------------------------------
#Tuples Methods => Two methods 1."Count" & 2."Index"
print(tup4.count(25))  # Count occurrences of 25 in the tuple
print(tup4.index(25))  # Find the index of the first occurrence of 25 in the tuple