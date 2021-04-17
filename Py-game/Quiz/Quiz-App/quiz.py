import tkinter as tk
from tkinter import *
import random
import sqlite3
import time

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=1200,height=800,bg="black")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Login to play the game",fg="black",bg="white")
    heading.config(font=('Calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                menu()
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=1200,height=800,bg="black")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Signup to play",fg="black",bg="white")
    heading.config(font=('Arial 35'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='black',bg='white')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='black',bg='white')
    clabel.place(relx=0.215,rely=0.7)
    c = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
#        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='black')
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()

def menu():
    login.destroy()
    global menu 
    menu = Tk()
    
    
    menu_canvas = Canvas(menu,width=1200,height=800,bg="black")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text='Q U I Z  G A M E  U S I N G  P Y T H O N',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    
    level = Label(menu_frame,text='Select your Difficulty Level !!',bg="white",font="Calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='Easy',bg="white",font="Calibri 16",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)
    
    mediumR = Radiobutton(menu_frame,text='Medium',bg="white",font="Calibri 16",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)
    
    hardR = Radiobutton(menu_frame,text='Hard',bg="white",font="Calibri 16",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="white",font="Calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def easy():
    
    global e
    e = Tk()
    
    easy_canvas = Canvas(e,width=1200,height=800,bg="#101357")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="white")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0

    easyQ = [
                 [
                     "What is the clock source for the timers?",
                     "some external crystal applied to the micro-controller for executing the timer",
                     "from the crystal applied to the microcontroller",
                     "through software",
                     "through programming"
                 ] ,
                 [
                     "Find out the roll over value for the timer in Mode 0, Mode 1 and Mode 2?" ,
                    "00FFH,0FFFH,FFFFH",
                    "1FFFH,0FFFH,FFFFH",
                    "1FFFH,FFFFH,00FFH",
                    "1FFFH,00FFH,FFFFH"

                 ],
                [
                    "What is the maximum delay that can be generated with the crystal frequency of 22MHz",
                    "2978.9 sec",
                    "0.011 msec",
                    "11.63 sec",
                    "2.97 msec"
                ],
                [
                    "What are the contents of the IE register, when the interrupt of the memory location 0x00 is caused?" ,
                    "0xFFH",
                    "0x00H",
                    "0x10H",
                    "0xF0H"
                ],
                [
                    "What should be done if we want to double the baud rate?" ,
                    "change a bit of the TMOD register",
                    "change a bit of the PCON register",
                    "change a bit of the SCON register",
                    "change a bit of the SBUF register"
                ],
                [
                    "The external interrupts of 8051 can be E. Which pin of the external hardware is said to exhibit INT0 interrupt?",
                    "pin no 10",
                    "pin no 11",
                    "pin no 12",
                    "pin no 13"
                ],
                [
                    "If Timer 0 is to be used as a counter, so what particular pin clock pulse need to be applied?",
                    "P3.3",
                    "P3.4",
                    "P3.5",
                    "P3.6"
                ],
                [
                    "Which pin of the external hardware is said to exhibit INT0 interrupt?",
                    "pin no 10",
                    "pin no 11",
                    "pin no 12",
                    "pin no 13"
                ],
                [
                    "Which of the following combination is the best to enable the external hardware interrupt 0 of the IE register (assuming initially all bits of the IE register are zero)?",
                    "EX0=1",
                    "EA=1",
                    "any of the mentioned",
                    "EX0=1 & EA=1"
                ],
                [
                    "How many machine cycle/s is / are executed by the counters in 8051 in order to detect '1' to '0' transition at the external pin?",
                    "One",
                    "Two",
                    "Four",
                    "Eight"
                ],
                [
                    "Which devices are specifically being used for converting serial to parallel and from parallel to serial respectively?",
                    "Timers",
                    "Counters",
                    "Registers",
                    "Serial Communication"
                ]
            ]
    answer = [
                "from the crystal applied to the microcontroller",
                "1FFFH,FFFFH,00FFH" ,
                "2.97 msec",
                "0x00H",
                "change a bit of the PCON register",
                "pin no 12",
                "P3.4",
                "pin no 13",
                "EX0=1 & EA=1",
                "Two",
                "Register"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQ[x][0],font="Calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="Calibri 10",value=easyQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],font="Calibri 10",value=easyQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQ[x][3],font="Calibri 10",value=easyQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQ[x][4],font="Calibri 10",value=easyQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium():
    
    global m
    m = Tk()
    
    med_canvas = Canvas(m,width=1200,height=800,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="white")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    mediumQ = [
                [
                   "With what frequency UART operates(where f denoted the crystal frequency)?",
                    "f/12",
                    "f/32",
                    "f/144",
                    "f/384"
                ],
                [
                    "Which of the following best states the reason that why baud rate is mentioned	in	serial communication?",
                    "to know about the no of bits being transmitted per second",
	                "to make the two devices compatible with each other, so that the transmission becomes easy and error free",
                    "to use Timer 1",
                    "for wasting memory"
                ],
                [
                    "Which of the following is the logic level understood by the micro- controller/micro-processor?",
                    "TTL logic level",
                    "RS232 logic level",
                    "None of the mentioned",
                    "TTL & RS232 logic level"
                ],
                [
                    "Which of the following best describes the use of framing in asynchronous means of communication?",
                    "a)	it binds the data properly",
	                "it tells us about the start and stops of the data to be transmitted or	received",
	                "it is used for error checking",
	                "it is used for flow control"
                    
                ],
                [
                    "Which of the following signal control  the  flow   of   data?",
                    "RTS",
                    "DTR",
                    "RTS & DTR",
                    "None of the mentioned"
                ],
                [
                    "What is the difference between UART and USART communication?"
                    "they are the names of the same particular thing, just the difference of A and S is there in it",
                    "one uses asynchronous means of communication and the other uses synchronous means of communication",
                    "one uses asynchronous means of communication and the other uses asynchronous and synchronous means	of communication",
                    "one uses angular means of the communication and the other uses linear means of communication"
                ],
                [
                    "In serial communication modes, mode 1 the Baud rate = "
                    "BR=2SMOD/32 * (Timer 0 over flow rate)",
                    "BR=2SMOD/16 * (Timer 1 over flow rate)",
                    "BR=2SMOD/16 * (Timer 0 over flow rate)",
                    "BR=2SMOD/32 * (Timer 1 over flow rate)"
                ]
            ]
    answer = [
            "f/384",
            "to make the two devices compatible with each other, so that the transmission becomes easy and error free",
            "TTL logic level",
            "it tells us about the start and stops of the data to be transmitted or	received",
            "RTS",
            "one uses asynchronous means of communication and the other uses asynchronous and synchronous means	of communication",
            "BR=2SMOD/32 * (Timer 1 over flow rate)"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =mediumQ[x][0],font="Calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=mediumQ[x][1],font="Calibri 10",value=mediumQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQ[x][2],font="Calibri 10",value=mediumQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQ[x][3],font="Calibri 10",value=mediumQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQ[x][4],font="Calibri 10",value=mediumQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
       
    global h
    h = Tk()
    
    hard_canvas = Canvas(h,width=1200,height=800,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="white")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    hardQ = [
                [
        "What is the disadvantage of a level triggered pulse?",
        "a constant pulse is to be maintained for a greater span of time",
        "another interrupt may be generated if the low-level signal is not removed before the ISR is finished",
        "it is difficult to produce",
        "another interrupt may be caused if the signal is still low before the completion of the last instruction"
    ],
    [
        "If two interrupts, of higher priority and lower priority occur simultaneously, then the service provided is for",
        "a)	interrupt	of	lower	priority",
        "interrupt	of	higher	priority",
        "lower & higher priority interrupts",
        "none of the mentioned"
    ],
    [
        "After RETI instruction is executed then the pointer will move to which location       in       the      program?",
        "next interrupt of the interrupt vector	table",
        "immediate	next	instruction where	interrupt is occurred",
        "next instruction after the RETI in the	memory",
        "none of the mentioned"
    ],
    [
        "Which of the following commands are used for addressing the off-chip data and associated codes respectively by data pointer?",
        "MOVC & MOVY",
        "MOVY & MOVB",
        "MOVZ & MOVA",
        "MOVX & MOVC"

    ],
    [
        "Serial port vector address is of _______. And causes an interrupt when ________.",
        "0013H, either TI or RI flag is set",
        "0023H, either TI or RI flag is reset",
        "0013H, either TI or RI flag is reset",
        "0023H, either TI or RI flag is set"

    ] 
            
]
    answer = [
            "another interrupt may be caused if the signal is still low before the completion of the last instruction",
            "interrupt	of	higher	priority",
            "immediate	next	instruction where	interrupt is occurred",
            "MOVX & MOVC",
            "0023H, either TI or RI flag is set"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(hard_frame,text =hardQ[x][0],font="Calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame,text=hardQ[x][1],font="Calibri 10",value=hardQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQ[x][2],font="Calibri 10",value=hardQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQ[x][3],font="Calibri 10",value=hardQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQ[x][4],font="Calibri 10",value=hardQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(hard_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=1200,height=800,bg="#101111")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Your score is "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    sh.mainloop()
def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 1200,height = 800)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="Home.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage) 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
