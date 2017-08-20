from tkinter import *
from tkinter import ttk

size = 500

root = Tk()
root.title("Flash Cards")
root.geometry('{}x{}'.format(size, size))

qFrame = ttk.Frame(root, height=size*0.4, width=size)
aFrame = ttk.Frame(root, height=size*0.6, width=size)


question = ttk.Label(qFrame, text="質問", anchor="center", font=("Meiryo", "108"))
answer   = ttk.Label(aFrame, text="答え", anchor="center", font=("Meiryo", "72"))
blank    = ttk.Label(aFrame, text="", background='#000')
wrong    = ttk.Button(aFrame, text="Wrong")
confused = ttk.Button(aFrame, text="Mixup")
again    = ttk.Button(aFrame, text="Ask again")
correct  = ttk.Button(aFrame, text="Correct")

qFrame.grid(row=0, column=0)
qFrame.grid_propagate(0)

question.grid(row=0, column=0)
qFrame.columnconfigure(0, weight=1)
qFrame.rowconfigure(0, weight=1)

aFrame.grid(row=1, column=0)
aFrame.grid_propagate(0)

answer.grid(row=0, column=0, columnspan=4)
blank.grid(row=1, column=0, columnspan=4)
wrong.grid(row=2, column=0)
confused.grid(row=2, column=1)
again.grid(row=2, column=2)
correct.grid(row=2, column=3)

aFrame.columnconfigure(0, weight=1)
aFrame.columnconfigure(1, weight=1)
aFrame.columnconfigure(2, weight=1)
aFrame.columnconfigure(3, weight=1)
aFrame.rowconfigure(0, weight=1)
aFrame.rowconfigure(1, weight=1)
aFrame.rowconfigure(2, weight=1)

aFrame.grid_remove()

def showAnswers():
	aFrame.grid()

qFrame.bind('<1>', lambda e: showAnswers())
question.bind('<1>', lambda e: showAnswers())
root.mainloop()
