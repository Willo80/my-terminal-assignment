
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

describe who for and why  ie diabetes type 2 to manage their condition and conmtrol BGL and to edu themsleves..

**What will the tracker be able to do**

exaplin what it does, can have 2 options, game or BGL or both but can have option to record BGL as well.. etc.. and how ends.

**Who for (ie target audience)**

For type 2 diasbtes person etc..

**how can the diabteic person use tracker**

Will use the executable file to launch tracker from the terminal (see [Installation](#Installation) in this document)
They will then follow the prompts and enter the information accordingly.


## References

add all refs here

## App Repository

Click [Here](https://github.com/Willo80/my-terminal-assignment.git) to access repository

## Style Guide

Followed the PEP 8 SG for Python Code, access it [Here](https://peps.python.org/pep-0008/#code-lay-out)

pep -8? check this

## Features

1. **Name input function**  

   This feature allows allows the user to input their full name, and will return their first name when they are asked what they would like to do today.
   The function will create a capital letter for their name regardless of what case they type in. If they only enter theor first name the program will prompt them to fill in their full name before they can continue.
   Although only their first name is returned in this app, making it appropriatly personal), the full name request is for future use, so that their name will be documented together with time/date of inputting their BGL, to share the information with their diabates educator.

  ![View input/return function](images/)

2. **Glucose reading function**

  This function takes a number input (expected as a possible float) from the user and uses it in an if elif statement, together with another user input to determine whether they were fasting or not. Based on their input, the outcome determines whether they have a high or low BGL and expresses what they should do about it. The time and date of the input is also automatically documented/processed.
  This will be a future feature of the app to gather more informtaion regarding glucose times and levels.

3. **Option to play an education game or record their Blood glucose level**



  

4. **Game function**
  
  <!-- - at least THREE features
<!-- - describe each feature --> 


<!-- - use of variables and the concept of variable scope
- loops and conditional control structures
- error handling -->

  Add descriotion heading of feature 1 here and bold this eg. Single-player Mode generates a Random word

  describe the feature 1 

  Title for feature 2

  describe feature 2

  Title for feature 3

  descibe feature 3

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

