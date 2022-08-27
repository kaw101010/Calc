import tkinter as t
w = t.Tk()

w.title('Calculator')
w['bg'] = 'blue'
w.geometry('457x680')
w.minsize(457,680)  
w.maxsize(457,680)


e1 = t.StringVar()
m = 0
def on_click(n):
    global s
    global s1
    global s2
    global y
    global m
    c = 0
    q = 0
    if n == 2:
        e.insert(t.END,'7')    
    elif n == 3:
        e.insert(t.END,'4')
    elif n == 4:
        e.insert(t.END,'1')
    elif n == 5:
        e.insert(t.END,'0')
    elif n == 7:
        e.insert(t.END,'8')
    elif n == 8:
        e.insert(t.END,'5')
    elif n == 9:
        e.insert(t.END,'2')
    elif n == 10:
        for i in range(len(s)):
            if s[i] in 'x+-÷%':
                for j in range(len(s[i+1:])):
                    if s[i+1:][j] == '.':
                        q = q + 1
                    elif s[i+1:][j] != '.':
                        q = 0
            elif s[i] == '.':
                q = q + 1
            else:
                None
        if q == 0:
            e.insert(t.END,'.')
        else:
            None
        
    elif n == 12:
        e.insert(t.END,'9')
    elif n == 13:
        e.insert(t.END,'6')
    elif n == 14:
        e.insert(t.END,'3')
    elif n == 15:
        e.insert(t.END,' % ')
    elif n == 16:
        e.insert(t.END,' ÷ ')
    elif n == 17:
        e.insert(t.END,' x ')
    elif n == 18:
        e.insert(t.END,' + ')
    elif n == 19:
        e.insert(t.END,' - ')
    elif n == 11:
        e.delete(0,t.END)
    elif n == 6:
        s = e.get()
        if len(s)>20:
            e.insert(0,'Invalid [Clear to proceed]')

        elif s!='':
            m = m + float(s)
            e.delete(0,t.END)
            em.delete(0,t.END)
            em.insert(0,m)
    elif n == 1:
        m = 0
        e.delete(0,t.END)
        em.delete(0,t.END)
        em.insert(0,'0')
    s = e.get()
    if n == 20:
        e.delete(0,t.END) 
        for i in range(len(s)):
            if s[i] in '+-x%÷':
                c = c+1
        for i in range(0,len(s)):
            if c > 1 or len(s)>20:
                e.insert(0,'Invalid [Clear to proceed]')
                break
            elif s[i] in '%÷x+-':
                s1 = s[:i].strip()
                s2 = s[i+1:].strip()
    
            if s[i] == '%' and c == 1:
                y = str(float(s1)*float(s2)/100)
                e.insert(t.END,y)   
                
            elif s[i] == '÷' and c == 1:
                y = str(float(s1)/float(s2))
                e.insert(t.END,y)
                
            elif s[i] == 'x' and c == 1:
                y = str(float(s1)*float(s2))
                e.insert(t.END,y)
                
            elif s[i] == '+' and c == 1:
                y = str(float(s1)+float(s2))
                e.insert(t.END,y)
                
            elif s[i] == '-' and c == 1:
                y = str(float(s1) - float(s2))
                e.insert(t.END,y)
        if c == 1:
            s = y    
           
