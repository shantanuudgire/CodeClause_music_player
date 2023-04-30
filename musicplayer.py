import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg = 'black')

rootpath = "C:\\Users\\shant\\New folder (2)\\music player"
pattern = "*.mp3"
mixer.init()
prev_img = tk.PhotoImage(file= "prev.png" )
play_img = tk.PhotoImage(file= "playy.png")
pause_img = tk.PhotoImage(file= "pause.png")
next_img = tk.PhotoImage(file= "nextt.png")
stop_img = tk.PhotoImage(file= "stopp.png")
def  select():
    label.config(text = listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()
def stop():
    mixer.music.stop()
    listbox.select_clear('active')
def p_next():
    nextsong = listbox.curselection()
    nextsong = nextsong[0]+1
    nextsong_name = listbox.get(nextsong)
    label.config(text=nextsong_name)
    mixer.music.load(rootpath + "\\" + nextsong_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(nextsong)
    listbox.select_set(nextsong)
def p_prev():
    nextsong = listbox.curselection()
    nextsong = nextsong[0]-1
    nextsong_name = listbox.get(nextsong)
    label.config(text=nextsong_name)
    mixer.music.load(rootpath + "\\" + nextsong_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(nextsong)
    listbox.select_set(nextsong)
def pause_s():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"]= "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"




listbox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100 , font = ('poppins', 14 ))
listbox.pack(padx = 15, pady = 15)
label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow' , font = ('ds-digital', 18))
label.pack(pady= 15)
top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10 , pady = 5, anchor='center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img , bg= "blue", borderwidth=0, command=p_prev )
prevButton.pack(pady = 15, in_ =top, side='left')
pauseButton = tk.Button(canvas, text = "Pause", image = pause_img , bg="blue", borderwidth=0, command=pause_s)
pauseButton.pack(pady = 15, in_ =top, side='left')
playButton = tk.Button(canvas, text = "Play", image = play_img , bg= "blue", borderwidth=0, command=select)
playButton.pack(pady = 15, in_ =top, side='left')

stopButton = tk.Button(canvas, text = "Stop", image= stop_img, bg= "blue", borderwidth=0, command=stop)
stopButton.pack(pady = 15, in_= top, side ='left')
nextButton = tk.Button(canvas, text = "Next", image=next_img, bg="blue", border=0, command=p_next)
nextButton.pack(pady = 15, in_= top, side ='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)
canvas.mainloop()

