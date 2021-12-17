from tkinter import *
from queue import Queue
from tkinter import messagebox
import sys

# Creates the GUI window
win = Tk()

# Sets the behavior of the window
win.configure(bg = 'gray')
win.geometry('1800x700+50+50')
win.resizable(False, False)
win.overrideredirect(True)		

# Creation of variables

line1Que = Queue(maxsize = 5)
line2Que = Queue(maxsize = 5)
line3Que = Queue(maxsize = 5)
line4Que = Queue(maxsize = 5)
recCom = Queue(maxsize = 5)

# Main function
def main():
	message = messagebox.askquestion("Info", "Would you like to restore to the most recent save?")
	if message == 'yes':
		load1()
		load2()
		load3()
		load4()
		loadCom()
		win.focus_force()
		entry.focus()
	else: 
		win.focus_force()
		entry.focus()

# Function to load previously saved data
def load(fstring, prod, que, queue):
	f = open(fstring, 'r')
	step = 1
	prod.insert(1, f.readline())
	for i in f.readlines():
		if i != '\n': 
			que.put(i)
			queue.insert(step, i)
			step += 1
	f.close()

def load1():
	load("line1Saved.txt", line1Production, line1Que, line1Queue)

def load2():
	load("line2Saved.txt", line2Production, line2Que, line2Queue)

def load3():
	load("line3Saved.txt", line3Production, line3Que, line3Queue)

def load4():
	load("line4Saved.txt", line4Production, line4Que, line4Queue)

def loadCom():
	f = open('recComplete.txt', 'r')
	step = 1
	for i in f.readlines():
		if i != '\n': 
			recCom.put(i)
			completedBox.insert(step, i)
			step += 1
	f.close()

# Functions will go in this section
# Simple function to run an exit command for exit button
def exitProg():
	win.quit
	win.destroy
	sys.exit()	

# Function to update que when line button is pressed
def updateLine(fstring, que, string, queue, prod):
	if entry.get() == "":return
	if que.full() == True:
		error = messagebox.showerror("Error", "Job not added to queue. " + string + " is full")
		entry.delete(0, 'end')
		return
	queue.delete(0, 'end')
	que.put(entry.get())
	entry.delete(0, 'end')
	step = 1
	f = open(fstring, 'w')
	f.write(prod.get(0))
	f.write('\n')
	for i in que.queue:
		queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def updateLine1():
	updateLine("line1Saved.txt", line1Que, 'Line 1', line1Queue, line1Production)

def updateLine2():
	updateLine("line2Saved.txt", line2Que, 'Line 2', line2Queue, line2Production)

def updateLine3():
	updateLine("line3Saved.txt", line3Que, 'Line 3', line3Queue, line3Production)

def updateLine4():
	updateLine("line4Saved.txt", line4Que, 'Line 4', line4Queue, line4Production)

# Function to update que when job complete button is pressed
def jobComplete(fstring, prod, que, queue):
	f = open(fstring, 'w')
	tmp = prod.get(0)
	prod.delete(0, 'end')
	if que.empty() == True:
		info = messagebox.showinfo("Nice!", "Good job!  The queue is done")
		f.write(prod.get(0))
		f.write('\n')
		recentlyCom(tmp)
		return
	recentlyCom(tmp)
	prod.insert(1, que.get(0))
	queue.delete(0, 'end')
	step = 1
	f.write(prod.get(0))
	f.write('\n')
	for i in que.queue:
		queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()
	
def jobComplete1():
	jobComplete("line1Saved.txt", line1Production, line1Que, line1Queue)

def jobComplete2():
	jobComplete("line2Saved.txt", line2Production, line2Que, line2Queue)

def jobComplete3():
	jobComplete("line3Saved.txt", line3Production, line3Que, line3Queue)

def jobComplete4():
	jobComplete("line4Saved.txt", line4Production, line4Que, line4Queue)

# Function to update recently complete que automatically when job complete button is pressed
def recentlyCom(que):
	if que != '\n':
		f = open('recComplete.txt', 'w')
		if que == "": return
		if recCom.full() == True:
				recCom.get()
		recCom.put(que)
		step = 1
		completedBox.delete(0, 'end')
		for i in recCom.queue:
			completedBox.insert(step, i)
			step += 1
			f.write(i)
			f.write('\n')
		f.close()
	
# Buttons, labels, etc.. will go in this section
# Creates the header label and sets the behavior
header = Label(win, text = "Production Queue", bg = 'gray', font = ("Arial", 30))
header.pack()

