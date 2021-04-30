from tkinter import *
import playsound
from tkinter import filedialog
#The Modules are extracted here

root=Tk()
root.title("Hwlo Musik")
root.geometry('1000x200')
root.config(bg="#3B4252")
buttonframe=Frame(root,bg="#4C566A")
buttonframe.pack(side=BOTTOM)

def play():
    
    new=filedialog.askopenfilename(initialdir="/",filetypes=(("Mp3 File", "*.mp3"),("WAV File","*.wav"),("All Files","*.*")))
    
    playsound.playsound(new)
labell=Label(root,text="Hwlo Musik!!! The MusiC Player of Hwloman",bd=10,relief="groove",font=("consolas",25,"bold"),bg="#2E3440",fg="green")
labell.pack(side=TOP,fill=X)    
button=Button(buttonframe,text="Click to play music file",bd=9,command=play,font=("Ubuntu Mono",14),bg="#4C566A",fg="green")
button.pack(side=TOP,fill=X)
root.mainloop()
