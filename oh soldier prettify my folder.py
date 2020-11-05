import os
def systemiser(path, file, extension):
    f = open(file)
    content = f.read()
    notToChange = content.split("\n")
    f.close() 
    os.chdir(path)
    a = os.listdir()
    for item in a:
        if os.path.isdir(item):
            pass
        else:
            if item in notToChange:
                pass
            else:
                newName = item.capitalize()
                os.rename(item, newName)
    no = 1
    for item in a:
        if (os.path.splitext(item)[1]) == extension:
            os.rename(item, str(no)+extension)
            no = no+1

path = input("Enter path: ")
filee = input("Enter exception file name: ")
extention = input("Enter extension: ")
systemiser(path, filee, extention)
print("Task completed")