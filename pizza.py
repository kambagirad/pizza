import tkinter
import tkinter.ttk as ttk

root = tkinter.Tk()

P=dict()
P['ПЕППЕРОНИ']={'Cостав':"Пепперони, моцарелла, томатный соус",'size':{'S':"395", 'M':"545"}}
P['МАРГАРИТА']={'Состав': 'Томаты, моцарелла, томатный соус','size':{'S':"395", 'M':"545"}}
P['ГАВАЙСКАЯ']={'Состав': 'Курица, ветчина, ананас, моцарелла, томатный соус','size':{'S':"415",'M':"595"}}

tkinter.Label(root, text='Выберите пиццу', borderwidth=8).grid(row=0,column=0)

for i in range(len(list(P))):
    tkinter.Label(root, text=list(P)[i], borderwidth=8).grid(row=i+1,column=0)
    
tkinter.Label(root, text='Введите время заказа', borderwidth=8).grid(row=len(list(P))+1,column=0)
entry0=tkinter.Entry(root)
entry0.grid(row=len(list(P))+2,column=0)


tkinter.Label(root, text='Выберите размер', borderwidth=8).grid(row=0,column=1)
sP = tkinter.StringVar()
sM= tkinter.StringVar()
sG= tkinter.StringVar()
comboboxP=ttk.Combobox(root, values=list(P['ПЕППЕРОНИ']['size'].keys()),textvariable=sP)
comboboxP.grid(row=0+1,column=1)
comboboxM=ttk.Combobox(root, values=list(P['МАРГАРИТА']['size'].keys()),textvariable=sM)
comboboxM.grid(row=1+1,column=1)
comboboxG=ttk.Combobox(root, values=list(P['ГАВАЙСКАЯ']['size'].keys()),textvariable=sG)
comboboxG.grid(row=2+1,column=1)



tkinter.Label(root, text='Введите адрес заказа', borderwidth=8).grid(row=len(list(P))+1,column=1)

entry1=tkinter.Entry(root)
entry1.grid(row=len(list(P))+2,column=1)

tkinter.Label(root, text='Укажите количество', borderwidth=8).grid(row=0,column=2)
cP=tkinter.IntVar()
cM=tkinter.IntVar()
cG=tkinter.IntVar()
spnboxP=tkinter.Spinbox(root, from_=0, to=20,textvariable=cP)
spnboxP.grid(row=0+1,column=2)
spnboxM=tkinter.Spinbox(root, from_=0, to=20,textvariable=cM)
spnboxM.grid(row=1+1,column=2)
spnboxG=tkinter.Spinbox(root, from_=0, to=20,textvariable=cG)
spnboxG.grid(row=2+1,column=2)

tkinter.Label(root, text='Введите ваш номер телефона', borderwidth=8).grid(row=len(list(P))+1,column=2)

entry2=tkinter.Entry(root)
entry2.grid(row=len(list(P))+2,column=2)

d=tkinter.StringVar()
tkinter.Label(root,text='Выберите день заказа', borderwidth=8).grid(row=len(list(P))+3,column=1)
entry=ttk.Combobox(root, values=("сегодня","завтра"),textvariable=d)
entry.grid(row=len(list(P))+4,column=1)

tkinter.Label(root, text='Сумма заказа', borderwidth=8).grid(row=len(list(P))+5,column=1)

def order():
    D=dict()
    L=list()
    C=list()
    if sP.get()!='':
        pP=int(P['ПЕППЕРОНИ']['size'][sP.get()])
        D['pep']={'size':sP.get(),'price':pP,'count':cP.get()}
        L.append(pP)
        C.append(cP.get())
    else:
        pP=0
    if sM.get()!='':
        pM=int(P['МАРГАРИТА']['size'][sM.get()])
        D['marg']={'size':sM.get(),'price':pM,'count':cM.get()}
        L.append(pM)
        C.append(cP.get())
    else:
        pM=0
    if sG.get()!='':
        pG=int(P['ГАВАЙСКАЯ']['size'][sG.get()])
        D['gav']={'size':sG.get(),'price':pG,'count':cG.get()}
        L.append(pG)
        C.append(cP.get())
    else:
        pG=0 
    m=0
    if sum(C)>=3:
        m=min(L)
    sumZ=pP*(cP.get())+pM*(cM.get())+pG*(cG.get())-m
    if d.get()=='завтра':
        sumZ=0.95*sumZ
    orderS.set(sumZ)
    D['adress']={entry1.get()}
    D['contact']={entry2.get()}
    D['time']={entry.get()}
    print(D)
    
orderS=tkinter.IntVar() 
label=tkinter.Label(root,textvariable=orderS).grid(row=len(list(P))+6,column=1)   

button = tkinter.Button(root, text='Заказать',command=order)
button.grid(row=len(list(P))+7,column=1)

button2 = tkinter.Button(root, text='Выход', command=root.destroy) 
button2.grid(row=len(list(P))+8,column=1)

root.mainloop()
