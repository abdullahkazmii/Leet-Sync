# string
s = input("Enter the value in string: ")
try:
    print("String Value", s)
except Exception as e:
    print("Invalid input. Please enter a string.", e)

# integer
x = int(input("Enter the value in intger: "))
try:
    print("Integer Value", x)
except Exception as e:
    print("Invalid input. Please enter an integer.", e)

# float
y = float(input("Enter the value in float: "))
try:
    print("Float Value", y)
except Exception as e:
    print("Invalid input. Please enter a float.", e)


# boolean
z = False
z = not z
print("Boolean Value", z)
