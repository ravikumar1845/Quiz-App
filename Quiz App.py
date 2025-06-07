import tkinter

# Window setup
root = tkinter.Tk()
root.title("QUIZ")
root.geometry('1200x700')

score = 0  # To store correct answers count
user_name = ""  # Global name to use later

# Title
label_t = tkinter.Label(root, text="QUIZ", font=("arial", 50))
label_t.place(x=500, y=50)

# Username label and entry
label_u = tkinter.Label(root, text="Username", font=("arial", 30))
label_u.place(x=250, y=250)
entry = tkinter.Entry(root, font=("arial", 30))
entry.place(x=500, y=250)

# Score increment function
def increase():
    global score
    score += 1

# Start Quiz
def info1():
    global user_name
    user_name = entry.get()

    # Destroy initial widgets
    label_t.destroy()
    label_u.destroy()
    entry.destroy()
    button.destroy()

    # Question 1
    label_q1 = tkinter.Label(root, text="Question 1", font=("Arial", 35))
    label_q1.place(x=500, y=50)
    label1 = tkinter.Label(root, text="Which of them is a Keyword in Python?", font=("Arial", 28))
    label1.place(x=300, y=130)

    def next1(correct):
        if correct:
            increase()
        label_q1.destroy()
        label1.destroy()
        for btn in [op1, op2, op3, op4]:
            btn.destroy()
        info2()

    op1 = tkinter.Button(root, text="range", font=("Arial", 20), command=lambda: next1(False))
    op2 = tkinter.Button(root, text="def", font=("Arial", 20), command=lambda: next1(True))
    op3 = tkinter.Button(root, text="Val", font=("Arial", 20), command=lambda: next1(False))
    op4 = tkinter.Button(root, text="to", font=("Arial", 20), command=lambda: next1(False))

    op1.place(x=400, y=230)
    op2.place(x=800, y=230)
    op3.place(x=400, y=300)
    op4.place(x=800, y=300)

def info2():
    label_q2 = tkinter.Label(root, text="Question 2", font=("Arial", 35))
    label_q2.place(x=500, y=50)
    label2 = tkinter.Label(root, text="Which is a built-in function in Python?", font=("Arial", 28))
    label2.place(x=300, y=130)

    def next2(correct):
        if correct:
            increase()
        label_q2.destroy()
        label2.destroy()
        for btn in [b1, b2, b3, b4]:
            btn.destroy()
        info3()

    b1 = tkinter.Button(root, text="factorial()", font=("Arial", 20), command=lambda: next2(False))
    b2 = tkinter.Button(root, text="print()", font=("Arial", 20), command=lambda: next2(True))
    b3 = tkinter.Button(root, text="seed()", font=("Arial", 20), command=lambda: next2(False))
    b4 = tkinter.Button(root, text="sqrt()", font=("Arial", 20), command=lambda: next2(False))

    b1.place(x=400, y=230)
    b2.place(x=800, y=230)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

def info3():
    label_q3 = tkinter.Label(root, text="Question 3", font=("Arial", 35))
    label_q3.place(x=500, y=50)
    label3 = tkinter.Label(root, text="Which is not a core datatype in Python?", font=("Arial", 28))
    label3.place(x=300, y=130)

    def next3(correct):
        if correct:
            increase()
        label_q3.destroy()
        label3.destroy()
        for btn in [b1, b2, b3, b4]:
            btn.destroy()
        info4()

    b1 = tkinter.Button(root, text="Tuple", font=("Arial", 20), command=lambda: next3(False))
    b2 = tkinter.Button(root, text="Dictionary", font=("Arial", 20), command=lambda: next3(False))
    b3 = tkinter.Button(root, text="Lists", font=("Arial", 20), command=lambda: next3(False))
    b4 = tkinter.Button(root, text="Class", font=("Arial", 20), command=lambda: next3(True))

    b1.place(x=400, y=230)
    b2.place(x=800, y=230)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

def info4():
    label_q4 = tkinter.Label(root, text="Question 4", font=("Arial", 35))
    label_q4.place(x=500, y=50)
    label4 = tkinter.Label(root, text="Who developed Python language?", font=("Arial", 28))
    label4.place(x=300, y=130)

    def next4(correct):
        if correct:
            increase()
        label_q4.destroy()
        label4.destroy()
        for btn in [b1, b2, b3, b4]:
            btn.destroy()
        info5()

    b1 = tkinter.Button(root, text="Wick Van Rossum", font=("Arial", 20), command=lambda: next4(False))
    b2 = tkinter.Button(root, text="Rasmus Lerdorf", font=("Arial", 20), command=lambda: next4(False))
    b3 = tkinter.Button(root, text="Guido Van Rossum", font=("Arial", 20), command=lambda: next4(True))
    b4 = tkinter.Button(root, text="Niene Stom", font=("Arial", 20), command=lambda: next4(False))

    b1.place(x=400, y=230)
    b2.place(x=800, y=230)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

def info5():
    label_q5 = tkinter.Label(root, text="Question 5", font=("Arial", 35))
    label_q5.place(x=500, y=50)
    label5 = tkinter.Label(root, text="Which is the extension of Python file?", font=("Arial", 28))
    label5.place(x=300, y=130)

    def next5(correct):
        if correct:
            increase()
        label_q5.destroy()
        label5.destroy()
        for btn in [b1, b2, b3, b4]:
            btn.destroy()
        show_score()

    b1 = tkinter.Button(root, text=".python", font=("Arial", 20), command=lambda: next5(False))
    b2 = tkinter.Button(root, text=".p", font=("Arial", 20), command=lambda: next5(False))
    b3 = tkinter.Button(root, text=".pl", font=("Arial", 20), command=lambda: next5(False))
    b4 = tkinter.Button(root, text=".py", font=("Arial", 20), command=lambda: next5(True))

    b1.place(x=400, y=230)
    b2.place(x=800, y=230)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

def show_score():
    score_label = tkinter.Label(root, text="QUIZ COMPLETED!", font=("Arial", 40), fg="green")
    score_label.place(x=400, y=100)
    user_label = tkinter.Label(root, text=f"Name: {user_name}", font=("Arial", 30))
    user_label.place(x=400, y=200)
    final_score = tkinter.Label(root, text=f"Your Score: {score}/5", font=("Arial", 30))
    final_score.place(x=400, y=270)

# Start Button
button = tkinter.Button(root, text="START QUIZ", font=("arial", 30), command=info1)
button.place(x=600, y=350)

root.mainloop()
