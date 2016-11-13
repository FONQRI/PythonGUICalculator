from tkinter import*
from tkinter import ttk
from tkinter import messagebox
root =Tk()
root.title('Calculator')
root.resizable(width=FALSE, height=FALSE)
#*******************************making basic**********************************
style=ttk.Style()
style.configure("TButton",bg='#91a7d0',fg='#011820')
frame =ttk.Frame(root)
frame.grid(row = 0 , column = 0)
entry=Entry(frame,bg='#f6cac9',fg='#0117d0')
entry.pack()
frame_num=Label(root,bg='#91a7d0',fg='#011820')
frame_num.grid(row =1 , column= 0)
frame_eq=Label(root,bg='#91a7d0',fg='#011820')
frame_eq.grid(row =2 , column= 0)
#*****************************numbers buttons*********************************
def cb1():
    entry.insert(entry.index(INSERT),'1')
b1=Button(frame_num,text='1',padx=12,command = cb1,bg='#91a7d0',fg='#011820')
b1.grid(row = 0 , column=0)
def cb2():
    entry.insert(entry.index(INSERT),'2')
b2=Button(frame_num,text='2',padx=12,command = cb2,bg='#91a7d0',fg='#011820')
b2.grid(row = 0 , column=1)
def cb3():
    entry.insert(entry.index(INSERT),'3')
b3=Button(frame_num,text='3',padx=12,command = cb3,bg='#91a7d0',fg='#011820')
b3.grid(row = 0 , column=2)
def cb4():
    entry.insert(entry.index(INSERT),'4')
b4=Button(frame_num,text='4',padx=12,command = cb4,bg='#91a7d0',fg='#011820')
b4.grid(row = 1 , column=0)
def cb5():
    entry.insert(entry.index(INSERT),'5')
b5=Button(frame_num,text='5',padx=12,command = cb5,bg='#91a7d0',fg='#011820')
b5.grid(row = 1 , column=1)
def cb6():
    entry.insert(entry.index(INSERT),'6')
b6=Button(frame_num,text='6',padx=12,command = cb6,bg='#91a7d0',fg='#011820')
b6.grid(row = 1 , column=2)
def cb7():
    entry.insert(entry.index(INSERT),'7')
b7=Button(frame_num,text='7',padx=12,command = cb7,bg='#91a7d0',fg='#011820')
b7.grid(row = 2 , column=0)
def cb8():
    entry.insert(entry.index(INSERT),'8')
b8=Button(frame_num,text='8',padx=12,command = cb8,bg='#91a7d0',fg='#011820')
b8.grid(row = 2 , column=1)
def cb9():
    entry.insert(entry.index(INSERT),'9')
b9=Button(frame_num,text='9',padx=12,command = cb9,bg='#91a7d0',fg='#011820')
b9.grid(row = 2 , column=2)
def cb0():
    entry.insert(entry.index(INSERT),'0')
b0=Button(frame_num,text='0',padx=12,command = cb0,bg='#91a7d0',fg='#011820')
b0.grid(row = 3 , column=1)
#**********************************oprators**********************************
def cb_dot():
    if entry.index(INSERT)== 0:
        entry.insert(entry.index(INSERT),'0')
    elif entry.get()[entry.index(INSERT)-1]==' 'or entry.get()[entry.index(INSERT)-1]=='+' or entry.get()[entry.index(INSERT)-1]=='-'or entry.get()[entry.index(INSERT)-1]=='/' or entry.get()[entry.index(INSERT)-1]=='*'or entry.get()[entry.index(INSERT)-1]=='(' or entry.get()[entry.index(INSERT)-1]==')':
        entry.insert(entry.index(INSERT),'0')
    entry.insert(entry.index(INSERT),'.')

b_point=Button(frame_num,text='. ',padx=12,command = cb_dot,bg='#91a7d0',fg='#011820')
b_point.grid(row = 3 , column=0)

def cb_Symmetry():
    entry.insert(entry.index(INSERT),'-')

b_sign=Button(frame_num,text='- ',padx=12,command = cb_Symmetry,bg='#91a7d0',fg='#011820')
b_sign.grid(row = 3 , column=2)

def cb_plus():
    entry.insert(entry.index(INSERT),'+')

b_plus=Button(frame_num,text='+',padx=12,command = cb_plus,bg='#91a7d0',fg='#011820')
b_plus.grid(row = 0 , column=3)

def cb_min():
    entry.insert(entry.index(INSERT),'-')
    
b_min=Button(frame_num,text='_',padx=12,command = cb_min,bg='#91a7d0',fg='#011820')
b_min.grid(row = 1 , column=3)

def cb_multiplication():
    entry.insert(entry.index(INSERT),'*')
    
b_ord=Button(frame_num,text='*',padx=12,command = cb_multiplication,bg='#91a7d0',fg='#011820')
b_ord.grid(row = 2 , column=3)

def cb_Division():
    entry.insert(entry.index(INSERT),'/')
    
b_tag=Button(frame_num,text='/ ',padx=12,command = cb_Division,bg='#91a7d0',fg='#011820')
b_tag.grid(row = 3 , column=3)

def cb_left_p():
    entry.insert(entry.index(INSERT),'(')
    
b_tag=Button(frame_eq,text='(',padx=12,command = cb_left_p,bg='#91a7d0',fg='#011820')
b_tag.pack(side=LEFT)

def cb_Equal():
    try :
        result=eval(entry.get())
        entry.delete(0,END)
        entry.insert(END,result)
    except Exception as error:
        messagebox.showerror("invalid value", error)

b_eq=Button(frame_eq,text='=',padx=34,command = cb_Equal,bg='#91a7d0',fg='#011820')
b_eq.pack(side=RIGHT)


def cb_right_p():
    entry.insert(entry.index(INSERT),')')
    
b_tag=Button(frame_eq,text=')',padx=12,command = cb_right_p,bg='#91a7d0',fg='#011820')
b_tag.pack(side=RIGHT)





def cb_enter(event):
    try :
        result=eval(entry.get())
        entry.delete(0,END)
        entry.insert(END,result)
    except Exception as error:
        messagebox.showerror("invalid value", error)
root.bind('<Return>',cb_enter)
