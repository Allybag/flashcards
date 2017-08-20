from tkinter import *
from tkinter import ttk

size = 500

def readFile(inFile):
	questions = []
	answers   = []
	comments  = []
	tags      = []

	with open(inFile, 'r', encoding='utf-8') as inFile:
		for line in inFile:
			if line.count(',') != 3:
				continue
			field1 = line.find(',')
			field2 = line.find(',', field1 + 1)
			field3 = line.find(',', field2 + 1)
			questions.append(line[:field1])
			answers.append(line[field1 + 1:field2])
			comments.append(line[field2 + 1:field3])
			tags.append(line[field3 + 1:])

		return(questions, answers, comments, tags)

def main():
	(questions, answers, comments, tags) = readFile("csv/Kanji.csv")
	index = 0
	root = Tk()
	root.title("Flash Cards")
	root.geometry('{}x{}'.format(size, size))
	q = StringVar()
	a = StringVar()
	q.set(questions[index])
	a.set(answers[index])

	qFrame = ttk.Frame(root, height=size*0.4, width=size)
	aFrame = ttk.Frame(root, height=size*0.6, width=size)

	def showAnswers():
		aFrame.grid()

	def nextQuestion():
		nonlocal index
		index = index + 1
		q.set(questions[index])
		a.set(answers[index])
		aFrame.grid_remove()

	question = ttk.Label(qFrame, textvariable=q, anchor="center", font=("Meiryo", "108"))
	answer   = ttk.Label(aFrame, textvariable=a, anchor="center", font=("Meiryo", "72"))
	blank    = ttk.Label(aFrame, text="", background='#000')
	wrong    = ttk.Button(aFrame, text="Wrong")
	confused = ttk.Button(aFrame, text="Mixup")
	again    = ttk.Button(aFrame, text="Ask again")
	correct  = ttk.Button(aFrame, text="Correct", command=nextQuestion)

	# The long process of sorting out the geometry manager
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

	qFrame.bind('<1>', lambda e: showAnswers())
	question.bind('<1>', lambda e: showAnswers())

	# Creating File Menu
	menu = Menu(root)
	root.config(menu=menu)

	fileMenu = Menu(menu)
	menu.add_cascade(label="File", menu=fileMenu)
	# Undo calls the clear function on the most recently played square.
	fileMenu.add_command(label="State", command=lambda: print(index))

	root.mainloop()

if __name__ == '__main__':
	main()
