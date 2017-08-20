import random
from tkinter import *
from tkinter import ttk

size = 500

def readFile(inFile):
	questions = []
	answers   = []
	comments  = []
	tags      = []

	with open(inFile, 'r', encoding='utf-8') as inFile:
		lines = inFile.readlines()
		random.shuffle(lines)
	for line in lines:
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
	# Read up the data to be studied
	(questions, answers, comments, tags) = readFile("csv/Kanji.csv")

	# Initalisation
	index = 0
	root = Tk()
	root.title("Flash Cards")
	root.geometry('{}x{}'.format(size, size))

	# Setting up the lists of answered cards
	wrongs   = []
	mixeds   = []
	repeats  = []
	corrects = []

	# Setting up the text variables which will be displayed on the cards
	q = StringVar()
	a = StringVar()
	c = StringVar()
	t = StringVar()
	q.set(questions[index])
	a.set(answers[index])
	c.set(comments[index])
	t.set(tags[index])

	qFrame = ttk.Frame(root, height=size*0.4, width=size)
	aFrame = ttk.Frame(root, height=size*0.6, width=size)

	def txtPrt(sVar):
		return sVar.get()

	def showAnswers():
		"""Makes the answer frame appear"""
		aFrame.grid()

	def showComment():
		"""Makes the comment frame appear"""
		comment.grid()

	def wrongAns():
		"""Appends the card to wrong list, and moves to the next card"""
		nonlocal wrongs
		wrongs.append((txtPrt(q), txtPrt(a), txtPrt(c), txtPrt(t)))
		nextQuestion()
		
	def mixedAns():
		"""Appends the card to mixed list, and moves to the next card"""
		nonlocal mixeds
		mixeds.append((txtPrt(q), txtPrt(a), txtPrt(c), txtPrt(t)))
		nextQuestion()

	def repeatCard():
		"""Appends the card to repeat list, and moves to the next card"""
		nonlocal repeats
		repeats.append((txtPrt(q), txtPrt(a), txtPrt(c), txtPrt(t)))
		nextQuestion()

	def correctAns():
		"""Appends the card to correct list, and moves to the next card"""
		nonlocal corrects
		corrects.append((txtPrt(q), txtPrt(a), txtPrt(c), txtPrt(t)))
		nextQuestion()

	def nextQuestion():
		"""Displays the question from the next card"""
		nonlocal index
		index = index + 1
		q.set(questions[index])
		a.set(answers[index])
		c.set(comments[index])
		t.set(tags[index])
		aFrame.grid_remove()
		comment.grid_remove()

	def csvWrite(name, ansList):
		with open("csv/{}".format(name), 'w', encoding='utf-8') as outFile:
			for line in ansList:
				ansLine = ",".join(line)
				outFile.write(ansLine)

	question = ttk.Label(qFrame, textvariable=q, anchor="center", font=("Meiryo", "108"))
	answer   = ttk.Label(aFrame, textvariable=a, anchor="center", font=("Meiryo", "72"))
	comment  = ttk.Label(aFrame, textvariable=c, anchor="center", font=("Meiryo", "72"))
	wrong    = ttk.Button(aFrame, text="Wrong", command=wrongAns)
	confused = ttk.Button(aFrame, text="Mixup", command=mixedAns)
	again    = ttk.Button(aFrame, text="Ask again", command=repeatCard)
	correct  = ttk.Button(aFrame, text="Correct", command=correctAns)

	# The long process of sorting out the geometry manager
	qFrame.grid(row=0, column=0)
	qFrame.grid_propagate(0)

	question.grid(row=0, column=0)
	qFrame.columnconfigure(0, weight=1)
	qFrame.rowconfigure(0, weight=1)

	aFrame.grid(row=1, column=0)
	aFrame.grid_propagate(0)

	answer.grid(row=0, column=0, columnspan=4)
	comment.grid(row=1, column=0, columnspan=4)
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
	comment.grid_remove()

	qFrame.bind('<1>', lambda e: showAnswers())
	question.bind('<1>', lambda e: showAnswers())
	aFrame.bind('<1>', lambda e: showComment())

	# Creating File Menu
	menu = Menu(root)
	root.config(menu=menu)

	fileMenu = Menu(menu)
	menu.add_cascade(label="File", menu=fileMenu)
	# Undo calls the clear function on the most recently played square.
	fileMenu.add_command(label="Index", command=lambda: print(index))
	fileMenu.add_command(label="Wrongs", command=lambda: csvWrite("wrongCards.csv",wrongs))
	fileMenu.add_command(label="Mixeds", command=lambda: csvWrite("mixedCards.csv",mixeds))
	fileMenu.add_command(label="Repeats", command=lambda: csvWrite("repeatCards.csv",repeats))
	fileMenu.add_command(label="Corrects", command=lambda: csvWrite("correctCards.csv",corrects))

	root.mainloop()

if __name__ == '__main__':
	main()
