from tkinter import *
from tkinter import ttk
from tkinter import tix
import os
import sqlite3
from gerarPdf import GeneratePDF


def notaF(nMesa):
   global jaNota, campoT, campo, imprimir, texto, total, d, t, tab;
   jaNota = Tk()

   tamax = jaNota.winfo_screenwidth()
   tamay = jaNota.winfo_screenheight()

   bordaTop = Frame(jaNota, height=60, bg="Teal")
   bordaTop.pack(side=TOP, expand=0, fill=X)

   bordaBot = Frame(jaNota, height=60, bg="Teal")
   bordaBot.pack(side=BOTTOM, expand=0, fill=X)

   BarraVertical = Scrollbar(jaNota, orient=VERTICAL)
   texto = Text(jaNota, insertontime=1, width=102, cursor="xterm",\
                relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                selectforeground="Black")
   texto.configure(yscrollcommand=BarraVertical.set)
   BarraVertical.pack(side=RIGHT, fill=Y)
   BarraVertical.configure(command= texto.yview)
   texto.pack(side=TOP, fill=Y, expand=1)


   style = ttk.Style()
   style.configure("BP.TButton", background="Teal",font=("Consolas", 13))
   nt = Label(bordaTop, text="NOTA FISCAL", bg="Teal", font=("Consolas", 25, "bold"))
   nt.place(x=((tamax/3)*0.37), y=((tamay/1.7)*0.02))
   ##############
   def tint(lista):
      listaT = []
      for i in lista:
         listaT.append(int(i))
      return listaT

   def tstr(lista):
      listaT = []
      for i in lista:
         listaT.append(str(i))
      return listaT   
   def chamaDis1():
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt", "r")
      listaDisponiveis = arquivo.read()
      listaDisponiveis = listaDisponiveis.split(",")
      arquivo.close()
      qtd = listaDisponiveis.count('')
      if qtd >= 1:
         listaDisponiveis.remove('')
      if len(listaDisponiveis) > 0 and (not "" in listaDisponiveis ):
         listaDisponiveis = tint(listaDisponiveis)
         listaDisponiveis.remove(int(nMesa))
         listaDisponiveis.sort()
         listaDisponiveis = tstr(listaDisponiveis)
         
      os.remove("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt")
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt", "w")
      if len(listaDisponiveis) > 0 and (not "" in listaDisponiveis):
         for i in listaDisponiveis:
            if i != listaDisponiveis[-1]:
               arquivo.write(i+",")
            else:
               arquivo.write(i)
      arquivo.close()
      
   def chamaOcu():
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasOcupadas.txt", "r")
      listaOcupadas = arquivo.read()
      listaOcupadas = listaOcupadas.split(",")
      arquivo.close()
      qtd = listaOcupadas.count('')
      if qtd >= 1:
         listaOcupadas.remove('')
      if len(listaOcupadas) > 0 and (not "" in listaOcupadas):
         listaOcupadas = tint(listaOcupadas)
         listaOcupadas.append(int(nMesa))
         listaOcupadas.sort()
         listaOcupadas = tstr(listaOcupadas)

      os.remove("C:/ProgramData/TMS/bancoMesa/mesasOcupadas.txt")
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasOcupadas.txt", "w")
      if len(listaOcupadas) > 0 and (not "" in listaOcupadas):
         for i in listaOcupadas:
            if i != listaOcupadas[-1]:
               arquivo.write(i+",")
            else:
               arquivo.write(i)
      arquivo.close()
   ###########
   def calc():
      global campo, campoT, imprimir, total, d, t, texto;
      d = float(campo.get())
      t = d-total
      campoT.configure(state="normal")
      campoT.delete(0, END)
      if t > 0:
         campoT.insert(0, str(t))
         campoT.configure(foreground="darkblue")
      elif t < 0:
         campoT.insert(0, str(t))
         campoT.configure(foreground="darkred")
      else:
         campoT.insert(0, str(t))
         campoT.configure(foreground="black")
      campoT.configure(state="disabled")
      imprimir.configure(state="normal")
      preencheNota()
      texto.configure(state="normal")
      texto.insert(END, "\nDinheiro: R$ "+str(d)+"\n")
      texto.insert(END, "Troco: R$ "+str(t)+"\n")
      texto.configure(state="disabled")
   def impr():
      global tab, jaNota, total, d, t, total;
      GeneratePDF(tab, total, d, t)
      bancoMesa = sqlite3.Connection("C:/ProgramData/TMS/bancoMesa/mesasDados.db")
      cursoMesa = bancoMesa.cursor()
      cursoMesa.execute("DROP TABLE %s"%tab)
      bancoMesa.commit()
      cursoMesa.execute("CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                        tipo TEXT, nome TEXT, qtd INTEGER, preco REAL)"%tab)
      bancoMesa.commit()
      cursoMesa.close()
      bancoMesa.close()
      jaNota.destroy()
   def fech():
      global jaNota;
      chamaDis1()
      chamaOcu()
      jaNota.destroy()
      # Aqui para quando não imprimir retorna 0
   def preencheNota():
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
         total += i[4]
         # formato de exibir compra
         formato = i[1]+" "+i[2]+"  "+str(i[3])+" unidade(s) - valor R$"+str(i[4])+" reais"
         texto.insert(END, formato)
         texto.insert(END, "\n")

      texto.insert(END, "\nTotal: R$ "+str(total))
      texto.config(state="disabled")
      
   ##############
   Label(bordaBot, text="Dinheiro:", bg="Teal", font=("Consolas", 13)).place(x=6, y=((tamay/1.7)*0.015))
   campo = ttk.Entry(bordaBot, width=12)
   campo.place(x=90, y=((tamay/1.7)*0.021))
   troco = Label(bordaBot,text="Troco:", bg="Teal", font=("Consolas", 13))
   troco.place(x=6, y=((tamay/1.7)*0.067))
   campoT = ttk.Entry(bordaBot, width=12)
   campoT.place(x=90, y=((tamay/1.7)*0.074))
   campoT.configure(state="disabled")
   
   preencheNota()
   calcular = ttk.Button(bordaBot, text="Calcular", style="BP.TButton",takefocus=0, command=calc)
   calcular.place(x=170, y=((tamay/1.7)*0.03))
   imprimir = ttk.Button(bordaBot, text="Imprimir", style="BP.TButton",takefocus=0, command=impr)
   imprimir.place(x=280, y=((tamay/1.7)*0.03))
   imprimir.configure(state="disabled")
   sair = ttk.Button(bordaBot, text="Sair", style="BP.TButton", takefocus=0, command=fech)
   sair.place(x=390, y=((tamay/1.7)*0.03))
   jaNota.geometry("%dx%d+%d+%d"%(tamax/2.7, tamay/1.7, tamax/2.9, tamay/5))
   jaNota.overrideredirect(1)
   jaNota.mainloop()
