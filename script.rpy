# Character definition
define y = Character("You")
define a = Character("Person A")

# HUD display
default boundary_score = 0
default communication_score = 0
default responsibility_score = 0

screen confidence_ui():
    vbox:
        xalign 0.98
        yalign 0.02
        spacing 5

        frame:
            text "Boundary Score: [boundary_score]"

        frame:
            text "Communication Score: [communication_score]"

        frame:
            text "Responsibility Score: [responsibility_score]"

label start:

    show screen confidence_ui

    "Welcome! To continue, please press left click on your mouse while your cursor is on the game."

    "Great! This is a simulated scenario based on Balancing Commitments and Wellbeing."

    "Please note that this is a fictional video game, and there are no real names used."

    "Once you are ready, press left click one more time and the simulated scenario will start!"

    "Balancing Commitments and Wellbeing: Scenario Start"

