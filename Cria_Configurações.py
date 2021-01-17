from tkinter import *
from tkinter import ttk
from tkinter import tix
from InformacaoDono import donoJanela 
from InformacaoFuncionario import funcionarioJanela
from InformacaoGerente import gerenteJanela
from InformacaoProduto import produtoJanela
import sqlite3

def configuraçaoJanela():
   global nme, labelN, campoP, campo1P, campo2P, cursorM, bancoM, janelacon, campoN, campoS, campoF, campoE, campo3P;
   janelacon = tix.Tk()

   tamaX = janelacon.winfo_screenwidth()
   tamaY = janelacon.winfo_screenheight()

   painel = Frame(janelacon)
   painel.pack(side=TOP, expand=1, fill=BOTH)

   panedD = tix.PanedWindow(painel, orientation='horizontal', height=542, background="gray80")
   configure= panedD.add('configure')
   list1= tix.Listbox(configure, background="gray80")
   list1.pack(side= LEFT, expand=1, fill= BOTH)

   configure1 = panedD.add('configure1')
   list11 = tix.Listbox(configure1, background="gray80")
   list11.pack(side= LEFT, expand=1, fill= BOTH)

   panedD.pack(side=TOP, expand=1, fill=BOTH)

   #
   style = ttk.Style()
   style.configure("BT.TButton", background="gray80")
   ########################
   def informaM(nome, tipo, conta):
      global cursorM, bancoM, janelacon, campoN, campoS, campoF, campoE;
      jainforma = Toplevel()
      tW = jainforma.winfo_screenwidth()
      tH = jainforma.winfo_screenheight()

      jainforma.transient(janelacon)
      jainforma.grab_set()
         
      bancoM = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursorM = bancoM.cursor()
      select = "SELECT * FROM %s WHERE nome = ?"%tipo
      cursorM.execute(select, (nome,))
      dados = cursorM.fetchall()      
      ###################
      Label(jainforma, text="Informações %s"%conta, font=("Consolas", 25, "bold"), background="gray90").pack(side=TOP)

      Label(jainforma, text="Nome:", font=("Consolas", 16, "bold"), background="gray90").place(x=10, y=90)
      Label(jainforma, text="CPF:", font=("Consolas", 16, "bold"), background="gray90").place(x=10, y=160)
      Label(jainforma, text="RG:", font=("Consolas", 16, "bold"), background="gray90").place(x=10, y=230)
      Label(jainforma, text="Salário:", font=("Consolas", 16, "bold"), background="gray90").place(x=10, y=300)

      campoN = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoN.place(x=125, y=90)
      campoC = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoC.place(x=125, y=160)
      campoR = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoR.place(x=125, y=230)
      campoS = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoS.place(x=125, y=300)

      Label(jainforma, text="Função:", font=("Consolas", 16, "bold"), background="gray90").place(x=330, y=90)
      Label(jainforma, text="Entrada:", font=("Consolas", 16, "bold"), background="gray90").place(x=330, y=160)
      Label(jainforma, text="Nascimento:", font=("Consolas", 16, "bold"), background="gray90").place(x=330, y=230)
      Label(jainforma, text="Email:", font=("Consolas", 16, "bold"), background="gray90").place(x=330, y=300)

      campoF = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoF.place(x=485, y=90)
      campoE = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoE.place(x=485, y=160)
      campoNS = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoNS.place(x=485, y=230)
      campoEL = ttk.Entry(jainforma, font=("Consolas", 13, "bold"))
      campoEL.place(x=485, y=300)

      campoN.insert(END, dados[0][1])
      campoC.insert(END, dados[0][2])
      campoR.insert(END, dados[0][3])
      campoS.insert(END, dados[0][4])
      campoF.insert(END, dados[0][5])
      campoE.insert(END, dados[0][6])
      campoNS.insert(END, dados[0][7])
      campoEL.insert(END, dados[0][8])
      
      jainforma.geometry("%dx%d+%d+%d"%(tW*0.5, tH*0.5, tW*0.24, tH*0.22))
      jainforma["bg"]="gray90"
      jainforma.title("TMS")
      jainforma.iconbitmap("C:/ProgramData/TMS/Imagens/unnamed.ico")
      jainforma.mainloop()

   def editarPro(nome, tipo):
      global cursorP, bancoP, janelacon, tipoP, nomeP, precoP;
      janelaPro = Toplevel()
      tamaTx = janelaPro.winfo_screenwidth()
      tamaTy = janelaPro.winfo_screenheight()

      janelaPro.transient(janelacon)
      janelaPro.grab_set()
            
      bancoP = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursorP = bancoP.cursor()
      select = "SELECT * FROM %s WHERE nome = ?"%tipo
      cursorP.execute(select, (nome,))
      dados = cursorP.fetchall()


      def editaNP(nomAnt, nomAtu):
         global cursorM, bancoP;
         edite = "UPDATE %s SET nome = ? WHERE nome = ?"%tipo
         cursorP.execute(edite, (nomAtu,nomAnt,))
         bancoP.commit()
      def editaTP(nome, salAnt, salAtu):
         global cursorM, bancoP;
         edite = "UPDATE %s SET nome = ?, tipo = ? WHERE tipo = ?"%tipo
         cursorP.execute(edite,(nome, salAtu, salAnt,))
         bancoP.commit()
      def editaPP(nome, funvAnt, funvAtu):
         global cursorM, bancoP;
         edite = "UPDATE %s SET  nome = ?, preco = ? WHERE preco = ?"%tipo
         cursorP.execute(edite, (nome, funvAtu, funvAnt,))
         bancoP.commit()
      def can():
         janelaPro.destroy()
      def alt():
         global tipoP, nomeP, precoP;
         nome = nomeP.get()
         tipo = tipoP.get()
         preco = precoP.get()
         editaNP(dados[0][2], nome)
         editaTP(nome, dados[0][1], tipo)
         editaPP(nome, dados[0][3], preco)
         janelaPro.destroy()

      Label(janelaPro, text="Editar Dados", font=("Consolas", 25, "bold"), background="gray90").pack(side=TOP)

      Label(janelaPro, text="Nome:", font=("Consolas", 16, "bold"), background="gray90").place(x=170, y=80)
      Label(janelaPro, text="Tipo:", font=("Consolas", 16, "bold"), background="gray90").place(x=170, y=150)
      Label(janelaPro, text="Preço:", font=("Consolas", 16, "bold"), background="gray90").place(x=170, y=220)

      nomeP = ttk.Entry(janelaPro, font=("Consolas", 14, "bold"))
      nomeP.place(x=300, y=80)
      tipoP = ttk.Entry(janelaPro, font=("Consolas", 14, "bold"))
      tipoP.place(x=300, y=150)
      precoP = ttk.Entry(janelaPro, font=("Consolas", 14, "bold"))
      precoP.place(x=300, y=220)

      style = ttk.Style()
      style.configure("BP.TButton", font=("Consolas", 13),  background="gray90")
      botaoC = ttk.Button(janelaPro, text="Cancelar", takefocus=0, style="BP.TButton", padding=5, command=can)
      botaoA =  ttk.Button(janelaPro, text="Alterar", takefocus=0, style="BP.TButton", padding=5, command=alt)
      botaoC.place(x=225, y=335)
      botaoA.place(x=350, y=335)

      tipoP.insert(END, dados[0][1])
      nomeP.insert(END, dados[0][2])
      precoP.insert(END, dados[0][3])   

      janelaPro.config(bg="gray90")
      janelaPro.title("TMS")
      janelaPro.geometry("%dx%d+%d+%d"%(tamaTx*0.5, tamaTy*0.5, tamaTx*0.24, tamaTy*0.22))
      janelaPro.iconbitmap("C:/ProgramData/TMS/Imagens/unnamed.ico")
      janelaPro.mainloop()
      
   def editeM(nome, tipo):
      global cursorM, bancoM, janelacon, campoN, campoS, campoF, campoE;
      jaedite = Toplevel()
      tW = jaedite.winfo_screenwidth()
      tH = jaedite.winfo_screenheight()

      jaedite.transient(janelacon)
      jaedite.grab_set()
      
      bancoM = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursorM = bancoM.cursor()
      select = "SELECT * FROM %s WHERE nome = ?"%tipo
      cursorM.execute(select, (nome,))
      dados = cursorM.fetchall()
      ###################
      def editaNF(nomAnt, nomAtu):
         global cursorM, bancoM;
         edite = "UPDATE %s SET nome = ? WHERE nome = ?"%tipo
         cursorM.execute(edite, (nomAtu,nomAnt,))
         bancoM.commit()
      def editaCF(nome, salAnt, salAtu):
         global cursorM, bancoM;
         edite = "UPDATE %s SET nome = ?, salario = ? WHERE salario = ?"%tipo
         cursorM.execute(edite,(nome, salAtu, salAnt,))
         bancoM.commit()
      def editaPF(nome, funvAnt, funvAtu):
         global cursorM, bancoM;
         edite = "UPDATE %s SET  nome = ?, funcao = ? WHERE funcao = ?"%tipo
         cursorM.execute(edite, (nome, funvAtu, funvAnt,))
         bancoM.commit()
      def editaSF(nome, emaAnt, emaAtu):
         global cursorM, bancoM;
         edite = "UPDATE %s SET nome = ?, email = ? WHERE email = ?"%tipo
         cursorM.execute(edite, (nome, emaAtu, emaAnt,))
         bancoM.commit()
      def can():
         jaedite.destroy()
      def alt():
         global campoN, campoS, campoF, campoE;
         nome = campoN.get()
         salario = campoS.get()
         funcao = campoF.get()
         email = campoE.get()
         editaNF(dados[0][1], nome)
         editaCF(nome, dados[0][4], salario)
         editaPF(nome, dados[0][5], funcao)
         editaSF(nome, dados[0][8], email)
         jaedite.destroy()
         
      ###################
      Label(jaedite, text="Editar Dados", font=("Consolas", 25, "bold"), background="gray90").pack(side=TOP)

      Label(jaedite, text="Nome:", font=("Consolas", 16, "bold"), background="gray90").place(x=170, y=80)
      Label(jaedite, text="Salário:", font=("Consolas", 16, "bold"), background="gray90").place(x=170, y=150)
      Label(jaedite, text="Funçao:", font=("Consolas", 16, "bold"), background="gray90").place(x=170, y=220)
      Label(jaedite, text="Email:", font=("Consolas", 16, "bold"), background="gray90").place(x=170, y=290)

      campoN = ttk.Entry(jaedite, font=("Consolas", 14, "bold"))
      campoN.place(x=300, y=80)
      campoS = ttk.Entry(jaedite, font=("Consolas", 14, "bold"))
      campoS.place(x=300, y=150)
      campoF = ttk.Entry(jaedite, font=("Consolas", 14, "bold"))
      campoF.place(x=300, y=220)
      campoE = ttk.Entry(jaedite, font=("Consolas", 14, "bold"))
      campoE.place(x=300, y=290)

      style = ttk.Style()
      style.configure("BP.TButton", font=("Consolas", 13),  background="gray90")
      botaoC = ttk.Button(jaedite, text="Cancelar", takefocus=0, style="BP.TButton", padding=5, command=can)
      botaoA =  ttk.Button(jaedite, text="Alterar", takefocus=0, style="BP.TButton", padding=5, command=alt)
      botaoC.place(x=225, y=335)
      botaoA.place(x=350, y=335)

      campoN.insert(END, dados[0][1])
      campoS.insert(END, dados[0][4])
      campoF.insert(END, dados[0][5])
      campoE.insert(END, dados[0][8])

      jaedite.geometry("%dx%d+%d+%d"%(tW*0.5, tH*0.5, tW*0.24, tH*0.22))
      jaedite["bg"]="gray90"
      jaedite.title("TMS")
      jaedite.iconbitmap("C:/ProgramData/TMS/Imagens/unnamed.ico")
      jaedite.mainloop()
   
   def verificar(nome, tipo):
      try:
         banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor = banco.cursor()
         select = "SELECT * FROM %s WHERE nome = ?"%tipo
         cursor.execute(select, (nome,))
         dados = cursor.fetchall()
         info = dados[0][2]
         return True
      except:
         return False
   def aDono():
      janelacon.destroy()
      donoJanela(1)
      configuraçaoJanela()
   def eDono():
      global campoP;
      nome = campoP.get()
      valor = verificar(nome, "dadosDono")
      if valor == True:
         editeM(nome, "dadosDono")
   def exDono():
      global campoP;
      nome = campoP.get()
      valor = verificar(nome, "dadosDono")
      if valor == True:
         banco = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor = banco.cursor()
         delete = "DELETE FROM dadosDono WHERE nome = ?"
         cursor.execute(delete, (nome,))
         banco.commit()
         cursor.close()
         banco.close()
         preencheD()
   def iDono():
      global campoP;
      nome = campoP.get()
      valor = verificar(nome, "dadosDono")
      if valor == True:
         informaM(nome, "dadosDono", "Dono")
   def aGerente():
      janelacon.destroy()
      gerenteJanela(1)
      configuraçaoJanela()
   def eGerente():
      global campo1P;
      nome = campo1P.get()
      valor = verificar(nome, "infoGerente")
      if valor == True:
         editeM(nome, "infoGerente")
   def exGerente():
      global campo1P;
      nome = campo1P.get()
      valor = verificar(nome, "infoGerente")
      if valor == True:
         banco = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor = banco.cursor()
         delete = "DELETE FROM infoGerente WHERE nome = ?"
         cursor.execute(delete, (nome,))
         banco.commit()
         cursor.close()
         banco.close()
         preencheG()
   def iGerente():
      global campo1P;
      nome = campo1P.get()
      valor = verificar(nome, "infoGerente")
      if valor == True:
         informaM(nome, "infoGerente", "Gerente")
   def aFuncionario():
      janelacon.destroy()
      funcionarioJanela(1)
      configuraçaoJanela()
   def eFuncionario():
      global campo2P;
      nome = campo2P.get()
      valor = verificar(nome, "infoFuncionario")
      if valor == True:
         editeM(nome, "infoFuncionario")
   def exFuncionario():
      global campo2P;
      nome = campo2P.get()
      valor = verificar(nome, "infoFuncionario")
      if valor == True:
         banco = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor = banco.cursor()
         delete = "DELETE FROM infoFuncionario WHERE nome = ?"
         cursor.execute(delete, (nome,))
         banco.commit()
         cursor.close()
         banco.close()
         preencheF()
   def iFuncionario():
      global campo2P;
      nome = campo2P.get()
      valor = verificar(nome, "infoFuncionario")
      if valor == True:
         informaM(nome, "infoFuncionario", "Funcionario")
   def aProduto():
      janelacon.destroy()
      produtoJanela(1)
      configuraçaoJanela()
   def eProduto():
      global campo3P;
      nome = campo3P.get()
      valor = verificar(nome, "dadosProduto")
      if valor == True:
         editarPro(nome, "dadosProduto")
   def exProduto():
      global campo3P;
      nome = campo3P.get()
      valor = verificar(nome, "dadosProduto")
      if valor == True:
         banco = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor = banco.cursor()
         delete = "DELETE FROM dadosProduto WHERE nome = ?"
         cursor.execute(delete, (nome,))
         banco.commit()
         cursor.close()
         banco.close()
         preencheP()
   def eInformacao():
      pass
   ########################

   ttk.Label(list1, text="Configuração Dono", font=("Consolas", 14, "bold"), background="gray80").place(x=140, y=6)
   ttk.Label(list1, text="Configuração Gerente", font=("Consolas", 14, "bold"), background="gray80").place(x=580, y=6)
   ttk.Label(list1, text="Configuração Funcionário", font=("Consolas", 14, "bold"), background="gray80").place(x=1020, y=6)

   BarraVertical = Scrollbar(list1, orient=VERTICAL)
   texto = Text(list1, insertontime=1, width=45, height=15, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto.configure(yscrollcommand=BarraVertical.set)
   BarraVertical.place(x=10, y=35, height=305)
   BarraVertical.configure(command= texto.yview)
   texto.place(x=27, y=35)
   botaoED = ttk.Button(list1, text="Editar", takefocus=0, style="BT.TButton", command=eDono)
   botaoEX = ttk.Button(list1, text="Excluir", takefocus=0, style="BT.TButton", command=exDono)
   botaoC = ttk.Button(list1, text="Criar", takefocus=0, style="BT.TButton", command=aDono)
   botaoI = ttk.Button(list1, text="Informação", takefocus=0, style="BT.TButton", command=iDono)
   campoP = ttk.Combobox(list1, font=("Consolas", 13), width=18)

   botaoED.place(x=200, y=350)
   botaoEX.place(x=281, y=350)
   botaoC.place(x=362, y=350)
   botaoI.place(x=10, y=380)
   campoP.place(x=10, y=350)
   #######################
   BarraVertical1 = Scrollbar(list1, orient=VERTICAL)
   texto1 = Text(list1, insertontime=1, width=45, height=15, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto1.configure(yscrollcommand=BarraVertical1.set)
   BarraVertical1.place(x=465, y=35, height=305)
   BarraVertical1.configure(command= texto1.yview)
   texto1.place(x=482, y=35)
   botao1ED = ttk.Button(list1, text="Editar", takefocus=0, style="BT.TButton", command=eGerente)
   botao1EX = ttk.Button(list1, text="Excluir", takefocus=0, style="BT.TButton", command=exGerente)
   botao1C = ttk.Button(list1, text="Criar", takefocus=0, style="BT.TButton", command=aGerente)
   botao1I = ttk.Button(list1, text="Informação", takefocus=0, style="BT.TButton", command=iGerente)
   campo1P = ttk.Combobox(list1, font=("Consolas", 13), width=18)

   botao1ED.place(x=655, y=350)
   botao1EX.place(x=736, y=350)
   botao1C.place(x=817, y=350)
   botao1I.place(x=465, y=380)
   campo1P.place(x=465, y=350)
   #######################
   BarraVertical2 = Scrollbar(list1, orient=VERTICAL)
   texto2 = Text(list1, insertontime=1, width=45, height=15, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto2.configure(yscrollcommand=BarraVertical2.set)
   BarraVertical2.place(x=924, y=35, height=305)
   BarraVertical2.configure(command= texto2.yview)
   texto2.place(x=941, y=35)
   botao2ED = ttk.Button(list1, text="Editar", takefocus=0, style="BT.TButton", command=eFuncionario)
   botao2EX = ttk.Button(list1, text="Excluir", takefocus=0, style="BT.TButton", command=exFuncionario)
   botao2C = ttk.Button(list1, text="Criar", takefocus=0, style="BT.TButton", command=aFuncionario)
   botao2I = ttk.Button(list1, text="Informação", takefocus=0, style="BT.TButton", command=iFuncionario)
   campo2P = ttk.Combobox(list1, font=("Consolas", 13), width=18)

   botao2ED.place(x=1115, y=350)
   botao2EX.place(x=1196, y=350)
   botao2C.place(x=1277, y=350)
   botao2I.place(x=925, y=380)
   campo2P.place(x=925, y=350)
   ###########################
   def preencheD():
      texto.configure(state="normal")
      texto.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM dadosDono")
      dados = cursor.fetchall()
      for i, n in enumerate(dados):
         texto.insert(END, "DONO %s\n"%(int(i)+1))
         texto.insert(END, "Nome: %s\n"%n[1])
         texto.insert(END, "CPF: %s\n"%n[2])
         texto.insert(END, "Email: %s"%n[8])
         texto.insert(END, "\n")
      texto.config(state="disabled")
   def preencheG():
      texto1.configure(state="normal")
      texto1.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM infoGerente")
      dados = cursor.fetchall()
      for i, n in enumerate(dados):
         texto1.insert(END, "GERENTE %s\n"%(int(i)+1))
         texto1.insert(END, "Nome: %s\n"%n[1])
         texto1.insert(END, "CPF: %s\n"%n[2])
         texto1.insert(END, "Email: %s\n"%n[8])
         texto1.insert(END, "\n")
      texto1.config(state="disabled")
   def preencheF():
      texto2.configure(state="normal")
      texto2.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM infoFuncionario")
      dados = cursor.fetchall()
      for i, n in enumerate(dados):
         texto2.insert(END, "FUNCIONÁRIO %s\n"%(int(i)+1))
         texto2.insert(END, "Nome: %s\n"%n[1])
         texto2.insert(END, "CPF: %s\n"%n[2])
         texto2.insert(END, "Email: %s"%n[8])
         texto2.insert(END, "\n")
      texto2.config(state="disabled")
   preencheD()
   preencheG()
   preencheF()
   ###########################

   ttk.Label(list1, text="Configuração Produto", font=("Consolas", 14, "bold"), background="gray80").place(x=150, y=381)
   ttk.Label(list1, text="Configuração Empresa", font=("Consolas", 14, "bold"), background="gray80").place(x=707, y=381)

   #######################
   BarraVertical3 = Scrollbar(list1, orient=VERTICAL)
   texto3 = Text(list1, insertontime=1, width=50, height=14, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto3.configure(yscrollcommand=BarraVertical3.set)
   BarraVertical3.place(x=15, y=410, height=287)
   BarraVertical3.configure(command= texto3.yview)
   texto3.place(x=32, y=410)
   botao3ED = ttk.Button(list1, text="Editar", takefocus=0, style="BT.TButton", command=eProduto)
   botao3EX = ttk.Button(list1, text="Excluir", takefocus=0, style="BT.TButton", command=exProduto)
   botao3C = ttk.Button(list1, text="Criar", takefocus=0, style="BT.TButton", command=aProduto)
   campo3P = ttk.Combobox(list1, font=("Consolas", 13), width=18)

   botao3ED.place(x=490, y=440)
   botao3EX.place(x=490, y=470)
   botao3C.place(x=490, y=500)
   campo3P.place(x=490, y=410)
   #######################
   BarraVertical4 = Scrollbar(list1, orient=VERTICAL)
   texto4 = Text(list1, insertontime=1, width=50, height=14, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto4.configure(yscrollcommand=BarraVertical4.set)
   BarraVertical4.place(x=690, y=410, height=287)
   BarraVertical4.configure(command= texto4.yview)
   texto4.place(x=707, y=410)
   botao4ED = ttk.Button(list1, text="Editar", takefocus=0, style="BT.TButton", command=eInformacao)
  
   botao4ED.place(x=1165, y=410)
   ######################
   def preencheP():
      texto3.configure(state="normal")
      texto3.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM dadosProduto")
      dados = cursor.fetchall()
      for i, n in enumerate(dados):
         texto3.insert(END, "Produto %s\n"%(int(i)+1))
         texto3.insert(END, "Tipo: %s\n"%n[1])
         texto3.insert(END, "Nome: %s\n"%n[2])
         texto3.insert(END, "Preço: %s\n"%n[3])
         texto3.insert(END, "\n")
      texto3.config(state="disabled")
   def preencheE():
      texto4.configure(state="normal")
      texto4.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM info")
      dados = cursor.fetchall()
      texto4.insert(END, "Sobre Empresa\n")
      for i, n in enumerate(dados):
         if i <= 13:
            texto4.insert(END, "%s: %s"%(n[1], n[2]))
            texto4.insert(END, "\n")
         else:
            break
      texto4.config(state="disabled")
   preencheP()
   preencheE()
   ###########################
   def eAdmin():
      pass
   def exAdmin():
      pass
   def eGeren():
      pass
   def exGeren():
      pass
   def eSem():
      pass
   def aTg():
      pass
   def aTs():
      pass
   def gTa():
      pass
   def gTs():
      pass
   def sTa():
      pass
   def sTg():
      pass
   def sub():
      global nme, labelN;
      nme -= 1
      if nme != 0: 
         labelN["text"]="%s remover mesas"%nme
      else:
         labelN["text"]="%s"%nme
   def mai():
      global nme, labelN;
      nme += 1
      if nme != 0: 
         labelN["text"]="%s adicionar mesas"%nme
      else:
         labelN["text"]="%s"%nme
   def alter():
      pass
   ###########################
   ttk.Label(list11, text="Conta Administrador", font=("Consolas", 14, "bold"), background="gray80").place(x=140, y=6)
   ttk.Label(list11, text="Conta Gerengiador", font=("Consolas", 14, "bold"), background="gray80").place(x=580, y=6)
   ttk.Label(list11, text="Sem Conta", font=("Consolas", 14, "bold"), background="gray80").place(x=1110, y=6)
   ttk.Label(list11, text="Configuração Mesa", font=("Consolas", 14, "bold"), background="gray80").place(x=10, y=422)
   
   BarraVertical11 = Scrollbar(list11, orient=VERTICAL)
   texto11 = Text(list11, insertontime=1, width=45, height=15, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto11.configure(yscrollcommand=BarraVertical11.set)
   BarraVertical11.place(x=10, y=35, height=305)
   BarraVertical11.configure(command= texto11.yview)
   texto11.place(x=27, y=35)
   botao11ED = ttk.Button(list11, text="Editar", takefocus=0, style="BT.TButton", padding=3, width=17, command=eAdmin)
   botao11EX = ttk.Button(list11, text="Excluir", takefocus=0, style="BT.TButton", padding=3, width=17, command=exAdmin)
   botao11C = ttk.Button(list11, text="Tornar Gerenciador", takefocus=0, style="BT.TButton", padding=4, width=19, command=aTg)
   botao11I = ttk.Button(list11, text="Tornar Sem conta", takefocus=0, style="BT.TButton", padding=4, width=19, command=aTs)
   campo11P = ttk.Combobox(list11, font=("Consolas", 13), width=18)

   botao11ED.place(x=200, y=349)
   botao11EX.place(x=323, y=349)
   botao11C.place(x=10, y=380)
   botao11I.place(x=145, y=380)
   campo11P.place(x=10, y=350)
   #######################
   BarraVertical22 = Scrollbar(list11, orient=VERTICAL)
   texto22 = Text(list11, insertontime=1, width=45, height=15, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto22.configure(yscrollcommand=BarraVertical22.set)
   BarraVertical22.place(x=465, y=35, height=305)
   BarraVertical22.configure(command= texto22.yview)
   texto22.place(x=482, y=35)
   botao22ED = ttk.Button(list11, text="Editar", takefocus=0, style="BT.TButton", padding=3, width=17, command=exGeren)
   botao22EX = ttk.Button(list11, text="Excluir", takefocus=0, style="BT.TButton", padding=3, width=17, command=exGeren)
   botao22C = ttk.Button(list11, text="Tornar Administrador", takefocus=0, style="BT.TButton", padding=4, width=19, command=gTa)
   botao22I = ttk.Button(list11, text="Tornar Sem conta", takefocus=0, style="BT.TButton", padding=4, width=19, command=gTs)
   campo22P = ttk.Combobox(list11, font=("Consolas", 13), width=18)

   botao22ED.place(x=655, y=350)
   botao22EX.place(x=777, y=350)
   botao22C.place(x=465, y=380)
   botao22I.place(x=605, y=380)
   campo22P.place(x=465, y=350)
   #######################
   BarraVertical33 = Scrollbar(list11, orient=VERTICAL)
   texto33 = Text(list11, insertontime=1, width=45, height=15, cursor="xterm",\
                 relief="flat", fg="Black", font=("Consolas", 13, "bold"),\
                 selectforeground="Black")
   texto33.configure(yscrollcommand=BarraVertical33.set)
   BarraVertical33.place(x=924, y=35, height=305)
   BarraVertical33.configure(command= texto33.yview)
   texto33.place(x=941, y=35)
   botao33ED = ttk.Button(list11, text="Editar", takefocus=0, style="BT.TButton", padding=3, width=17, command=eSem)
   botao33C = ttk.Button(list11, text="Tornar Administrador", takefocus=0, style="BT.TButton", padding=4, width=19, command=sTa)
   botao33I = ttk.Button(list11, text="Tornar Gerenciador", takefocus=0, style="BT.TButton", padding=4, width=19, command=sTg)
   campo33P = ttk.Combobox(list11, font=("Consolas", 13), width=18)

   botao33ED.place(x=1115, y=350)
   botao33C.place(x=925, y=380) 
   botao33I.place(x=1065, y=380)
   campo33P.place(x=925, y=350)

   ##
   nme = 0
   style = ttk.Style()
   style.configure("BS.TButton", background="gray80", font=("Consolas", 16, "bold"))
   botaoplus = ttk.Button(list11, text="+", takefocus=0, style="BS.TButton", padding=6, command=mai)
   labelN = ttk.Label(list11, text="%s"%nme, takefocus=0, background="gray80", font=("Consolas", 16, "bold"))
   botaomenos = ttk.Button(list11, text="-", takefocus=0, style="BS.TButton", padding=6, command=sub)
   botaoA = ttk.Button(list11, text="Alterar", takefocus=0, style="BS.TButton", padding=6, command=alter)

   botaoplus.place(x=25, y=460)
   labelN.place(x=25, y=520)
   botaomenos.place(x=25, y=560)
   botaoA.place(x=25, y=620)
   ###########################
   def preencheCA():
      texto11.configure(state="normal")
      texto11.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/contaAcesso.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM contaAdministrador")
      dados = cursor.fetchall()
      for i, n in enumerate(dados):
         texto11.insert(END, "Conta %s\n"%(int(i)+1))
         texto11.insert(END, "Nome: %s\n"%n[4])
         texto11.insert(END, "Tipo: %s\n"%n[3])
         texto11.insert(END, "Email: %s\n"%n[1])
         texto11.insert(END, "Senha: %s"%n[2])
         texto11.insert(END, "\n")
      texto11.config(state="disabled")
   def preencheCG():
      texto22.configure(state="normal")
      texto22.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/contaAcesso.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM contaGerenciamento")
      dados = cursor.fetchall()
      for i, n in enumerate(dados):
         texto22.insert(END, "Conta %s\n"%(int(i)+1))
         texto22.insert(END, "Nome: %s\n"%n[4])
         texto22.insert(END, "Tipo: %s\n"%n[3])
         texto22.insert(END, "Email: %s\n"%n[1])
         texto22.insert(END, "Senha: %s"%n[2])
         texto22.insert(END, "\n")
      texto22.config(state="disabled")
   def preencheSC():
      texto33.configure(state="normal")
      texto33.delete("1.0", END)
      banco = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/contaAcesso.db")
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM semConta")
      dados = cursor.fetchall()
      for i, n in enumerate(dados):
         texto33.insert(END, "Conta %s\n"%(int(i)+1))
         texto33.insert(END, "Nome: %s\n"%n[4])
         texto33.insert(END, "Tipo: %s\n"%n[3])
         texto33.insert(END, "Email: %s\n"%n[1])
         texto33.insert(END, "Senha: %s"%n[2])
         texto33.insert(END, "\n")
      texto33.config(state="disabled")
   preencheCA()
   preencheCG()
   preencheSC()
   ###########################

   janelacon.geometry("%dx%d+%d+%d"%(tamaX, tamaY, 0, 0))
   janelacon.state("zoomed")
   janelacon["bg"]="gray80"
   janelacon.title("TMS")
   janelacon.iconbitmap("C:/ProgramData/TMS/Imagens/unnamed.ico")
   janelacon.mainloop()
