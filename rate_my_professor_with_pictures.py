from msilib.schema import ListBox
from textwrap import fill
import tkinter.messagebox
from tkinter import  *
import tkinter as tk
import random as rd
import os
from secrets import choice
from turtle import width
import mysql.connector
from PIL import ImageTk, Image

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Avamery2021!",
    database = "rateprofessor"
)
mycursor = db.cursor()


#Option Number one will search the professor of the user's choice
def searchProfessor():
    root1 = Tk()
    root1.geometry("800x700")
    root1.resizable(False, False)
    image_2 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\PCT.png', master = root1)
    background1 = Label(root1, image = image_2, bd = 0)
    background1.place(x = 0, y = 0)
    img4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sn.png', master = root1)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\snl.png', master = root1)
    img6 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\lop.png', master = root1)
    fn=Button(root1,image = img4,command= search_n, bd = 0)
    ln=Button(root1,image = img5, command=search_ln, bd = 0)
    all=Button(root1,image = img6,command=search_all, bd = 0)
    fn.pack(side=LEFT,padx=(50,25), pady = (200,0))
    ln.pack(side=LEFT,padx=25, pady = (200,0))
    all.pack(side=LEFT,padx=25, pady = (200,0))
    frame=Frame(root1)
    frame.pack()
    root1.mainloop()
#Function that search by name
def search_n(): 
    global e1
    root2=Tk()
    root2.geometry("400x300")
    root2.resizable(False, False)
    image_3 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sbn.png', master = root2)
    background1 = Label(root2, image = image_3, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root2)
    frame.pack()
    e1=tkinter.Entry(root2)
    e1.place(x=200,y=130, height = 35)
    image_4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sup.png', master = root2)
    b1=Button(root2,image = image_4,command=result_n, borderwidth= 0 )
    b1.place(x=120,y=200)
    root2.mainloop()
