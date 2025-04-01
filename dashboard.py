import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from  tkinter import messagebox
t=tkinter.Tk()
t.geometry('900x900')
recd=''
def showservicecentre():
    
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(a2,text='service center details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=200,y=5)
        cdi=[]
        def dest():
            cdi.clear()
            a2.destroy
        def filldatac():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select id from service_center"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            db.close()    
            
        def dest():
            t.destroy()
        def savedata():
            if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or len(e6.get())==0:
                
                
                messagebox.showerror('hii','please check all')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=int(e1.get())
                xb=e2.get()
                xc=e3.get()
                xd=e4.get()
                xe=e5.get()
                xf=e6.get()
                
                sql="insert into service_center values(%d,'%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            sql="select count(*)from service_center where id=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                 messagebox.showinfo('hii','already exit')
            db.close()
        l1=Label(a2,text='id',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldatac()
        e1['values']=cdi
        e1.place(x=450,y=60)
        l2=Label(a2,text='cname',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='email',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='phone',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l6=Label(a2,text='regno',bg='pink',font=('arial',20))
        l6.place(x=150,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        btn11=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn11.place(x=150,y=330)
        btn12=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn12.place(x=300,y=330)
        btn13=Button(a2,text='close',command=dest,fg='white',bg='black',font=('arial',15))
        btn13.place(x=470,y=330)
        t.mainloop()
        
         
        
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='service center details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select id from service_center"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()    
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=e6.get()
            sql="update Service_center set cname='%s',address='%s',email='%s',phone='%s',regno='%s' where id=%d"%(xb,xc,xd,xe,xf,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
        l1=Label(a2,text='id',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        l2=Label(a2,text='cname',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='email',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='phone',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l6=Label(a2,text='regno',bg='pink',font=('arial',20))
        l6.place(x=150,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=350)
        t.mainloop()
       
        
        
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='service center details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            sql="delete from service_center where id=%d"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='id',bg='pink',font=('arial',20))
        b.place(x=200,y=100)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=350,y=100)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=200,y=200)
        t.mainloop()
        
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='service center details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select id from service_center"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()    
        
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
        
            sql="Select cname,address,email,phone,regno from service_center where id=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            db.close()
        r5=Label(a2,text='service center details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=200,y=5)   
        b=Label(a2,text='id',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=finddata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='cname',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        h=Label(a2,text='email',bg='pink',font=('arial',20))
        h.place(x=150,y=220)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=220)
        i=Label(a2,text='phone',bg='pink',font=('arial',20))
        i.place(x=150,y=260)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=260)
        k=Label(a2,text='regno',bg='pink',font=('arial',20))
        k.place(x=150,y=300)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=300)
        t.mainloop()
        
        
        
     
    def showdatashow():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(a2,text='service center details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=300,y=5)   
        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select *from service_center"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+str(res[0])
                recd=recd+'\t'+res[1]
                recd=recd+'\t'+res[2]
                recd=recd+'\t'+res[3]
                recd=recd+'\t'+res[4]
                recd=recd+'\t'+res[5]
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=100,height=50,bg='pink',fg='black',font=('arial',15)) 
        showdata() 
        e.insert(tkinter.END,recd)
        e.place(x=10,y=70)
        t.mainloop()
        
       
    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='service center details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=650,y=10)
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from service_center"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            
        b=Label(a2,text='id',bg='pink',font=('arial',20))
        b.place(x=60,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='cname',bg='pink',font=('arial',20))
        e.place(x=60,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=60,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        j=Label(a2,text='email',bg='pink',font=('arial',20))
        j.place(x=60,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l=Label(a2,text='phone',bg='pink',font=('arial',20))
        l.place(x=60,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l=Label(a2,text='regno',bg='pink',font=('arial',20))
        l.place(x=60,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',15))
        bt1.place(x=100,y=350)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',15))
        bt2.place(x=200,y=350)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',15))
        bt3.place(x=300,y=350)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',15))
        bt4.place(x=430,y=350)
        filldata()
        t.mainloop()
    a1=Canvas(t,height=900,width=250,bg='cyan')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='cyan',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='teal',fg='white')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='teal',fg='white')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='teal',fg='white')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='teal',fg='white')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=showdatashow,font=('Arial',12,'bold'),width=14,bg='teal',fg='white')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='teal',fg='white')
    b1.place(x=35,y=450)
    
    
    
    
def showproductcategory():
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='product category details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        cdi=[]
        def close():
            cdi.clear()
            t.destroy
        def filldatac():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from product_category"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            db.close()    
            
        def dest():
            t.destroy()
        
        
        def savedata():
            if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or len(e6.get())==0:
                
                
                messagebox.showerror('hii','please check all')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                xb=e2.get()
                xc=e3.get()
                sql="insert into product_category values('%s','%s','%s')"%(xa,xb,xc)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
            
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from product_category where prodcatid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                 messagebox.showinfo('hii','already exit')
            db.close()    
            
        l1=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l1.place(x=150,y=100)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldatac()
        e1['values']=cdi
        e1.place(x=450,y=100)
        l2=Label(a2,text='catname',bg='pink',font=('arial',20)) 
        l2.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        l3=Label(a2,text='description',bg='pink',font=('arial',20))
        l3.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        btn11=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn11.place(x=150,y=300)
        btn12=Button(a2,text='close',command=dest,fg='white',bg='black',font=('arial',15))
        btn12.place(x=250,y=300)
        btn13=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn13.place(x=350,y=300)
        t.mainloop()
        
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='poduct category details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from product_category"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            sql="update product_category set catname='%s',description='%s' where prodcatid='%s'"%(xb,xc,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            
        l1=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l1.place(x=150,y=100)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=100)
        l2=Label(a2,text='catname',bg='pink',font=('arial',20))
        l2.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        l3=Label(a2,text='description',bg='pink',font=('arial',20))
        l3.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=300)
        t.mainloop()
       
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='product category details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from product_category where prodcatid='%s'"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        b.place(x=150,y=100)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=100)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=200)
        t.mainloop()
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='product category details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from product_category"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            e2.delete(0,100)
            e3.delete(0,100)
            sql="Select catname,description from product_category where prodcatid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            db.close()
           
        b=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=finddata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='catname',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='description',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        t.mainloop()
        
    def show():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='product category details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
     

        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from product_category"
            
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+res[0]
                recd=recd+'\t'+res[1]
                recd=recd+'\t'+res[2]
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=150,height=50,bg='pink',font=('arial',20))
        showdata() 
        e.insert(tkinter.END,recd) 
        e.place(x=10,y=70)
        t.mainloop()

    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='product category details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        xa=[]
        xb=[]
        xc=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from product_category"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            
            
            
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            
            
            
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            
            
            
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            
            
            
            
            
        b=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        b.place(x=30,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='catname',bg='pink',font=('arial',20))
        e.place(x=30,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='description',bg='pink',font=('arial',20))
        g.place(x=30,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',20))
        bt1.place(x=100,y=300)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',20))
        bt2.place(x=200,y=300)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',20))
        bt3.place(x=300,y=300)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',20))
        bt4.place(x=450,y=300)
        filldata()
        t.mainloop()

        
    a1=Canvas(t,height=900,width=250,bg='violet')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='violet',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='purple',fg='white')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='purple',fg='white')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='purple',fg='white')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='purple',fg='white')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=show,font=('Arial',12,'bold'),width=14,bg='purple',fg='white')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='purple',fg='white')
    b1.place(x=35,y=450)
