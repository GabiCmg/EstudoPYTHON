from tkinter import *
from tkinter import messagebox
import re

janela = Tk()

def limpar():
   label_2['text'] = ""
   l1['text'] = ""

def funcao():
   if str(caixa_1.get()) == '' or str(caixa_2.get()) == '':
      messagebox.showinfo('Resultado', 'Insira um valor!')
   else:
      n1 = int(caixa_1.get())
      n2 = int(caixa_2.get())
      # Para quando eu souber usar...
      # import re
      # string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', string_velha.decode('utf-8')) 
      if calculo.get() == 1:
         limpar()
         l1["text"]= "+"
         resultado = n1+n2
         label_2['text'] = str(resultado)
      elif calculo.get() == 2:
         limpar()
         l1["text"] = "-"
         resultado = n1-n2
         label_2['text'] = str(resultado)
      elif calculo.get() == 3:
         limpar()
         l1["text"] = "/"
         if n2 == 0:
            messagebox.showinfo('Atenção!', 'O divisor não pode ser zero!\nVocê consegue dividir uma bolacha para ninguém?\nPois é...\nNão cometa esse erro novamente >:(')   
         else:
            resultado = n1/n2
            label_2['text'] = str(resultado)
      elif calculo.get() == 4:
         limpar()
         l1["text"] = "*"
         resultado = n1*n2
         label_2['text'] = str(resultado)
      else:
         messagebox.showinfo('Atenção!','Selecione uma operação matemática!')

## TEXTOS
#Criando uma caixa de entrada de dados
caixa_1 = Entry(janela, background='white', width=10, font='Arial 30')#Cor teste background='#E0FFFF'
caixa_1.place(x=10, y=50)
caixa_2 = Entry(janela, background='white', width=10, font='Arial 30')
caixa_2.place(x=365, y=50)

#Colocando um texto dentro da janela
label_1 = Label(janela, text='O resultado do seu cálculo é: ', font = 'Arial 18', background='#B0C4DE')
label_1.place(x=150,y=200)

#Resultado
label_2 = Label(janela, text='???', font = 'Arial 18 bold', background='#B0C4DE')
label_2.place(x=480,y=200)

## RADIOBUTTON
#Cria o sinal da operação
l1 = Label(janela,text="?",font="Arial 20 bold",background="#B0C4DE",foreground="black")
l1.place(x=290,y=60)

#Cria o radiobutton da operação
calculo = IntVar()
Radiobutton(janela,text="Soma",background="#B0C4DE",variable= calculo, value=1).place(x=10,y=200)
Radiobutton(janela,text="Subtração",background="#B0C4DE",variable= calculo, value=2).place(x=10,y=230)
Radiobutton(janela,text="Divisão",background="#B0C4DE",variable= calculo, value=3).place(x=10,y=260)
Radiobutton(janela,text="Multiplicação",background="#B0C4DE",variable= calculo, value=4).place(x=10,y=290)
#Para setar um valor
Radiobutton(janela,text="Selecione algo!",background="#B0C4DE",variable= calculo, value=5)
calculo.set(5)

#BOTÃO
Button(janela,text="Calcular",font='Arial 16 bold',command=funcao,background="#A442DC",cursor = 'heart').place(x=10,y=350)
Button(janela, text='Sair',font='Arial 16 bold', command=janela.quit,background="#A442DC",cursor = 'heart').place(x=530,y=350)

#Cria a janela
janela.geometry("600x400+400+100")
janela.configure(background="#B0C4DE")
janela.title("Calculadora")
janela.mainloop()