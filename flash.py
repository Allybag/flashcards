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
		with open("csv/randomCards.csv", 'w', encoding='utf-8') as outFile:
			outFile.writelines(lines)
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
	root = Tk()
	root.title("Flash Cards")
	root.geometry('{}x{}'.format(size, size))

	# Setting up the lists of answered cards
	wrongs   = []
	mixeds   = []
	corrects = []

	# ansList is a record of which buttons were pressed
	# len(ansList) is the index of how many cards we've dealt with
	ansList  = []

	# Setting up the text variables which will be displayed on the cards
	q = StringVar()
	a = StringVar()
	c = StringVar()
	t = StringVar()
	q.set(questions[len(ansList)])
	a.set(answers[len(ansList)])
	c.set(comments[len(ansList)])
	t.set(tags[len(ansList)])

	qFrame = ttk.Frame(root, height=size*0.4, width=size)
	aFrame = ttk.Frame(root, height=size*0.6, width=size)

	def showAnswers():
		"""Makes the answer frame appear"""
		aFrame.grid()

	def showComment():
		"""Makes the comment frame appear"""
		comment.grid()

	def wrongAns():
		"""Appends the card to wrong list, and moves to the next card"""
		wrongs.append((q.get(), a.get(), c.get(), t.get()))
		ansList.append("wrong")
		nextQuestion()

	def mixedAns():
		"""Appends the card to mixed list, and moves to the next card"""
		mixeds.append((q.get(), a.get(), c.get(), t.get()))
		ansList.append("mixed")
		nextQuestion()

	def correctAns():
		"""Appends the card to correct list, and moves to the next card"""
		corrects.append((q.get(), a.get(), c.get(), t.get()))
		ansList.append("correct")
		nextQuestion()

	def nextQuestion():
		"""Displays the question from the next card"""
		q.set(questions[len(ansList)])
		a.set(answers[len(ansList)])
		c.set(comments[len(ansList)])
		t.set(tags[len(ansList)])
		aFrame.grid_remove()
		comment.grid_remove()

	def undo():
		"""Displays the question from the previous card"""
		if len(ansList) == 0:
			return

		# Dictionary mapping strings to lists
		switcher = {"wrong":wrongs, "mixed": mixeds, "correct":corrects}
		# Removes the last record in ansList, and removes that's last record
		switcher.get(ansList.pop()).pop()

		q.set(questions[len(ansList)])
		a.set(answers[len(ansList)])
		c.set(comments[len(ansList)])
		t.set(tags[len(ansList)])
		aFrame.grid_remove()
		comment.grid_remove()

	def csvWrite(name, cardList):
		with open("csv/{}".format(name), 'w', encoding='utf-8') as outFile:
			for line in cardList:
				cardLine = ",".join(line)
				outFile.write(cardLine)

	def remWrite():
		with open("csv/remainingCards.csv", 'w', encoding='utf-8') as outFile:
			with open("csv/randomCards.csv", 'r', encoding='utf-8') as inFile:
				lines = inFile.readlines()
				index = 0
				for line in lines:
					if index < len(ansList):
						index = index + 1
						continue
					outFile.write(line)

	question = ttk.Label(qFrame, textvariable=q, anchor="center", font=("Meiryo", "108"))
	answer   = ttk.Label(aFrame, textvariable=a, anchor="center", font=("Meiryo", "72"))
	comment  = ttk.Label(aFrame, textvariable=c, anchor="center", font=("Meiryo", "72"))
	wrong    = ttk.Button(aFrame, text="Wrong", command=wrongAns, width=100)
	confused = ttk.Button(aFrame, text="Mixup", command=mixedAns, width=100)
	correct  = ttk.Button(aFrame, text="Correct", command=correctAns, width=100)

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
	correct.grid(row=2, column=2)

	aFrame.columnconfigure(0, weight=1)
	aFrame.columnconfigure(1, weight=1)
	aFrame.columnconfigure(2, weight=1)
	aFrame.rowconfigure(0, weight=1)
	aFrame.rowconfigure(1, weight=1)
	aFrame.rowconfigure(2, weight=1)

	aFrame.grid_remove()
	comment.grid_remove()

	qFrame.bind('<1>', lambda e: showAnswers())
	question.bind('<1>', lambda e: showAnswers())
	aFrame.bind('<1>', lambda e: showComment())
	root.bind('<Return>', lambda e: correctAns())
	root.bind('<space>', lambda e: showAnswers())
	root.bind('<BackSpace>', lambda e: undo())
	root.bind('<Escape>', lambda e: wrongAns())
	root.bind('<Tab>', lambda e: mixedAns())

	# Creating File Menu
	menu = Menu(root)
	root.config(menu=menu)

	fileMenu = Menu(menu)
	menu.add_cascade(label="File", menu=fileMenu)
	# Undo only works properly once
	fileMenu.add_command(label="Undo", command=lambda: undo())
	fileMenu.add_command(label="Wrongs", command=lambda: csvWrite("wrongCards.csv",wrongs))
	fileMenu.add_command(label="Mixeds", command=lambda: csvWrite("mixedCards.csv",mixeds))
	fileMenu.add_command(label="Corrects", command=lambda: csvWrite("correctCards.csv",corrects))
	fileMenu.add_command(label="Remaining", command=lambda: remWrite())

	root.mainloop()

if __name__ == '__main__':
	main()
