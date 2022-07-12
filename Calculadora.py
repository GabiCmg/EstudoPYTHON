import tkinter as tk 
from tkinter import *

#CÁLCULO DE ADIÇÃO
def func_botao():
  n1 = int(caixa_1.get())
  n2 = int(caixa_2.get())
  result1 = n1+n2
  label_1['text'] ='O resultado da soma é: '
  label_1['text']=label_1['text'] + str(result1)
  #CÁLCULO DE SUBTRAÇÃO
  n3 = int(caixa_3.get())
  n4 = int(caixa_4.get())
  result2 = n3-n4
  label_2['text'] ='O resultado da subtração é: '
  label_2['text']=label_2['text'] + str(result2)
  #CÁLCULO DE MULTIPLICAÇÃO
  n5 = int(caixa_5.get())
  n6 = int(caixa_6.get())
  result3 = n5*n6
  label_3['text'] ='O resultado da multiplicação é: '
  label_3['text']=label_3['text'] + str(result3)
  #CÁLCULO DE DIVISÃO
  n7 = int(caixa_7.get())
  n8 = int(caixa_8.get())
  result4 = n7/n8
  label_4['text'] ='O resultado da divisão é: '
  label_4['text']=label_4['text'] + str(result4)

#CRIAR JANELA
janela = Tk()

#TÍTULO
label_tlt = Label(janela,text='CALCULADORA 1.0',font = 'Arial 17 bold')
label_tlt.place(x=350,y=20)

#RESULTADOS
label_1 = Label(janela,text='O resultado da soma é: ',font = 'Arial 17')
label_1.place(x=300,y=350)
label_2 = Label(janela,text='O resultado da subtração é: ',font = 'Arial 17')
label_2.place(x=300,y=380)
label_3 = Label(janela,text='O resultado da multiplicação é: ',font = 'Arial 17')
label_3.place(x=300,y=410)
label_4 = Label(janela,text='O resultado da divisão é: ',font = 'Arial 17')
label_4.place(x=300,y=440)


#BOTÃO
botao_1 = Button(janela, width=40, height=2, text='RESULTADO', font = 'Arial 12 bold', command=func_botao, background='#73C2FB',cursor = 'heart')
botao_1.place(x=240,y=510)

#ADIÇÃO
caixa_1 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_1.place(x=150,y=90)
caixa_2 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_2.place(x=550,y=90)
label_mais = Label(janela,text=" + ", font = 'Arial 30')
label_mais.place(x=430,y=80)
  
#SUBTRAÇÃO
caixa_3 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_3.place(x=150,y=150)
caixa_4 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_4.place(x=550,y=150)
label_sub = Label(janela,text=" - ", font = 'Arial 30')
label_sub.place(x=430,y=140)

#MULTIPLICAÇÃO
caixa_5 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_5.place(x=150,y=210)
caixa_6 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_6.place(x=550,y=210)
label_sub = Label(janela,text=" * ", font = 'Arial 30')
label_sub.place(x=430,y=210)

#DIVISÃO
caixa_7 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_7.place(x=150,y=270)
caixa_8 = Entry(janela, background='#F0FFFF', width=12, font='Arial 25')
caixa_8.place(x=550,y=270)
label_sub = Label(janela,text=" / ", font = 'Arial 30')
label_sub.place(x=430,y=270)

#TAMANHO DA JANELA
janela.geometry('900x600+150+50')

janela.mainloop()