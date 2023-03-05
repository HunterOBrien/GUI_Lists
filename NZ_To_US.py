import easygui

nzWord = easygui.enterbox("What is your word with NZ spelling?")
letters = list(nzWord)
letters.remove("u")
easygui.msgbox(f"The American spelling of that word is: {''.join(letters)}", "result")





