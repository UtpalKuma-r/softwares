#imports
import tkinter  
import random


root = tkinter.Tk()


root.title("Password Generator")
root.geometry("350x270")


sugelem = []
spc = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '|', '/', '?']

#function to check the password
def passLeng():
    if leng.get() == '' or not(leng.get().strip().isdigit()):
        display.config(text = "Error.........\nLength of password not defined or wrong input.\nPlease check your entry.")
    else:
        generatePassword()

#function to generate the password
def generatePassword():

    if char.get()==1:
        for i in range(65,91):
            a_ = chr(i)
            sugelem.append(a_)

    if num.get() == 1:
        sugelem.extend("1234567890")

    if spechr.get() == 1:
        sugelem.extend(spc)

    
    if len(sugelem) == 0:
        display.config(text = "Password cannot be generated..............\nNo element selected")
        

    else:
        password = ''

        a = int(leng.get())
        while a>0:
            ta = random.choice(sugelem)
            password = password + ta
            a -= 1 
        display.config(text = password)
        sugelem.clear()


#declaration line
tkinter.Label(root, text = "This application will help you generate a password").pack(padx =5 , pady =5 )


#inputs
char,num,spechr = tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()
tkinter.Label(root, text = "Enter the required length").pack(padx =10 , pady =0 )
leng = tkinter.Entry(root)
leng.pack(padx =10 , pady =5 )
tkinter.Checkbutton(root, text = "Character", variable = char ,onvalue = 1, offvalue = 0).pack(padx =0 , pady =0 )
tkinter.Checkbutton(root, text = "Number",variable = num, onvalue = 1, offvalue = 0).pack(padx =5 , pady =5 )
tkinter.Checkbutton(root, text = "Special Character",variable = spechr, onvalue = 1, offvalue = 0).pack(padx =10 , pady =0 )


tkinter.Button(root, text = "submit", command = passLeng).pack(padx =20 , pady =5 ) #button to submit the data

#lable to display output
display = tkinter.Label(root, text = '', width = 400) 
display.pack(padx =25 , pady =5 )



root.mainloop()
