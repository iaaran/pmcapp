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

# Day4 Examples to understand for loop, list and tuples
# List is mutable means modifiable, editable, and it will be initialized with square parentheses
# The below example will rename then filenames by changing first occurrence of dot with hyphen and print.
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

# Example for immutable types are string and tuples
# string types are immutable means not possible to edit any character in a string
# rather only possible to assign new string
# tuple is also like list, but it shall be initialized by using round braces.
# It's not modifiable

weeks_name = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
print(type(weeks_name))
# weeks_name[1] = "Monday" # tuple variable is not modifiable

# Example usage of enumerate function in for loop and list sorting
name_list = ["John", "ben", "singh"]
# list sort method sorts the content in ascending order by default.
# In sorting, capital letter has higher precedence than small letter i.e  J then b not b, J
name_list.sort()

for index, item in enumerate(name_list):
    row = f"{index + 1}.{item}"
    print(row)

# Example of using multiple variable in for loop
matrix3x3 = [[1, 4, 6], [3, 1, 8], [4, 6, 1]]
for i, j, k in matrix3x3:
    print(i, j, k)
