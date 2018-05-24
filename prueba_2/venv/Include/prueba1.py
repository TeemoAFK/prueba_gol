import vlc
from tkinter import *

tk=Tk()
cancion = vlc.MediaPlayer("1.mp3")
canvas=Canvas(tk,width =1200,height=800)
canvas.pack()
cancion.play()
pelota=PhotoImage(file="pelota.png")
arco=PhotoImage(file="arco.png")
canvas.create_image(800,370,anchor=NW,image=pelota)
canvas.create_image(60,350,anchor=NW,image=arco)
canvas.create_text(200,100,fill="blue",font="ComicSans 50 italic bold",
                        text="GOOOL!!!")
def movetriangle(event):
    canvas.move(1,-6,0)
    pos=canvas.move(1,-6,0)
    print(pos)
canvas.bind_all('<KeyPress-Left>',movetriangle)
tk.mainloop()