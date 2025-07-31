#Print the smaller and larger number

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Larger number:", num1)
    print("Smaller number:", num2)
elif num2 > num1:
    print("Larger number:", num2)
    print("Smaller number:", num1)
else:
    print("Both numbers are equal.")