# bonus example 1 for while loop
password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password was correct!")

# bonus example2 shall be executed only if the correct password is entered
x = 1

while x <= 3:
    print(x)
    x = x + 1

# bonus example of for loop on day3

meals = ["pizza", "dosa", "burger"]
for meal in meals:
    print(meal.title())
print("\n")
for char in "letters":
    print(char.upper())

print("Example 2 was executed successfully !!!")

# Day4 Examples to understand for loop, list and tuples
# List is mutable means modifiable, editable, and it will be initialized with square parentheses
# The below example will rename then filenames by changing first occurrence of dot with hyphen and print.
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

print("Example 3 was executed successfully !!!")

# Example for immutable types are string and tuples
# string types are immutable means not possible to edit any character in a string
# rather only possible to assign new string
# tuple is also like list, but it shall be initialized by using round braces.
# It's not modifiable

weeks_name = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
print(type(weeks_name))
# weeks_name[1] = "Monday" # tuple variable is not modifiable

print("Example 4 was executed successfully !!!")
# Example usage of enumerate function in for loop and list sorting
name_list = ["John", "ben", "singh"]
# list sort method sorts the content in ascending order by default.
# In sorting, capital letter has higher precedence than small letter i.e  J then b not b, J
name_list.sort()

for index, item in enumerate(name_list):
    row = f"{index + 1}.{item}"
    print(row)
print("Example 5 was executed successfully !!!")
# Example of using multiple variable in for loop
matrix3x3 = [[1, 4, 6], [3, 1, 8], [4, 6, 1]]
for i, j, k in matrix3x3:
    print(i, j)
    print(k)
    print(i, j, k, "\n")
print("Example 6 was executed successfully !!!")
# Example of using zip function
# Initializing long list values in multiple lines
contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]
# List contains the name of the files to be created to store the above contents
file_names = ['doc.txt', 'report.txt', 'presentation.txt']

# for loop to copy the first value from contents and write the same in the file in file_names list
for content, file_name in zip(contents, file_names):
    file = open(file_name, 'w')
    file.write(content)
    file.close()
print("Example 7 was executed successfully !!!")

# Example for list comprehension
filenames = ["1.doc", "2.report", ".presentation"]
print(filenames)
filenames = [filename.replace('.', '-') + ".txt" for filename in filenames]
print(filenames)
print("Example 8 was executed successfully !!!")

# Example of using list comprehension and sum function
user_entries = ['10', '19.1', '20']   # values are in string
print(sum([float(item) for item in user_entries]))
print(" Example 9 using sum function and list comprehension was executed & answer is 49.1")
