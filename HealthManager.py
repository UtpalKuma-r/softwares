def getdate():
    import datetime
    return datetime.datetime.now()
time = str(getdate())


def fileCreator():
    name = input("Enter your name: ").lower()
    fileToOpen = input("\nwhat you want to enter\nenter exercise or dite: ").lower()
    if fileToOpen.lower() != "exercise" and fileToOpen.lower() != "dite":
        print("\nyou entered a wrong input\n")
        conTinue()
    Add = input("\ntype your entry:\n")
    toAdd = "["+time+"]"+ Add+"\n"
    f = open(name+fileToOpen+".txt", "a")
    f.write(toAdd)
    f.close()
    print("\n\nyour entry has been saved\n")
    conTinue()


def conTinue():
    print("do you want to input again\nenter y for yes or any other key to exit")
    choice = input()
    if choice.lower() == "y":
        start()
    else:
        print("thank you")


def logOpner():
    name = input("Enter your name: ").lower()
    fileToOpen = input("\nwhich log do you want to open\nenter exercise or dite: ").lower()
    if fileToOpen.lower() != "exercise" and fileToOpen.lower() != "dite":
        print("\nyou entered a wrong input\n")
        conTinue()
    try:
        f = open(name+fileToOpen+".txt")
        content = f.read()
        print(content)
        conTinue()
    except:
        print("no related file found, try making one")
        conTinue()


def start():
    entryOrLog = input("do you want to do entry or see logs: ")
    if entryOrLog.lower() != "entry" and entryOrLog.lower() != "logs":
        print("wrong input")
        conTinue()
    if entryOrLog.lower() == "entry":
        fileCreator()
    elif entryOrLog.lower() == "logs":
        logOpner()
    else:
        print("wrong input")
        conTinue()

start()
