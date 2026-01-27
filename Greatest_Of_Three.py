# WAP to find the greatest of 3 numbers entered  by the user:
num1=int(input("Enter first no. : "))
num2=int(input("Enter second no. : "))
num3=int(input("Enter third no. : "))

if(num1>=num2 and num1>=num3):
    print("First no. is gratest")
elif(num2>=num3):
    print("Second no. is gratest")
else:
    print("Third no. is gratest")