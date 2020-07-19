import webbrowser


def pd():
    webbrowser.open('https://drive.google.com/file/d/1S6SFPMHa_okdY0kfJHg2KXA3p_DPFRdx/view')


import tkinter as tk
win = tk.Tk()
win.title("Food by Neshaa")
win.configure(bg='yellow')
win.geometry('300x300')
l2 = tk.Label(win, text="Potato Deluge", bg='black', fg='red')
l1 = tk.Button(win, text="press to watch the video", command=pd, bg='red', fg='black', )
l2.pack()
l1.pack()
win.mainloop()
