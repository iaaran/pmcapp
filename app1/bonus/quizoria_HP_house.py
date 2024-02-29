import json


def hp_house(score_arg):
    if 50 <= score_arg <= 120:
        return "Ravenclaw"
    elif 130 <= score_arg <= 170:
        return "Slytherin"
    elif 180 <= score_arg <= 230:
        return "Gryffindor"
    elif 240 <= score_arg <= 300:
        return "Hufflepuff"
    else:
        return "None"


with open("Files/hphousequery.json", 'r') as file:
    content = file.read()  # Read contents from the json file and stored it as string

data = json.loads(content)  # Convert string contents into dictionary of list

print(f"***** Quizoria ***** \n",
      f"This Quiz helps you to determine which house you belong to in Hogwarts.\n",
      f"Choose the options which best suits you in the following questionaire.\n")

for question in data:
    print(question['query'])
    for index, options in enumerate(question['options']):
        print(f"{index + 1} - {options.title()}")
    user_choice = int(input('Enter your choice: '))
    question['user_choice'] = user_choice

score = 0
for query in data:
    user_choice = query['user_choice']
    points = query['points']
    score = score + points[user_choice - 1]

house = hp_house(score)
print(f"Score is {score} ")
print(f"You belong to {house}")