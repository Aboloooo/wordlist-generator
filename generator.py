print("     --- Welcome to Abo worldlist generator! ---     ")
print("Please ansewer the follwoing questions to generate your custom worldlist!")

answers = []


def ask(prompt, check, hint):
    while True:
        value = input(prompt).strip()
        if check(value):
            answers.append(value)
            return value
        print(hint)

def isYear(p1):
    return p1.stript() and len(p1) == 4 and p1[0] != "0" and p1.isdigit()

def isMonth(p1):
    return p1.stript() and int(p1) >= 1 and int(p1) <= 12 and p1.isdigit()

def CNSnumberCheck(p1):
    return p1.stript() and len(p1) == 13 and p1.isdigit() and p1[0] != "0"

def noCondition(p1):
    return True


FirstN = ask("A first name: ", str.isalpha, "Alphabetic input only!")
LastN = ask("A last name: ", str.isalpha, "Alphabetic input only!")
BirthY = ask("A birth year: ", isYear , "4 digit start with 1 at least!")
BirthM = ask("A bith month: ", isMonth, "Numbers 1-12 only!")
CNS = ask("A socialsecurity number: ", CNSnumberCheck, "Birthyear + birth month + birth day + 5 random digit = 13 digit!")
AIM =  ask("An AIM(Optional): ", noCondition, "Optional!")

""" questions = [
    'A First name? ',
    'A Last name? ',
    'A Birth year: ',
    'A Birth month in number: ',
    'A Social security number: ',
    'An AIM: '
]

answers = []

print("     --- Alphabetic answers only! ---     ")
for question in questions[0:2]:
    while True:
        valueS = input(question).strip()
        if valueS.isalpha():
            answers.append(valueS)
            break
        else:
            print("Alphabetic values only!")

print("     --- Now Numerical answers only! ---         ")

# a birth year can not start with 0
# a birth year can not be more than 4 digit
# a birth month can not be bigger than 12 and less that 1
# a socialsecurity number must be only 13 digit and can not start with 0
for question in questions[2:5]:
    while True:   
        valueN = input(question).strip()
        if valueN.isdigit():
            answers.append(valueN)
            break
        print("Numeric answer is required!") """


