import easygui
import random


def roll():
    return random.randint(1, 6)


def scoring(pnum, proll):
    occurrences = 0
    total_score = 0
    for i in range(6):
        occurrences = proll.count(i)
        if occurrences > 2:
            num = i
            break

    if occurrences < 3:
        easygui.msgbox("You got no points that round, unlucky!", f"Player {pnum}")
        return 0

    else:
        if occurrences == 3:
            round_score = 10
            easygui.msgbox(f"{proll}\n you got three of a kind so score for that round is {round_score}",
                           f"Player {pnum}")
            return 10
        elif occurrences == 4:
            round_score = 30
            easygui.msgbox(f"{proll}\n you got a four of a kind so score for that round is {round_score}",
                           f"Player {pnum}")
            return 30
        elif occurrences == 5:
            round_score = 50
            easygui.msgbox(f"{proll}\n you got a five of a kind so score for that round is {round_score}",
                           f"Player {pnum}")
            return 50


def re_roll_dice(pnum, proll):
    roll_again = easygui.ynbox(f"Player {pnum} rolled {proll}\n\n Choose", "Do You Want To Roll Again?",
                               choices=("Roll again", "Stick"))

    if roll_again == 0:
        return proll

    else:
        roll_dice = easygui.multchoicebox("Enter the dices you want to re-roll", "re-roll",
                                          choices=("Dice one", "Dice two", "Dice three",
                                                   "Dice four", "Dice five"))

        if "Dice one" in roll_dice:
            proll.pop(0)
            proll.insert(0, roll())
        if "Dice two" in roll_dice:
            proll.pop(1)
            proll.insert(1, roll())
        if "Dice three" in roll_dice:
            proll.pop(2)
            proll.insert(2, roll())
        if "Dice four" in roll_dice:
            proll.pop(3)
            proll.insert(3, roll())
        if "Dice five" in roll_dice:
            proll.pop(4)
            proll.insert(4, roll())
        return proll



def yahtzee():

    p1 = easygui.enterbox("Enter the name of the first player", "Player One Name")
    p2 = easygui.enterbox("Enter the name of the second player", "Player Two Name")

    dice_p1 = []
    dice_p2 = []

    for i in range(5):
        dice_p1.append(roll())
        dice_p2.append(roll())

    dice_p1 = re_roll_dice("1", dice_p1)
    dice_p1 = re_roll_dice("1", dice_p1)
    dice_p2 = re_roll_dice("2", dice_p2)
    dice_p2 = re_roll_dice("2", dice_p2)

    p1score = scoring("1", dice_p1)
    p2score = scoring("2", dice_p2)
    if p1score > p2score:
        winner = p1score
        loser = p2score
        ans = easygui.msgbox(
            f"The winner of the game was {p2} with a score of {p2score}\n {p1} had a score of {p1score}\n "
            "Game Results")
    elif p2score > p1score:
        winner = p2score
        loser = p1score
        ans = easygui.msgbox(
            f"The winner of the game was {p1} with a score of {p1score}\n {p2} had a score of {p2score}\n "
            "Game Results")

    else:
        ans = easygui.ynbox(
            f"The game was a draw\n the score for both players was {p1score}\n Do you want to play another game?",
            "Game Results")
        if ans:
            print()
        else:
            quit()


yahtzee()