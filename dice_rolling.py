import tkinter
from PIL import Image, ImageTk#pip install Pillow
import random


root = tkinter.Tk()
root.geometry('800x800')
root.title('Roll the Dice')


l0 = tkinter.Label(root, text= "  Welcome  " )
l0.pack()


l1 = tkinter.Label(root, text="Hey there!", fg = "black",
        bg = "pink",
        font = "bold")
l1.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1 = tkinter.Label(root, image=image1)
label1.image = image1


label1.pack( expand=True)


def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    label1.configure(image=image1)
#reference
    label1.image = image1



button = tkinter.Button(root, text='Roll the Dice', fg='pink' , bg='black', command=rolling_dice  , )

button.pack( expand=True)


root.mainloop()