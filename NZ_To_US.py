import easygui
import PIL

image = "C:\\Users\\obrie\\Downloads\\Ethan Gamer.png"
image1 = "C:\\Users\\obrie\\Downloads\\Michael Rosen.jpg"
incorrectList = ["our", "ise", "yse"]
correction1 = "or"
correction2 = "ize"
correction3 = "yze"

def nz_to_us():
    nzWord = easygui.enterbox("What is your word with NZ spelling to turn in US spelling?",
                              "Spelling Converter NZ to US", image=image1, )
    us_word = nzWord
    nzWordList = list(nzWord)

    if "our" in nzWord or "ise" in nzWord or "yse" in nzWord:
        us_word = nzWord.replace("our", correction1)
        us_word = us_word.replace("ise", correction2)
        us_word = us_word.replace("yse", correction3)

    else:
        easygui.msgbox("There is no change in spelling")
        return
    easygui.msgbox(f"You word is now {us_word}")


while True:
    yorn = easygui.ynbox("Do you want to translate a sentence", "Translator", choices=("Yes", "No"))

    if yorn == 1:
        nz_to_us()

    else:
        quit(easygui.msgbox("Too Bad", image=image))
