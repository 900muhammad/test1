import tkinter as tk
root = tk.Tk()
root.title('BANANA INTEREST SURVEY')
root.geometry('640x480+300+300')
title = tk.Label(root,text='Please take a survey',font=('Arial 16 bold'),bg='brown',fg='#FF0')
name_label = tk.Label(root,text='WHAT IS YOUR NAME?')
name_inp = tk.Entry(root)
eater_inp = tk.Checkbutton(root,text='check this button if you eat bananas')
num_label = tk.Label(root,text='How many bananas do you eat?')
num_inp = tk.Spinbox(root,from_=0,to=1000,increment=1)
color_label = tk.Label(root,text='What is the best color for banana?')
color_inp = tk.Listbox(root,height=1)
color_choices = ('Any','Green','Yellow','Green-Yellow','Black')
for choice in color_choices:
    color_inp.insert(tk.END,choice)
plantain_label = tk.Label(root,text='Do you eat bananas?')
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame,text='Yes')
plantain_no_inp  = tk.Radiobutton(plantain_frame,text='No')
banana_haiku_label = tk.Label(root,text='write a poem on bananas')
banana_haiku_inp = tk.Text(root,height=3)
submit_btn = tk.Button(root,text='Submit Survey')
output_line = tk.Label(root,text='',anchor='w',justify='left')
title.grid(columnspan=2)
name_label.grid(row=3, sticky=tk.W)
name_inp.grid(row=3, sticky=(tk.W + tk.E))
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)
plantain_yes_inp.pack(side='left',fill='x',ipadx=10,ipady=5)
root.mainloop()



 


