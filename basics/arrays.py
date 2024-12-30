arr = [1, 2, 3.3, 4, 5, 6]
print(arr[2])
print(type(arr[1]))

# Create a 2D array with 3 rows and 5 columns, initialized with zeros
arr1 = [[0 for _ in range(5)] for _ in range(3)]

# Assign a value to a specific element
arr1[2][4] = 79  # Correcting the index to fit within the 0-based range

# Access a value from the 2D array
print(arr1[2][4])  # This will print the value at row 1, column 4 (0-based index)

name = "abdullah"
print(name[-1])
