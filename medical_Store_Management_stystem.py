import pymysql
from tkinter import *
import tkinter as tk
import tkinter.messagebox
class project:
       def __init__(self, master):
         self.master = master
         self.frame = tk.Frame(self.master,bg="black")
         self.label1 = tk.Label(self.frame, text=" Welcome to S&A Pharmacy ", fg="black",bg="brown", font=('Times new roman', 23, 'bold'))
         self.label1.grid(row=1, column=1)
         self.button1 = tk.Button(self.frame, text='Login', width=17, command=self.new_window, fg="green",bg="silver",font=('Ariel', 16, 'bold'))
         self.button1.grid(row=5, column=1, padx=20, pady=20)
        
         self.frame.grid()
         
       
       def new_window(self):
          
          self.newWindow = tk.Toplevel(self.master)
          self.app = login(self.newWindow)
          


#####################################
class login:
     
    def __init__(self, master):
        
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.label2=tk.Label(self.frame, text="Login Details",fg="black",bg="silver", font=('Times new roman', 20, 'bold'))
        self.label2.grid(sticky="nsew",column=1)
        self.label2=tk.Label(self.frame, text="Username", fg="white",bg="black",font=('Verdena', 14, 'bold',))
        self.label2.grid(row=3)
        self.label3=tk.Label(self.frame, text="Password", fg="white",bg="black",font=('Verdena', 14, 'bold',))
        self.label3.grid(row=5)
        self.entry1=tk.Entry(self.frame)
        self.entry1.grid(row=3,column=1,padx=10,pady=10)
        self.entry2=tk.Entry(self.frame,show='*')
        
        self.entry2.grid(row=5,column=1,padx=10,pady=10)
        self.button2=tk.Button(self.frame,text='Enter',width=8,fg="green",bg="silver",font=('Ariel', 11, 'bold'),command=self.new_window1)
        self.button2.grid()
        
        self.frame.configure(background = 'black')
        self.frame.grid()

    def new_window1(self):
        
        username=self.entry1.get()
        password=self.entry2.get()
        
        
        x=username=="shamraiz",password=="12345"
        
        if all(x):
               self.newWindow = tk.Toplevel(self.master)
               self.app = Menu(self.newWindow)
        else:
               tkinter.messagebox.showinfo('Warning','Please insert correct details.')
        
            
                
    
        

