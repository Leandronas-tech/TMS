from tkinter import*
from tkinter import ttk
from tkinter import tix
import sqlite3
from InformacaoDono import donoJanela
from InformacaoFuncionario import funcionarioJanela
from InformacaoGerente import gerenteJanela
from InformacaoProduto import produtoJanela
from Entrar_conta import entrarJanela

def criaDadoMesa():
   global valorMesa;
   bancoMesa = sqlite3.Connection("C:/ProgramData/TMS/bancoMesa/mesasDados.db")
   cursoMesa = bancoMesa.cursor()
   for i in range(1, int(valorMesa)+1):
      cursoMesa.execute("CREATE TABLE IF NOT EXISTS _%s_(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                        tipo TEXT, nome TEXT, qtd INTEGER, preco REAL)"%(i))
   bancoMesa.commit()
   cursoMesa.close()
   bancoMesa.close()
def arquivoMesas():
   global valorMesa;
   arq1 = open("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt", "w")
   arq2 = open("C:/ProgramData/TMS/bancoMesa/mesasOcupadas.txt", "w")
   arq3 = open("C:/ProgramData/TMS/bancoMesa/mesasReservadas.txt", "w")
   arq4 = open("C:/ProgramData/TMS/bancoMesa/mesaNumero.txt", "w")
   arq1.close()
   arq2.close()
   arq3.close()
   arq4.close()
   ########
   arq1 = open("C:/ProgramData/TMS/bancoMesa/mesasDisponiveis.txt", "a")
   arq4 = open("C:/ProgramData/TMS/bancoMesa/mesaNumero.txt", "a")
   arq4.write(str(valorMesa))
   for i in range(1, int(valorMesa)+1):
      if i != int(valorMesa):
         arq1.write(str(i)+",")
      else:
         arq1.write(str(i))
   arq1.close()
   arq4.close()
def guardarDados():
   global num, listaValor, listaInfo;
   bancoInfo = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
   cursoInfo = bancoInfo.cursor()
   bancoInfo.execute("CREATE TABLE IF NOT EXISTS info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                     informacao TEXT, valor TEXT)")
   inserir = "INSERT INTO info(informacao, valor) VALUES(?, ?)"
   for i in range(len(listaInfo)):
      cursoInfo.execute(inserir, (listaInfo[i], listaValor[i],))

   bancoInfo.commit()
   cursoInfo.close()
   bancoInfo.close()
def preencheLista():
   global listaValor, variavelB, variavelR, nomeF, social, CNPJ, endereco, cidade, estado, CEP, nomeR, cpf, cargo, telefon, e_mail, mesa, dono, gerente, funcio, produto, senhapin, senhapinR;
   listaValor.append(senhapin.get())
   if variavelB.get() == 1:
      listaValor.append("Bar")
   else:
      listaValor.append("Restaurante")
   listaValor.extend([nomeF.get(), social.get(), CNPJ.get(), endereco.get(), cidade.get(), estado.get(), CEP.get(),])
   listaValor.extend([mesa.get(), dono.get(), gerente.get(), funcio.get(), produto.get(),])
   listaValor.extend([nomeR.get(), cpf.get(), cargo.get(), telefon.get(), e_mail.get(),])