def showservicetype():
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='servicetype details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        cdi=[]
        def dest():
            cdi.clear()
            t.destroy
        def filldatac():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select serviceid from servicetype"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            db.close()
        cdi1=[]
        def dest():
            cdi1.clear()
            t.destroy()
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from servicetype"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi1.append(res[0])
            db.close()     
        
        
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=int(e4.get())
            xe=e5.get()
            sql="select *from servicetype where prodcatid='%s'"%(xb)
            cur.execute(sql)
            data=cur.fetchone()
            if data:
                messagebox.showerror('invalid','data already exist')
            else:
                if xa=='' or xb=='' or xc=='' or xe=='':
                    messagebox.showerror('invalid','fill entries')
                else:
                    if xd<100:
                        messagebox.showerror("invalid entry","charge can't less 100")
                    else:
                        sql="insert into servicetype values('%s','%s','%s',%d,'%s')"%(xa,xb,xc,xd,xe)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('save','Data successfully saved')
                        db.close()
                        e1.delete(0,100)
                        e2.delete(0,100)
                        e3.delete(0,100)
                        e4.delete(0,100)
                        x5.delete(0,100)
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from servicetype where prodcatid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                 messagebox.showinfo('hii','already exit')
            db.close()    
                    
            
        l1=Label(a2,text='serviceid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldatac()
        e1['values']=cdi
        e1.place(x=450,y=60)
        l2=Label(a2,text='prodcatid',bg='pink',font=('arial',20)) 
        l2.place(x=150,y=100)
        e2=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e2['values']=cdi1
        e2.place(x=450,y=100)
        l3=Label(a2,text='sname',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='charge',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='timesolve',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        btn1=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=150,y=300)
        btn1=Button(a2,text='close',command=dest,fg='white',bg='black',font=('arial',15))
        btn1.place(x=250,y=300)
        btn1=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=350,y=300)
        t.mainloop()
        
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='servicetype details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select serviceid from servicetype"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()    
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=int(e4.get())
            xe=e5.get()
            sql="update servicetype set prodcatid='%s', sname='%s',charges=%d,timesolve='%s' where serviceid='%s'"%(xb,xc,xd,xe,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
        l1=Label(a2,text='serviceid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        l2=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='sname',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='charges',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='timesolve',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',20))
        btn.place(x=150,y=300)
        t.mainloop()
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='servicetype details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from servicetype where serviceid='%s'"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='serviceid',bg='pink',font=('arial',20))
        b.place(x=150,y=100)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=100)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=200)
        t.mainloop()
        
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='servicetype details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select serviceid from servicetype"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()  
        
        
        def showfind():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            sql="Select prodcatid ,sname,charges,timesolve from servicetype where serviceid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            db.close()
           
        b=Label(a2,text='serviceid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=showfind,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='sname',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        h=Label(a2,text='charges',bg='pink',font=('arial',20))
        h.place(x=150,y=220)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=220)
        i=Label(a2,text='timesolve',bg='pink',font=('arial',20))
        i.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        t.mainloop()
        
    def show():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='servicetype details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
     

        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select * from servicetype"
            
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+res[0]
                recd=recd+'\t'+res[1]
                recd=recd+'\t'+res[2]
                recd=recd+'\t'+str(res[3])
                recd=recd+'\t'+str(res[4])
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=100,height=50,bg='pink',font=('arial',20))
        showdata() 
        e.insert(tkinter.END,recd) 
        e.place(x=10,y=70)
        t.mainloop()
     
    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='servicetype details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=5)
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from servicetype"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,str(xd[i]))
            e5.insert(0,xe[i])
            
            
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,str(xd[i]))
            e5.insert(0,xe[i])
            
            
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,str(xd[i]))
            e5.insert(0,xe[i])
            
            
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,str(xd[i]))
            e5.insert(0,xe[i])
            
            
            
            
        b=Label(a2,text='serviceid',bg='pink',font=('arial',20))
        b.place(x=30,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        e.place(x=30,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='sname',bg='pink',font=('arial',20))
        g.place(x=30,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        j=Label(a2,text='charges',bg='pink',font=('arial',20))
        j.place(x=30,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l=Label(a2,text='timesolve',bg='pink',font=('arial',20))
        l.place(x=30,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',20))
        bt1.place(x=100,y=300)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',20))
        bt2.place(x=200,y=300)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',20))
        bt3.place(x=300,y=300)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',20))
        bt4.place(x=470,y=300)
        filldata()
        t.mainloop()
    a1=Canvas(t,height=900,width=250,bg='lime')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='lime',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=show,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=450)
    
def showengineers():
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='engineers details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        cdi=[]
        def dest():
            cdi.clear()
            t.destroy()
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select engid from engineers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            db.close()    
        cdi1=[]
        def dest():
            cdi1.clear()
            t.destroy()
        def filldatac():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from engineers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi1.append(res[0])
            db.close()
         
        def savedata():
          
            if len(e1.get())==0 or  len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or len(e6.get())==0 or len(e7.get())==0:
                messagebox.showerror('hii','please check all')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                xb=e2.get()
                xc=e3.get()
                xd=e4.get()
                xe=e5.get()
                xf=e6.get()
                xg=e7.get()
                
                sql="insert into engineers values('%s','%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                
        def checkdata():
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from engineers where prodcatid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                messagebox.showinfo('hii','already exit')
            db.close()    
                
        l1=Label(a2,text='engid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=cdi
        e1.place(x=450,y=60)
        l2=Label(a2,text='ename',bg='pink',font=('arial',20)) 
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='phone',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='email',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l6=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l6.place(x=150,y=260)
        e6=ttk.Combobox(a2,width=30,font=('arial',15))
        filldatac()
        e6['values']=cdi1
        e6.place(x=450,y=260)
        l7=Label(a2,text='status',bg='pink',font=('arial',20))
        l7.place(x=150,y=300)
        e7=Entry(a2,width=30,font=('arial',15))
        e7.place(x=450,y=300)
        btn1=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=150,y=340)
        b2 = Button(a2,text='Close',fg='white',font=('arial',15,'bold'), bg='black',command=dest)
        b2.place(x=250,y=340)
        btn1=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=400,y=340)
        t.mainloop()   
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='engineers details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select engid from engineers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=e6.get()
            xg=e7.get()
            sql="update engineers set  ename='%s',address='%s',phone='%s',email='%s',prodcatid='%s',status='%s' where engid='%s'"%(xb,xc,xd,xe,xf,xg,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            
        l1=Label(a2,text='engid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        l2=Label(a2,text='ename',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='phone',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='email',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l6=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l6.place(x=150,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        l7=Label(a2,text='status',bg='pink',font=('arial',20))
        l7.place(x=150,y=300)
        e7=Entry(a2,width=30,font=('arial',15))
        e7.place(x=450,y=300)
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=340)
        t.mainloop()
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='engineers details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        
        
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from engineers where engid='%s'"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='engidid',bg='pink',font=('arial',20))
        b.place(x=150,y=100)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=100)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=200)
        t.mainloop()
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='engineers details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=700,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select engid from engineers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        
         
         
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            sql="Select ename,address,phone, email, prodcatid,status from engineers where engid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            e7.insert(0,data[5])
            db.close()
            
        b=Label(a2,text='engid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=finddata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='ename',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        h=Label(a2,text='phone',bg='pink',font=('arial',20))
        h.place(x=150,y=220)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=220)
        i=Label(a2,text='email',bg='pink',font=('arial',20))
        i.place(x=150,y=260)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=260)
        j=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        j.place(x=150,y=300)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=300)
        k=Label(a2,text='status',bg='pink',font=('arial',20))
        k.place(x=150,y=340)
        e7=Entry(a2,width=30,font=('arial',15))
        e7.place(x=450,y=340)
        t.mainloop()
    def show():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(a2,text='engineers details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=350,y=10)
     

        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select *from engineers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+str(res[0])
                recd=recd+'\t'+res[1]
                recd=recd+'\t'+res[2]
                recd=recd+'\t'+res[3]
                recd=recd+'\t'+res[4]
                recd=recd+'\t'+str(res[5])
                recd=recd+'\t'+res[6]
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=70,height=30,bg='pink',font=('arial',15)) 
        showdata() 
        e.insert(tkinter.END,recd) 
        e.place(x=5,y=50)
        t.mainloop()
    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(a2,text='engineers details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=250,y=10)
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        xg=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from engineers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
                xg.append(res[6])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            e7.insert(0,xg[i])
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            e7.insert(0,xg[i])
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            e7.insert(0,xg[i])
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            e7.insert(0,xg[i])
            
            
        b=Label(a2,text='engid',bg='pink',font=('arial',20))
        b.place(x=30,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='ename',bg='pink',font=('arial',20))
        e.place(x=30,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=30,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        j=Label(a2,text='phone',bg='pink',font=('arial',20))
        j.place(x=30,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l=Label(a2,text='email',bg='pink',font=('arial',20))
        l.place(x=30,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l.place(x=30,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        l=Label(a2,text='status',bg='pink',font=('arial',20))
        l.place(x=30,y=300)
        e7=Entry(a2,width=30,font=('arial',15))
        e7.place(x=450,y=300)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',15))
        bt1.place(x=100,y=340)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',15))
        bt2.place(x=200,y=340)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',15))
        bt3.place(x=300,y=340)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',15))
        bt4.place(x=400,y=340)
        filldata()
        t.mainloop()

    a1=Canvas(t,height=900,width=250,bg='salmon')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='salmon',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='crimson',fg='white')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='crimson',fg='white')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='crimson',fg='white')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='crimson',fg='white')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=show,font=('Arial',12,'bold'),width=14,bg='crimson',fg='white')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='crimson',fg='white')
    b1.place(x=35,y=450)