######################################
class Menu:
    def __init__(self, master):
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="MENU", fg="black",bg="PowderBlue", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.button3=tk.Button(self.frame,text='Add Stock',width=15, command=self.new_window2, fg="white",bg="grey",font=('Ariel', 18, 'bold',))
        self.button3.grid(row=3, column=1, padx=15, pady=15)
        self.button4=tk.Button(self.frame,text='Search Stock',width=15, command=self.new_window3, fg="black",bg="grey",font=('Ariel', 18, 'bold',))
        self.button4.grid(row=5, column=1, padx=15, pady=15)
        self.button5=tk.Button(self.frame,text='Update Stock',width=15, command=self.new_window4, fg="black",bg="silver",font=('ariel', 18, 'bold',))
        self.button5.grid(row=7, column=1, padx=15, pady=15)
        self.button6=tk.Button(self.frame,text='Delete Stock',width=15, command=self.new_window5, fg="white",bg="grey",font=('ariel', 18, 'bold',))
        self.button6.grid(row=9, column=1, padx=15, pady=15)
        self.button7=tk.Button(self.frame,text='Buy',width=15, command=self.new_window00, fg="white",bg="POWDERBLUE",font=('ariel', 18, 'bold',))
        self.button7.grid(row=11, column=1, padx=15, pady=15)
        
        self.frame.configure(background = 'black')
        self.frame.grid()
        
    def new_window2(self):
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = Add_Stock(self.newWindow)
        
    def new_window3(self):
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = Search_Stock(self.newWindow)
        
    def new_window4(self):
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = Update_Stock(self.newWindow)
        
    def new_window5(self):
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = Delete_Stock(self.newWindow)
    def new_window00(self):
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = Buy(self.newWindow)
###########################################
class Add_Stock:
    def __init__(self, master):
        root.withdraw()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="ENTER STOCK DETAILS", fg="white",bg="BLUE", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.label4=tk.Label(self.frame,text="ID", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label4.grid(row=3)
       
        self.label5=tk.Label(self.frame,text="Name", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label5.grid(row=5)
       
        self.label6=tk.Label(self.frame,text="Price", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label6.grid(row=7)
       
        self.label7=tk.Label(self.frame,text="Exp.date", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label7.grid(row=9)
        
        self.label8=tk.Label(self.frame,text="Company", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label8.grid(row=11)
        
        self.label9=tk.Label(self.frame,text="Amount", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label9.grid(row=13)
        self.label10=tk.Label(self.frame,text="Quantity", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label10.grid(row=15)

        self.entry3=tk.Entry(self.frame)
        self.entry3.grid(row=3,column=1, padx=10, pady=10)
        
        self.entry4=tk.Entry(self.frame)
        self.entry4.grid(row=5,column=1, padx=10, pady=10)
        self.entry5=tk.Entry(self.frame)
        self.entry5.grid(row=7,column=1, padx=10, pady=10)
        self.entry6=tk.Entry(self.frame)
        self.entry6.grid(row=9,column=1, padx=10, pady=10)
        self.entry7=tk.Entry(self.frame)
        self.entry7.grid(row=11,column=1, padx=10, pady=10)
        self.entry8=tk.Entry(self.frame)
        self.entry8.grid(row=13,column=1, padx=10, pady=10)
        self.entry9=tk.Entry(self.frame)
        self.entry9.grid(row=15,column=1, padx=10, pady=10)
        
        self.button1=tk.Button(self.frame,text='Add',command=self.new_window,fg="white",bg="POWDERBLUE",font=('Comic Sans MSrial', 11, 'bold'))
        self.button1.grid(row=17,column=1)
        
        self.frame.configure(background = 'black')
        self.frame.grid()
    def new_window(self):
        a=self.entry3.get()
        b=self.entry4.get()
        c=self.entry5.get()
        d=self.entry6.get()
        e=self.entry7.get()
        f=self.entry8.get()
        g=self.entry9.get()
        db = pymysql.connect("localhost","shamraiz","12345","shamdb")
        cursor = db.cursor()
        sql = ("""INSERT INTO shamtb(id, name, price, Edate, company, amount,quantity) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(a,b,c,d,e,f,int(g)))
        try:
            cursor.execute(*sql)
            db.commit()
        except:
            db.rollback()
            db.close()
        
    

            
###########################################
class Search_Stock:
    def __init__(self, master):
        root.withdraw()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="SEARCH", fg="white",bg="BLUE", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.label4=tk.Label(self.frame,text="ID", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label4.grid(row=3)
        self.Entry6 = tk.Entry(self.frame)
        self.Entry6.grid(row=3, column=1, padx=10, pady=10)
        self.button2=tk.Button(self.frame,text='Search',fg="white",bg="POWDERBLUE",font=('Comic Sans MSrial', 11, 'bold'),command=self.new_window6)
        self.button2.grid(row=5,column=1,padx=10,pady=10)
        
        self.frame.configure(background = 'black')
        self.frame.grid()
        
    def new_window6(self):  
        global u
        global v
        global w
        global x
        global y
        global z
        global z1
        u=0
        m=self.Entry6.get()
        db = pymysql.connect("localhost","shamraiz","12345","shamdb")
        cursor = db.cursor()
        sql = "SELECT * FROM shamtb WHERE id = '%s'" % (m)
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           for row in results:
              u = row[0]
              v = row[1]
              w = row[2]
              x = row[3]
              y = row[4]
              z = row[5]
              z1 = row[6]
        except:
           print ("Error: unable to fecth data")
           db.close()
        if(m==u):
               self.newWindow = tk.Toplevel(self.master)
               self.app = Search(self.newWindow)
        else:
               tkinter.messagebox.showinfo('Warning','Please insert a valid ID.')
############
class Search:
   def __init__(self, master):
        root.withdraw()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="SEARCH DETAILS ", fg="white",bg="BLUE", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.label4=tk.Label(self.frame,text="ID", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label4.grid(row=3)
       
        self.label5=tk.Label(self.frame,text="Name", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label5.grid(row=5)
       
        self.label6=tk.Label(self.frame,text="Price", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label6.grid(row=7)
       
        self.label7=tk.Label(self.frame,text="Exp.date", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label7.grid(row=9)
        
        self.label8=tk.Label(self.frame,text="Company", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label8.grid(row=11)
        
        self.label9=tk.Label(self.frame,text="Amount", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label9.grid(row=13)
        self.label10=tk.Label(self.frame,text="Quantity", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label10.grid(row=15)
        

        self.entry3=tk.Entry(self.frame)
        self.entry3.grid(row=3,column=1, padx=10, pady=10)
        self.entry3.insert(END, u)
        self.entry4=tk.Entry(self.frame)
        self.entry4.grid(row=5,column=1, padx=10, pady=10)
        self.entry4.insert(END, v)
        self.entry5=tk.Entry(self.frame)
        self.entry5.grid(row=7,column=1, padx=10, pady=10)
        self.entry5.insert(END, w)
        self.entry6=tk.Entry(self.frame)
        self.entry6.grid(row=9,column=1, padx=10, pady=10)
        self.entry6.insert(END, x)
        self.entry7=tk.Entry(self.frame)
        self.entry7.grid(row=11,column=1, padx=10, pady=10)
        self.entry7.insert(END, y)
        self.entry8=tk.Entry(self.frame)
        self.entry8.grid(row=13,column=1, padx=10, pady=10)
        self.entry8.insert(END, z)
        self.entry9=tk.Entry(self.frame)
        self.entry9.grid(row=15,column=1, padx=10, pady=10)
        self.entry9.insert(END, z1)
        
        
        self.frame.configure(background = 'black')
        self.frame.grid()


    
    
###########################################
class Update_Stock:
    def __init__(self, master):
        root.withdraw()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="Update", fg="white",bg="BLUE", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.label4=tk.Label(self.frame,text="ID", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label4.grid(row=3)
        self.Entry6 = tk.Entry(self.frame)
        self.Entry6.grid(row=3, column=1, padx=10, pady=10)
        self.button2=tk.Button(self.frame,text='Update',fg="white",bg="POWDERBLUE",font=('Comic Sans MSrial', 11, 'bold'),command=self.new_window7)
        self.button2.grid(row=5,column=1,padx=10,pady=10)
        
        self.frame.configure(background = 'black')
        self.frame.grid()
        
    def new_window7(self):
        global o
        global p
        global q
        global r
        global s
        global t
        global u
        o=0
        m=self.Entry6.get()
        db = pymysql.connect("localhost","shamraiz","12345","shamdb")
        cursor = db.cursor()
        sql = "SELECT * FROM shamtb WHERE id = '%s'" % (m)
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           for row in results:
              o = row[0]
              p = row[1]
              q = row[2]
              r = row[3]
              s = row[4]
              t = row[5]
              u = row[6]
        except:
           print ("Error: unable to fecth data")
           db.close()
        if(m==o):
               self.newWindow = tk.Toplevel(self.master)
               self.app = Update(self.newWindow)
        else:
               tkinter.messagebox.showinfo('Warning','Please insert a valid ID.')
        
        
########################
class Update:
    def __init__(self, master):
        root.withdraw()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="UPDATE DETAILS", fg="white",bg="BLUE", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.label4=tk.Label(self.frame,text="ID", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label4.grid(row=3)
       
        self.label5=tk.Label(self.frame,text="Name", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label5.grid(row=5)
       
        self.label6=tk.Label(self.frame,text="Price", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label6.grid(row=7)
       
        self.label7=tk.Label(self.frame,text="Exp.date", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label7.grid(row=9)
        
        self.label8=tk.Label(self.frame,text="Company", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label8.grid(row=11)
        
        self.label9=tk.Label(self.frame,text="Amount", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label9.grid(row=13)
        self.label10=tk.Label(self.frame,text="Quantity", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label10.grid(row=15)

        self.entry3=tk.Entry(self.frame)
        self.entry3.grid(row=3,column=1, padx=10, pady=10)
        self.entry3.insert(END, o)
        self.entry4=tk.Entry(self.frame)
        self.entry4.grid(row=5,column=1, padx=10, pady=10)
        self.entry4.insert(END, p)
        self.entry5=tk.Entry(self.frame)
        self.entry5.grid(row=7,column=1, padx=10, pady=10)
        self.entry5.insert(END, q)
        self.entry6=tk.Entry(self.frame)
        self.entry6.grid(row=9,column=1, padx=10, pady=10)
        self.entry6.insert(END, r)
        self.entry7=tk.Entry(self.frame)
        self.entry7.grid(row=11,column=1, padx=10, pady=10)
        self.entry7.insert(END, s)
        self.entry8=tk.Entry(self.frame)
        self.entry8.grid(row=13,column=1, padx=10, pady=10)
        self.entry8.insert(END, t)
        self.entry9=tk.Entry(self.frame)
        self.entry9.grid(row=15,column=1, padx=10, pady=10)
        self.entry9.insert(END, u)
        

        self.button1=tk.Button(self.frame,text='Update', fg="white",bg="POWDERBLUE",font=('Comic Sans MSrial', 11, 'bold'),command=self.new_window)
        self.button1.grid(row=17,column=1)
        
        
        self.frame.configure(background = 'black')
        self.frame.grid()
    def new_window(self):
        a=self.entry3.get()
        b=self.entry4.get()
        c=self.entry5.get()
        d=self.entry6.get()
        e=self.entry7.get()
        f=self.entry8.get()
        g=self.entry9.get()
        db = pymysql.connect("localhost","shamraiz","12345","shamdb")
        cursor = db.cursor()
        sql = "UPDATE shamtb SET id = '%s', name='%s', price ='%s', Edate= '%s', company ='%s', amount ='%s', quantity='%s' WHERE id = '%s'" % (a,b,c,d,e,f,int(g),a)
        try:
            tkinter.messagebox.showinfo('Alert','Updated.')
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()

    
###########################################
class Delete_Stock:
     def __init__(self, master):
        root.withdraw()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="DELETE", fg="white",bg="BLUE", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.label4=tk.Label(self.frame,text="ID", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label4.grid(row=3)
        self.Entry6 = tk.Entry(self.frame)
        self.Entry6.grid(row=3, column=1, padx=10, pady=10)
        self.button2=tk.Button(self.frame,text='Delete',fg="white",bg="POWDERBLUE",font=('Comic Sans MSrial', 11, 'bold'),command=self.new_window)
        self.button2.grid(row=5,column=1,padx=10,pady=10)
        
        self.frame.configure(background = 'black')
        self.frame.grid()
     def new_window(self):
        a=self.Entry6.get()
        db = pymysql.connect("localhost","shamraiz","12345","shamdb")
        cursor = db.cursor()
        sql = "DELETE FROM shamtb WHERE id = '%s'" % (a)
        try:
           cursor.execute(sql)
           db.commit()
           tkinter.messagebox.showinfo('Alert','Deleted.')
        except:
           db.rollback()
           db.close()

################################
class Buy:
    def __init__(self, master):
        root.withdraw()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label1 = tk.Label(self.frame, text="BUY", fg="white",bg="BLUE", font=('ARIEL', 27, 'bold'))
        self.label1.grid(sticky="nsew",column=1)
        self.label4=tk.Label(self.frame,text="ID", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label4.grid(row=3)
        self.label5=tk.Label(self.frame,text="Quantity", fg="white",bg="black",font=('Verdena', 15, 'bold',))
        self.label5.grid(row=5)
        self.Entry6 = tk.Entry(self.frame)
        self.Entry6.grid(row=3, column=1, padx=10, pady=10)
        self.Entry7 = tk.Entry(self.frame)
        self.Entry7.grid(row=5, column=1, padx=10, pady=10)
        
        self.button2=tk.Button(self.frame,text='Buy',fg="white",bg="POWDERBLUE",font=('Comic Sans MSrial', 11, 'bold'))
        self.button2.grid(row=7,column=1,padx=10,pady=10)
  
        self.frame.configure(background = 'black')
        self.frame.grid()
    

        a=self.Entry6.get()
        b= self.Entry7.get()
        db = pymysql.connect("localhost","shamraiz","12345","shamdb")
        cursor = db.cursor()
        sql = "SELECT * FROM shamtb WHERE id = '%s'" % (a)
        sql = "UPDATE SHAMTB SET quantity='%s' * WHERE id = '%s'" % (b,a)
        
        global k
        
        
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           for row in results:
              o = row[0]
              p = row[1]
              q = row[2]
              r = row[3]
              s = row[4]
              t = row[5]
              u = row[6]
              print (row[6])
        except:
           print ("Error: unable to fecth data")
           db.close()

        
##        if(b<=u):
##               k=u-x
##               print(k)
##               self.newWindow = tk.Toplevel(self.master)
##               self.app = Update1(self.newWindow)
               
       # else:
              # tkinter.messagebox.showinfo('Warning','Your entered quantity is more then available.')
#####################
class Update1:
       def __init__(self, master):
              root.withdraw()
              tkinter.messagebox.showinfo('Warning','Your entered quantity is more then available.')

   

               
               

              self.frame.configure(background = 'black')
              self.frame.grid()


root = tk.Tk()

root["bg"] = "grey"
root.title("S&A Pharmacy")
app = project(root)

root.mainloop()

