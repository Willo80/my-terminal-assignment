
# Diabetes Diary Tracker :drop_of_blood:

---

## Table of Contents

- [References](#references)
- [App Repository](#app-repository)
- [Style Guide](#style-guide)
- [Features](#features)
- [Implemention Plan](#implemenation-plan)
- [Help and Installation](#help-and-installation)

## Related Documents

- [SLIDE DECK VIDEO - Development Walkthrough](https://vimeo.com/763209952/191aaef127)

## Software Development Plan

### Purpose and Scope

The diabates tracker app is designed for a person with type 2 diabtetes, who would like to manage their diabetes by being able to track and document their blood glucose levels throughout the day. They can also improve their knowlegde and wellness by opting to do the multiple choice quiz which will help them identify good eating habits. They will receive a percentage of how well scored. The app so much potential for future updates, to create a more robust app with more educational questions and many other featurees that would be benefical to a person with diabetes.

### What the Diabates Tracker App be able to do

The user has the option of just enetering their blood glucose level or doing the multiple choice quiz or both. As the most important feature is adding the BGL reading, if they choose to go dowbn the quiz opathway first, at the end of the quiz they will have the option of going back to the start and inputting their reading. Apon inouting the BGL reading they will be prompted to input whether they were fastiunbg nor not and then based on the resulst they will inform them whether their sugar is too high or too low and what they can do about it.

### The Target Audience

- This Diabates Tracker App is for a person with type 2 diabates, who would like to track and manage thier blood sugar levels and inprove their knowldege for future wellness.
- The usre should be using the finger prick method and BGL reading device to determine the digital reading.

### How the to use Diabates Tracker App

Will use the executable file to launch tracker from the terminal (see [Installation](#Help/Install Documentation) in this document)
They will then follow the prompts and enter the information accordingly.

## References

Source reference [Here](https://www.diabetesaustralia.com.au/news-resources/useful-links/)

Source reference [Here](https://www.gisymbol.com/low-gi-products/#product-grid+product_cat:fruit-vegetables)

Source reference [Here](https://www.cdc.gov/diabetes/managing/managing-blood-sugar/bloodglucosemonitoring.html)

Python Package Index - PyPI. (Van Kemenade, 2022). Python Software Foundation. Retrieved from [Here](https://pypi.org/project/termcolor/)

## App Repository

Click [Here](https://github.com/Willo80/my-terminal-assignment.git) to access repository

## Style Guide

Followed the PEP 8 SG for Python Code, access it [Here](https://peps.python.org/pep-0008/#code-lay-out)
MD032 lists [Here](https://github.com/DavidAnson/markdownlint/blob/v0.26.2/doc/Rules.md#md032)

## Features

### **Name input**  

This feature allows the user to input their full name, and will return their first name when they are asked what they would like to do today. For error handling here I have used .title() which means it will not be case sensitive and have also included .strip() a space remover either side of their name.
The program will create a capital letter for their name regardless of what case they type in. If they only enter their first name the program will prompt them to fill in their full name before they can continue. This has an except ValueError and is contained in a while loop (with a break when both first name and surname is correctly entered)
Although only their first name is returned in this app, making it appropriatly personal), the full name request is for future use, so that their name will be documented together with time/date of inputting their BGL, to share the information with their diabetes educator.

### **Glucose reading input**

This function takes a number input (expected as a possible float) from the user and uses it in an if elif statement, (conditionals) together with another user input to determine whether they were fasting or not. Based on their input, the outcome determines whether they have a high or low BGL and expresses what they should do about it. There is an exception error handing condition here that will ensure that only a number is accepted. It can be a whole number or a float. The BGL reading are usually floats which is the reason I have built this to capture that probable instance. The time and date of the input is also automatically documented/processed.
This will be a future feature of the app to gather more information regarding glucose times and levels and perhaps out put as a bar chart using matplotlib (available in Pypi.org)

### **Fasting input**

It is essential to the app that the user inputs whether they have eaten or not as it determines the outcome of their BGL reading. Whether fasting or not fasting contributes to their low or high BGL reading and what the suggestion is to do to control their wellness based on the results.

### **Option to play an education game or record their Blood glucose level**

The user has an option to play an education multiple choice game or go straight to entering their blood glucose level reading.
If they choose Yes, they will play the game and if they choose No they will go down the BGL pathway.
As it is still important for them to document their BGL reading, they are then also given the option at the end of the game to return to the begining input their reading.

### **Begin quiz_Class function**

Here we have a Question class, which means keeping the code DRY, thus calling functions from this class. Also, for future upgrades of the app more questions can be created/added to the Question Class function, and the ability to 'append' and 'pop' could come into play here as a list is mutable. This would allow for a different question selection each time player plays the educational game.
The quiz has a score variable which totals the final amount to determine whether they passed or not. They are given appropriate and immediate feedback based on their result and encouraged to do better. They have an option to start again.

## **Implemenation Plan**

- Approval for app receieved from the a CoderAcademy educator.
- Researched some diabetes websites and the apple iphone app store for some ideas and educational information.
- Set up my Trello board [Access it here](https://trello.com/invite/b/xYGLG3I0/ATTIf5b890746903b998e9fc6efbc5f7f5206CF52825/terminal-app-assignment) and added some content, ie. design flowchart and outcomes.
- Started designing the app flowchart, this changed along the way as some things/features became more obvious, for a logical working flow.
- Began writing the code and this also changed with the flowchart evolving, and particulary when it came to ensuring that the code was DRY.

ADD FLOW CHART SCREEN GRAB HERE and trello board

## Feature tasks/checklist

### [Name Input:](#name-input)

- Input full name
- Call only the first name
- Capitalise name .title()
- Error handling
- Explanation statements

### [Glucose Reading:](#glucose-reading-input)

- Create a float user input
- error handling for number only entry
- if elif condition required
- Fasting input - essential
- Create output statements

### [Option to play or record BGL:](#option-to-play-an-education-game-or-record-their-blood-glucose-level)

- Create an input for Yes or No
- if else required
- Yes must take user straight to quiz
- No must go straight to BGL input
- Create output statements of encouragement

### [Quiz multiple choice:](#quiz-multiple-choice)

- Research appropriate diabetes questions
- multiple chice layout
- Class with list
- immediate feedback after user answers questions
- color code feedback
- create a score variable
- allow user to resart at end of quiz

## [Help and Installation:](#help-and-installation)

You must include

- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application
  