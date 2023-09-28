'''from tkinter import *
from tkinter import Tk
from tkinter import ttk
import pymysql
class emp:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x800')
        title1=Label(self.root,text='Dalai Restrurant',
                     font=('Broadway',40),bg='cyan',fg='magenta',bd=5,relief=RAISED)
        title1.pack(fill='x')

        self.rollnoVar = StringVar()
        self.firstnameVar = StringVar()
        self.lastnameVar = StringVar()
        self.emailidVar = StringVar()
        self.contactVar = StringVar()
        self.locVar = StringVar()
        self.instuteVar = StringVar()
        self.qualificationVar = StringVar()
        
        #creating frame
        dataentry= Frame(self.root , bg='green')
        dataentry.place(x=10,y=80,width=500,height=800 )


        # woking with frame
        
        #--------data entry frame---------------
        title2=Label(dataentry,text='Clint Entry',font=('Broadway',20),fg='white',relief=RAISED,bd=5,bg='red')
        title2.grid(row=0,columnspan=2,padx=100,pady=20)
        
        
        #Roll no:
        rollno= Label(dataentry,text='RollNo',font=('dubai',20),bg='green',fg='white')
        rollno.grid(row=1,column=0,padx=10,sticky='w')
        
        rollnoe=Entry(dataentry,font=('dubai',15),textvariable =self.rollnoVar )
        rollnoe.grid(row=1,column=1,sticky='e')
        # First name:
        firstname= Label(dataentry,text='First name',font=('dubai',20),bg='green',fg='white')
        firstname.grid(row=2,column=0,padx=10,sticky='w')
        
        firstnamee=Entry(dataentry,font=('dubai',15),textvariable =self.firstnameVar )
        firstnamee.grid(row=2,column=1,sticky='e')
        
        # Last name:
        lastname=Label(dataentry,text='Last name', font=('dubai',20),bg='green',fg='white')
        lastname.grid(row=3,column=0,sticky='w',padx=10)
        
        lastnamee=Entry(dataentry,font=('dubai',15),textvariable =self.lastnameVar )
        lastnamee.grid(row=3,column=1,sticky='e')        

        #Email Id:
        emailid=Label(dataentry,text='Emailid',font=('dubai',20 ),bg='green',fg='white')
        emailid.grid(row=4,column=0,sticky='w',padx=10)
        
        emailide=Entry(dataentry,font=('dubai',15),textvariable =self.emailidVar )
        emailide.grid(row=4,column=1,sticky='e',)

        #contact
        contact=Label(dataentry,text='Contact',font=('dubai',20),bg='green',fg='white')
        contact.grid(row=5,column=0,sticky='w',padx=10)

        contacte=Entry(dataentry,font=('dubai',15),textvariable =self.contactVar )
        contacte.grid(row=5,column=1,sticky='e')

        #location:
        loc=Label(dataentry,text='Location',font=('dubai',20),bg='green',fg='white')
        loc.grid(row=6,column=0,sticky='w',padx=10)

        loce=Entry(dataentry,font=('dubai',15),textvariable =self.locVar )
        loce.grid(row=6,column=1,sticky='e')
        #instute
        instute=Label(dataentry,text='Instute',font=('dubai',20),bg='green',fg='white')
        instute.grid(row=7,column=0,sticky='w',padx=10)

        instutee=Entry(dataentry,font=('dubai',15),textvariable =self.instuteVar )
        instutee.grid(row=7,column=1,sticky='e')
        #qualification:
        qalification=Label(dataentry,text='Qualification',font=('dubai',20),bg='green',fg='white')
        qalification.grid(row=8,column=0,padx=10,sticky='w')

        qalificatione=Entry(dataentry,font=('dubai',15),textvariable =self.qualificationVar )
        qalificatione.grid(row=8,column=1,sticky='e')

        # button frame
        btnframe=Frame(dataentry,bg='green',relief=RAISED,bd=5)
        btnframe.place(x=15,y=520, width=470,height=100)
        #add button
        addbtn=Button(btnframe,text='ADD',command=self.addingdata,bg='red',font=('dubai',15),fg='white',bd=5)
        addbtn.grid(row=0,column=0,pady=20,padx=10)
        #update button
        updatebtn=Button(btnframe,text='UPDATE',command=self.updatingdata,font=('dubai',15),bg='blue',fg='white',bd=5)
        updatebtn.grid(row=0,column=1,padx=10)
        #delete button
        deletebtn=Button(btnframe,text='DELETE',command=self.deletingdata,font=('dubai',15),bd=5,bg='magenta',fg='white')
        deletebtn.grid(row=0,column=2,padx=10)
        #clear button
        clearbtn=Button(btnframe,text='CLEAR',command=self.clearingdata,font=('dubai',15),bd=5,bg='brown',fg='white')
        clearbtn.grid(row=0,column=3,padx=10)

        # ----------data display frame------------------
        datadisplay=Frame(self.root,bg='green')
        datadisplay.place(x=520,y=80,width=970,height=800)

        title3=Label(datadisplay,text='datadisplay here',font=('Broadway',20),fg='white',relief=RAISED,bd=5,bg='red')
        title3.grid(row= 0,columnspan=2,padx=320,pady=20)

        tableframe=Frame(datadisplay,bd=5,relief=RAISED,bg='green')
        tableframe.place(x=20,y=70,width=920,height=550)

        self.studentinfo=ttk.Treeview(tableframe,height=450,columns=('rollno','firstname','lastname','emailid','contact','loc','instute','qualification'))
        self.studentinfo.heading('rollno',text='Roll No')
        self.studentinfo.heading('firstname',text='First Name')
        self.studentinfo.heading('lastname',text='Last Name')
        self.studentinfo.heading('emailid',text='Email Id')
        self.studentinfo.heading('contact',text='Contact')
        self.studentinfo.heading('loc',text='Location')
        self.studentinfo.heading('instute',text='Instute')
        self.studentinfo.heading('qualification',text='Qualification')


        # column adjustment:
        self.studentinfo.column('rollno',width=100,anchor='center')
        self.studentinfo.column('firstname',width=100,anchor='center')
        self.studentinfo.column('lastname',width=100,anchor='center')
        self.studentinfo.column('emailid',width=150,anchor='center')
        self.studentinfo.column('contact',width=150,anchor='center')
        self.studentinfo.column('loc',width=100,anchor='center')
        self.studentinfo.column('instute',width=100,anchor='center')
        self.studentinfo.column('qualification',width=100,anchor='center')

        
        self.studentinfo['show']='headings'
        self.fetchingdata()
        self.studentinfo.pack()

        self.studentinfo.bind('<ButtonRelease-1>',self.crusor)

        
    def addingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='prasan@7205',db='guiproject')
        c=connection.cursor()
        c.execute('insert into studentdata values (%s, %s, %s, %s, %s, %s, %s, %s)' ,
                 (
                     self.rollnoVar.get(),
                     self.firstnameVar.get(),
                     self.lastnameVar.get(),
                     self.emailidVar.get(),
                     self.contactVar.get(),
                     self.locVar.get(),
                     self.instuteVar.get(),
                     self.qualificationVar.get(),
                     ))
        connection.commit()
        self.fetchingdata() 
        self.clearingdata()
        connection.close()
    def clearingdata(self):
        self.rollnoVar.set(''),
        self.firstnameVar.set(''),
        self.lastnameVar.set(''),
        self.emailidVar.set(''),
        self.contactVar.set(''),
        self.locVar.set(''),
        self.instuteVar.set(''),
        self.qualificationVar.set(''),

    def fetchingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='prasan@7205',db='guiproject')
        c=connection.cursor()
        c.execute('select * from studentdata ')
        self.studentinfo.delete(*self.studentinfo.get_children())
        data=c.fetchall()
        for i in data:
            self.studentinfo.insert('',END,value=i)
        connection.commit()
        connection.close()
    #click to view
    def crusor(self,a):
        crusorrow=self.studentinfo.focus()
        content=self.studentinfo.item(crusorrow)
        row=content['values']
        self.rollnoVar.set(row[0])
        self.firstnameVar.set(row[1])
        self.lastnameVar.set(row[2])
        self.emailidVar.set(row[3])
        self.contactVar.set(row[4])
        self.locVar.set(row[5])
        self.instuteVar.set(row[6])
        self.qualificationVar.set(row[7])

    # updating
    def updatingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='prasan@7205',db='guiproject')
        c=connection.cursor()
        c.execute('update studentdata set firstname=%s, lastname=%s, emailid=%s, contact=%s, loc=%s, instute=%s, qualification=%s where rollno=%s',
                 (
                    self.firstnameVar.get(),
                    self.lastnameVar.get(),
                    self.lastnameVar.get(),
                    self.emailidVar.get(),
                    self.contactVar.get(),
                    self.locVar.get(),
                    self.instuteVar.get(),
                    self.qualificationVar.get()
                     ))
        connection.commit()
        self.fetchingdata()
        self.clearingdata()
        connection.close()


    #deleting data
    def deletingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='prasan@7205',db='guiproject')
        c=connection.cursor()
        c.execute('delete from studentdata where rollno=%s',self.rollnoVar.get())
        connection.commit()
        self.fetchingdata()
        self.clearingdata()
        connection.close()
root=Tk()
s=emp(root)





root.mainloop()
'''
'''
import requests
from bs4 import BeautifulSoup
# url="https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
url="https://www.google.com/search?q=bark&rlz=1C1RXQR_enIN1015IN1015&oq=bark&aqs=chrome..69i57j46i67i199i465i650j46i131i433i512j46i433i512j46i131i433i512j46i175i199i512j0i131i433i650j46i512j46i131i433i512j0i271.1001j0j15&sourceid=chrome&ie=UTF-8"
response=requests.get(url)
htmlcontent=response.content
soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup.find_all('a'))
# if want to get only href link then you can use this
# for i in soup.find_all('a'):
#     print(i.get('href'))

# if you want get all images then you can use this
# for image in soup.find_all('img'):
#     print(image.get('src'))
'''


















'''



import pandas as np
file_path='{download/participants_report_262694252566328660 (1)}'
df=np.read_json(file_path)
print(df)
'''


'''
import os
cwd=os.getcwd()
print(cwd)
'''
import pandas as np
import os
download='/Download/'
jsonfile='json'
json_file_name=os.path.join(download,jsonfile)
df=np.read_json(jsonfile,encodeing='utf-8')
print(df)
