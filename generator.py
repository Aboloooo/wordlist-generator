questions = {
    'First Name': 'What is your first name? ',
    'Last Name': 'What is your last name? ',
    'Year of brith': 'Your birth year: ',
    'Month of birth(number)': 'Birth month in number: ',
    'Socialsecurity Number': 'Your social security number: ',
    'AIM(Optional)': 'Your AIM: '
}

answers = []

for question in questions:
    answers.append(input(questions[question]))

# now that we have all answers we have to check them
for answer in answers[2:4]:
    if not answer.isdigit():
        print(f'Your input for question ... is {answer} and it is not a number!')