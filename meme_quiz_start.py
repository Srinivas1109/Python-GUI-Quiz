import tkinter as tk
from tkinter import Radiobutton
import tkinter.font as font
import random
from PIL import Image, ImageTk
import data

randlist = []

def anscall():
  global que, op1, op2, op3, op4, nex, imgLabel,start_but
  imgLabel.destroy()
  que.destroy()
  op1.destroy()
  op2.destroy()
  op3.destroy()
  op4.destroy()
  nex.destroy()

  global points
  if (data.ans[rand] == ansVal.get()):
    points += 1
  
  show_ques()

def show_ques():
  global rand, cou, points,start_wind, randlist

  cou += 1
  if cou == 11:
    res_but = tk.Button(text = "Your Score : " + str(points))
    res_but.place(height = 100, width = 200, x = 300, y = 400)
    res_but['font'] = font.Font(size = 15)
    if points == 10:
      txt=tk.Label(start_wind, text = "Man. Myth. Legend!!", font=("Times",24), background="#ffffff")
      txt.place(x=320, y=550)
    elif points >= 8:
      txt=tk.Label(start_wind, text = "EXCELLENT!! ", font=("Times",24), background="#ffffff")
      txt.place(x=320,y=550)
    elif points in (4, 5, 7):
      txt=tk.Label(start_wind, text = "Good,,,, could be better", font=("Times",24), background="#ffffff")
      txt.place(x=220,y=550)
    else:
      txt=tk.Label(start_wind, text = "You ought to be a normie", font=("Times",24), background="#ffffff")
      txt.place(x=220,y=550)
      
      
    

    points = 0
  else:
    while True:
      rand = random.randint(0,22) 
      if rand not in randlist:
        randlist.append(rand)
        break

    global img, test, imgLabel

    img = Image.open("image" + str(rand) + ".jpg") 
    img.resize((800, 800), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(img)

    imgLabel = tk.Label(image = test)
    imgLabel.image = test
    imgLabel.place(x = 0, y = 0)

    global ansVal
    global que, op1, op2, op3, op4, nex
    ansVal = tk.IntVar()

    que = tk.Button(text = str(cou) + ") " + data.que[rand],font=("Impact",15))
    op1 = Radiobutton(text = "a) " + data.options[rand][0], variable = ansVal, value = 1)
    op2 = Radiobutton(text = "b) " + data.options[rand][1], variable = ansVal, value = 2)
    op3 = Radiobutton(text = "c) " + data.options[rand][2], variable = ansVal, value = 3)
    op4 = Radiobutton(text = "d) " + data.options[rand][3], variable = ansVal, value = 4)
    nex = tk.Button(text = "Next", command = anscall)
    

    que.place(x = 50, y = 480)
    op1.place(x = 50, y = 530)
    op2.place(x = 50, y = 580)
    op3.place(x = 50, y = 630)
    op4.place(x = 50, y = 680)
    nex.place(x = 50, y = 730)

    ##que['font'] = font.Font(size = 15)
    op1['font'] = font.Font(size = 12)
    op2['font'] = font.Font(size = 12)
    op3['font'] = font.Font(size = 12)
    op4['font'] = font.Font(size = 12)
    nex['font'] = font.Font(size = 12)

def start_quiz():
  global cou,start_but,lblrules,lblinstructions
  start_but.destroy()
  lblrules.destroy()
  lblinstructions.destroy()
  cou = 0
  show_ques()


def main():
  global points,start_but,lblrules,lblinstructions,start_wind
  points = 0

  start_wind = tk.Tk()
  start_wind.title("Meme Quiz")
  start_wind.config(background="#ffffff")
  start_wind.geometry("800x800")

  img2=tk.PhotoImage(file="frame.png")
  start_but = tk.Button(start_wind, text = "Start Test", command = start_quiz,background="#ffffff",image=img2,relief=tk.FLAT,border=0,)
  start_but.place(height = 110, width = 240, x = 295, y = 200)
  start_but['font'] = font.Font(size = 15)

  lblrules=tk.Label(start_wind,
    
    text="This Quiz contains 10 questions\n each question carries 1 mark,Once you select the option that is final\n So think before you choose",
    width=100, 
    font=("Times",14),
    background="#000000",
    foreground="#FACA2F",)
  lblrules.pack(pady=(700,0))

  lblinstructions=tk.Label(
    start_wind,
    text="These questions are just for fun.\n Click Start Once You Are ready",
    background="#ffffff",
    font=("Book Antiqua",14),
    justify="center",)

  lblinstructions.place(x = 270, y = 310)

  start_wind.resizable(0,0)
  
  start_wind.mainloop()

main()
