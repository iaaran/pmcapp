# Coding Exercise 3 on Day 4
# We have defined the same ranking list as in the previous exercise: 
# This time you should create a program that:
# 1. Contains the list.
# 2 Prompts the user to input the person's name.
# 3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']
name = input("Enter name to know rank : ")
for i in ranking:
    if i == name:
        rank = ranking.index(i)
        print(rank + 1)

# Need to expand for wront entry and error case.
