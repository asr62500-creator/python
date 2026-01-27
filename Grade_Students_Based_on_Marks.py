marks=float(input("Enter Student's marks: "))

if (marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
elif(marks>=60 and marks<70):
    grade="D"
elif(marks>=50 and marks<60):
    grade="E"
else:
    grade="F= Fail"
print("Grade of the student is:",  grade) 