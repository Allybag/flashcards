from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Flash Cards")

qFrame = ttk.Frame(root)
aFrame   = ttk.Frame(root)


question = ttk.Label(qFrame, text="Question", anchor="center")
answer   = ttk.Label(aFrame, text="Answer", anchor="center")
wrong    = ttk.Button(aFrame, text="Wrong")
confused = ttk.Button(aFrame, text="Mixup")
again    = ttk.Button(aFrame, text="Ask again")
correct  = ttk.Button(aFrame, text="Correct")

qFrame.pack()

question.grid(row=0, column=0, sticky=(E, W), columnspan=4)
answer.grid(row=1, column=0, sticky=(E, W), columnspan=4)

wrong.grid(row=2, column=0, sticky=(E, W))
confused.grid(row=2, column=1, sticky=(E, W))
again.grid(row=2, column=2, sticky=(E, W))
correct.grid(row=2, column=3, sticky=(E, W))

def showAnswers():
	aFrame.pack()

question.bind('<1>', lambda e: showAnswers())
root.mainloop()
