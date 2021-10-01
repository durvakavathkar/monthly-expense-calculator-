from tkinter import *
from tkcalendar import Calendar
from csv import writer
import pandas as pd
from tkinter import ttk
from matplotlib import pyplot as plt
import csv
import matplotlib.pyplot as plt
import numpy as np
import os 


def save():
       error=""
       if name_entry.get()=="":
              error="Name cannot be empty"
       if income_entry.get()=="":
              erroe="Pls enter your income"
       if monthchoosen.get()=="":
              error="Pls select a valid month"
              
       if error=="":
              if os.path.isfile(name_entry.get()+'.csv')==True:
                     savelbl.config(text="Saved !")
              else:
                     header_list=["income","month","rent","Maintainance","Bills",
                                 "grocery","restaurant","transport","health","Insurance","loan","others"]
                     with open(name_entry.get()+'.csv', 'a',newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(header_list)
       else:
              savelbl.config(text=error )
                      
       
def get_bar():
       error=""
       if name_entry.get()=="":
              error="Pls enter your name"
       if error=="":
              data= pd.read_csv(name_entry.get()+".csv")
              Name_list = list(data["month"])
              print(Name_list)
              income=data.iloc[:,0].tolist()
              print(income)
              expenses=data.iloc[:,2:]
              
              
              
              total=0
              for i in expenses:
                     total=total+expenses[i]
                     exp=list(total)
              print(exp) 
                     
              
           
              plt.figure(figsize=[10,8])
             
              labels = Name_list
              income_list=income
              expense_list=exp
              X_axis = np.arange(len(labels))
              plt.bar(X_axis - 0.2, income_list, 0.4, label = 'Income')
              plt.bar(X_axis + 0.2, expense_list, 0.4, label = 'Expenses')
              plt.xticks(X_axis, labels)
              plt.xlabel("Months")
              plt.ylabel("Amont")
              plt.title("Your yearly Expense")
              plt.legend()
              plt.show()        
       
      
def homee():
       frame9.place_forget()
       frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)
       
def back_1():
       frame8.place_forget()
       frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)
       
       
       
            
              
       
       
       

def get_year():
       global name_entry
       frame1.place_forget()
       frame=Frame(root,bg="#e0baad")
       name=Label(frame,text="Username", bg="#e0baad", font=("Arial", 14)).place(relx=0.07,rely=0.1)
       name_entry = Entry(frame)
       name_entry.place(relx=0.47,rely=0.1)
       homebutton=Button(frame,text="next",font=("Arial",14),command=get_bar)
       homebutton.place(relx=0.3,rely=0.3)
       frame.place(relx=0.2,rely=0.2,relwidth=0.3,relheight=0.3)

       
       
