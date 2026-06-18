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
    correct_answers = 0
    #get difficulty level
    difficulty = difficulty_level()
    #get question number
    question_number = question_amount()
    #use a for loop to ask the amount of questions entered in question_number
    for _ in range(question_number):
        #generate two random numbers based on the difficult
        if difficulty == 1: 
            x = random_generator.randint(0, 9)
            y = random_generator.randint(0, 9)
        elif difficulty == 2:
            x = random_generator.randint(10, 99)
            y = random_generator.randint(10, 99)
        elif difficulty == 3:
            x = random_generator.randint(100, 999)
            y = random_generator.randint(100, 999)

        times_question_asked = 0

        while(True):
            try:
                user_answer = int(input(f"{x} + {y} = "))

            except:
                print("Wrong!!!!!!!!!!!!!!!")
                times_question_asked += 1
                continue

            if user_answer != (x + y):
                print("Wrong!!!!!!!!!!!!!")
                times_question_asked += 1

            elif user_answer == (x + y):
                print("Correct")
                correct_answers += 1
                break

            if times_question_asked == 3:
                print(f"Correct answer: {x} + {y} = {x + y}")
                break

    print(f"You got {correct_answers} questions correct out of {question_number}. {correct_answers / question_number * 100}")

main()
