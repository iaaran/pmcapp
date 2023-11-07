# bonus example 1 for while loop
password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password was correct!")

# bonus example2 shall be executed only if the correct password is entered
x = 1

while x <= 6:
    print(x)
    x = x + 1

# bonus example of for loop on day3

meals = ["pizza", "dosa", "burger"]
for meal in meals:
    print(meal.title())
print("\n")
for char in "letters":
    print(char.upper())

print("Examples were executed successfully !!!")
