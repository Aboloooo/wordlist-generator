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
    return p1.strip() and len(p1) == 4 and p1[0] != "0" and p1.isdigit()

def isMonth(p1):
    return p1.strip() and p1.isdigit() and int(p1) >= 1 and int(p1) <= 12

def CNSnumberCheck(p1):
    return p1.strip() and p1.isdigit() and len(p1) == 13 and p1[0] != "0"

def noCondition(p1):
    return True

# checking for dublications in the answer array
def check_dublication(array):
    arrayL = len(array)
    for i in range(arrayL -1):
        for j in range(i+1, arrayL):
            if array[i] == array[j]:
                #array.remove(array[j])
                #instead of removing item from we can remove dublication from final generated wordlist and use this True bolean like a trigger
                print("Dublication found in your responds, one will be removed")
                return True
    return False
        
            
        

questions = [
    'A First name? ',
    'A Last name? ',
    'A Birth year: ',
    'A Birth month in number: ',
    'A Social security number: ',
    'An AIM: '
]
FirstN = ask(questions[0], str.isalpha, "Alphabetic input only!")
LastN = ask(questions[1], str.isalpha, "Alphabetic input only!")
BirthY = ask(questions[2], isYear , "4 digit start with 1 at least!")
BirthM = ask(questions[3], isMonth, "Numbers 1-12 only!")
CNS = ask(questions[4], CNSnumberCheck, "Birthyear + birth month + birth day + 5 random digit = 13 digit!")
AIM =  ask(questions[5], noCondition, "Optional!")


# next step: generate your list what supposed to be concatinated