f22 = t.Frame(w,bg = 'blue',borderwidth = 3)
f22.grid(row = 1,column = 0)
lm = t.Label(f22,text = 'MEM',font = ('',12,'bold'),bg = 'blue')
lm.pack()
f23 = t.Frame(w,bg = 'blue')
f23.grid(row = 1,columnspan = 5)
em = t.Entry(f23,textvariable = m,font = ('',12,'bold'),bg = 'blue')
em.pack()
f21 = t.Frame(w,bg = 'blue',borderwidth = 53)
f21.grid(row = 0,columnspan = 10)
e = t.Entry(f21,textvariable = e1,bg = 'white',font = ('',22),borderwidth = 12)
e.pack()
f1 = t.Frame(w,bg = 'blue',borderwidth = 5)
f1.grid(row = 2,column = 0)
b1 = t.Button(f1,text = 'MC',fg = 'Black',font = ('',24,),bg = 'red',borderwidth = 10,height = 1,width = 4,command = lambda:on_click(1))
b1.pack()
f2 = t.Frame(w,bg = 'blue',borderwidth = 6)
f2.grid(row = 3,column = 0)
b2 = t.Button(f2,text = '7',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(2))
b2.pack()
f3 = t.Frame(w,bg = 'blue',borderwidth = 6)
f3.grid(row = 4,column = 0)
b3 = t.Button(f3,text = '4',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(3))
b3.pack()
f4 = t.Frame(w,bg = 'blue',borderwidth = 6)
f4.grid(row = 5,column = 0)
b4 = t.Button(f4,text = '1',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(4))
b4.pack()
f5 = t.Frame(w,bg = 'blue',borderwidth = 6)
f5.grid(row = 6,column = 0)
b5 = t.Button(f5,text = '0',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(5))
b5.pack()
f6 = t.Frame(w,bg = 'blue',borderwidth = 6)
f6.grid(row = 2,column = 1)
b6 = t.Button(f6,text = 'M+',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(6))
b6.pack()
f7 = t.Frame(w,bg = 'blue',borderwidth = 6)
f7.grid(row = 3,column = 1)
b7 = t.Button(f7,text = '8',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(7))
b7.pack()
f8 = t.Frame(w,bg = 'blue',borderwidth = 6)
f8.grid(row = 4,column = 1)
b8 = t.Button(f8,text = '5',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(8))
b8.pack()
f9 = t.Frame(w,bg = 'blue',borderwidth = 6)
f9.grid(row = 5,column = 1)
b9 = t.Button(f9,text = '2',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(9))
b9.pack()
f10 = t.Frame(w,bg = 'blue',borderwidth = 6)
f10.grid(row = 6,column = 1)
b10 = t.Button(f10,text = '.',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(10))
b10.pack()
f11 = t.Frame(w,bg = 'blue',borderwidth = 6)
f11.grid(row = 2,column = 2)
b11 = t.Button(f11,text = 'C',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(11))
b11.pack()
f12 = t.Frame(w,bg = 'blue',borderwidth = 6)
f12.grid(row = 3,column = 2)
b12 = t.Button(f12,text = '9',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(12))
b12.pack()
f13 = t.Frame(w,bg = 'blue',borderwidth = 6)
f13.grid(row = 4,column = 2)
b13 = t.Button(f13,text = '6',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(13))
b13.pack()
f14 = t.Frame(w,bg = 'blue',borderwidth = 6)
f14.grid(row = 5,column = 2)
b14 = t.Button(f14,text = '3',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(14))
b14.pack()
f15 = t.Frame(w,bg = 'blue',borderwidth = 6)
f15.grid(row = 6,column = 2)
b15 = t.Button(f15,text = '%',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(15))
b15.pack()
f16 = t.Frame(w,bg = 'blue',borderwidth = 6)
f16.grid(row = 2,column = 3)
b16 = t.Button(f16,text = '÷',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(16))
b16.pack()
f17 = t.Frame(w,bg = 'blue',borderwidth = 6)
f17.grid(row = 3,column = 3)
b17 = t.Button(f17,text = 'x',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(17))
b17.pack()
f18 = t.Frame(w,bg = 'blue',borderwidth = 6)
f18.grid(row = 4,column = 3)
b18 = t.Button(f18,text = '+',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(18))
b18.pack()
f19 = t.Frame(w,bg = 'blue',borderwidth = 6)
f19.grid(row = 5,column = 3)
b19 = t.Button(f19,text = '-',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(19))
b19.pack()
f20 = t.Frame(w,bg = 'blue',borderwidth = 6)
f20.grid(row = 6,column = 3)
b20 = t.Button(f20,text = '=',fg = 'Black',font = ('',25,),bg = 'red',borderwidth = 9,height = 1,width = 4,command = lambda:on_click(20))
b20.pack()

w.mainloop()


