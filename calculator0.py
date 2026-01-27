# Take input from user
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Choose operation
operation = input("Select the operation (+, -, *, /): ")

# Calculation
print(" -----*****---Calculator---*****-----\n")
if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation")
