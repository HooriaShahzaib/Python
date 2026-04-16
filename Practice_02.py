# python program to add two numbers given by the user
print("This program adds two numbers given by the user")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a + b
print("The sum of", a, "and", b, "is", c)

# this is the program to find the remainder of two numbers given by the user
print("\nThis program finds the remainder of two numbers given by the user")
x = int(input("Enter the number that you want to divide: "))
z = int(input("Enter the number that you want to divide by: "))
y = x % z
print("The remainder of ", x, "divided by", z, "is: ",y)

# this is the program to find the mod of two numbers given by the user
print("\nThis program finds the mod of two numbers given by the user")
x = int(input("Enter the number that you want to divide: "))
z = int(input("Enter the number that you want to divide by: "))
y = x / z
print("The mod of ", x, "divided by", z, "is: ",y)

# comparison of two numbers wether num1 is greater than num2 or not
print("\nThis program compares two numbers given by the user")
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
result = num1 > num2
print("Is num1 greater than num2: ", result)

# Finding the average of two numbers entered by the user
print("\nThis program calculates the average of two numbers given by the user")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
average = (a+b)/2
print("The average of ", a, "and", b, "is: ", average)

# Finding the square of a number given by the user
print("\nThis program finds the square of a number given by the user")
s = int(input("Enter number to find its square: "))
sq = s*s
print("The square of ", s, "is: ", sq)

# printing the type of square
print("\nThis is the type of the sqaure given above: ", type(sq))

# typecasting the suare to float
sq = float(sq)
print("\nThis is the same square root but typecasted to other type: ",type(sq))
