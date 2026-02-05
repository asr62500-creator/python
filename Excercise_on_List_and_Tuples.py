# WAP to ask the user to enter names of their 3 favourite movies
mov1 = input("Enter your 1st favourite movie name: ")
mov2 = input("Enter your 2nd favourite movie name: ")
mov3 = input("Enter your 3rd favourite movie name: ")

movies = []
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


# # Using Loop
# movies = []
# for i in range(3):
#     name = input("Enter the movie name: ")
#     movies.append(name)

# print(movies)

#--------------------------------------------------------------------
# WAP to check if a list contains a Paloindrome of elements;
list1 = [1, 2, 3, 2, 1] 
list2 = [1, 2, 3, 4, 5]
list3 = ["m", "a", "d", "a", "m"]

copy_list1 = list1.copy()
copy_list2 = list2.copy()
copy_list3 = list3.copy()

copy_list1.reverse()
copy_list2.reverse()
copy_list3.reverse()

if(copy_list1 == list1):
    print("List 1 is a palindrome")
else:
    print("List 1 is not a palindrome")

if(copy_list2 == list2):
    print("List 2 is a palindrome")
else:
    print("List 2 is not a palindrome")

if(copy_list3 == list3):
    print("List 3 is a palindrome")
else:
    print("List 3 is not a palindrome")

#--------------------------------------------------------------------
#WAP to count the numver of students with the "A" grade in the following tuple;
grades = ("C", "D", "A", "A", "B", "B", "A")

count = grades.count("A")
print("The No. of students with grade 'A' is: ", count)

#--------------------------------------------------------------
#Store the above values in a list & sort them form "A" to "D";

grades_list = list(grades) #
grades_list.sort()
print("The Sorted Grade List is: ", grades_list)