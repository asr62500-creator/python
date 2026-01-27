#WAP to check if the no entered by user is odd or even.
num=int(input("Enter a number:"))

if(num%2==0): #if num is divisible by 2 and has remainder equal to 0
    print("Number is Even")
else:
    print("Number is Odd")