def result_n():
    global e1
    root3=Tk()
    root3.geometry("800x700")
    root3.resizable(False, False)
    image_5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\rbn.png', master = root3)
    background1 = Label(root3, image = image_5, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root3)
    frame.pack()
    entry= e1.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT faculty_name, course_name,course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where faculty_name =%s", (entry_0,))
    mydata = mycursor.fetchall()
    text = tk.Text(root3,font = ("Times New Roman", 15), bd = 5, spacing1= 12 , wrap = WORD)
    scroll_bar = Scrollbar(root3,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')

    root3.mainloop()
#Function that search by last name
def search_ln():
    global e2
    root4=Tk()
    root4.geometry("400x300")
    root4.resizable(False, False)
    image_6 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sbln.png', master = root4)
    background1 = Label(root4, image = image_6, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root4)
    frame.pack()
    e2=tkinter.Entry(root4)
    e2.place(x=200,y=125, height = 30)
    image_7 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\suln.png', master = root4)
    b1=Button(root4,image = image_7,command=results_ln, borderwidth=0)
    b1.place(x=130,y=200)
    root4.mainloop()
def results_ln():
    global e2
    root4=Tk()
    root4.geometry("800x700")
    root4.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\rbln.png', master = root4)
    background1 = Label(root4, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root4)
    frame.pack()
    entry= e2.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT faculty_lastname,faculty_name, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where faculty_lastname =%s", (entry_0,))
    mydata = mycursor.fetchall()
    text = tk.Text(root4,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root4,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')

    root4.mainloop()
#Function that prints all the courses and teachers available with their reviews
def search_all():
    root5=Tk()
    root5.geometry("800x700")
    root5.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\loallp.png', master = root5)
    background1 = Label(root5, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root5)
    frame.pack()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
    mydata = mycursor.fetchall()
    text = tk.Text(root5,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root5,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
        #answer = Label(root5,text = str(rows, ), font = ("Times New Roman", 15))
        #answer.pack(side = LEFT, fill = BOTH)

    root5.mainloop()

def searchCourse():
    root6 = Tk()
    root6.geometry("800x700")
    root6.resizable(False, False)
    image_2 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sbci.png', master = root6)
    background1 = Label(root6, image = image_2, bd = 0)
    background1.place(x = 0, y = 0)
    img4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sbucn.png', master = root6)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sbuallc.png', master = root6)
    fn=Button(root6,image = img4,command= course_name, borderwidth=0)
    all=Button(root6,image = img5, command=all_courses, borderwidth=0)
    fn.pack(side=LEFT,padx=(150,50), pady = (200,0))
    all.pack(side=LEFT,padx=25, pady = (200,0))
    frame=Frame(root6)
    frame.pack()
    root6.mainloop()

def course_name(): 
    global e3
    root7=Tk()
    root7.geometry("400x300")
    root7.resizable(False, False)
    image_3 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sbcn.png', master = root7)
    background1 = Label(root7, image = image_3, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root7)
    frame.pack()
    e3=tkinter.Entry(root7)
    e3.place(x=170,y=130, height = 35)
    image_4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sup.png', master = root7)
    b1=Button(root7,image = image_4,command=result_course_name)
    b1.place(x=150,y=200)
    root7.mainloop()
def result_course_name():
    global e3
    root8=Tk()
    root8.geometry("800x700")
    root8.resizable(False, False)
    image_16 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\scs.png', master = root8)
    background16 = Label(root8, image= image_16, bd = 0)
    background16.image = image_16
    background16.place(x = 0, y = 0)
    frame=Frame(root8)
    frame.pack()
    entry= e3.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where course_name =%s", (entry_0,))
    mydata = mycursor.fetchall()
    text = tk.Text(root8,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root8,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
   
def  all_courses():
    root9=Tk()
    root9.geometry("800x700")
    root9.resizable(False, False)
    image_15 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\allc.png', master = root9)
    background15 = Label(root9, image= image_15)
    background15.image = image_15
    background15.place(x = 0, y = 0)
    frame=Frame(root9)
    frame.pack()
    mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
    mydata = mycursor.fetchall()
    text = tk.Text(root9,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root9,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')

def writeReview():
    root10 = Tk()
    root10.geometry("800x700")
    root10.resizable(False, False)
    image_2 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\writeReview.png', master = root10)
    background1 = Label(root10, image = image_2, bd = 0)
    background1.place(x = 0, y = 0)
    img4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\lh.png', master = root10)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\gm.png', master = root10)
    img6 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\je.png', master = root10)
    img7 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\fl.png', master = root10)
    img8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\an.png', master = root10)
    luis=Button(root10,image = img4, command= choice_luis)
    german=Button(root10,image = img5, command= choice_german)
    jerry=Button(root10,image = img6,command=choice_jerry)
    frank=Button(root10,image = img7,command=choice_frank)
    add_new=Button(root10,image = img8,command= write_new)
    luis.place(x= 50, y = 280)
    german.place(x = 300, y = 280)
    jerry.place(x = 550, y = 280)
    frank.place(x = 180, y = 430 )
    add_new.place(x = 450, y = 430)
    frame=Frame(root10)
    frame.pack()
    root10.mainloop()
    
def choice_luis():
    global e4
    root11=tk.Tk()
    root11.geometry("610x500")
    root11.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\wcfl.png', master = root11)
    background1 = Label(root11, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root11)
    frame.pack()
    e4=tk.Text(root11, font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD)
    scroll_bar = Scrollbar(root11,command=e4.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    e4['yscrollcommand'] = scroll_bar.set
    e4.place(x = 10, y = 180, width = 570, height = 200)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sup.png', master = root11)
    b1=Button(root11,image = img5,command=choice_luis_review)
    b1.place(x=180, y = 400)
    root11.mainloop()
def choice_luis_review():
    global e4
    root12=Tk()
    root12.geometry("510x400")
    root12.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\yourReview.png', master = root12)
    background1 = Label(root12, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root12)
    frame.pack()
    entry= e4.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,1)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    text = tk.Text(root12,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root12,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 10, y = 120, width = 480, height = 200)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
    root12.mainloop()

def choice_german():
    global e5
    root13=tk.Tk()
    root13.geometry("610x500")
    root13.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\wcfg.png', master = root13)
    background1 = Label(root13, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root13)
    frame.pack()
    e5=tk.Text(root13, font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD)
    scroll_bar = Scrollbar(root13,command=e5.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    e5['yscrollcommand'] = scroll_bar.set
    e5.place(x = 10, y = 180, width = 570, height = 200)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sup.png', master = root13)
    b1=Button(root13,image = img5,command=choice_german_review)
    b1.place(x=180, y = 400)
    root13.mainloop()
def choice_german_review():
    global e5
    root14=Tk()
    root14.geometry("510x400")
    root14.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\yourReview.png', master = root14)
    background1 = Label(root14, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root14)
    frame.pack()
    entry= e5.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,2)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    text = tk.Text(root14,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root14,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 10, y = 120, width = 480, height = 200)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
    root14.mainloop()

def choice_jerry():
    global e6
    root15=tk.Tk()
    root15.geometry("610x500")
    root15.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\wcfj.png', master = root15)
    background1 = Label(root15, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root15)
    frame.pack()
    e6=tk.Text(root15,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD)
    scroll_bar = Scrollbar(root15,command=e6.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    e6['yscrollcommand'] = scroll_bar.set
    e6.place(x = 10, y = 180, width = 570, height = 200)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sup.png', master = root15)
    b1=Button(root15,image = img5,command=choice_jerry_review)
    b1.place(x=180, y = 400)
    root15.mainloop()
def choice_jerry_review():
    global e6
    root16=Tk()
    root16.geometry("510x400")
    root16.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\yourReview.png', master = root16)
    background1 = Label(root16, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root16)
    frame.pack()
    entry= e6.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,3)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    text = tk.Text(root16,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root16,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 10, y = 120, width = 480, height = 200)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
    root16.mainloop()

def choice_frank():
    global e7
    root17=tk.Tk()
    root17.geometry("610x500")
    root17.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\wcff.png', master = root17)
    background1 = Label(root17, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root17)
    frame.pack()
    e7=tk.Text(root17,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD)
    scroll_bar = Scrollbar(root17,command=e7.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    e7['yscrollcommand'] = scroll_bar.set
    e7.place(x = 10, y = 180, width = 570, height = 200)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sup.png', master = root17)
    b1=Button(root17,image = img5,command=choice_frank_review)
    b1.place(x=180, y = 400)
    root17.mainloop()
def choice_frank_review():
    global e7
    root18=Tk()
    root18.geometry("510x400")
    root18.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\yourReview.png', master = root18)
    background1 = Label(root18, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root18)
    frame.pack()
    entry= e7.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,4)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    text = tk.Text(root18,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root18,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 10, y = 120, width = 480, height = 200)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
    root18.mainloop()

def write_new():

    global mydata
    f = []
    c = []
    r = []
    root18=tk.Tk()
    root18.geometry("800x1200")
    root18.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\newReviewPerson.png', master = root18)
    background1 = Label(root18, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root18)
    frame.pack()

    name=tkinter.Entry(root18)
    name.place(x=230,y=150, height = 35, width = 230)
    entry_name= name.get()
    entry_name_string = str(entry_name)
    f.append(entry_name_string)

    lname=tkinter.Entry(root18)
    lname.place(x=230,y=220, height = 35, width = 230)
    entry_lname= lname.get()
    entry_lname_string = str(entry_lname)
    f.append(entry_lname_string)
    cont_faculty = (f)
    sql_faculty = "INSERT INTO faculty (faculty_name, faculty_lastname) VALUES (%s,%s)"
    mycursor.execute(sql_faculty,cont_faculty)
    db.commit()
    last_digit = mycursor.lastrowid

    course=tkinter.Entry(root18)
    course.place(x=230,y=290, height = 35, width = 230)
    entry_course= course.get()
    entry_course_string = str(entry_course)
    c.append(entry_course_string)


    data = IntVar()
    course_number=tkinter.Entry(root18, textvariable = data)
    course_number.place(x=230,y=360, height = 35, width = 230)
    entry_course_number= course_number.get()
    c.append(entry_course_number)


    data2 = IntVar()
    credit=tkinter.Entry(root18, textvariable = data2)
    credit.place(x=230,y=430, height = 35, width = 230)
    entry_credit= credit.get()
    c.append(entry_credit)
    c.append(last_digit)

    cont_course = (c)
    sql_course = "INSERT INTO course (course_name, course_number, credits, faculty_id) VALUES (%s,%s,%s,%s)"
    mycursor.execute(sql_course,cont_course)
    db.commit()

    e6=tk.Text(root18,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD)
    scroll_bar = Scrollbar(root18,command=e6.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    e6['yscrollcommand'] = scroll_bar.set
    e6.place(x = 10, y = 180, width = 570, height = 200)
    
    
    entry= e7.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit_r = mycursor.lastrowid
    r.append(last_digit_r)
    r.append(last_digit)
    cont_r = (r)
    sql_r = "INSERT INTO reviews_has_faculty VALUES (%s,%s)"
    mycursor.execute(sql_r, cont_r)
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit_r,))
    mydata = mycursor.fetchall()


def print_result():
    for row in mydata:
        print(row)
    return 

root=Tk()
root.title('Rate my Professor')
root.geometry("800x700")
root.resizable(False, False)
image_1 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\byui.png')
background = Label(root, image = image_1, bd = 0)
background.place(x = 0, y = 0)
img1 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sp1.png')
img2 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\sc1.png')
img3 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\images\\wr1.png')
b1=Button(root, image = img1,command=searchProfessor, borderwidth = 0)
b2=Button(root,image = img2,command=searchCourse,borderwidth = 0)
b3=Button(root,image = img3,command=writeReview, borderwidth = 0)
b1.pack(side=LEFT,padx=(50,25), pady = (300,0))
b2.pack(side=LEFT,padx=25, pady = (300,0))
b3.pack(side=LEFT,padx=25, pady = (300,0))
frame=Frame(root)
frame.pack()
root.mainloop()
    