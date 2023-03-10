import easygui

commas = 0
null = 0
while null == 0:
    dreamDestinations = easygui.enterbox("Enter five places you would like to visit separated by a comma",
                                         "Dream Destinations")

    for i in range(len(dreamDestinations)):
        if (dreamDestinations[i]) == ",":
            commas = commas + 1

    if commas == 4:
        null = 1

    else:
        easygui.msgbox(f"Sorry you need five places entered you entered {commas}", "Wrong Number Of Places")

dreamDestinationsList = list(dreamDestinations.split(","))

for place in dreamDestinations:
    output = f"\n*  ".join(dreamDestinationsList)

easygui.msgbox(f"Your bucket list is: \n\n*  {output}", 'Travel Bucket List')
