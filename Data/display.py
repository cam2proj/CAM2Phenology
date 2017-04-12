import tkinter
from tkinter import *
from PIL import Image, ImageTk
import frontEnd
from frontEnd import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


root=tkinter.Tk()


def plot():
	plotAllPoints(sourceVar.get(), a)
	pltCanvas.show()	
def configureDisplay():
#	addPoint(sourceVar.get(), a)	
#	pltCanvas.show()
	image=imageDisplay.activeImage.resize((960, 540), Image.ANTIALIAS)
	im=ImageTk.PhotoImage(image)
	canvas.image=im
	canvas.create_image(0, 0, image=canvas.image, anchor='nw')
def next():
	imageDisplay.getNext()
	configureDisplay()
def previous():
	imageDisplay.getNext()
	configureDisplay()
def updateDisplay(sourceName):
	imageDisplay.changeActive(sourceName)
	configureDisplay()
def sourceMenu():
	menu=OptionMenu(root, sourceVar, *list(imageDisplay.sourceList.keys()), command=updateDisplay)
	menu.grid(row=17, column=13)

def newLocal(source):
	imageDisplay.addLocal(source)
	configureDisplay()
	sourceMenu()

def newTimeSlider():
	imageDisplay.addTimeSlider()
	configureDisplay()
	sourceMenu()
def nextD():
	imageDisplay.nextDy()
	configureDisplay()
def previousD():
	imageDisplay.previousDy()
	configureDisplay()
def nextY():
	imageDisplay.nextYr()
	configureDisplay()
def previousY():
	imageDisplay.previousYr()
	configureDisplay()
def goTo():
	yr=yearEntry.get()
	mn=monthEntry.get()
	dy=dayEntry.get()
	if yr=="":
		yr='0'
	if mn=="":
		mn='0'
	if dy=="":
		dy='0'
	print(mn+', '+dy+', '+yr)
	imageDisplay.goTo(yr, mn, dy)
	configureDisplay()	


imageDisplay=ImageManager()
sourceVar=StringVar(root)
dataVar=StringVar(root)

#Image Canvas+management(under image) 
canvas=Canvas(root, width=960, height=540)
canvas.grid(row=0, column=5, rowspan=15, columnspan=15)
canvas.configure(background='blue')
configureDisplay()

#figure for having pyplot
f = Figure(figsize=(4, 3), dpi=70)
a=f.add_subplot(111)
pltCanvas = FigureCanvasTkAgg(f, master=root)
pltCanvas.get_tk_widget().grid(row=0, column=22)
pltCanvas._tkcanvas.grid(row=0, column=22)
plotFlag=0

#Left management widgets
L1=Label(root, text='sources')
L1.grid(row=7, column=0, sticky='n')
"""bufferEntry=Entry(root, bd=5)
bufferEntry.grid(row=10, column=0)"""
yearEntry=Entry(root, bd=5, width=5)
monthEntry=Entry(root, bd=5, width=5)
dayEntry=Entry(root, bd=5, width=5)
localData=os.listdir('data')

dataMenu=OptionMenu(root, dataVar, *frontEnd.localData, command=newLocal)
dataMenu.grid(row=8, column=0)
next=Button(root, text='>>>', width=5, command=next)
pre=Button(root, text='<<<', width=5, command=previous)
plot=Button(root, text='Plot Geo', width=5, command=plot)
newSlider=Button(root, text='time slider', command=newTimeSlider) 
nextDay=Button(root, text='next day', width=5, command=nextD)
previousDay=Button(root, text='previous day', width=5, command=previousD)
nextYear=Button(root, text='next year', width=5, command=nextY)
previousYear=Button(root, text='previous year', width=5, command=previousY)
goToDay=Button(root, text='go to day', width=5, command=goTo)

newSlider.grid(row=16, column=11)
yearEntry.grid(row=16, column=14)
monthEntry.grid(row=16, column=13)
dayEntry.grid(row=16, column=12)
plot.grid(row=17, column=18)
next.grid(row=17, column=19)
pre.grid(row=17, column=5)
nextDay.grid(row=17, column=17)
nextYear.grid(row=17, column=16)
previousDay.grid(row=17, column=6)
previousYear.grid(row=17, column=5)
goToDay.grid(row=16, column=15)
root.mainloop()
