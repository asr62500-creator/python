#If-Else condition
age=16

if(age>=18):
    print("Person is eligible to vote")
    print("And also eligible to drive")
else:
    print("Person is not eligible to vote \n as well as for driving")

#If-elif-else condito
signal="red"

if(signal=="red"):
    print("Stop")
elif(signal=="yellow"): #elif can be written multiple time 
    print("Wait")
else:
    print("Go")


# **INDENTATION**= i) Space before each print 
#                  ii) (Used instead of braces/brackets "{}" as we used in C++)

# Nesting IF
age=int(input("Enter age of Person: "))

if(age>=18):
    if(age>=70):
        print("Person cannot drive")
    else:
        print("Person can drive")
else:
    print("Person cannot drive")