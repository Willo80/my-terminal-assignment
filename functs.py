#menu select button

    from simple_term_menu import TerminalMenu

    def main():
        options = ["QUIZ", "BGL ENTRY", "QUIT"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")

    if __name__ == "__main__":
        main()








# import termcolor



#  # option to play again and improve score or quit  
# def play_again():
#     response = input (" Would you like to have another go? (Yes or No): ")
#     response = response.lower()
#     if response == "Yes":
#         return True
#     else:
#         return False