def showcustomer():
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='customers details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        cdi=[]
        def dest():
            cdi.clear()
            t.destroy
            
        def filldatac():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select custid from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            db.close()
        cdi1=[]
        def dest():
            cdi1.clear()
            t.destroy()
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi1.append(res[0])
            db.close()     
            
       
            
        def dest():
            t.destroy()
        def savedata():
            if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
                
                
                messagebox.showerror('hii','please check all')
            else:
                
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                xb=e2.get()
                xc=e3.get()
                xd=e4.get()
                xe=e5.get()
                xf=e6.get()
                
                
                sql="insert into customers values('%s','%s','%s',%s,'%s')"%(xa,xb,xc,xd,xe,xf)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)    
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from customers where custid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                 messagebox.showinfo('hii','already exit')
            db.close()                
                    
        
        l1=Label(a2,text='custid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldatac()
        e1['values']=cdi
        e1.place(x=450,y=60)
        
        l2=Label(a2,text='cname',bg='pink',font=('arial',20)) 
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='phone',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='email',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l6=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l6.place(x=150,y=260)
        e6=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e6['values']=cdi1
        e6.place(x=450,y=260)
        
        btn11=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn11.place(x=200,y=320)
        btn11=Button(a2,text='close',command=dest,fg='white',bg='black',font=('arial',15))
        btn11.place(x=300,y=320)
        btn11=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn11.place(x=400,y=320)
        t.mainloop()
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='customers details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select custid from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=e6.get()
            sql="update customers set  cname='%s',address='%s',phone='%s',email='%s',prodcatid='%s' where custid='%s'"%(xb,xc,xd,xe,xf,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            
            
        l1=Label(a2,text='custid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        l2=Label(a2,text='cname',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='phone',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='email',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l6=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l6.place(x=150,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=340)
        t.mainloop()
       
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='customers details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from customers where custid='%s'"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='custid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        t.mainloop()
        
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='customers details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select custid from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            
            sql="Select cname,address,phone, email, prodcatid from customers where custid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            db.close()
           
        b=Label(a2,text='custid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=finddata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='cname',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        h=Label(a2,text='phone',bg='pink',font=('arial',20))
        h.place(x=150,y=220)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=220)
        i=Label(a2,text='email',bg='pink',font=('arial',20))
        i.place(x=150,y=260)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=260)
        j=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        j.place(x=150,y=300)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=300)
        t.mainloop()
        
    def show():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='customers details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=750,y=10)
        
     

        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select * from customers"
            
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+str(res[0])
                recd=recd+'\t'+res[1]
                recd=recd+'\t'+res[2]
                recd=recd+'\t'+res[3]
                recd=recd+'\t'+res[4]
                recd=recd+'\t'+str(res[5])
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=150,height=50,bg='pink',font=('arial',20)) 
        showdata() 
        e.insert(tkinter.END,recd) 
        e.place(x=10,y=70)
        t.mainloop()
    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='customers details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
           
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,xf[i])
            
            
            
        b=Label(a2,text='custid',bg='pink',font=('arial',20))
        b.place(x=30,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='cname',bg='pink',font=('arial',20))
        e.place(x=30,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=30,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        j=Label(a2,text='email',bg='pink',font=('arial',20))
        j.place(x=30,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l=Label(a2,text='phone',bg='pink',font=('arial',20))
        l.place(x=30,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l=Label(a2,text='prodcatid',bg='pink',font=('arial',20))
        l.place(x=30,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',15))
        bt1.place(x=100,y=300)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',15))
        bt2.place(x=200,y=300)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',15))
        bt3.place(x=300,y=300)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',15))
        bt4.place(x=440,y=300)
        filldata()
        t.mainloop()
        
    a1=Canvas(t,height=900,width=250,bg='steelblue')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='steelblue',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='blue',fg='white')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='blue',fg='white')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='blue',fg='white')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='blue',fg='white')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=show,font=('Arial',12,'bold'),width=14,bg='blue',fg='white')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='blue',fg='white')
    b1.place(x=35,y=450)
