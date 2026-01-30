# List 
# List is a Collection of items that is;
# Ordered,
# Mutable(changable), 
# Allows duplicate values,
# Written using square brackets i.e.,[]

marks = [85, 92, 78, 96, 88]
print(marks) # Output: [85, 92, 78, 96, 88]

#---------------------------------------------------------------------
#Indexing(Print the element at mentioned index)
print(marks[0]) # Output: 85
print(marks[3]) # Output: 96

#---------------------------------------------------------------------
#Updating ( Replace the pre-existing element with a new one)
marks[3]=100 # Update the element at index 3
print(marks) # Display the updated list

#---------------------------------------------------------------------
# ## In Python, The List can store elements of different datatypes(integers, floats, strings, etc...)
List=[10, 25.5 , "Amit", True , 5 , 90.8 , "Nitin" ]

#---------------------------------------------------------------------
#List Slicing
print(List[3:6]) #Output : [True, 5, 90.8]
print(List[5:]) # [90.8, 'Nitin']
print(List[2:len(List)]) # ['Amit', True, 5, 90.8, 'Nitin']
print(List[ : : 3]) # [10, True, 90.8]
print(List[:5]) # [10, 25.5, 'Amit', True, 5]
print(List[-5:-2]) # ['Amit', True, 5]

#---------------------------------------------------------------------
#List Method
Listc=[10, 25.5 , "Amit", True , 5 , 90.8 , "Nitin" ]

#---------------------------------------------------------------------
Listc.append("Suman") # To Add an Element at the end of the List
print(Listc)

#---------------------------------------------------------------------
Listc.extend([100, 200, "myBaby"])  # Extend with multiple elements
print(Listc)

#---------------------------------------------------------------------
# Insert "myBaby" at index 2 ,
# Doesn't replace the prexisting just push the Elements and 
# make the index 2 empty and then insert the given data.
Listc.insert(2, "myBaby")   
print(Listc)

#---------------------------------------------------------------------
Listc.remove("Nitin")  # Remove "Nitin" from the list
print(Listc)

#---------------------------------------------------------------------
Listc.index("Amit") # Give the index of "Amit" in the list
print(Listc.index("Amit"))

#---------------------------------------------------------------------
Listc.count("myBaby") # Count occurrences of "myBaby" in the list
print(Listc.count("myBaby"))

#---------------------------------------------------------------------
Listc.reverse()  # Reverse the list in place
print(Listc)

#---------------------------------------------------------------------
List_copy = Listc.copy()  # Create a copy of the list
print(List_copy)

#---------------------------------------------------------------------
List_copy.append("NewElement") # Add "NewElement" to the end of List_copy
print(List_copy)

#---------------------------------------------------------------------
List_copy.clear()  # Clear all elements from the List_copy
print(List_copy)

#---------------------------------------------------------------------
marks = [85, 92, 78, 96, 88] # Sort List in Accending order
marks.sort()
print(marks)

marks.sort(reverse=True) # Sort List in Decending order
print(marks)    
#---------------------------------------------------------------------