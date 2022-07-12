from tkinter import *

def imprimir_op():
    vop=op.get()
    print(vop)

janela=Tk()
janela.geometry('300x170')
#Coloca nome na barra de título da janela
janela.title('Aula Button')

lb_titulo = Label(janela, text='Componente botão de rádio')
lb_titulo.pack()

op=StringVar()
#Seta o botão de rádio padrão
op.set('Op4')

rb_radio = Radiobutton(janela, text='opção 1', value='op1', variable=op)
rb_radio.pack()

rb_radio2 = Radiobutton(janela, text='opção 2', value='op2', variable=op)
rb_radio2.pack()

rb_radio3 = Radiobutton(janela, text='opção 3', value='op3', variable=op)
rb_radio3.pack()

rb_radio4 = Radiobutton(janela, text='opção 4', value='op4', variable=op)
#Centraliza na tela
#rb_radio4.pack()

btn_ok = Button(janela, text='ok', command=imprimir_op)
btn_ok.pack()

janela.mainloop()