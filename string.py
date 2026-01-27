# str1="Amit"
# str2="Singh"

# str3=str1+ " " +str2 #concatination 
# print(str3) #Amit Singh

# l1=len(str1) #length of str1
# l2=len(str2) #length of str2
# l3=len(str3) #length of str3/concatinated str

# #Display/Print
# print(l1)
# print(l2)
# print(l3)

# #Indexing  str[i] , i=0,1,2,...,n-1(index no)
# print(str1[0]) #first character of str1
# print(str2[3]) #first character of str2
# print(str3[6]) #6th character of str3/concatinated str

# #Slicing  str[ : ]
# str4="nitinsingh"
# print(str4[6:9])  #=> ing
# print(str3[1: ])  #=> mit Singh /print(str3[1:len(str3)]) 
# print(str3[0:len(str3)])
# print(str4[-7:-2]) #=> insin    

# #Replace 
# str5="I like Java"
# print(str5.replace("Java","Python")) # I like Python

# #Split and Join
# s1 = "Python is easy"
# print(s1.split())  # ['Python', 'is', 'easy']

# s2 = ["Python", "is", "easy"]
# print(" ".join(s2))  # Python is easy


# #String Formatting operation(*f-String)
# name = "Amit"
# marks = 90

# print(f"{name} scored {marks} marks")  # Amit scored 90 marks


#WAP to input user's first name & print its length.
name=input("Enter the user's first name: ") #eg., nitin
print("Length of the name is:",len(name)) #5


#WAP find occurance the  $ in a string
str1="Hi, $Iam the $ symbol $99.99"
print("Occurance of $ in a string is:",str1.count("$")) #3
 
 