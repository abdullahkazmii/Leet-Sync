def sum(num1, num2):
    num = num1 + num2
    return num


result = sum(5, 7)
print("Sum:", result)


name = "abdullah"


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def data(name):
    print("Data====>", name)


data("Ali")
print(name)


arr = [10]
for x in range(10):
    arr.append(x)
    print(arr)


def array(arr=[]):
    print(f"array items {arr}")


array([10, 12, 13, 14, 15, 16, 17, 18])