def showstaff():
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='staff details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=800,y=10)
        cdi=[]
        def close():
            cdi.clear()
            t.destroy
        def filldatac():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select staffid from staff"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            db.close()    
            
        def dest():
            t.destroy()
        
        
        def savedata():
            if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
                
                
                messagebox.showerror('hii','please check all')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=int(e1.get())
                xb=e2.get()
                xc=e3.get()
                xd=e4.get()
                xe=e5.get()
                sql="insert into staff values(%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from staff where staffid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                 messagebox.showinfo('hii','already exit')
            db.close()         
            
            
            
        l1=Label(a2,text='staffid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldatac()
        e1['values']=cdi
        e1.place(x=450,y=60)
        l2=Label(a2,text='sname',bg='pink',font=('arial',20)) 
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='phone',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='email',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        btn1=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=150,y=260)
        btn1=Button(a2,text='close',command=dest,fg='white',bg='black',font=('arial',15))
        btn1.place(x=250,y=260)
        btn1=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=350,y=260)
        t.mainloop()
        
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='staff details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=800,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select staffid from staff"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            
            sql="update staff set  sname='%s',address='%s',phone='%s',email='%s' where staffid=%d"%(xb,xc,xd,xe,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
            
            
        l1=Label(a2,text='staffid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        l2=Label(a2,text='sname',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='address',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='phone',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='email',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=260)
        t.mainloop()
       
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='staff details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=800,y=10)
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            sql="delete from staff where staffid=%d"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='staffid',bg='pink',font=('arial',20))
        b.place(x=150,y=100)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=100)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=200)
        t.mainloop()
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='staff details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=800,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select staffid from staff"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        
        
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
            sql="Select sname,address,phone, email from staff where staffid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            db.close()
           
        b=Label(a2,text='staffid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=finddata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='sname',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        h=Label(a2,text='phone',bg='pink',font=('arial',20))
        h.place(x=150,y=220)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=220)
        i=Label(a2,text='email',bg='pink',font=('arial',20))
        i.place(x=150,y=260)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=260)
        t.mainloop()
        
    def show():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='staff details',bg='pink',fg='black',font=('arial',25))
        r5.place(x=800,y=10)
     

        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select *from staff"
            
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+str(res[0])
                recd=recd+'\t'+res[1]
                recd=recd+'\t'+res[2]
                recd=recd+'\t'+res[3]
                recd=recd+'\t'+res[4]
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=150,height=50,bg='pink',fg='black',font=('arial',25))
        showdata() 
        e.insert(tkinter.END,recd) 
        e.place(x=10,y=70)
        t.mainloop()
    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='staff details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from staff"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,str(xa[i]))
            e2.insert(0,xb[i])
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
            
            
        b=Label(a2,text='staffid',bg='pink',font=('arial',20))
        b.place(x=30,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='sname',bg='pink',font=('arial',20))
        e.place(x=30,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='address',bg='pink',font=('arial',20))
        g.place(x=30,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        j=Label(a2,text='email',bg='pink',font=('arial',20))
        j.place(x=30,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l=Label(a2,text='phone',bg='pink',font=('arial',20))
        l.place(x=30,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',15))
        bt1.place(x=100,y=300)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',15))
        bt2.place(x=200,y=300)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',15))
        bt3.place(x=300,y=300)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',15))
        bt4.place(x=400,y=300)
        filldata()
        t.mainloop()
        
    a1=Canvas(t,height=900,width=250,bg='olive')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='olive',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=show,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='darkgreen',fg='white')
    b1.place(x=35,y=450)
def showcallassignment():
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callassignment details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        
        cdi1=[]
        def close():
            cdi1.clear()
            t.destroy
        def filldata1():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select callid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi1.append(res[0])
            db.close()    
        cdi2=[]
        def close():
            cdi2.clear()
            t.destroy
        def filldata2():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select staffid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi2.append(res[0])
            db.close()
        cdi3=[]    
        def close():
            cdi3.clear()
            t.destroy
        def filldata3():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select custid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi3.append(res[0])
            db.close()    
                       
        def dest():
            t.destroy()
        
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=int(e2.get())
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=int(e6.get())
            sql="select *from callassignment where callid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data:
                messagebox.showerror('invalid','data already exist')
            else:
                if xa=='' or xb=='' or xc=='' or xd=='' or xe=='' or xf=='':
                    messagebox.showerror('invalid','fill entries')
                else:
                    if xf<100:
                        messagebox.showerror("invalid entry","charge can't less 100")
                    else:
                        sql="insert into callassignment values('%s',%d,'%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('saved','data successfully')
                        db.close()
                        e1.delete(0,100)
                        e2.delete(0,100)
                        e3.delete(0,100)
                        e4.delete(0,100)
                        e5.delete(0,100)
                        e6.delete(0,100)
                
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from callassignment where callid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                 messagebox.showinfo('hii','already exit')
            db.close()         
                
        
        
            
            
        xa=Label(a2,text='callid',bg='pink',font=('arial',20))
        xa.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata1()
        e1['values']=cdi1
        e1.place(x=450,y=60)
        xb=Label(a2,text='staffid',bg='pink',font=('arial',20)) 
        xb.place(x=150,y=100)
        e2=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata2()
        e2['values']=cdi2
        e2.place(x=450,y=100)
        xc=Label(a2,text='custid',bg='pink',font=('arial',20))
        xc.place(x=150,y=140)
        e3=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata3()
        e3['values']=cdi3
        e3.place(x=450,y=140)
        xd=Label(a2,text='engid',bg='pink',font=('arial',20))
        xd.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        xe=Label(a2,text='dateofcall',bg='pink',font=('arial',20))
        xe.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        xf=Label(a2,text='charges',bg='pink',font=('arial',20))
        xf.place(x=150,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        btn1=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=150,y=300)
        btn1=Button(a2,text='close',command=dest,fg='white',bg='black',font=('arial',15))
        btn1.place(x=250,y=300)
        btn1=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=350,y=300)
        t.mainloop()
        
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callassignment details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select callid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=int(e2.get())
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=int(e6.get())
            sql="update callassignment set staffid=%d,custid='%s',engid='%s',dateofcall='%s',charges=%d where callid='%s'"%(xb,xc,xd,xe,xf,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            
            
        l1=Label(a2,text='callid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        l2=Label(a2,text='staffid',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='custid',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='engid',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='dateofcall',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l6=Label(a2,text='charges',bg='pink',font=('arial',20))
        l6.place(x=150,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        t.title('database')
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=300)
        t.mainloop()
       
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callassignment details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from callassignment where callid='%s'"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='callid',bg='pink',font=('arial',20))
        b.place(x=150,y=100)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=100)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=200)
        t.mainloop()
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callassignment details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select callid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            sql="Select staffid,custid,engid, dateofcall,charges from callassignment where callid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            db.close()
           
        b=Label(a2,text='callid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=finddata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='staffid',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='custid',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        h=Label(a2,text='engid',bg='pink',font=('arial',20))
        h.place(x=150,y=220)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=220)
        i=Label(a2,text='dateofcall',bg='pink',font=('arial',20))
        i.place(x=150,y=260)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=260)
        j=Label(a2,text='charges',bg='pink',font=('arial',20))
        j.place(x=150,y=300)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=300)
        t.mainloop()
        
    def show():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callassignment details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
     

        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select * from callassignment"
            
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+res[0]
                recd=recd+'\t'+str(res[1])
                recd=recd+'\t'+res[2]
                recd=recd+'\t'+res[3]
                recd=recd+'\t'+str(res[4])
                recd=recd+'\t'+str(res[5])
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=70,height=50,bg='pink',font=('arial',20))
        showdata() 
        e.insert(tkinter.END,recd) 
        e.place(x=10,y=70)
        t.mainloop()
    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callassignment details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,str(xf[i]))
            
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,str(xf[i]))
            
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,str(xf[i]))
            
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            e6.insert(0,str(xf[i]))
            
            
            
        b=Label(a2,text='callid',bg='pink',font=('arial',20))
        b.place(x=30,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='staffid',bg='pink',font=('arial',20))
        e.place(x=30,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='custid',bg='pink',font=('arial',20))
        g.place(x=30,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        j=Label(a2,text='engid',bg='pink',font=('arial',20))
        j.place(x=30,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l=Label(a2,text='dateofcall',bg='pink',font=('arial',20))
        l.place(x=30,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        l=Label(a2,text='charges',bg='pink',font=('arial',20))
        l.place(x=30,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',15))
        bt1.place(x=100,y=300)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',15))
        bt2.place(x=200,y=300)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',15))
        bt3.place(x=300,y=300)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',15))
        bt4.place(x=400,y=300)
        filldata()
        t.mainloop()
    a1=Canvas(t,height=900,width=250,bg='gold')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='gold',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='yellow',fg='black')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='yellow',fg='black')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='yellow',fg='black')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='yellow',fg='black')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=show,font=('Arial',12,'bold'),width=14,bg='yellow',fg='black')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='yellow',fg='black')
    b1.place(x=35,y=450)
