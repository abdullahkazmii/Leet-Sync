name = "abdulla"
if name == "abdullah":
    print(True)
else:
    print(False)


age = int(input("Enter Age: "))
if age < 5:
    print("Child must be 5 years old")
elif age < 13:
    print("Junior High School Student")
elif age <= 18:
    print("High School Student")
elif age <= 20:
    print("College Student")
elif age <= 25:
    print("Under Grad Student")
else:
    print("Graduate Student")