#getting mothwise details and graph 
def get():
       global data
       global frame9
       error=""
       if name_entry.get()=="":
              error="Pls enter your name"
       if monthchoosen.get()=="":
              error="Pls enter the month"

       if error=="":
              
               if os.path.isfile(name_entry.get()+'.csv')==True:
                      df=pd.read_csv(name_entry.get()+".csv")
                      if monthchoosen.get() in df.values:
                             
                             frame8.place_forget()
                             frame9=Frame(root,bg="#cab6b3")
                             Label(frame9,text="Expense Analysis", bg="#cab6b3" ,font=("Arial", 14)).pack()
                             Label(frame9,text=monthchoosen.get(), bg="#cab6b3" , font=("Arial", 14)).place(relx=0.45,rely=0.1)
                             with open(name_entry.get()+".csv",'r') as f:
                                    data_list = list(csv.reader(f, delimiter=','))
                                    
                             for i in range (0, len(data_list)):
                                    if monthchoosen.get()in data_list[i][1]:
                                           data=(data_list[i])
                                           
                                           break
                             total = 0
                             expenses_list=data[2:]
                             integer_map = map(int, expenses_list)
                             exp_list = list(integer_map)
                             for ele in range(0, len(exp_list)):
                                    total = total + exp_list[ele]
                            
                             print(int(data[0])-total)
                             rent=Label(frame9,text="Rent",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.18)
                             Label(frame9,text=exp_list[0],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.18)
                             
                             maintenance=Label(frame9,text="Maintenance:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.23)
                             Label(frame9,text=exp_list[1],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.23)

                             bills=Label(frame9,text="Bills:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.28)
                             Label(frame9,text=exp_list[2],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.28)

                             groceries=Label(frame9,text="Groceries:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.33)
                             Label(frame9,text=exp_list[3],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.33)

                             restaurant=Label(frame9,text="restaurant:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.38)
                             Label(frame9,text=exp_list[4],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.38)

                             transport=Label(frame9,text="Transport:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.43)
                             Label(frame9,text=exp_list[5],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.43)

                             health_care=Label(frame9,text="Health_care:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.48)
                             Label(frame9,text=exp_list[6],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.48)

                             Insurance=Label(frame9,text="Insurance:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.53)
                             Label(frame9,text=exp_list[7] ,bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.53)

                             Loan=Label(frame9,text="Loan:",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.58)
                             Label(frame9,text=exp_list[8],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.58)

                             Others=Label(frame9,text="Other(s):",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.63)
                             Label(frame9,text=exp_list[9],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.63)

                             line=Label(frame9,text="___________",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.25,rely=0.68)
                             Label(frame9,text="____________",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.68)

                             Others=Label(frame9,text="Total",font=("Arial", 10)).place(relx=0.3,rely=0.73)
                             Label(frame9,text=total,font=("Arial", 10)).place(relx=0.6,rely=0.73)

                             income=Label(frame9,text="Income",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.2,rely=0.78)
                             Label(frame9,text=data[0],bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.3,rely=0.78)
                             balance=Label(frame9,text="Balance",bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.4,rely=0.78)
                             Label(frame9,text=(int(data[0])-total),bg="#cab6b3" ,font=("Arial", 10)).place(relx=0.6,rely=0.78)
                             homebutton=Button(frame9,text="Home",font=("Arial",14),command=homee)
                             homebutton.place(relx=0.4,rely=0.85)
                             frame9.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.8)

                             #plotting graph
                             plt.figure(figsize=[10,8])
                             labels = ['Rent', 'maintenance', 'bills', 'grocery','restaurant','transport',
                                       'health','loan','insurance','others']
                             sizes=exp_list
                             
                             
                             plt.title(monthchoosen.get())
                             plt.pie(sizes,  labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
                             plt.legend()

                             plt.show()
                      else:
                            status.config(text="No details found for this month")
               else:
                      status.config(text="file doesn't exist")
       else:
              status.config(text=error)
       
#month_wise graph
def get_month():
       global frame8
       global name_entry
       global monthchoosen
       global status
     
               
       frame1.place_forget()
       frame8=Frame(root,bg="#f9c6a2")
       name=Label(frame8,text="Username", bg="#f9c6a2", font=("Arial", 14)).place(relx=0.1,rely=0.1)
       name_entry = Entry(frame8,width=20)
       name_entry.place(relx=0.36,rely=0.1)

       monthchoosen=Label(frame8, text = "Select the Month :",bg="#f9c6a2",
       font = ("Arial", 14)).place(relx=0.1,rely=0.3)
  

       n =StringVar()
       monthchoosen =ttk.Combobox(frame8, width = 27, textvariable = n)
  

       monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
       monthchoosen.place(relx=0.3,rely=0.4)
       monthchoosen.current()
       incomebutton=Button(frame8,text=" graph ",font=("Arial",14),command=get)
       incomebutton.place(relx=0.1 ,rely=0.6)
       incomebutton=Button(frame8,text="Back ",font=("Arial",14),command=back_1)
       incomebutton.place(relx=0.3 ,rely=0.6)
       status=Label(frame8,bg="#f9c6a2")
       status.place(relx=0.1,rely=0.7)
              
       frame8.place(relx=0.2,rely=0.2,relwidth=0.5,relheight=0.5)
       
       

     

def home():
       frame4.place_forget()
       frame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
       


def get_graph():
       try:
              global data
              global frame4
              frame3.place_forget()
              frame4=Frame(root,bg="#fee9c8")
              frame4.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
              Label(frame4,text="Expense Analysis", bg="#fee9c8", font=("Broadway", 14)).pack()
              Label(frame4,text=monthchoosen.get(),bg="#fee9c8",  font=("Arial", 14)).place(relx=0.45,rely=0.1)
              with open(name_entry.get()+".csv",'r') as f:
                     data_list = list(csv.reader(f, delimiter=','))
              for i in range (0, len(data_list)):
                     if monthchoosen.get()in data_list[i][1]:
                            data=(data_list[i])
                            break
              total = 0
              expenses_list=data[2:]
              integer_map = map(int, expenses_list)
              exp_list = list(integer_map)
              
              for ele in range(0, len(exp_list)):
                     total = total + exp_list[ele]
                     

              rent=Label(frame4,text="Rent",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.18)
              Label(frame4,text=exp_list[0],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.18)

              maintenance=Label(frame4,text="Maintenance:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.23)
              Label(frame4,text=exp_list[1],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.23)

              bills=Label(frame4,text="Bills:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.28)
              Label(frame4,text=exp_list[2],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.28)

              groceries=Label(frame4,text="Groceries:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.33)
              Label(frame4,text=exp_list[3],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.33)

              restaurant=Label(frame4,text="restaurant:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.38)
              Label(frame4,text=exp_list[4],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.38)

              transport=Label(frame4,text="Transport:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.43)
              Label(frame4,text=exp_list[5],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.43)

              health_care=Label(frame4,text="Health_care:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.48)
              Label(frame4,text=exp_list[6],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.48)

              Insurance=Label(frame4,text="Insurance:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.53)
              Label(frame4,text=exp_list[7],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.53)

              Loan=Label(frame4,text="Loan:",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.58)
              Label(frame4,text=exp_list[8],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.58)

              Others=Label(frame4,text="Other(s):",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.63)
              Label(frame4,text=exp_list[9],bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.63)

              line=Label(frame4,text="___________",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.68)
              Label(frame4,text="____________",bg="#fee9c8",font=("Arial", 10)).place(relx=0.55,rely=0.68)

              Others=Label(frame4,text="Total",bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.73)
              Label(frame4,text=total,bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.73)

              income=Label(frame4,text="Income",bg="#fee9c8",font=("Arial", 10)).place(relx=0.2,rely=0.78)
              Label(frame4,text=data[0],bg="#fee9c8",font=("Arial", 10)).place(relx=0.3,rely=0.78)

              balance=Label(frame4,text="Balance",bg="#fee9c8",font=("Arial", 10)).place(relx=0.5,rely=0.78)
              Label(frame4,text=(int(data[0])-total),bg="#fee9c8",font=("Arial", 10)).place(relx=0.6,rely=0.78)

              homebutton=Button(frame4,text="Home",font=("Arial",14),command=home)
              homebutton.place(relx=0.4,rely=0.85)

              #plotting graph 

              plt.figure(figsize=[10,8])
              labels = ['Rent', 'maintenance', 'bills', 'grocery','restaurant','transport',
                 'health','loan','insurance','others']
              sizes=exp_list
              
              plt.title(monthchoosen.get())
              plt.pie(sizes,  labels=labels,autopct='%1.1f%%', shadow=False, startangle=140)
              plt.legend()
              plt.show()
      
       except Exception:
              print("An exception occured")
       
# saving the income month and expenses details in csv file 
def save1():
       try:
              List=[income_entry.get(),monthchoosen.get(),rent_entry.get(), maintain_entry.get(), bill_entry.get(),
                  grocery_entry.get(),rest_entry.get(),transport_entry.get(),
                  health_entry.get(),loan_entry.get(),insurance_entry.get(),other_entry.get()]
              print(List)
              with open(name_entry.get()+'.csv', 'a',newline='') as file:
                     writer = csv.writer(file, delimiter=',')
                     writer.writerow(List)
              text.config(text="Saved successfully")

       except Exception:
              text.config(text="Error while saving")

def back():
       frame3.place_forget()
       frame2.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
        
def go_back():
       frame2.place_forget()
       frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)
        
        
#getting expenses
       #Frame 3
def exp_get():
       global frame3
              
       global text
       global rent_entry
       global maintain_entry
       global bill_entry
       global grocery_entry
       global rest_entry
       global transport_entry
       global health_entry
       global loan_entry
       global insurance_entry
       global other_entry
      
       error=""
       if name_entry.get()=="":
              error="Name cannot be blank"
       if income_entry.get()=="":
              error="Income cannot be blank"
       if monthchoosen.get()=="":
              error="Month cannot be blank"
       if error=="":
              if os.path.isfile(name_entry.get()+'.csv')==True:
                     df=pd.read_csv(name_entry.get()+".csv")
                     if monthchoosen.get() in df.values:
                             savelbl.config(text="details for this month already exists")
                     else:
                            frame2.place_forget()
                            frame3=Frame(root,bg="#eec4c0")
                            Label(frame3,text="Enter your expenses",bg="#eec4c0", font=("Broadway", 14)).pack()

                            Label(frame3,text=monthchoosen.get(),bg="#eec4c0", font=("Broadway", 14)).place(relx=0.44 ,rely=0.1)
                            
                            Label(frame3,text="Rent",bg="#eec4c0", font=("Arial", 14)).place(relx=0.1,rely=0.2)
                            rent_entry = Entry(frame3)
                            rent_entry.insert(0, "0")
                            rent_entry.place(relx=0.2,rely=0.2)

                            Label(frame3,text="Maintenance",bg="#eec4c0",  font=("Arial", 14)).place(relx=0.45,rely=0.2)
                            maintain_entry = Entry(frame3)
                            maintain_entry.insert(0, "0")
                            maintain_entry.place(relx=0.64,rely=0.2)

                            Label(frame3,text="Bills ",bg="#eec4c0",  font=("Arial", 14)).place(relx=0.1,rely=0.3)
                            bill_entry = Entry(frame3)
                            bill_entry.insert(0, "0")
                            bill_entry.place(relx=0.2,rely=0.3)

                            Label(frame3,text="grocery", bg="#eec4c0", font=("Arial", 14)).place(relx=0.08,rely=0.4)
                            grocery_entry = Entry(frame3)
                            grocery_entry.insert(0, "0")
                            grocery_entry.place(relx=0.2,rely=0.4)

                            Label(frame3,text="Restaurant",bg="#eec4c0",  font=("Arial", 14)).place(relx=0.45,rely=0.3)
                            rest_entry = Entry(frame3)
                            rest_entry.insert(0, "0")
                            rest_entry.place(relx=0.64,rely=0.3)

                            Label(frame3,text="transportation",bg="#eec4c0",  font=("Arial", 14)).place(relx=0.45,rely=0.4)
                            transport_entry = Entry(frame3)
                            transport_entry.insert(0, "0")
                            transport_entry.place(relx=0.64,rely=0.4)

                            Label(frame3,text="Health care", bg="#eec4c0", font=("Arial", 14)).place(relx=0.45,rely=0.5)
                            health_entry = Entry(frame3)
                            health_entry.insert(0, "0")
                            health_entry.place(relx=0.64,rely=0.5)

                            Label(frame3,text="Loans",bg="#eec4c0",  font=("Arial", 14)).place(relx=0.1,rely=0.5)
                            loan_entry = Entry(frame3)
                            loan_entry.insert(0, "0")
                            loan_entry.place(relx=0.2,rely=0.5)

                            Label(frame3,text="Insurance",bg="#eec4c0",  font=("Arial", 14)).place(relx=0.06,rely=0.6)
                            insurance_entry = Entry(frame3,width=20)
                            insurance_entry.insert(0, "0")
                            insurance_entry.place(relx=0.2,rely=0.6)

                            Label(frame3,text="other(s)",bg="#eec4c0",  font=("Arial", 14)).place(relx=0.45,rely=0.6)
                            other_entry = Entry(frame3)
                            other_entry.insert(0, "0")
                            other_entry.place(relx=0.64,rely=0.6)

                            incomebutton=Button(frame3,text="save ",font=("Arial",14),command=save1)
                            incomebutton.place(relx=0.1 ,rely=0.8)

                            

                            expensebutton=Button(frame3,text="next",font=("Arial",14),command=get_graph)
                            expensebutton.place(relx=0.2,rely=0.8)

                            text=Label(frame3,bg="#eec4c0")
                            text.place(relx=0.1,rely=0.9)

                            frame3.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
       else:
              savelbl.config(text=error )
              


       

#income and expense details
  #frame2      

def getdata():
       global frame2
       global name_entry
       global income_entry
       global monthchoosen
       global savelbl
      
       frame1.place_forget()
       frame2=Frame(root,bg='#d5bbb4')

       Label(frame2,text="Enter your income details",bg="#d5bbb4" ,font=("Broadway", 14)).pack()

       name=Label(frame2,text="Username",bg="#d5bbb4",font=("Arial", 14)).place(relx=0.1,rely=0.1)
       name_entry = Entry(frame2,width=20)
       name_entry.place(relx=0.3,rely=0.1)

       income=Label(frame2,text="Income",bg="#d5bbb4" ,font=("Arial", 14)).place(relx=0.1,rely=0.2)
       income_entry = Entry(frame2)
       income_entry.place(relx=0.3,rely=0.2)

       month=Label(frame2, text = "Select the Month :",bg="#d5bbb4",
       font = ("Arial", 14)).place(relx=0.1,rely=0.3)
  

       n =StringVar()
       monthchoosen =ttk.Combobox(frame2, width = 27, textvariable = n)
  

       monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
       monthchoosen.place(relx=0.3,rely=0.4)
       monthchoosen.current()

       expensebutton=Button(frame2,text="Back",font=("Arial",14),command=go_back)
       expensebutton.place(relx=0.3,rely=0.6)

       expensebutton=Button(frame2,text="next",font=("Arial",14),command=exp_get)
       expensebutton.place(relx=0.5,rely=0.6)
       
       expensebutton=Button(frame2,text="save",font=("Arial",14),command=save)
       expensebutton.place(relx=0.1,rely=0.6)
       
       savelbl=Label(frame2,bg="#d5bbb4")
       savelbl.place(relx=0.1,rely=0.7)
      
       frame2.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)

      

#Main window created with frame1       
root=Tk()

#canvas
canvas=Canvas(root,height=800,width=800)
canvas.pack()
img = PhotoImage(file="bg.png")
label = Label(root,image=img)
label.place(relwidth=1, relheight=1)

#Frame1 on root
frame1=Frame(root,bg='#fce0c8')


title=Label(frame1,text="Expense calculator and visualizer",bg="#fce0c8", width="300", height="1",
font=("Broadway",16)).pack()

detailsbutton=Button(frame1,text="Income & Expenses ",bg="#df7b57",font=("Arial",14),command=getdata)
detailsbutton.place(relx=0.3 ,rely=0.2)

graphbutton=Button(frame1,text="Monthly graph",bg="#f29466",font=("Arial",14),command=get_month)
graphbutton.place(relx=0.37,rely=0.4)

graphbutton=Button(frame1,text="Yearly graph ",bg="#fdbc9b",font=("Arial",14),command=get_year)
graphbutton.place(relx=0.37,rely=0.6)

frame1.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)

root.mainloop()        


              


