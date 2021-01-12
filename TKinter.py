from tkinter import *

def click():
    counter.set(counter.get() + 1)

def down():
    counter.set(counter.get() - 1)



if __name__ == '__main__':

    window = Tk()
    window.title('Python_Program')
    counter = IntVar()
    counter.set(0)

    label = Label(window, textvariable = counter)
    label.pack()

    button = Button(window, text='Count Up!', command=click)
    button.pack()

    but1 = Button(window, text='Count Down!', command=down)
    but1.pack()


    window.mainloop()