def showcallclose():
    def insert():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callclose details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        cdi1=[]
        def close():
            cdi1.clear()
            t.destroy
        def filldata1():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select callid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi1.append(res[0])
            db.close()    
        cdi2=[]
        def close():
            cdi2.clear()
            t.destroy
        def filldata2():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select staffid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi2.append(res[0])
            db.close()
        cdi3=[]    
        def close():
            cdi3.clear()
            t.destroy
        def filldata3():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select custid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi3.append(res[0])
            db.close()    
                       
        def dest():
            t.destroy()
        
        def savedata():
             db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
             cur=db.cursor()
             xa=e1.get()
             xb=int(e2.get())
             xc=e3.get()
             xd=e4.get()
             xe=e5.get()
             xf=int(e6.get())
             sql="select *from callclose where callid='%s'"%(xa)
             cur.execute(sql)
             data=cur.fetchone()
             if data:
                 messagebox,showerror('invalid','data already exist')
             else:
                 if xa=='' or xb=='' or xc=='' or xd=='' or xe=='' or xf=='':
                     messagebox.showerror('invalid','fill entries')
                 else:
                     if xf<100:
                         messagebox.showerror("invalid entry","charge can't less 100")
                     else:
                         sql="insert into callassignment values('%s',%d,'%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
                         cur.execute(sql)
                         db.commit()
                         messagebox.showinfo('Hi','Saved')
                         db.close()
                         e1.delete(0,100)
                         e2.delete(0,100)
                         e3.delete(0,100)
                         e4.delete(0,100)
                         e5.delete(0,100)
                         e6.delete(0,100)
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from callassignment where callid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                 messagebox.showinfo('hii','already exit')
            db.close()         
                
        
        
            
            
        xa=Label(a2,text='callid',bg='pink',font=('arial',20))
        xa.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata1()
        e1['values']=cdi1
        e1.place(x=450,y=60)
        xb=Label(a2,text='staffid',bg='pink',font=('arial',20)) 
        xb.place(x=150,y=100)
        e2=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata2()
        e2['values']=cdi2
        e2.place(x=450,y=100)
        xc=Label(a2,text='custid',bg='pink',font=('arial',20))
        xc.place(x=150,y=140)
        e3=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata3()
        e3['values']=cdi3
        e3.place(x=450,y=140)
        xd=Label(a2,text='engid',bg='pink',font=('arial',20))
        xd.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        xe=Label(a2,text='dateofcall',bg='pink',font=('arial',20))
        xe.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        xf=Label(a2,text='charges',bg='pink',font=('arial',20))
        xf.place(x=150,y=260)
        e6=Entry(a2,width=30,font=('arial',15))
        e6.place(x=450,y=260)
        btn1=Button(a2,text='save',command=savedata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=150,y=300)
        btn1=Button(a2,text='close',command=dest,fg='white',bg='black',font=('arial',15))
        btn1.place(x=250,y=300)
        btn1=Button(a2,text='check',command=checkdata,fg='white',bg='black',font=('arial',15))
        btn1.place(x=350,y=300)
        t.mainloop()
    def update():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callclose details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=800,y=10)
        
        
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select callid from callclose"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=int(e2.get())
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            sql="update callclose set staffid=%d,custid='%s',engid='%s',dateofclose='%s' where callid='%s'"%(xb,xc,xd,xe,xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','updatedone')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
            
            
        l1=Label(a2,text='callid',bg='pink',font=('arial',20))
        l1.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        l2=Label(a2,text='staffid',bg='pink',font=('arial',20))
        l2.place(x=150,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        l3=Label(a2,text='custid',bg='pink',font=('arial',20))
        l3.place(x=150,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        l4=Label(a2,text='engid',bg='pink',font=('arial',20))
        l4.place(x=150,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l5=Label(a2,text='dateofclose',bg='pink',font=('arial',20))
        l5.place(x=150,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        btn=Button(a2,text='update',command=updatedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=260)
        t.mainloop()
       
       
    def delete():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(a2,text='callclose details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=250,y=10)
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from callclose where callid='%s'"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Deleted')
            db.close()
            e1.delete(0,100)
        b=Label(a2,text='callid',bg='pink',font=('arial',20))
        b.place(x=150,y=100)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=100)
        btn=Button(a2,text='delete',command=deletedata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=200)
        t.mainloop()
        
    def find():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(a2,text='callclose details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=300,y=10)
        lt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select callid from callclose"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            sql="Select staffid,custid,engid, dateofclose from callclose where callid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            db.close()
           
        b=Label(a2,text='callid',bg='pink',font=('arial',20))
        b.place(x=150,y=60)
        e1=ttk.Combobox(a2,width=30,font=('arial',15))
        filldata()
        e1['values']=lt
        e1.place(x=450,y=60)
        btn=Button(a2,text='Find',command=finddata,fg='white',bg='black',font=('arial',15))
        btn.place(x=150,y=100)
        e=Label(a2,text='staffid',bg='pink',font=('arial',20))
        e.place(x=150,y=140)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=140)
        g=Label(a2,text='custid',bg='pink',font=('arial',20))
        g.place(x=150,y=180)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=180)
        h=Label(a2,text='engid',bg='pink',font=('arial',20))
        h.place(x=150,y=220)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=220)
        i=Label(a2,text='dateofclose',bg='pink',font=('arial',20))
        i.place(x=150,y=260)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=260)
        
        t.mainloop()
        
    def show():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(a2,text='callclose details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=400,y=10)
        
        
        
        def showdata():
            global recd
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select *from callclose"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                recd=recd+'\t'+res[0]
                recd=recd+'\t'+str(res[1])
                recd=recd+'\t'+res[2]
                recd=recd+'\t'+res[3]
                recd=recd+'\t'+res[4]
                recd=recd+'\n'
            db.close()
        e=Text(a2,width=100,height=50,bg='pink',font=('arial',20))
        showdata() 
        e.insert(tkinter.END,recd) 
        e.place(x=10,y=70)
        t.mainloop()
           
    def navigate():
        a2=Canvas(t,height=900,width=900,bg='pink')
        a2.place(x=500,y=0)
        r5=Label(t,text='callclose details',bg='pink',fg='black',font=('arial',20))
        r5.place(x=700,y=10)
        
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from callclose"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
            db.close()
        def first():
            global i
            i=0
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
            
        def next():
            global i
            i=i+1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
            
        def previous():
            global i
            i=i-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
        def last():
            global i
            i=len(xa)-1
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e1.insert(0,xa[i])
            e2.insert(0,str(xb[i]))
            e3.insert(0,xc[i])
            e4.insert(0,xd[i])
            e5.insert(0,xe[i])
            
            
            
            
        b=Label(a2,text='callid',bg='pink',font=('arial',20))
        b.place(x=60,y=60)
        e1=Entry(a2,width=30,font=('arial',15))
        e1.place(x=450,y=60)
        e=Label(a2,text='staffid',bg='pink',font=('arial',20))
        e.place(x=60,y=100)
        e2=Entry(a2,width=30,font=('arial',15))
        e2.place(x=450,y=100)
        g=Label(a2,text='custid',bg='pink',font=('arial',20))
        g.place(x=60,y=140)
        e3=Entry(a2,width=30,font=('arial',15))
        e3.place(x=450,y=140)
        j=Label(a2,text='engid',bg='pink',font=('arial',20))
        j.place(x=60,y=180)
        e4=Entry(a2,width=30,font=('arial',15))
        e4.place(x=450,y=180)
        l=Label(a2,text='dateofcall',bg='pink',font=('arial',20))
        l.place(x=60,y=220)
        e5=Entry(a2,width=30,font=('arial',15))
        e5.place(x=450,y=220)
        bt1=Button(a2,text='first',command=first,fg='white',bg='black',font=('arial',15))
        bt1.place(x=100,y=300)
        bt2=Button(a2,text='next',command=next,fg='white',bg='black',font=('arial',15))
        bt2.place(x=200,y=300)
        bt3=Button(a2,text='previous',command=previous,fg='white',bg='black',font=('arial',15))
        bt3.place(x=300,y=300)
        bt4=Button(a2,text='last',command=last,fg='white',bg='black',font=('arial',15))
        bt4.place(x=400,y=300)
        filldata()
        t.mainloop()

    a1=Canvas(t,height=900,width=250,bg='yellowgreen')
    a1.place(x=250,y=0)
    r6=Label(a1,text='Buttons',bg='yellowgreen',fg='black',font=('arial',25,'bold'))
    r6.place(x=38,y=23)
    b1=Button(a1,text='Insert',command=insert,font=('Arial',12,'bold'),width=14,bg='green',fg='white')
    b1.place(x=35,y=75)
    b1=Button(a1,text='Update',command=update,font=('Arial',12,'bold'),width=14,bg='green',fg='white')
    b1.place(x=35,y=150)
    b1=Button(a1,text='Delete',command=delete,font=('Arial',12,'bold'),width=14,bg='green',fg='white')
    b1.place(x=35,y=225)
    b1=Button(a1,text='Find',command=find,font=('Arial',12,'bold'),width=14,bg='green',fg='white')
    b1.place(x=35,y=300)
    b1=Button(a1,text='Show',command=show,font=('Arial',12,'bold'),width=14,bg='green',fg='white')
    b1.place(x=35,y=375)
    b1=Button(a1,text='Navigate',command=navigate,font=('Arial',12,'bold'),width=14,bg='green',fg='white')
    b1.place(x=35,y=450)

    
    
        
a=Canvas(t,height=900,width=250,bg='violet')
a.place(x=0,y=0)
a1=Canvas(t,height=900,width=250,bg='cyan')
a1.place(x=250,y=0)
a2=Canvas(t,height=900,width=900,bg='pink')
a2.place(x=500,y=0)
b=Label(a,text='SCM project',bg='violet',font=('arial',25,'bold'))
b.place(x=35,y=25)
b=Button(a,text='Service centre',width=14,font=('arial',12,'bold'),bg='deep pink',command=showservicecentre)
b.place(x=35,y=75)
c=Button(a,text='Product Category',width=14,font=('arial',12,'bold'),bg='deep pink',command=showproductcategory)
c.place(x=35,y=150)
d=Button(a,text='Service Type',width=14,font=('arial',12,'bold'),bg='deep pink',command=showservicetype)
d.place(x=35,y=225)
e=Button(a,text='Engineers',width=14,font=('arial',12,'bold'),bg='deep pink',command=showengineers)
e.place(x=35,y=300)
f=Button(a,text='Customers',width=14,font=('arial',12,'bold'),bg='deep pink',command=showcustomer)
f.place(x=35,y=375)
g=Button(a,text='Staff',width=14,font=('arial',12,'bold'),bg='deep pink',command=showstaff)
g.place(x=35,y=450)
h=Button(a,text='Call Assignment',width=14,font=('arial',12,'bold'),bg='deep pink',command=showcallassignment)
h.place(x=35,y=525)
j=Button(a,text='Call Close',width=14,font=('arial',12,'bold'),bg='deep pink',command=showcallclose)
j.place(x=35,y=600)
t.mainloop()
