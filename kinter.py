from tkinter import*
root = Tk()
root.title('MY FIRST KINTER WINDOW')#this is the main window 
Label(root,text='WELCOME TO KINTER').pack(padx=10)
root.configure(background='green')
t1 = Toplevel(root)#this the second window opened along side the root its a child
Label(t1,text='This a child of the main toplevel').pack(pady=10)
t1.configure(background='orange')
t2 = Toplevel(root)
Label(t2,text='this is a transient window of root').pack(padx=10,pady=10)
t2.transient(root)
root.mainloop()