valorDono = 0
valorGerente = 0
valorFuncionario = 0
valorProduto = 0
valorMesa = 0
valorSenha = ""
valorSenhaR = ""
valorSR = 0
valorSB = 0
# var para informações da empresa
valorNE =""
valorRE = ""
valorCNE = ""
valorEE = ""
valorCE = ""
valorESE = ""
valorCEE = ""
# var para informações do responsável
valorNR = ""
valorCR = ""
valorCAR = ""
valorTR = ""
valorER = ""
################################
listaInfo = ["Senha Pin", "Área Setor Comercia", "Nome Fantasia", "Razão Social", "CNPJ", "Endereço", "Cidade", "Estado", "CEP", "Quantidade de Mesa", "Quantidade de Dono", "Quantidade de Gerente", "Quantidade de Funcionário", "Quantidade de Produto", "Nome", "CPF", "Cargo", "Telefone", "E-mail"]
listaValor = []
def principal():
   global listaInfo, listaValor, disabledB, disabledR, janela, painel, borda,  corP, corL, corD, btB, btR, clickT, nomeF, social, CNPJ, endereco, cidade, estado, CEP, nomeR, cpf, cargo, telefon, e_mail, mesa, dono, gerente, funcio, produto, senhapin, senhapinR, valorDono, valorGerente, valorFuncionario, valorProduto, valorMesa, valorSenha, valorSenhaR, valorNE, valorRE, valorCNE, valorEE, valorCE, valorESE, valorCIE, valorNE, valorCR, valorCAR, valorTR, valorER, variavelB, variavelR, valorSB, valorSR;
   janela = tix.Tk()
   tamX = janela.winfo_screenwidth()
   tamY = janela.winfo_screenheight()
      
   corP = "Ivory"
   corL = "gray40"
   corD = "Teal" 

   logo = Canvas(janela, bg=corD, height=95, relief=FLAT, highlightcolor=corD, highlightbackground=corD)
   logo.pack(side=TOP, expand=False, anchor=N, fill=X)
   painel = Canvas(janela, bg=corP, relief=FLAT, highlightcolor=corD, highlightbackground=corD)
   painel.pack(side=TOP, expand=True, fill=BOTH)
   borda = Canvas(painel, bg=corD, height=35, relief=FLAT, highlightcolor=corD,highlightbackground=corD)
   borda.pack(side=BOTTOM, expand=True, fill=X, anchor=SW)
   
   status = tix.Label(borda, text="para instruções passe o mause nos componentes!!", width=40, relief=FLAT, foreground=corP, background=corD, font=("Arial", 12))
   status.pack(anchor=CENTER, fill=Y)
   
   nomeP = Label(janela, text="Formulário", fg=corP, background=corD, font=("Klavika Med Caps", 45, "bold"))
   nomeP.place(x=105, y=15)

   Label(painel, text="Forneça os dados da sua empresa:", fg=corL, background=corP, font=("Klavika Med Caps", 23, "bold")).place(x=25, y=5)

   painel.create_line(0, 50 , tamX, 50, width=2, fill=corD)
   #############
   def salvar():
      global janela, variavelB, variavelR, nomeF, social, CNPJ, endereco, cidade, estado, CEP, nomeR, cpf, cargo, telefon, e_mail, mesa, dono, gerente, funcio, produto, senhapin, senhapinR;
      if nomeF.get() != "" and social.get() != "" and CNPJ.get()!= "" and endereco.get() != "" and cidade.get() != "" and estado.get() != "" and CEP.get() != "" and mesa.get() != "" and dono.get() != "" and gerente.get() != "" and funcio.get() != "" and produto.get() != "" and nomeR.get() != "" and cpf.get() != "" and cargo.get() != "" and telefon.get() != "" and e_mail.get != "" and senhapin != "" and senhapinR != "" and (variavelR.get() == 1 or variavelB.get() == 1):
         if senhapin.get() == senhapinR.get():
            criaDadoMesa()
            arquivoMesas()
            preencheLista()
            guardarDados()
            janela.destroy()
            entrarJanela()
         else:
            labr = ttk.Label(painel, text="         Senhas Diferentes", font=("Klavika Med Caps", 14), background=corD, foreground=corP, width=20, padding=10)
            labr.place(x=180, y=tamY-265)
            janela.after(3500, labr.destroy)
            
   def cancelar():
      global janela;
      janela.destroy()
   ##################
   ttk.Label(painel, text="Área/Setor Comercial:", font=("Klavika Med Caps", 11, "bold"), foreground=corL, background=corP).place(x=60, y=55)

   clickT = 0
   variavelB = IntVar()
   variavelR = IntVar()

   def disabledR():
      global btR, clickT;
      if clickT%2 == 0:
         btR.config(state="disabled", disabledforeground=None)
      else:
         btR.config(state="normal")
      clickT += 1
   def disabledB():  
      global btB, clickT;
      if clickT%2 == 0:
         btB.config(state="disabled", disabledforeground=None)
      else:
         btB.config(state="normal")
      clickT += 1
   btB = Checkbutton(painel, text="Bar", takefocus=0, foreground=corL, font=("Klavika Med Caps", 10, "bold"), background=corP, variable=variavelB, command=disabledR)
   btB.place(x=65, y=80)
   btR = Checkbutton(painel, text="Restaurante", takefocus=0, foreground=corL, font=("Klavika Med Caps", 10, "bold"), background=corP, variable=variavelR, command=disabledB)
   btR.place(x=120, y=80)


   def donoIn():
      global janela, dono, valorDono;
      try:
         recolhe()
         valorDono = int(dono.get())
         janela.destroy()
         donoJanela(valorDono)
         principal()
      except:
         pass
   def gerenteIn():
      global janela, gerente, valorGerente;
      try:
         recolhe()
         valorGerente = int(gerente.get())
         janela.destroy()
         gerenteJanela(valorGerente)
         principal()
      except:
         pass
   def funcionarioIn():
      global janela, funcio, valorFuncionario;
      recolhe()
      try:
         valorFuncionario = int(funcio.get())
         janela.destroy()
         funcionarioJanela(valorFuncionario)
         principal()
      except:
         pass
      
   def produtoIn():
      recolhe()
      try:
         valorProduto = int(produto.get())
         janela.destroy()
         produtoJanela(valorProduto)
         principal()
      except:
         pass
    # estilo de Label
   style= ttk.Style()
   style.configure("PL.TLabel", background=corP, font=("Klavika Med Caps", 12, "bold"), foreground=corL)

   # estilo de entry
   style= ttk.Style()
   style.configure("PE.TEntry", font=("Arial", 12), background=corP)

   # estilo de button
   style= ttk.Style()
   style.configure("PB.TButton", font=("Klavika Med Caps", 10), background=corP, foreground=corL)
   ########################
   ttk.Label(painel, text="Nome Fantasia: ", style="PL.TLabel").place(x=10, y=110)

   nomeF = ttk.Entry(painel, style="PE.TEntry", width=20)
   nomeF.place(x=150, y=110)

   ttk.Label(painel, text="Razão Social: ", style="PL.TLabel").place(x=10, y=140)

   social = ttk.Entry(painel, style="PE.TEntry", width=20)
   social.place(x=150, y=140)

   ttk.Label(painel, text="CNPJ: ", style="PL.TLabel").place(x=10, y=170)

   CNPJ = ttk.Entry(painel, style="PE.TEntry", width=20)
   CNPJ.place(x=150, y=170)

   ttk.Label(painel, text="Endereço: ", style="PL.TLabel").place(x=10, y=200)
   
   endereco = ttk.Entry(painel, style="PE.TEntry", width=20)
   endereco.place(x=150, y=200)

   ttk.Label(painel, text="Cidade: ", style="PL.TLabel").place(x=10, y=230)

   cidade = ttk.Entry(painel, style="PE.TEntry", width=20)
   cidade.place(x=150, y=230)
   
   ttk.Label(painel, text="Estado: ", style="PL.TLabel").place(x=10, y=260)
   
   estado = ttk.Entry(painel, style="PE.TEntry", width=20)
   estado.place(x=150, y=260)

   ttk.Label(painel, text="CEP: ", style="PL.TLabel").place(x=10, y=290)
   
   CEP = ttk.Entry(painel, style="PE.TEntry", width=20)
   CEP.place(x=150, y=290)

   ttk.Label(painel, text="Responsável pelo preenchimento:", font=("Klavika Med Caps", 11, "bold"), foreground=corL, background=corP).place(x=298, y=55)
   
   painel.create_line(0, 320, tamX, 320, width=2, fill=corD)
   painel.create_line(290, 50, tamY-478, 320, width=2, fill=corD)

   ttk.Label(painel, text="Nome: ", style="PL.TLabel").place(x=303, y=140)

   nomeR = ttk.Entry(painel, style="PE.TEntry", width=20)
   nomeR.place(x=405, y=140)

   ttk.Label(painel, text="CPF: ", style="PL.TLabel").place(x=303, y=170)

   cpf = ttk.Entry(painel, style="PE.TEntry", width=20)
   cpf.place(x=405, y=170)

   ttk.Label(painel, text="Cargo: ", style="PL.TLabel").place(x=303, y=200)

   cargo = ttk.Entry(painel, style="PE.TEntry", width=20)
   cargo.place(x=405, y=200)
   
   ttk.Label(painel, text="Telefone: ", style="PL.TLabel").place(x=303, y=230)
   
   telefon = ttk.Entry(painel, style="PE.TEntry", width=20)
   telefon.place(x=405, y=230)

   ttk.Label(painel, text="E-mail: ", style="PL.TLabel").place(x=303, y=260)
   
   e_mail = ttk.Entry(painel, style="PE.TEntry", width=20)
   e_mail.place(x=405, y=260)
   
   ttk.Label(painel, text="Quantidade de Mesa: ", style="PL.TLabel").place(x=10, y=330)

   mesa = ttk.Entry(painel, style="PE.TEntry", width=10)
   mesa.place(x=230, y=330)
   
   ttk.Label(painel, text="Quantidade de Dono: ", style="PL.TLabel").place(x=10, y=360)
   
   dono = ttk.Entry(painel, style="PE.TEntry", width=10)
   dono.place(x=230, y=360)
   
   indados = ttk.Button(painel, text="Informar Dados", style="PB.TButton", takefocus=0, command=donoIn)
   indados.place(x=305, y=359)

   ttk.Label(painel, text="Quantidade de Gerente: ", style="PL.TLabel").place(x=10, y=390)

   gerente = ttk.Entry(painel, style="PE.TEntry", width=10)
   gerente.place(x=230, y=390)

   infodados = ttk.Button(painel, text="Informar Dados", style="PB.TButton", takefocus=0, command=gerenteIn)
   infodados.place(x=305, y=389)

   ttk.Label(painel, text="Quantidade de Funcionário: ", style="PL.TLabel").place(x=10, y=420)

   funcio = ttk.Entry(painel, style="PE.TEntry", width=10)
   funcio.place(x=230, y=420)

   infordados = ttk.Button(painel, text="Informar Dados", style="PB.TButton", takefocus=0, command=funcionarioIn)
   infordados.place(x=305, y=419)
   
   ttk.Label(painel, text="Quantidade de Produto: ", style="PL.TLabel").place(x=10, y=450)

   produto = ttk.Entry(painel, style="PE.TEntry", width=10)
   produto.place(x=230, y=450)

   informdados = ttk.Button(painel, text="Informar Dados", style="PB.TButton", takefocus=0, command=produtoIn)
   informdados.place(x=305, y=449)

   style =ttk.Style()
   style.configure("PP.TLabel", font=("Arial", 12, "bold"), background=corP, foreground=corL)

   style =ttk.Style()
   style.configure("PP.TEntry", font=("Arila", 12, "bold"), background=corP,padding=5)
      
   painel.create_line(0, tamY-280, tamX, tamY-280, width=2, fill=corD)

   sp1 = ttk.Label(painel, text="Senha Pin: ", style="PP.TLabel")
   sp1.place(x=10, y=tamY-258)
   senhapin =  ttk.Entry(painel, show="*",style="PP.TEntry")
   senhapin.place(x=110, y=tamY-260)
   sp2 = ttk.Label(painel, text="Repita Senha: ", style="PP.TLabel")
   sp2.place(x=270, y=tamY-258)
   senhapinR =  ttk.Entry(painel, show="*", style="PP.TEntry")
   senhapinR.place(x=395, y=tamY-260)

   style= ttk.Style()
   style.configure("CB.TButton", font=("Klavika Med Caps", 12), background=corP, foreground=corL)
   sl = ttk.Button(painel, text="Salvar", style="CB.TButton",takefocus=0,command=salvar, width=20)
   sl.place(x=80,y=tamY-218)
   cn = ttk.Button(painel, text="Cancelar", style="CB.TButton",takefocus=0,command=cancelar, width=20)
   cn.place(x=280,y=tamY-218)

   def recolhe():
      global janela, nomeF, social, CNPJ, endereco, cidade, estado, CEP, nomeR, cpf, cargo, telefon, e_mail, mesa, dono, gerente, funcio, produto, senhapin, senhapinR, valorDono, valorGerente, valorFuncionario, valorProduto, valorMesa, valorSenha, valorSenhaR, valorNE, valorRE, valorCNE, valorEE, valorCE, valorESE, valorCEE,  valorCR, valorNR, valorCAR, valorTR, valorER, valorSB, valorSR, variavelB, variavelR, btB, btR;
      valorSB = variavelB.get()
      valorSR = variavelR.get()
      #######
      valorNE = nomeF.get()
      valorRE = social.get()
      valorCNE = CNPJ.get()
      valorEE = endereco.get()
      valorCE = cidade.get()
      valorESE = estado.get()
      valorCEE = CEP.get()
      ########
      valorNR = nomeR.get()
      valorCR = cpf.get()
      valorCAR = cargo.get()
      valorTR = telefon.get()
      valorER = e_mail.get()
      valorMesa = mesa.get()
      valorDono = dono.get()
      valorGerente = gerente.get()
      valorFuncionario = funcio.get()
      valorProduto = produto.get()
      valorSenha = senhapin.get()
      valorSenhaR = senhapinR.get()
   ################
   def atualizar():
      global  janela, nomeF, social, CNPJ, endereco, cidade, estado, CEP, nomeR, cpf, cargo, telefon, e_mail, mesa, dono, gerente, funcio, produto, senhapin, senhapinR, valorDono, valorGerente, valorFuncionario, valorProduto, valorMesa, valorSenha, valorSenhaR, valorNE, valorRE, valorCNE, valorEE, valorCE, valorESE, valorCEE,  valorCR, valorNR, valorCAR, valorTR, valorER, valorSB, valorSR, variavelB, variavelR, btB, btR;
      if valorSB == 1:
         btB.select()
         disabledR()
      elif valorSR == 1:
         btR.select()
         disabledB() 

      nomeF.insert(END, valorNE)
      social.insert(END, valorRE)
      CNPJ.insert(END, valorCNE)
      endereco.insert(END, valorEE)
      cidade.insert(END, valorCE)
      estado.insert(END, valorESE)
      CEP.insert(END, valorCEE)
      ###
      nomeR.insert(END, valorNR)
      cpf.insert(END, valorCR)
      cargo.insert(END, valorCAR)
      telefon.insert(END, valorTR)
      e_mail.insert(END, valorER)
      mesa.insert(END, valorMesa)
      dono.insert(END, valorDono)
      gerente.insert(END, valorGerente)
      funcio.insert(END, valorFuncionario)
      produto.insert(END, valorProduto)
      senhapin.insert(END, valorSenha)
      senhapinR.insert(END, valorSenhaR)
      

   instrucao = tix.Balloon(janela, status=status, initwait=100, state='both')
   
   instrucao.bind_widget(cn, balloonmsg='click',
   statusmsg='cancelar e fechar janela')
   #
   instrucao.bind_widget(sl, balloonmsg='click',
   statusmsg='salvar os dados da empresa')
   #
   instrucao.bind_widget(indados, balloonmsg='click',
   statusmsg='informar dados dos donos')
   #
   instrucao.bind_widget(infodados, balloonmsg='click',
   statusmsg='informar dados dos gerentes')
   #
   instrucao.bind_widget(infordados, balloonmsg='click',
   statusmsg='informar dados dos funcionários')
   #
   instrucao.bind_widget(informdados, balloonmsg='click',
   statusmsg='informar os produtos do estoque')
   #
   instrucao.bind_widget(mesa, balloonmsg='inserir',
   statusmsg='quantidade de mesa')
   #
   instrucao.bind_widget(dono, balloonmsg='inserir',
   statusmsg='quantidade de dono')
   #
   instrucao.bind_widget(gerente, balloonmsg='inserir',
   statusmsg='quantidade de gerente')
   #
   instrucao.bind_widget(funcio, balloonmsg='inserir',
   statusmsg='quantidade de funcionário')
   #
   instrucao.bind_widget(produto, balloonmsg='inserir',
   statusmsg='quantidade de produto')
   #
   instrucao.bind_widget(senhapin, balloonmsg='inserir',
   statusmsg='a senha pin')
   #
   instrucao.bind_widget(senhapinR, balloonmsg='inserir',
   statusmsg='repita a senha pin')
   #
   instrucao.bind_widget(btB, balloonmsg='selecione',
   statusmsg='o setor da sua empresa')
   #
   instrucao.bind_widget(btR, balloonmsg='selecione',
   statusmsg='o setor da sua empresa')
   #
   instrucao.bind_widget(nomeF, balloonmsg='inserir',
   statusmsg='o nome fantasia da empresa')
   #
   instrucao.bind_widget(social, balloonmsg='inserir',
   statusmsg='a razão social da empresa')
   #
   instrucao.bind_widget(CNPJ, balloonmsg='inserir',
   statusmsg='o cnpj da empresa')
   #
   instrucao.bind_widget(endereco, balloonmsg='inserir',
   statusmsg='o endereço da empresa')
   #
   instrucao.bind_widget(cidade, balloonmsg='inserir',
   statusmsg='a cidade onde a empresa se localiza')
   #
   instrucao.bind_widget(estado, balloonmsg='inserir',
   statusmsg='o estado onde a empresa se localiza')
   #
   instrucao.bind_widget(CEP, balloonmsg='inserir',
   statusmsg='o cep da cidade onde a empresa se localiza')
   #
   instrucao.bind_widget(nomeR, balloonmsg='inserir',
   statusmsg='O seu nome')
   #
   instrucao.bind_widget(cpf, balloonmsg='inserir',
   statusmsg='o número do seu cpf')
   #
   instrucao.bind_widget(cargo, balloonmsg='inserir',
   statusmsg='o cargo exercido por você')
   #
   instrucao.bind_widget(telefon, balloonmsg='inserir',
   statusmsg='o número do seu telefone')
   #
   instrucao.bind_widget(e_mail, balloonmsg='inserir',
   statusmsg='o seu e-mail')
   #
   instrucao.bind_widget(sp1, balloonmsg='info',
   statusmsg='Para segurança e fazer alterações de configurações.\nCriar senha Pin')
   #
   instrucao.bind_widget(sp2, balloonmsg='info',
   statusmsg="Para segurança e fazer alterações de configurações.\nCriar senha Pin")
   #
   atualizar()
   janela.geometry("%ix%i+%i+%i"%(tamX/2.5, tamY//1.06, 0, 0))
   janela.config(relief=FLAT)
   janela.config(bg=corP)
   janela.overrideredirect(1)
   janela.mainloop()
