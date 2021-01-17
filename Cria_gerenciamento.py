from tkinter import *
from tkinter import ttk
from tkinter import tix
import sqlite3
import os
from notaFiscal import notaF
from alocarCompra import alocarC
from InformacaoDono import donoJanela
from InformacaoFuncionario import funcionarioJanela
from InformacaoGerente import gerenteJanela
from InformacaoProduto import produtoJanela
from Cria_Configurações import configuraçaoJanela
from editeMesa import mesajanela
from Entrar_conta import entrarJanela

def gerenciarJanela(nome, usuario, conta):
   global janelaPrincipal, n, listaDisponiveis, listaOcupadas, listaReservadas, lb1, lb2, lb3;
   janelaPrincipal = Tk()

   tamaX = janelaPrincipal.winfo_screenwidth()
   tamaY = janelaPrincipal.winfo_screenheight()

   logo = Canvas(janelaPrincipal, bg="green4", height=100, relief=FLAT, highlightcolor="gray97")
   logo.pack(side=TOP, expand=False, fill=X)
   painel = Canvas(janelaPrincipal, bg="gray97", bd=0.0, relief=FLAT, highlightcolor="gray97")
   painel.pack(side=TOP, expand=True, fill=BOTH)

   borda = Canvas(painel, bg="green4", height=30, relief=FLAT, highlightcolor="gray97")
   borda.pack(side=BOTTOM, expand=True, fill=X, anchor=S)
   ##############
   def chamaParaAbrir():
      arquivo = open("C:/ProgramData/TMS/contaUser.txt", "r")
      arq = arquivo.read()
      arquivo.close()
      valores = arq.split(",")
      gerenciarJanela(valores[0], valores[1], valores[2])
               
   def fechar():
      janelaPrincipal.destroy()
      arquivoV = open("C:/ProgramData/TMS/verificar.txt", "w")
      arquivoV.write("2")
      arquivoV.close()
      
      arquivoC = open("C:/ProgramData/TMS/contaUser.txt", "w")
      arquivoC.write(nome+",")
      arquivoC.write(usuario+",")
      arquivoC.write(conta)
      arquivoC.close()
   def sair():
      janelaPrincipal.destroy()
      arquivo = open("C:/ProgramData/TMS/verificar.txt", "w")
      arquivo.write("1")
      arquivo.close()
      entrarJanela()
   def editeM():
      janelaPrincipal.destroy()
      mesajanela()
      gerenciarJanela(nome, usuario, conta)
   def editeP():
      janelaPrincipal.destroy()
      produtoJanela(1)
      gerenciarJanela(nome, usuario, conta)
   def configure():
      janelaPrincipal.destroy()
      configuraçaoJanela()
      gerenciarJanela(nome, usuario, conta)
   def novaCO():
      jan = Toplevel()
      def dono():
         jan.destroy()
         janelaPrincipal.destroy()
         donoJanela(1)
         gerenciarJanela(nome, usuario, conta)
      def gerente():
         jan.destroy()
         janelaPrincipal.destroy()
         gerenteJanela(1)
         gerenciarJanela(nome, usuario, conta)
      def funcionario():
         jan.destroy()
         janelaPrincipal.destroy()
         funcionarioJanela(1)
         gerenciarJanela(nome, usuario, conta)
   
      variaveD = IntVar()
      variavelG = IntVar()
      variavelF = IntVar()
      Label(jan, text="Escolha um Tipo para Conta:", font=("Klavika Med Caps", 13, "bold")).pack(side=TOP)
      btD = Checkbutton(jan, text="Tipo Dono", takefocus=0, font=("Klavika Med Caps", 13, "bold"), variable=variaveD, command=dono)
      btD.pack(side=TOP)
      btG = Checkbutton(jan, text="Tipo Gerente", takefocus=0, font=("Klavika Med Caps", 13, "bold"), variable=variavelG, command=gerente)
      btG.pack(side=TOP)
      btF = Checkbutton(jan, text="Tipo Funcionário", takefocus=0, font=("Klavika Med Caps", 13, "bold"), variable=variavelF, command=funcionario)
      btF.pack(side=TOP)
      
      jan.resizable(0, 0)
      jan.title(" Tipo")
      jan.geometry("270x140")
      jan.transient(janelaPrincipal)
      jan.grab_set()
      jan.wait_window()
      jan.mainloop()
   #############
   imC = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/ImageConta.png")
   imM = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/imagemesa.png")
   imP = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/imageproduto.png")
   imCo = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/imageconfig.png")
   imS = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/ImageSair.png")

   style = ttk.Style()
   style.configure("BP.TButton", background="gray95", foreground="green4")
   
   novaC = ttk.Button(painel, image=imC, underline=2, text="+ Nova Conta", style="BP.TButton", compound=LEFT, takefocus=False, command=novaCO)
   novaC.place(x=30, y=10)
   editarM = ttk.Button(painel, image=imM, underline=2, text="+ Editar Mesa", style="BP.TButton", compound=LEFT, takefocus=False, command=editeM)
   editarM.place(x=150, y=10)
   editarP = ttk.Button(painel, image=imP, underline=2, text="+ Editar Produto", style="BP.TButton", compound=LEFT, takefocus=False, command=editeP)
   editarP.place(x=267, y=10)
   config = ttk.Button(painel, image=imCo, underline=2, text="+ Configuração", style="BP.TButton", compound=LEFT, takefocus=False, command=configure)
   config.place(x=399, y=10)
   sair_B = ttk.Button(painel, image=imS, underline=2, text=" Fechar Janela", style="BW.TButton", compound=LEFT, takefocus=False, command=sair)
   sair_B.place(x=527, y=10)

   nomeP = Label(janelaPrincipal, text="Sistema de Gerenciamento Comercial", fg="white", background="green4", font=("Klavika Med Caps", 40, "bold"))
   nomeP.place(x=240, y=20)

   note = ttk.Notebook(painel, cursor="hand2", name='notebook')

   estilo = ttk.Style()
   estilo.configure("PF.TFrame", background="white")

   frame1 = ttk.Frame(note, style="PF.TFrame", height=490, width=tamaX-3, name="disponiveis")
   frame2 = ttk.Frame(note, style="PF.TFrame", height=490, width=tamaX-3, name="ocupadas")
   frame3 = ttk.Frame(note, style="PF.TFrame", height=490, width=tamaX-3, name="reservadas")
   frame1.pack()
   frame2.pack()
   frame3.pack()

   note.add(frame1, text='Disponíveis', underline=0)
   note.add(frame2, text='Ocupadas', underline=0)
   note.add(frame3, text='Reservadas', underline=0)

   note.pack()
   note.place(x=0, y=51)
   #####
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
   #####
   def guardaDis1():
      global listaDisponiveis;
      os.remove("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt")
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt", "w")
      qtd = listaDisponiveis.count('')
      if qtd >= 1:
         listaDisponiveis.remove('')
      if len(listaDisponiveis) > 0 and (not "" in listaDisponiveis):
         listaDisponiveis = tint(listaDisponiveis)
         listaDisponiveis.sort()
         listaDisponiveis = tstr(listaDisponiveis)
         for i in listaDisponiveis:
            if i != listaDisponiveis[-1]:
               arquivo.write(i+",")
            else:
               arquivo.write(i)
            
   ###
   def guardaOcu2():
      global listaOcupadas;
      os.remove("C:/ProgramData/TMS/bancoMesa/mesasOcupadas.txt")
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasOcupadas.txt", "w")
      qtd = listaOcupadas.count('')
      if qtd >= 1:
         listaOcupadas.remove('')
      if len(listaOcupadas) > 0 and (not "" in listaOcupadas):
         listaOcupadas = tint(listaOcupadas)
         listaOcupadas.sort()
         listaOcupadas = tstr(listaOcupadas)
         for i in listaOcupadas:
            if i != listaOcupadas[-1]:
               arquivo.write(i+",")
            else:
               arquivo.write(i)
      arquivo.close()
   ###
   def guardaRes3():
      global listaReservadas;
      os.remove("C:/ProgramData/TMS/bancoMesa/mesasReservadas.txt")
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasReservadas.txt", "w")
      qtd = listaReservadas.count('')
      if qtd >= 1:
         listaReservadas.remove('')
      if len(listaReservadas) > 0 and (not "" in listaReservadas):
         listaReservadas = tint(listaReservadas)
         listaReservadas.sort()
         listaReservadas = tstr(listaReservadas)
         for i in listaReservadas:
            if i != listaReservadas[-1]:
               arquivo.write(i+",")
            else:
               arquivo.write(i)
      arquivo.close()
   #######################
   def nmesa(n):
      total = 0
      bancoMesa = sqlite3.Connection("C:/ProgramData/TMS/bancoMesa/mesasDados.db")
      cursoMesa = bancoMesa.cursor()
      tab = "_"+str(n)+"_"
      cursoMesa.execute("CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                        tipo TEXT, nome TEXT, qtd INTEGER, preco REAL)"%tab)
      cursoMesa.execute("SELECT * FROM %s"%tab)
      compras = cursoMesa.fetchall()
      lista = list(compras)
      for i in compras:
         total += i[4]
      return total
   #######################
   def chamaDis1():
      global listaDisponiveis, lb1;
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt", "r")
      listaDisponiveis = arquivo.read()
      listaDisponiveis = listaDisponiveis.split(",")
      arquivo.close()
      qtd = listaDisponiveis.count('')
      if qtd >= 1:
         listaDisponiveis.remove('')
      if len(listaDisponiveis) > 0 and (not "" in listaDisponiveis ):
         listaDisponiveis = tint(listaDisponiveis)
         listaDisponiveis.sort()
         listaDisponiveis = tstr(listaDisponiveis)
         for i in listaDisponiveis:
            lb1.insert(END, "MESA:  %s    TOTAL:  %s"%(i, nmesa(i)))
         if len(listaDisponiveis) > 42:
            lb1.insert(END, " ")
   ###
   def chamaOcu2():
      global listaOcupadas,lb2;
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasOcupadas.txt", "r")
      listaOcupadas = arquivo.read()
      listaOcupadas = listaOcupadas.split(",")
      arquivo.close()
      qtd = listaOcupadas.count('')
      if qtd >= 1:
         listaOcupadas.remove('')
      if len(listaOcupadas) > 0 and (not "" in listaOcupadas):
         listaOcupadas = tint(listaOcupadas)
         listaOcupadas.sort()
         listaOcupadas = tstr(listaOcupadas)
         for i in listaOcupadas:
            lb2.insert(END, "MESA:  %s    TOTAL:  %s"%(i, nmesa(i)))
         if len(listaOcupadas) > 42:
            lb2.insert(END, " ")
   ###
   def chamaRes3():
      global listaReservadas, lb3;
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesasReservadas.txt", "r")
      listaReservadas = arquivo.read()
      listaReservadas = listaReservadas.split(",")
      arquivo.close()
      qtd = listaReservadas.count('')
      if qtd >= 1:
         listaReservadas.remove('')
      if len(listaReservadas) > 0 and (not "" in listaReservadas):
         listaReservadas = tint(listaReservadas)
         listaReservadas.sort()
         listaReservadas = tstr(listaReservadas)
         for i in listaReservadas: 
            lb3.insert(END, "MESA:  %s   TOTAL:  %s"%(i, nmesa(i)))
         if len(listaReservadas) > 42:
            lb3.insert(END, " ")

   style = ttk.Style()
   style.configure("PB.TButton", background="gray97", font=("Klavika Med Caps", 12))
   ################################################################
   def res():
      global lb1, lb3, listaDisponiveis, listaReservadas;
      select = lb1.get("active")#texto
      listaS = select.split(" ")
      numes = listaS[2]
      listaDisponiveis.remove(numes)
      listaReservadas.append(numes)
      qtd1 = lb1.size()
      if qtd1 > 0:
         for i in range(qtd1):
            lb1.delete(END)
            
      qtd2 = lb3.size()
      if qtd2 > 0:
         for i in range(qtd2):
            lb3.delete(END)
      guardaDis1()
      guardaRes3()
      chamaDis1()
      chamaRes3()
   def ocu1():
      global lb1, lb2, listaDisponiveis, listaOcupadas;
      select = lb1.get("active")#texto
      listaS = select.split(" ")
      numes = listaS[2]
      listaDisponiveis.remove(numes)
      listaOcupadas.append(numes)
      qtd1 = lb1.size()
      if qtd1 > 0:
         for i in range(qtd1):
            lb1.delete(END)
            
      qtd2 = lb2.size()
      if qtd2 > 0:
         for i in range(qtd2):
            lb2.delete(END)
      guardaDis1()
      guardaOcu2()
      chamaDis1()
      chamaOcu2()
   def imnf():
      global lb2, lb1, listaOcupadas, listaDisponiveis;
      select = lb2.get("active")#texto
      listaS = select.split(" ")
      numes = listaS[2]
      qtd1 = lb2.size()
      # aqui está o erro ele remove mesmo sem saber se o cliente vai pagar, a mesa fica disponivel
      listaOcupadas.remove(numes)
      listaDisponiveis.append(numes)
      if qtd1 > 0:
         for i in range(qtd1):
            lb2.delete(END)
      qtd2 = lb1.size()
      if qtd2 > 0:
         for i in range(qtd2):
            lb1.delete(END)
      guardaOcu2()
      guardaDis1()
      chamaOcu2()
      chamaDis1()
      janelaPrincipal.destroy()
      notaF(numes)
      chamaParaAbrir()
      #essa forma de chamar a janela principal está 
      #gerenciarJanela(nome, conta, usuario)
   def alc():
      global lb1, lb2, lb3;
      select = lb2.get("active")#texto
      listaS = select.split(" ")
      numes = listaS[2]
      janelaPrincipal.destroy()
      alocarC(numes)
      chamaParaAbrir()
      #gerenciarJanela(nome, conta, usuario)
   def dis():
      global lb1, lb3, listaDisponiveis, listaReservadas;
      select = lb3.get("active")#texto
      listaS = select.split(" ")
      numes = listaS[2]
      listaReservadas.remove(numes)
      listaDisponiveis.append(numes)
      qtd1 = lb3.size()
      if qtd1 > 0:
         for i in range(qtd1):
            lb3.delete(END)
            
      qtd2 = lb1.size()
      if qtd2 > 0:
         for i in range(qtd2):
            lb1.delete(END)
      guardaRes3()
      guardaDis1()
      chamaRes3()
      chamaDis1()
   def ocu2():
      global lb3, lb2, listaOcupadas, listaReservadas;
      select = lb3.get("active")#texto
      listaS = select.split(" ")
      numes = listaS[2]
      listaReservadas.remove(numes)
      listaOcupadas.append(numes)
      qtd1 = lb3.size()
      if qtd1 > 0:
         for i in range(qtd1):
            lb3.delete(END)
            
      qtd2 = lb2.size()
      if qtd2 > 0:
         for i in range(qtd2):
            lb2.delete(END)
      guardaRes3()
      guardaOcu2()
      chamaRes3()
      chamaOcu2()
   ################################################################
   lb1 = Listbox(frame1, height=23, width=80, font=("Consolas", 13))
   sb1 = Scrollbar(frame1)
   lb1.place(x=17, y=0)
   sb1.pack(side=LEFT, anchor=W, expand=1, fill=Y)
   sb1.configure(command=lb1.yview)
   lb1.configure(yscrollcommand= sb1.set)

   botaor1 = ttk.Button(frame1, text="Reservar", style="PB.TButton", takefocus=0, command=res)
   botaor1.place(x=742, y=1)
   botaoo1 = ttk.Button(frame1, text="ocupar", style="PB.TButton", takefocus=0, command=ocu1)
   botaoo1.place(x=742, y=33)
   #######
   lb2 = Listbox(frame2, height=23, width=80, font=("Consolas", 13))
   sb2 = Scrollbar(frame2)
   lb2.place(x=17, y=0)
   sb2.pack(side=LEFT, anchor=W, expand=1, fill=Y)
   sb2.configure(command=lb2.yview)
   lb2.configure(yscrollcommand= sb2.set)

   botaoi2 = ttk.Button(frame2, text="imprimir nota fiscal", style="PB.TButton", takefocus=0, command=imnf)
   botaoi2.place(x=742, y=1)
   botaoa2 = ttk.Button(frame2, text="alocar compra", style="PB.TButton", takefocus=0, command=alc)
   botaoa2.place(x=742, y=33)
   #######
   lb3 = Listbox(frame3, height=23, width=80, font=("Consolas", 13))
   sb3 = Scrollbar(frame3)
   lb3.place(x=17, y=0)
   sb3.place(x=0, y=0, height=tamaY-278)
   sb3.configure(command=lb3.yview)
   lb3.configure(yscrollcommand= sb3.set)

   botaod3 = ttk.Button(frame3, text="disponibilizar", style="PB.TButton", takefocus=0, command=dis)
   botaod3.place(x=742, y=1)
   botaoo3 = ttk.Button(frame3, text="ocupar", style="PB.TButton", takefocus=0, command=ocu2)
   botaoo3.place(x=742, y=33)
   ################################################################################

   n = 0
   def status():
      global n, canvas;
      if n%2 == 0:
         botao.place(x=tamaX-490, y=104)
         corP = "green4"
         canvas = Canvas(janelaPrincipal, width=472, height=tamaX*0.41544444, bg=corP, relief=FLAT)
         canvas.place(x=tamaX-476, y=102)
         banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor = banco.cursor()
         cursor.execute("SELECT * FROM info")
         info = cursor.fetchall()
         cursor.close()
         banco.close()
         Label(canvas, text="Informações sobre o usuário;", fg="white", bg=corP, font=("Arial", 14, "bold")).place(x=2, y=4)
         Label(canvas, text="Nome:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=30)
         Label(canvas, text="%s"%nome, fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=50)
         Label(canvas, text="Email Logado:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=71)
         Label(canvas, text="%s"%usuario, fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=95)
         Label(canvas, text="Tipo Conta:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=118)
         Label(canvas, text="%s"%conta, fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=140)
         Label(canvas, text="Informações sobre a empresa;", fg="white", bg=corP, font=("Arial", 14,"bold")).place(x=2, y=163)
         Label(canvas, text="Nome Fantasia:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=188)
         Label(canvas, text="%s"%info[1][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=209)
         Label(canvas, text="Área Comercial:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=230)
         Label(canvas, text="%s"%info[2][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=251)
         Label(canvas, text="Razão Social:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=272)
         Label(canvas, text="%s"%info[3][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=293)
         Label(canvas, text="Endereço:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=313)
         Label(canvas, text="%s"%info[5][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=334)
         Label(canvas, text="Quantidade de Dono:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=354)
         Label(canvas, text="%s"%info[12][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=375)
         Label(canvas, text="Quantidade de Gerente:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=395)
         Label(canvas, text="%s"%info[11][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=416)
         Label(canvas, text="Quantidade de Funcionário:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=436)
         Label(canvas, text="%s"%info[12][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=457)
         Label(canvas, text="Quantidade de Produto:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=478)
         Label(canvas, text="%s"%info[13][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=499)
         Label(canvas, text="Quantidade de Mesa:", fg="white", bg=corP, font=("Arial", 12)).place(x=8, y=520)
         Label(canvas, text="%s"%info[9][2], fg="white", bg=corP, font=("Arial", 13, "bold")).place(x=18, y=541)
      else:
         janelaPrincipal.after(1, canvas.destroy)
         botao.place(x=tamaX-15, y=104)
      n += 1
   style = ttk.Style()
   style.configure("BW.TLabel", background="green4", relief=FLAT)

   ft = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/ImageResizer.png")
   botao = ttk.Button(janelaPrincipal, image=ft, style="BW.TLabel", command=status, takefocus=0)
   botao.place(x=tamaX-15, y=104)

   chamaDis1()
   chamaOcu2()
   chamaRes3()
   if conta.capitalize() != "Administrador":
      novaC.configure(state="disabled")
      editarM.configure(state="disabled")
      editarP.configure(state="disabled")
      config.configure(state="disabled")
   
      
   janelaPrincipal.protocol("WM_DELETE_WINDOW", fechar)
   janelaPrincipal.geometry("%dx%d"%(tamaX, tamaY))
   janelaPrincipal.state("zoomed")
   janelaPrincipal.title(" TMS")
   janelaPrincipal.iconbitmap("C:/ProgramData/TMS/Imagens/unnamed.ico")
   janelaPrincipal.mainloop()
