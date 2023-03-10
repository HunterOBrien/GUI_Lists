import easygui
daysGoal = easygui.integerbox("How many days is your goal for being tech free")
daysFree = easygui.enterbox("What Days have you been tech free, (Please include a space between each day)")
techDaysFree = list(daysFree.split())
daysReached = len(techDaysFree)

if daysGoal > daysReached:
    easygui.msgbox(f"Unfortunate! You did not meet your goal of {daysGoal} days without tech, you reached {daysReached}"
                   f"day/s!")
else:
    easygui.msgbox(f"Congratulations! You met your goal of {daysGoal} days without tech "
                   f"with {daysReached} days reached")
    