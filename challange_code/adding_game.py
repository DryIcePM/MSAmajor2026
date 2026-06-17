import random
random_generator = random.Random()
random_number = random_generator.randint(0, 999)
def difficulty_level():
    while(True):
        try:
            difficulty = int(input("Choose Difficulty Level: (1, 2, 3) "))
            if(difficulty != 3 and difficulty != 2 and difficulty != 1):
                print("ERROR: Enter a valid level")
                continue
            else: 
                break
        except:
            print("ERROR: Enter a valid level")
            continue
    return difficulty

def question_amount():
    while(True):
        try:
            question_number = int(input("Choose Question Amount: (3-10) "))
            if(question_number > 10 or question_number < 3):
                print("ERROR: enter a valid question amount")
                continue
            else:
                break
        except:
            print("ERROR: enter a valid question amount")
            continue
    return question_number

def main():
    #get difficulty level
    difficulty = difficulty_level()
    #get question number
    question_number = question_amount()
    #use a for loop to ask the amount of questions entered in question_number
    for _ in question_amount:
        print(random_generator.randint(0, 100))
        #generate two random numbers based on the difficult




main()