from  tkinter import *
from  tkinter import ttk
from  tkinter import tix
import datetime
import sqlite3
import os
from alocarCompra import alocarC
from Cria_Configurações import configuraçaoJanela
from Cria_conta import principal
from Cria_gerenciamento import gerenciarJanela
from editeMesa import mesajanela
from Entrar_conta import entrarJanela
from InformacaoDono import donoJanela
from InformacaoFuncionario import funcionarioJanela
from InformacaoGerente import gerenteJanela
from InformacaoProduto import produtoJanela
from notaFiscal import notaF

if not os.path.exists("C:/ProgramData/TMS/verificar.txt"):
   arquivo = open("C:/ProgramData/TMS/verificar.txt", "w")
   arquivo.write("0")
   arquivo.close()

if not os.path.exists("C:/ProgramData/TMS/cumpomFiscal/"):
	os.system("mkdir cumpomFiscal")

if not os.path.exists("C:/ProgramData/TMS/bancoMesa/"):
	os.system("mkdir bancoMesa")

if not os.path.exists("C:/ProgramData/TMS/bancoMeus/"):
	os.system("mkdir bancoMeus")


def boasJanela():
   boasja = Tk()

   tx = boasja.winfo_screenwidth()
   ty = boasja.winfo_screenheight()

   hora = datetime.datetime
   hora = hora.today()
   hora = hora.hour
   hora = int(hora)

   ima = PhotoImage(file=("C:/ProgramData/TMS/Imagens/Sem título1.png"))
   ttk.Label(image=ima).pack(side=TOP, anchor=CENTER)
   style = ttk.Style()
   style.configure("PL.TLabel", font=("Consolas", 40, "bold"), foreground="white", background="DodgerBlue1")
   if hora >= 0  and hora <= 12:
      ttk.Label(boasja, text="Bom Dia, Cliente", style="PL.TLabel").pack(side=TOP, anchor=CENTER)
   elif hora >= 13 and hora <= 18:
      ttk.Label(boasja, text="Boa Tarde, Cliente", style="PL.TLabel").pack(side=TOP, anchor=CENTER)
   else:
      ttk.Label(boasja, text="Boa Noite, Cliente", style="PL.TLabel").pack(side=TOP, anchor=CENTER)
   style = ttk.Style()
   style.configure("SL.TLabel", font=("Consolas", 30, "bold"), foreground="white", background="DodgerBlue1")
   ttk.Label(boasja, text="Seja Bem Vindo Ao TMS,", style="SL.TLabel").pack(side=TOP, anchor=CENTER)
   ttk.Label(boasja, text="O seu gerenciador comercial.", style="SL.TLabel").pack(side=TOP, anchor=CENTER)
   
   boasja.geometry("%ix%i+%i+%i"%(tx/2.1, ty/1.7, tx/3.3, ty/5))
   boasja.config(relief=FLAT)
   boasja.config(bg="DodgerBlue1")
   boasja.overrideredirect(1)
   boasja.after(5999, boasja.destroy)
   boasja.mainloop()

boasJanela()
arquivo = open("C:/ProgramData/TMS/verificar.txt", "r")
arq = arquivo.read()
if arq == "0":
   arquivo = open("C:/ProgramData/TMS/verificar.txt", "w")
   arquivo.write("1")
   arquivo.close()
   principal()
elif arq == "1":
   entrarJanela()
elif arq == "2":
   arquivo = open("C:/ProgramData/TMS/contaUser.txt", "r")
   arq = arquivo.read()
   arquivo.close()
   valores = arq.split(",")
   gerenciarJanela(valores[0], valores[1], valores[2])
