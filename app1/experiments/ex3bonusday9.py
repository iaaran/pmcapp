password = input("Enter new password")

result = {}  # initializd dictionary

if len(password) >= 8:
  result["length"] = True
else:
  result["length"] = False
  
digit = False
uppercase = False

for i in password:
  if i.isdigit():
    digit = True
  if i.isupper():
    uppercase = True

result["digits"] = digit
result["upper-case"] = uppercase

print(result)
# print(all(result)) This will print True always
print(result.values()) # This prints dict_values

 # if all the values in the dict are True then it is True
if all(result.values()):   
  print("Strong Password")
else:
  print("Weak Password")
