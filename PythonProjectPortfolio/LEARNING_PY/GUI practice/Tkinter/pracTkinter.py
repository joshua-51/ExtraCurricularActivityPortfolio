from tkinter import * #THIS BASICALLY IMPORTS EVERYTHING RELATED TO TKINTER
from PIL import ImageTk
#LABEL - AN AREA.WIDGET THAT HOLDS TEXT AND/OR IMAGE WITHIN A WINDOW

window = Tk() #MAKE A WINDOW
window.title("Joshua first GUI") #NAMING THE WINDOW
#window.geometry("300x300") #SETTING THE SIZE OF YOUR WINDOW
'''
icon = PhotoImag(file='logo.png')
window.iconphoto(True, icon)
#ONLY WORKS ON WINDOWS
window.iconphoto(True, icon)
'''

photo = ImageTk.PhotoImage(file='/Users/3041067/Desktop/CODE/Python/tkinterPractice/logo.png')  #Use the ImageTk from Pillow to make this wokr

#HOW TO MAKE A LABEL
'''
label = Label(window,
              text="This is very,very cool",#This is the text that you are displaying
              font=('Arial',40,'bold'),#This is the font
              fg='#00f2ff',#This is the text color
              bg='#1d3233',#This is the background of the text color
              relief=RAISED, #This adds a border around the label
              #relief-SUNKEN, #This changes the border to appear more sunken
              bd=10, #This increases the border thickness
              padx=20, #This will add space between the text and the surrounding
              pady=20, #This will add space between the text and the surrounding
              image=photo, #This will add a picture, however the image will be on top of the text
              compound='bottom') #This will change the image to be on the bottom, if we put top it would be on the top

label.place(x=0,y=0) #Chooses where to place the label
'''



#SETTING BACKGROUND COLOR
'''
window.config(background="#000000") #SETTING THE BACKGROUND COLOR
'''

#HOW TO MAKE A BUTTON

'''
count =0
def click():
    global count
    count+=1
    print("You clicked the button", count, "times")

button = Button(window,
                text="Click me!",
                command=click,
                font=('Comic Sans', 30),
                fg="#00FF00",
                bg="#000000",
                activeforeground="#00FF00",
                activebackground='#000000',
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()
'''

#HOW TO MAKE AN ENTRY WIDGET


def submit():
    username = entry.get()
    print("Hello " + username)

def delete():
    entry.delete(0,END)

entry = Entry(window,
              font=("Arial",50))
entry.pack(side=LEFT)

submit_button = Button(window,text="submit", command=submit)


delete_button = Button(window,text="delete", command=delete)

window.mainloop()