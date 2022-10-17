
# Diabetes Diary Tracker :drop_of_blood:

---

## Table of Contents

- [References](#references) 
- [App Repository](#app-repository)
- [Style Guide](#style-guide)
- [Features](#Features)
- [Implemention Plan](#implemenation-plan)
- [Help/Install Documentation](#help-install-documentation)

## Related Documents

- [Software Development Plan](#software-development-plan)

## Software Development Plan

### Purpose and Scope

The diabates tracker app is designed for a person with type 2 diabtetes, who would like to manage their diabetes by being able to track and document their blood glucose levels throughout the day. They can also improve their knowlegde and wellness by opting to do the multiple choice quiz which will help them identify good eating habits. They will receive a percentage of how well scored. The app so much potential for future updates, to create a more robust app with more educational questions and many other featurees that would be benefical to a person with diabetes.

**What the Diabates Tracker App be able to do:**

The user has the option of just enetering their blood glucose level or doing the multiple choice quiz or both. As the most important feature is adding the BGL reading, if they choose to go dowbn the quiz opathway first, at the end of the quiz they will have the option of going back to the start and inputting their reading. Apon inouting the BGL reading they will be prompted to input whether they were fastiunbg nor not and then based on the resulst they will inform them whether their sugar is too high or too low and what they can do about it.

**The Target Audience)**

- This Diabates Tracker App is for a person with type 2 diabates, who would like to track and manage thier blood sugar levels and inprove their knowldege for future wellness.
- The usre should be using the finger prick method and BGL reading device to determine the digital reading.

**How the to use Diabates Tracker App**

Will use the executable file to launch tracker from the terminal (see [Installation](#Installation) in this document)
They will then follow the prompts and enter the information accordingly.

## References
Source reference [Here](https://www.diabetesaustralia.com.au/news-resources/useful-links/)

Source reference [Here](https://www.gisymbol.com/low-gi-products/#product-grid+product_cat:fruit-vegetables)

Source reference [Here](https://www.cdc.gov/diabetes/managing/managing-blood-sugar/bloodglucosemonitoring.html)

## App Repository

Click [Here](https://github.com/Willo80/my-terminal-assignment.git) to access repository

## Style Guide

Followed the PEP 8 SG for Python Code, access it [Here](https://peps.python.org/pep-0008/#code-lay-out)
MD032 lists [Here](https://github.com/DavidAnson/markdownlint/blob/v0.26.2/doc/Rules.md#md032)

## Features

**Name input function**
This feature allows allows the user to input their full name, and will return their first name when they are asked what they would like to do today. For error handling here I have used .title() which means it will not be case senstive and have also included .strip() a space remover either side of their name.
The function will create a capital letter for their name regardless of what case they type in. If they only enter their first name the program will prompt them to fill in their full name before they can continue. Here is an except ValueError and is included in a while statement (with a break when both first name and surname is correctly entered)
Although only their first name is returned in this app, making it appropriatly personal), the full name request is for future use, so that their name will be documented together with time/date of inputting their BGL, to share the information with their diabates educator.
![View input/return function](images/)

**Glucose reading input function**
  This function takes a number input (expected as a possible float) from the user and uses it in an if elif statement, (conditionals) together with another user input to determine whether they were fasting or not. Based on their input, the outcome determines whether they have a high or low BGL and expresses what they should do about it. The time and date of the input is also automatically documented/processed.
  This will be a future feature of the app to gather more informtaion regarding glucose times and levels.

**Option to play an education game or record their Blood glucose level**
  The user has an option to play an education multiple choice game or go straight to entering their blood glucose level reading.
  If they choose Yes, they willplay the game and if they choose No they will go down the BGL pathway. 
  As it is still important for them to document their BGL reading, they are given the option at the end of the game to return to the begining and do so.

**Begin quiz function**
Here we have a Question class, which means keeping the code DRY, thus calling functions from this class. Also, for future upgrades of the app more questions can be created/added to the Question class, and the ability to 'append' and 'pop' could come into play here as a question list (mutable) is included here. This would allow for a different question selection each time player plays the educational game.

## Implemenation Plan


Describe here - talk about getting approval , flow chart was key to design etc..as well as .. add screen grab.
Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan. (trello board screen grab in here)
Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 
> Your checklists for each feature should have at least 5 items

## Installation  <!-- Design help documentation which includes a set of instructions which accurately describe how to use and install the application) -->

You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application



<!-- could add some code here as an example using triple back ticks and py at beginning, to make it display must enable.. and say allow insecure content form http, I have notdne that yet. eg: -->
```py
def hello:
    print("hello")
    ```

