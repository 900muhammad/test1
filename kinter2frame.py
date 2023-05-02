from tkinter import*
root = Tk()
root.title('GUI WITH TKINTER')
root.configure(background='black')
root.geometry('300x300+50+50')
text = Label(root,text='THIS IS A black BACKGROUND')
text.pack()
text2 = Label(root,text='Mango Park')
text2.pack()
root.mainloop()

