from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Gabriela_2003",
    database="bd_cadastro"
)

def cadastro():
    
    login = str (caixa_1.get())
    senha = str(caixa_2.get())
    
    if  login == "":
         messagebox.showerror('Erro', 'Preencha todos os campos corretamente')
    elif senha == "":
         messagebox.showerror('Erro', 'Preencha todos os campos corretamente')
    else:
         messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!!!")

    mycursor = mydb.cursor()
#
    sql = "INSERT INTO tb_dados ( nome, senha) VALUES (%s, %s)"
    cadastro = (login, senha) 
    mycursor.execute( sql, cadastro)
#     
    mydb.commit()
      
def Apagar():
   
   caixa_1.delete(0,'end')
   caixa_2.delete(0,'end')

def IExit ():
    janela.destroy()
    
janela = Tk()
janela.title("Cadastro")

lb1 = Label(janela, text="Login: ",background="#B5FFBC")
lb2 = Label(janela, text="Senha: ",background="#B5FFBC")

caixa_1 = Entry(janela,)
caixa_2 = Entry(janela, show="*")

bt1 = Button(janela, text="Cadastrar", command=cadastro,background="#4CA346",overrelief=FLAT, activebackground='#91FF91',cursor='STAR')

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
caixa_1.grid(row=0, column=1)
caixa_2.grid(row=1, column=1)
bt1.grid(row=6, column=1)
bt1.place(x=75,y=70)
Button(janela,text="Apagar",font='Consolas 10',command= Apagar ,background="#4CA346",overrelief=FLAT, activebackground='#91FF91',cursor='STAR').place(x=3,y=70)
Button(janela,text="Sair",font='Consolas 10',command= IExit ,background="#4CA346",overrelief=FLAT, activebackground='#91FF91',cursor='STAR').place(x=195,y=70)
janela.geometry("240x100+500+150")
janela.configure(background="#B5FFBC")
janela.mainloop()