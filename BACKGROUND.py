import json
from difflib import get_close_matches as g

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

    w = e1_value.get().lower()
    for vocabula in data:
        for lexeme in data[vocabula]:
            counter = 1
            if w in lexeme["meaning"].lower():
                t1.insert(END,vocabula)
                t1.insert(END, ": ")
                t1.insert(END,"\n")
                for i in data[vocabula]:
                    t1.insert(END,counter)
                    t1.insert(END, ". ")
                    t1.insert(END,"".join(i["pos"]))
                    t1.insert(END," ")
                    t1.insert(END,i["meaning"])
                    t1.insert(END,". ")
                    t1.insert(END,"\n")
                    t1.insert(END,"\n")
                    counter += 1

            elif w in lexeme["meaning"].upper():
                t1.insert(END,vocabula)
                t1.insert(END, ": ")
                t1.insert(END,"\n")
                for i in data[vocabula.upper()]:
                    t1.insert(END,counter)
                    t1.insert(END,". ")
                    t1.insert(END,"".join(i["pos"]))
                    t1.insert(END," ")
                    t1.insert(END,i["meaning"])
                    t1.insert(END,". ")
                    t1.insert(END,"\n")
                    t1.insert(END,"\n")
                    counter += 1

            elif w in lexeme["meaning"].title():
                t1.insert(END,vocabula)
                t1.insert(END, ": ")
                t1.insert(END,"\n")
                for i in data[vocabula.title()]:
                    t1.insert(END,counter)
                    t1.insert(END,". ")
                    t1.insert(END,"".join(i["pos"]))
                    t1.insert(END," ")
                    t1.insert(END,i["meaning"])
                    t1.insert(END,". ")
                    t1.insert(END,"\n")
                    t1.insert(END,"\n")
                    counter += 1

            elif w in lexeme["pos"]:
                t1.insert(END,vocabula)
                t1.insert(END, ": ")
                t1.insert(END,"\n")
                for i in data[vocabula]:
                    t1.insert(END,counter)
                    t1.insert(END,". ")
                    t1.insert(END," ")
                    t1.insert(END,i["meaning"])
                    t1.insert(END,". ")
                    t1.insert(END,"\n")
                    t1.insert(END,"\n")
                    counter += 1

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

    elif w.upper() in data:
        t1.insert(END,w)
        t1.insert(END, ": ")
        t1.insert(END,"\n")
        for i in data[w.upper()]:
            t1.insert(END,cnt)
            t1.insert(END,". ")
            t1.insert(END,"".join(i["pos"]))
            t1.insert(END," ")
            t1.insert(END,i["meaning"])
            t1.insert(END,". ")
            t1.insert(END,"\n")
            t1.insert(END,"\n")
            cnt += 1

    elif w.title() in data:
        t1.insert(END,w)
        t1.insert(END, ": ")
        t1.insert(END,"\n")
        for i in data[w.title()]:
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
                t1.insert(END,w)
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

def meaning2():
    t1.delete(1.0,END)
    e1.delete(0,END)

from tkinter import *
import tkinter.messagebox
root=Tk()
bg = PhotoImage(file = "benimo1.png")
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title("Veliso.")
root.attributes('-fullscreen', False)
root.resizable(1, 1)

header=Label(root, text="Okinawian-English Dictionary.", font = ("Courier", 40), bg="#b4a7d6", fg="white")
header.pack(fill=X)

label1=Label(root, text="Enter your word:", font = ("Courier", 16), bg= "#d9d2e9")
label1.pack()

e1_value=StringVar()
e1=Entry(root, textvariable=e1_value)
e1.pack()

button=Button(root, text="Meaning!", command=meaning, font = ("Courier", 20))
button.pack()

t1=Text(root)
t1.pack(fill=X)

label2=Label(root, text="Press it for clearing screen.", font = ("Courier", 16), bg = "#d9d2e9")
label2.pack()

button2=Button(root,text="Clear Screen!", command=meaning2, font = ("Courier", 20))
button2.pack()


root.mainloop()
