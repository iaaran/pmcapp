import json

with open("Files/questions.json", 'r') as file:
    content = file.read()  # Read contents from the json file and stored it as string

data = json.loads(content)  # Convert string contents into dictionary of list

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(f"{index + 1} - {alternative}")
    user_choice = int(input('Enter your choice: '))
    question['user_choice'] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["answer"]:
        score += 1

    message = (f"{index + 1} - Correct answer {question['answer']} "
               f", Your answer {question['user_choice']} ")
    print(message)

print(f"Score is {score} / {len(data)}")
