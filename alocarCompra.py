from tkinter import *
from tkinter import ttk
from tkinter import tix
import os
import sqlite3

def alocarC(nMesa):
   global jaAloca, campoT, campoN, campoQ, texto, total, tab, listaT, listaA, lista, listaN, listaA1, lista1, t_value, n_value;
   jaAloca = Tk()

   tamax = jaAloca.winfo_screenwidth()
   tamay = jaAloca.winfo_screenheight()

   bordaTop = Frame(jaAloca, height=60, bg="Teal")
   bordaTop.pack(side=TOP, expand=0, fill=X)

   bordaBot = Frame(jaAloca, height=107, bg="Teal")
   bordaBot.pack(side=BOTTOM, expand=0, fill=X)

   BarraVertical = Scrollbar(jaAloca, orient=VERTICAL)
   texto = Text(jaAloca, insertontime=1, width=102, cursor="xterm",\
                relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                selectforeground="Black")
   texto.configure(yscrollcommand=BarraVertical.set)
   BarraVertical.pack(side=RIGHT, fill=Y)
   BarraVertical.configure(command= texto.yview)
   texto.pack(side=TOP, fill=Y, expand=1)


   style = ttk.Style()
   style.configure("BP.TButton", background="Teal",font=("Consolas", 13))
   nt = Label(bordaTop, text="Alocar Compra: Mesa %s"%str(nMesa), bg="Teal", font=("Consolas", 25, "bold"))
   nt.place(x=((tamax/3)*0.15), y=((tamay/1.7)*0.01))
   ##############
   def alocar():
      global campoT, campoN, campoQ, textotexto, tab, t_value, n_value;
      tipo = t_value.get()
      nome = n_value.get()
      qtd = int(campoQ.get())
      preco = float(0)
      bancoProduto = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursorProduto = bancoProduto.cursor()
      cursorProduto.execute("SELECT * FROM dadosProduto WHERE tipo = ?", (tipo,))
      info = cursorProduto.fetchall()
      for i in info:
         if nome == i[2]:
            preco += qtd*float(i[3])
      ###
      bancoMesa = sqlite3.Connection("C:/ProgramData/TMS/bancoMesa/mesasDados.db")
      cursoMesa = bancoMesa.cursor()
      tab = "_"+str(nMesa)+"_"
      insert = "INSERT INTO %s(tipo, nome, qtd, preco) VALUES(?, ?, ?, ?)"%tab
      cursoMesa.execute(insert, (tipo, nome, qtd, preco,))
      bancoMesa.commit()
      cursoMesa.close()
      bancoMesa.close()
      cursorProduto.close()
      bancoProduto.close()
      preencheAloca()
   def preencheAloca():
      global texto, total, tab;
      total = 0
      texto.config(state="normal")
      bancoMesa = sqlite3.Connection("C:/ProgramData/TMS/bancoMesa/mesasDados.db")
      cursoMesa = bancoMesa.cursor()
      tab = "_"+str(nMesa)+"_"
      cursoMesa.execute("CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                        tipo TEXT, nome TEXT, qtd INTEGER, preco REAL)"%tab)
      cursoMesa.execute("SELECT * FROM %s"%tab)
      compras = cursoMesa.fetchall()
      texto.delete("1.0", END)
      lista = list(compras)
      for i in compras:
         # formato de exibir compra
         formato = i[1]+" "+i[2]+"  "+str(i[3])+" unidade(s) - valor R$"+str(i[4])+" reais"
         total += i[4]
         texto.insert(END, formato)
         texto.insert(END, "\n")
      texto.insert(END, "\nTotal: R$ "+str(total))
      texto.config(state="disabled")
   def fech():
      global jaAloca;
      jaAloca.destroy()
   preencheAloca()
   ##############
   bancoP = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
   cursorP = bancoP.cursor()
   cursorP.execute("SELECT tipo, * FROM dadosProduto")
   lista = cursorP.fetchall()
   listaA = []
   listaT = []
   for i in lista:
      listaA.append(i[0])
   for i in listaA:
      if not i in listaT:
         listaT.append(i)
   listaT.sort()
   listaT.insert(0, "...")
   listaT = tuple(listaT)
   t_value = StringVar()
   #
   cursorP.execute("SELECT nome, * FROM dadosProduto")
   lista1 = cursorP.fetchall()
   listaA1 = []
   listaN = []
   for i in lista1:
      listaA1.append(i[0])
   for i in listaA1:
      if not i in listaN:
         listaN.append(i)
   listaN.sort()
   listaN.insert(0, "...")
   listaN = tuple(listaN)
   n_value = StringVar()
   def filtrarT():
      fil = t_value.get()
      if fil != "":
         tam = len(fil)
         selecio = []
         selecioN = []
         for i in listaT:
            if fil == i[0:tam]:
               selecio.append(i)
         selecio = tuple(selecio)
         campoT["values"] = selecio
         #
         bancoP = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursorP = bancoP.cursor()
         for i in selecio:
            cursorP.execute("SELECT * FROM dadosProduto WHERE tipo = ?", (i,))
            info = cursorP.fetchall()
            for j in info:
               selecioN.append(j[2])
         selecioN = tuple(selecioN)
         campoN["values"] = selecioN
      else:
         campoT["values"] = listaT
         campoN["values"] = listaN
   cursorP.close()
   bancoP.close()
   ##############
   Label(bordaBot, text="Tipo:", bg="Teal", font=("Consolas", 16, "bold")).place(x=95, y=0)
   campoT = ttk.Combobox(bordaBot, textvariable=t_value, width=24, font=("Consolas", 12), postcommand=filtrarT)
   campoT["values"] = listaT
   campoT.current(0)
   campoT.place(x=8, y=((tamay/1.7)*0.058))
   Label(bordaBot,text="Nome Produto:", bg="Teal", font=("Consolas", 16, "bold")).place(x=295, y=0)
   campoN = ttk.Combobox(bordaBot, textvariable=n_value, width=24, font=("Consolas", 12))
   campoN["values"] = listaN
   campoN.current(0)
   campoN.place(x=256, y=((tamay/1.7)*0.058))
   Label(bordaBot, text="Quantidade:", bg="Teal", font=("Consolas", 16, "bold")).place(x=57, y=((tamay/1.7)*0.1199))
   campoQ = ttk.Entry(bordaBot, width=26, font=("Consolas", 12))
   campoQ.place(x=8, y=((tamay/1.7)*0.18))

   aloc = ttk.Button(bordaBot, text="Alocar", style="BP.TButton", takefocus=0, command=alocar)
   aloc.place(x=256, y=((tamay/1.7)*0.145))
   sair = ttk.Button(bordaBot, text="Sair", style="BP.TButton", takefocus=0, command=fech)
   sair.place(x=385, y=((tamay/1.7)*0.145))

   preencheAloca()
   jaAloca.geometry("%dx%d+%d+%d"%(tamax/2.7, tamay/1.38, tamax/2.9, tamay/7.7))
   jaAloca.overrideredirect(1)
   jaAloca.mainloop()
