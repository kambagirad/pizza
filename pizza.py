import pprint
 
P=dict()
P['ПЕППЕРОНИ']={'Cостав':"Пепперони, моцарелла, томатный соус",'size':{'S':"395", 'M':"545"}}
P['МАРГАРИТА']={'Состав': 'Томаты, моцарелла, томатный соус','size':{'S':"395", 'M':"545"}}
P['ГАВАЙСКАЯ']={'Состав': 'Курица, ветчина, ананас, моцарелла, томатный соус','size':{'S':"415",'M':"595"}}
print('ДоПицца приветствует! \n Программа для заказа пиццы. \n Спасибо, что выбрали нашу компанию!')
ad=input('Укажите адрес доставки: ')
date=input('Укажите дату(сегодня,завтра): ')
time= input('Укажите время: ')
c= input('Укажите контактные данные: ')
print('Пиццы в наличии:')
pprint.pprint(P)
D=dict()
L=[]
K=[]
i=0
while True:
    pizza=input('Укажите пиццу для заказа или "выход" для окончания ввода: ')
    if pizza=='выход':
        print('Всего доброго! До свидания!')
        break
    elif pizza.upper() in P:
        choose_size=input('Укажите размер пиццы (S или M)')
        price=int(P[pizza.upper()]['size'][choose_size.upper()])
        k=int(input('Укажите количество: '))
        D[i]={'count':k,'pizza':pizza.upper(),'size':choose_size.upper(),'tm':time, 'Price': k*price}
        L.append(price)
        K.append(k)
    else:
        continue
    i+=1
p=0    
for i in range(len(L)):
    p+=L[i]*K[i]
if sum(K)>=3:
    p=p-min(L)
    
if date.lower()=='завтра':
    p=p-0.95*p
else:
    p=p
    
    

D['adress']={ad}
D['contact']={c}
D['date']={date}
pprint.pprint(D)
print('Адрес: ',str(D['adress']))
print('Номер телефона: ',str(D['contact']))
print('Итог: ', p, 'руб')
print('Заказ сформирован!')
