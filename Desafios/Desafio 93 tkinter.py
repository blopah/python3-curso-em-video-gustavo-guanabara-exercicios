from tkinter import *

janela =Tk()

cadastro = {}
lista = []
sidade = []
mulheres = []
v = IntVar()
texto1 = StringVar()
texto2 = StringVar()

def bt1_click():
    cadastro['nome'] = txb1.get()
    cadastro['idade'] = txb2.get()

    if v.get() == 1:
        cadastro['sexo'] = 'Masculino'
    elif v.get() == 2:
        cadastro['sexo'] = 'Feminino'
        mulheres.append(cadastro['nome'])
    lista.append(cadastro.copy())
    sidade.append(int(cadastro['idade'][:]))
    txt.delete(0.0,'end')
    txt.insert(0.0, str(f'\n- O grupo tem {len(lista)} pessoas\n- A media de idade é {sum(sidade)/len(lista):.0f}\n'))
    if len(mulheres) != 0:
        for i in mulheres:
            txt.insert(0.0, str(f'{i} '))
        txt.insert(0.0, str('- As mulheres cadastradas foram: '))
    txt.insert(0.0, str('\n--------------------------------------------------------\n'))
    for i in lista:
        if len(mulheres) == 0:
            txt.insert(0.0, f'\n- {i["nome"]} tem {i["idade"]} anos e é do sexo {i["sexo"]}')
        else:
            txt.insert(0.0, f'\n- {i["nome"]} tem {i["idade"]} anos e é do sexo {i["sexo"]}')
    texto2.set('')
    texto1.set('')



janela.title('EX094 - CADASTRO DE PESSOAS')

lb1 = Label(janela,text='Nome: ',font=('arial',12))
lb1.grid(row=0,column=0,sticky=E)
lb2 = Label(janela,text='Idade: ',font=('arial',12))
lb2.grid(row=1,column=0,sticky=E)
lb3 = Label(janela,text='Sexo[M/F]: ',font=('arial',12))
lb3.grid(row=2,column=0,sticky=E)


txb1 = Entry(janela,width=30,textvariable=texto1)
txb1.grid(row=0,column=1,sticky=W)
txb2 = Entry(janela,width=30,textvariable=texto2)
txb2.grid(row=1,column=1,sticky=W)

rdb1 = Radiobutton(janela,text='Masculino',value=1,variable=v)
rdb1.grid(row=2,column=1,sticky=W)
rdb2 = Radiobutton(janela,text='Feminino',value=2,variable=v)
rdb2.grid(row=2,column=1)

bt1 = Button(janela,text='CADASTRAR',font=('arialblack',12,'bold'),command=bt1_click)
bt1.grid(row=3,column=1,)

txt = Text(janela,bd=4,fg='green',bg='white',width=50,height=15,font=('arialblack',10,'bold'))
txt.place(x=10,y=110)


janela.geometry('380x400+100+100')
janela.mainloop()