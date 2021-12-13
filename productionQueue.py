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

# Functions will go in this section
# Simple function to run an exit command for exit button
def exitProg():
	win.quit
	win.destroy
	sys.exit()

def load():
	f = open('line1Saved.txt', 'r')
	step = 1
	line1Production.insert(1, f.readline())
	for i in f.readlines():
		if i != '\n': 
			line1Que.put(i)
			line1Queue.insert(step, i)
			step += 1
	f.close()

	f = open('line2Saved.txt', 'r')
	step = 1
	line2Production.insert(1, f.readline())
	for i in f.readlines():
		if i != '\n': 
			line2Que.put(i)
			line2Queue.insert(step, i)
			step += 1
	f.close()

	f = open('line3Saved.txt', 'r')
	step = 1
	line3Production.insert(1, f.readline())
	for i in f.readlines():
		if i != '\n': 
			line3Que.put(i)
			line3Queue.insert(step, i)
			step += 1
	f.close()

	f = open('line4Saved.txt', 'r')
	step = 1
	line4Production.insert(1, f.readline())
	for i in f.readlines():
		if i != '\n': 
			line4Que.put(i)
			line4Queue.insert(step, i)
			step += 1
	f.close()

	f = open('recComplete.txt', 'r')
	step = 1
	for i in f.readlines():
		if i != '\n': 
			recCom.put(i)
			completedBox.insert(step, i)
			step += 1
	f.close()	

def updateLine1():
	f = open('line1Saved.txt', 'w')
	if entry.get() == "":return
	if line1Que.full() == True:
		error = messagebox.showerror("Error", "Job not added to queue.  Line 1 is full")
		entry.delete(0, 'end')
		return
	line1Queue.delete(0, 'end')
	line1Que.put(entry.get())
	entry.delete(0, 'end')
	step = 1
	f.write(line1Production.get(0))
	f.write('\n')
	for i in line1Que.queue:
		line1Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def updateLine2():
	f = open('line2Saved.txt', 'w')
	if entry.get() == "":return
	if line2Que.full() == True:
		error = messagebox.showerror("Error", "Job not added to queue.  Line 2 is full")
		entry.delete(0, 'end')
		return
	line2Queue.delete(0, 'end')
	line2Que.put(entry.get())
	entry.delete(0, 'end')
	step = 1
	f.write(line2Production.get(0))
	f.write('\n')
	for i in line2Que.queue:
		line2Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def updateLine3():
	f = open('line3Saved.txt', 'w')
	if entry.get() == "":return
	if line3Que.full() == True:
		error = messagebox.showerror("Error", "Job not added to queue.  Line 3 is full")
		entry.delete(0, 'end')
		return
	line3Queue.delete(0, 'end')
	line3Que.put(entry.get())
	entry.delete(0, 'end')
	step = 1
	f.write(line3Production.get(0))
	f.write('\n')
	for i in line3Que.queue:
		line3Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def updateLine4():
	f = open('line4Saved.txt', 'w')
	if entry.get() == "":return
	if line4Que.full() == True:
		error = messagebox.showerror("Error", "Job not added to queue.  Line 4 is full")
		entry.delete(0, 'end')
		return
	line4Queue.delete(0, 'end')
	line4Que.put(entry.get())
	entry.delete(0, 'end')
	step = 1
	f.write(line4Production.get(0))
	f.write('\n')
	for i in line4Que.queue:
		line4Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def jobComplete1():
	f = open('line1Saved.txt', 'w')
	tmp = line1Production.get(0)
	line1Production.delete(0, 'end')
	if line1Que.empty() == True:
		error = messagebox.showinfo("Nice!", "Good job!  The queue is done")
		f.write(line1Production.get(0))
		f.write('\n')
	recentlyCom(tmp)
	line1Production.insert(1, line1Que.get(0))
	line1Queue.delete(0, 'end')
	step = 1
	f.write(line1Production.get(0))
	f.write('\n')
	for i in line1Que.queue:
		line1Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def jobComplete2():
	f = open('line2Saved.txt', 'w')
	tmp = line2Production.get(0)
	line2Production.delete(0, 'end')
	if line2Que.empty() == True:
		error = messagebox.showinfo("Nice!", "Good job!  The queue is done")
		f.write(line2Production.get(0))
		f.write('\n')
	recentlyCom(tmp)
	line2Production.insert(1, line2Que.get(0))
	line2Queue.delete(0, 'end')
	step = 1
	f.write(line2Production.get(0))
	f.write('\n')
	for i in line2Que.queue:
		line2Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def jobComplete3():
	f = open('line3Saved.txt', 'w')
	tmp = line3Production.get(0)
	line3Production.delete(0, 'end')
	if line3Que.empty() == True:
		error = messagebox.showinfo("Nice!", "Good job!  The queue is done")
		f.write(line3Production.get(0))
		f.write('\n')
	recentlyCom(tmp)
	line3Production.insert(1, line3Que.get(0))
	line3Queue.delete(0, 'end')
	step = 1
	f.write(line3Production.get(0))
	f.write('\n')
	for i in line3Que.queue:
		line3Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

def jobComplete4():
	f = open('line4Saved.txt', 'w')
	tmp = line4Production.get(0)
	if line4Que.empty() == True:
		error = messagebox.showinfo("Nice!", "Good job!  The queue is done")
		f.write(line4Production.get(0))
		f.write('\n')
	recentlyCom(tmp)
	line4Production.delete(0, 'end')
	line4Production.insert(1, line4Que.get(0))
	line4Queue.delete(0, 'end')
	step = 1
	f.write(line4Production.get(0))
	f.write('\n')
	for i in line4Que.queue:
		line4Queue.insert(step, i)
		step += 1
		f.write(i)
		f.write('\n')
	f.close()

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
		f.close()
	
# Buttons, labels, etc.. will go in this section
# Creates the header label and sets the behavior
header = Label(win, text = "Production Queue", bg = 'gray', font = ("Arial", 30))
header.pack()

# Creates the exit and load button and the behavior of the button
exitBtn = Button(win, text = "Exit", width = 10, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = exitProg)
exitBtn.place(x = 1700, y = 650)
loadBtn = Button(win, text = "Load", width = 10, bg = 'white', 
	activebackground = 'blue', relief = SUNKEN, command = load)
loadBtn.place(x = 20, y = 650)

# Creates labels displaying line number
line1Label = Label(win, text = "Line 1 production", bg = 'gray', font = ("Arial", 18))
line1Label.place(x = 200, y = 100)
line2Label = Label(win, text = "Line 2 production", bg = 'gray', font = ("Arial", 18))
line2Label.place(x = 600, y = 100)
line3Label = Label(win, text = "Line 3 production", bg = 'gray', font = ("Arial", 18))
line3Label.place(x = 1000, y = 100)
line4Label = Label(win, text = "Line 4 production", bg = 'gray', font = ("Arial", 18))
line4Label.place(x = 1400, y = 100)

# Creates a list box showing current production
line1Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line1Production.place(x = 190, y = 150)
line2Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line2Production.place(x = 590, y = 150)
line3Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line3Production.place(x = 990, y = 150)
line4Production = Listbox(win, height = 1, width = 35, fg = 'blue')
line4Production.place(x = 1390, y = 150)

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

win.mainloop()

# Notes
# Make executable with pyinstaller --onefile productionQueue.py --exclude-module _bootlocale