# Creates the exit and load button and the behavior of the button
exitBtn = Button(win, text = "Exit", width = 10, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = exitProg)
exitBtn.place(x = 1700, y = 650)
# loadBtn = Button(win, text = "Load", width = 10, bg = 'white', 
	#activebackground = 'blue', relief = SUNKEN, command = load)
# loadBtn.place(x = 20, y = 650)

# Creates labels displaying line number
line1Label = Label(win, text = "Line 1 production", bg = 'gray', font = ("Arial", 18))
line1Label.place(x = 200, y = 100)
line2Label = Label(win, text = "Line 2 production", bg = 'gray', font = ("Arial", 18))
line2Label.place(x = 600, y = 100)
line3Label = Label(win, text = "Line 3 production", bg = 'gray', font = ("Arial", 18))
line3Label.place(x = 1000, y = 100)
line4Label = Label(win, text = "Line 4 production", bg = 'gray', font = ("Arial", 18))
line4Label.place(x = 1400, y = 100)

# Creates a complete button for all lines
line1Com = Button(win, text = "Complete Job", width = 12, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = jobComplete1)
line1Com.place(x = 250, y = 180)
line2Com = Button(win, text = "Complete Job", width = 12, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = jobComplete2)
line2Com.place(x = 650, y = 180)
line3Com = Button(win, text = "Complete Job", width = 12, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = jobComplete3)
line3Com.place(x = 1050, y = 180)
line4Com = Button(win, text = "Complete Job", width = 12, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = jobComplete4)
line4Com.place(x = 1450, y = 180)

# Creates lables to display queue
line1LblQue = Label(win, text = "Line 1 queue", bg = 'gray', font = ("Arial", 18))
line1LblQue.place(x = 220, y = 220)
line2LblQue = Label(win, text = "Line 2 queue", bg = 'gray', font = ("Arial", 18))
line2LblQue.place(x = 620, y = 220)
line3LblQue = Label(win, text = "Line 3 queue", bg = 'gray', font = ("Arial", 18))
line3LblQue.place(x = 1020, y = 220)
line4LblQue = Label(win, text = "Line 4 queue", bg = 'gray', font = ("Arial", 18))
line4LblQue.place(x = 1420, y = 220)

# Creates a list box showing current production
line1Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line1Production.place(x = 190, y = 150)
line2Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line2Production.place(x = 590, y = 150)
line3Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line3Production.place(x = 990, y = 150)
line4Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line4Production.place(x = 1390, y = 150)

# Creates a list box showing current queue
line1Queue = Listbox(win, height = 5, width = 35, fg = 'yellow', bg = 'black')
line1Queue.place(x = 190, y = 270)
line2Queue = Listbox(win, height = 5, width = 35, fg = 'yellow', bg = 'black')
line2Queue.place(x = 590, y = 270)
line3Queue = Listbox(win, height = 5, width = 35, fg = 'yellow', bg = 'black')
line3Queue.place(x = 990, y = 270)
line4Queue = Listbox(win, height = 5, width = 35, fg = 'yellow', bg = 'black')
line4Queue.place(x = 1390, y = 270)

# Creates recently completed label and list box
completed = Label(win, text = "Recently Completed", bg = 'gray', font = ("Arial", 18))
completed.place(x = 1000, y = 400)
completedBox = Listbox(win, height = 5, width = 35, fg = 'green', bg = 'black')
completedBox.place(x = 1000, y = 450)

# Creates add que entry box and buttons
entryLbl = Label(win, text = "Add to queue", bg = 'gray', font = ("Arial", 18))
entryLbl.place(x = 600, y = 400)
entry = Entry(win, bd = 5)
entry.place(x = 600, y = 450)
line1Btn = Button(win, text = "Line 1", width = 5, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = updateLine1)
line1Btn.place(x = 600, y = 500)
line2Btn = Button(win, text = "Line 2", width = 5, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = updateLine2)
line2Btn.place(x = 650, y = 500)
line3Btn = Button(win, text = "Line 3", width = 5, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = updateLine3)
line3Btn.place(x = 600, y = 550)
line4Btn = Button(win, text = "Line 4", width = 5, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = updateLine4)
line4Btn.place(x = 650, y = 550)

if __name__=="__main__":
	main()

win.mainloop()

# Notes
# Make executable with pyinstaller --onefile productionQueue.py --exclude-module _bootlocale