from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Flash Cards")

question = ttk.Label(root, text="Question", anchor="center")
answer   = ttk.Label(root, text="Answer", anchor="center")
wrong    = ttk.Button(root, text="Wrong")
confused = ttk.Button(root, text="Mixup")
again    = ttk.Button(root, text="Ask again")
correct  = ttk.Button(root, text="Correct")

question.grid(row=0, column=0, sticky=(E, W), columnspan=4)
answer.grid(row=1, column=0, sticky=(E, W), columnspan=4)

wrong.grid(row=2, column=0, sticky=(E, W))
confused.grid(row=2, column=1, sticky=(E, W))
again.grid(row=2, column=2, sticky=(E, W))
correct.grid(row=2, column=3, sticky=(E, W))

def showAnswers():
	pass

question.bind('<1>', lambda e: showAnswers())
root.mainloop()
