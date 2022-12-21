##Color GAME:In this game we have type correctly the names of text within 30 sec.if our score becomes greater than 7,
#them we will bw the winner.

import tkinter
import random

#list of colors possibility
colours=["Red","Blue","Green","Black","Yellow","Orange","White","Purple","Brown"]
score=0
timeleft=30
#function that will start the game
def startGame(event): ##Here event argument will be enter action
    if timeleft==30:
        countdown()##inbuilt function
    nextColour()  ##it will call nextColur Function

#function that will shuffle and show the next colour
def nextColour():
    global score ##taken global variable that can use anywhere
    global timeleft
    if timeleft>0:
        #set focus on entry box
        entry.focus_set()
        #compare the input from entrybox with colors list [1st element]
        if entry.get().lower()==colours[1].lower():
            #increment the score
            score+=1
        #clear the entry box
        entry.delete(0,tkinter.END)
        #shuffle the colors list like we don for cards
        random.shuffle(colours)
        #color configuration to dispaly foreground color,text is the 0th elemnt
        Colourlabel.config(fg=str(colours[1]),text=str(colours[0]))
        ScoreLabel.config(text="Scores: "+str(score))
    else:
    
        if score>7:
            instructions.config(fg="green",text="Congrats!!You Won the Game!")
        else:
            instructions.config(fg="red",text="Good Trial!!Try again.")


#start the timer
def countdown():
    global timeleft
    if timeleft>0:
       timeleft-=1
       TimeLabel.config(text="Time Left:"+str(timeleft))
       TimeLabel.after(1000,countdown)

#front-end
root=tkinter.Tk()
root.title("Color Game")
root.geometry("500x500")

instructions=tkinter.Label(root,text="type in the colors of the words,not text",font=("TimesNewRoman",12))
instructions.pack()

ScoreLabel=tkinter.Label(root,text="Press Enter to start",font=("TimesNewRoman",12))
ScoreLabel.pack()

TimeLabel=tkinter.Label(root,text="Time Left: "+str(timeleft),font=("TimesNewRoman",12))
TimeLabel.pack()

Colourlabel=tkinter.Label(root,font=("Helvetika",12))
Colourlabel.pack()

entry=tkinter.Entry(root)
entry.pack()
root.bind("<Return>",startGame)
entry.focus_set()
root.mainloop()