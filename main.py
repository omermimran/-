from tkinter import *
import time
root = Tk()
root.title("פרויקט")
root.geometry("1000x1000")

canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
def debugger():
    if MemoryError: raise Exception('There is an error with the memory')
    elif EOFError: raise Exception('There is an error with the code')
    elif EnvironmentError: raise Exception('There is an error with the modules or the lang may be corrupted')
    else: print('you fucked up the program')
def timer(tk, time_label, no):
    time_label.configure(text=now)
    tk.after(1000, timer)
    now += 1
def story():
    master= Tk()
    master.title("the untold tales")
    master.geometry("500x500")
    Label("""
    ננעלתם בחדר רדוף ערפד מפחיד
    שמאיים לרצוח אותכם
    אם לא תצאו מחדר בחצי שעה הקרובה""")
def questions(title, level, question, sizepx, size, xx, yy, x, y, ex, ey, result):
    master = Tk()
    master.configure(bg="white")
    master.title(title)
    master.geometry("800x600")
    e=Entry(master,width=45)
    Label(master,text=level, font=("arial",size), bg="white").place(x=xx,y=yy)
    Label(master, text= question, bg="white", font=("arial", sizepx)).place(x=x, y=y)
    e.place(x=ex,y=ey)
    def submit(value,result, tk=None):
        if value == result: return tk.quit()
        else: Label("התשובה לא היתה נכונה").pack(side="bottom")
    button = Button(master, text="submit", command=lambda: submit(e.get(),result, master))
    button.place(x=ex-50,y=ey+40)

def main(*functions, statement):
    if statement:
        for function in functions:
            function()
    else:
        debugger()
canvas.create_text(500,50,text="חדר בריחה"[::-1],font=("arial",40))

button1 = Button(root, text="level1", command=lambda: questions(
    "question 1", "level 1", "hi", 20,
    20, 100, 100 , 400, 300, 400 , 400, 15)
)# button 1
canvas.create_window(500,100,window=button1)
"""
button2 = Button(root, text="level2", command=question2)
canvas.create_window(500,200,window=button2)

button3 = Button(root, text="level3", command=question3)
canvas.create_window(500,300,window=button3)

button4 = Button(root, text="level4", command=question4)
canvas.create_window(500,400,window=button4)

button5 = Button(root, text="level5", command=question5)
canvas.create_window(500,500,window=button5)
"""
root.mainloop()
print(0b1111)