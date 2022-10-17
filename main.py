# Diabetes tracker and educational game
import datetime
from termcolor import cprint
from Question import Question

def main():
# Wrapped entire code - user has option to restart at end of quiz

    # input full name - surname used for future ref on app updates, but not in this first instance.
    while True:
        try:
            name = input("\nPlease type your name: ").title().strip()
            first, last = name.split(" ")
            break
        except ValueError:
            cprint("\nBoth your first AND surname is required", "red")

    # user has an option to play game or input reading
    print("\nWhat would you like to do first " + first + "?" + " Improve your diabetes knowledge or record your BGL reading?")

    play = "Yes"
    fasting = "F"

    # User will now complete the glucose recording pathway and skip the game

    play = input ("\nType Yes for a quick game or NO to enter your reading: ").lower()
    if play != "yes":
        glucose_reading = float(input("\nEnter the number reading from your finger prick test: "))
        fasting = input("\nType in F if you were fasting or NF if you were not fastng: ").capitalize()

        if glucose_reading < 8 and fasting == "F":
            print("\nYour blood glucose level is normal")

        elif glucose_reading > 8 and fasting == "F":
            print("\nYour reading is High, try to manage your diet and excersie, but see how a second reading goes today")

        elif glucose_reading > 8 and fasting != "F":
            print("\nYour reading is high, but this could be because you had just eaten, a second fasting reading may be more accurate")

        elif glucose_reading < 8 and fasting != "F":
            print("\nYour reading is low for having just eaten, a second fasting reading may be more accurate")

        # The date and time of input is recorded for future reference
        cprint(f"\nThe time and date of your input is {datetime.datetime.now()}", "green")

        exit()


    # Quiz begins here
    elif play == "yes":
        cprint("\nExcellent! There are 4 questions, try and score 100%", "green")
        # User can play or quit at this point if they don't want to continue
        play = input("Okay, if you are ready type Yes, or No to quit: ").lower()
        if play != "yes":
            quit()


    # Q's' = my own Class function, allows updates in future
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
        """def to ask user questions."""
        score = 0
        for question in questions:
            answer = input(question.ask)
            if answer == question.answer:
                cprint("\nCorrect!", "green")
                score +=25
            else:
                cprint("\nThat is incorrect", "red")

        cprint("\nYou scored " + str(score) + "%"
        + "\n\nContinue learning more about diabetes for better control over your wellness", "green")

    begin_quiz(questions)
    # option to go back and enter BGL
    restart=input("\nWould you like to return to the start and add your BGL?: ").lower()
    if restart == "yes":
        main()
    else:
        exit()

main()
