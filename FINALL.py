import json
from difflib import get_close_matches as g
from tkinter import *
import tkinter.messagebox

data=json.load(open("dictionary.json", encoding="utf-8"))
word_data = data.values()
keys = data.keys()

def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res == True:
        root.destroy()

    else:
        pass
def meaning():

    t1.delete(1.0,END)

    w = e1_value.get().lower()
    for vocabula in data:
        for lexeme in data[vocabula]:
            cnt = 1
            if w in lexeme["meaning"].lower():
                t1.insert(END,vocabula)
                t1.insert(END, ": ")
                t1.insert(END,"\n")
                for i in data[vocabula]:
                    t1.insert(END,cnt)
                    t1.insert(END, ". ")
                    t1.insert(END,"".join(i["pos"]))
                    t1.insert(END," ")
                    t1.insert(END,i["meaning"])
                    t1.insert(END,". ")
                    t1.insert(END,"\n")
                    t1.insert(END,"\n")
                    cnt += 1

            elif w in lexeme["pos"]:
                t1.insert(END,vocabula)
                t1.insert(END, ": ")
                t1.insert(END,"\n")
                for i in data[vocabula]:
                    t1.insert(END,cnt)
                    t1.insert(END,". ")
                    t1.insert(END," ")
                    t1.insert(END,i["meaning"])
                    t1.insert(END,". ")
                    t1.insert(END,"\n")
                    t1.insert(END,"\n")
                    cnt += 1

    if w in data:
        cnt = 1
        t1.insert(END,w)
        t1.insert(END, ": ")
        t1.insert(END,"\n")
        for i in data[w]:
            t1.insert(END,cnt)
            t1.insert(END,". ")
            t1.insert(END,"".join(i["pos"]))
            t1.insert(END," ")
            t1.insert(END,i["meaning"])
            t1.insert(END,". ")
            t1.insert(END,"\n")
            t1.insert(END,"\n")
            cnt += 1

    else:
        real_list=g(w,keys,cutoff=0.8)
        if len(real_list) == 0:
            pass
        else:
            cnt = 1
            for real in real_list:
                t1.insert(END,real)
                t1.insert(END, ": ")
                t1.insert(END,"\n")
                for i in data[real]:
                    t1.insert(END,cnt)
                    t1.insert(END,". ")
                    t1.insert(END,"".join(i["pos"]))
                    t1.insert(END," ")
                    t1.insert(END,i["meaning"])
                    t1.insert(END,". ")
                    t1.insert(END,"\n")
                    t1.insert(END,"\n")
                    cnt += 1


root=Tk()
bg = PhotoImage(file = "benimo1.png")
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title("Veliso.")
root.attributes('-fullscreen', False)
root.resizable(1, 1)

header=Label(root, text="OKINAWAN-ENGLISH DICTIONARY.", font = ("Baskerville", 40), bg="#b4a7d6", fg="white")
header.pack(fill=X)

label1=Label(root, text="Enter your word:", font = ("Baskerville", 20), bg= "#d9d2e9")
label1.pack()

e1_value=StringVar()
e1=Entry(root, textvariable=e1_value, font=('Baskerville', 30, 'italic'))
e1.pack()

button=Button(root, text="Meaning!", command=meaning, font = ("Baskerville", 20))
button.pack()

t1=Text(root, font = ("Baskerville", 18))
t1.pack(fill=X)
t1.insert(END, 'Hi, colleagues.')
t1.insert(END, '\n')
t1.insert(END, '\n')
t1.insert(END, "We've prepared an Okinawan-English dictionary. Here, the vocabula search in both variants is possible. Search via Part of Speech and definitions are also provided.")
t1.insert(END, '\n')
t1.insert(END, '\n')
t1.insert(END, "We wanted to make our dictionary as accessible as Google Translator, but for the language not many of you are familiar with.")
t1.insert(END, '\n')
t1.insert(END, '\n')
t1.insert(END, 'Buttons are present for click-searching and clearing the screen.')
t1.insert(END, '\n')
t1.insert(END, '\n')
t1.insert(END, 'Delete the following text before getting to work and good luck.')
t1.insert(END, '\n')
t1.insert(END, '\n')
t1.insert(END, 'Team Veliso - Vera, Liza, Sophia.')

root.mainloop()
