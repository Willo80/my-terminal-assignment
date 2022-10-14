# Diabetes tracker and educational game
import datetime
from Question import Question

# user inputs full name
while True:
    try:
        name = input("\nPlease type your name: ").title().strip()
        first, last = name.split(" ")
        break
    except ValueError:
        print("\nBoth your first AND surname is required")

# user has an option to play game or input reading
print("\nWhat would you like to do first " + first + "?" + " Improve your diabetes knowledge or record your BGL reading?")

play = "Yes"
fasting = "F"


play = input ("\nType Yes for a quick game or NO to enter your reading: ").lower()
if play != "yes":
    glucose_reading = float(input("\nEnter the number reading from your finger prick test: "))
    fasting = input("\nType in F if you were fasting or NF if you were not fastng: ").capitalize()

    if glucose_reading < 8 and fasting == "F":
        print("\nYour blood glucose level is normal")

    elif glucose_reading > 8 and fasting != "F":
        print("\nYour reading is high, but this could be because you had just eaten, a second fasting reading may be more accurate")





# User will now complete the glucose recording pathway and skip the game
    # glucose_reading = input("\nEnter the reading from your finger prick test: ")
    
    

    
        

    # The date and time of input is recorded for future reference
    print(f"\nThe time and date of your input is {datetime.datetime.now()}")

    # elif glucose_reading > 8 and fasting != "Yes":
    # print("\nYour blood glucose level is too high")
    # print("\nContinue foccussing on your carb intake and do daily exercises to manage your glucose levels")
    # exit()

    # determine if fasting as this impacts the results
    # input("\nFor your glucose reading of " + glucose_reading + ", were you fasting: ").capitalize()
    # if answer == "no" and "glucose_reading > 10":
    #     print("\nYour blood glucose level is too high")
    #     # need to fix this code as not registering if it high or low
    # elif answer == "yes" and "glucose_reading < 8": 
    #     print("\nYour blood glucose level is normal") 
        
    # print("\nContinue foccussing on your carb intake and do daily exercises to manage your glucose levels")
    # exit()

       
# add error handling here so that can only add ints and if incorrect must go back to inout else continue

else:
    # begin_quiz = input("Welcome to this quick knowldege quiz, would you like to play now?: " )
    print("\nExcellent! There are 4 questions, try and score 100%")
    # print("Type 'quit' to move to the next question")
    play = input("Okay, are you ready? ").lower()
    
    if play != "yes":
        quit()
    
    print("\nYou can type the word 'skip' to move to the next question if you cannot answer.\nHere is your first question!")

    

 


# Questions as Class function from my created class function

ask_question = [
"\nWhich of these will control your blood sugar better?\n(a) Chocolate\n(b) Banana\n(c) Pizza\n\n",
"\nLook out for food with a ___ Glycemic Index: high or low?\n(a) High\n(b) Low\n\n",
"\nDaily exercise will help manage your diabetes:\n(a) True\n(b) False\n\n",
"\nWhen should you do a finger prick reading?\n\n(a) After eating\n(b) Before eating\n\n",
]

questions = [
    Question(ask_question[0], "b"),
    Question(ask_question[1], "b"),
    Question(ask_question[2], "a"),
    Question(ask_question[3], "b"),
]

def begin_quiz(questions):
    """This is def to ask user questions."""
    score = 0
    for question in questions:
        answer = input(question.ask)
        if answer == question.answer:
            print("\nCorrect!")
            score +=25
        else:
            print("\nThat is incorrect")

        


    print("\nYou scored " + str(score) + "%" + "Learn more about diabetes \nfor better control over your wellness" )

begin_quiz(questions)
