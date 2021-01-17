from tkinter import*
from tkinter import ttk
from tkinter import tix
import sqlite3

def guardarDados():
   global num, listaNomes, listaCpfs, listaRgs, listaSalarios, listaEmails, listaNascimento, listaEntrada, listaFuncao, listaConta, listaV, listaSenha;
   bancoFuncionario = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
   cursoFuncionario = bancoFuncionario.cursor()
   cursoFuncionario.execute("CREATE TABLE IF NOT EXISTS infoFuncionario(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                            nome TEXT, cpf TEXT, identidade TEXT, salario TEXT, funcao TEXT, entrada TEXT, dtn TEXT, email TEXT, conta TEXT)")
   inserir = "INSERT INTO infoFuncionario(nome, cpf, identidade, salario, funcao, entrada, dtn, email, conta) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
   for i in range(1, num+1):
      if listaConta[i] == "1":
         conta = "Não tem conta"
      elif listaConta[i] == "2":
         conta = "Conta gerenciamento"
      else:
         conta = "Conta administrador"
      cursoFuncionario.execute(inserir, (listaNomes[i], listaCpfs[i], listaRgs[i], listaSalarios[i], listaFuncao[i], listaEntrada[i], listaNascimento[i], listaEmails[i], conta,))
      bancoFuncionario.commit()
   cursoFuncionario.close()
   bancoFuncionario.close()
def criaConta():
   global num, listaEmails, listaConta, listaSenha, listaNomes;
   bancoConta = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/contaAcesso.db")
   cursoConta1 = bancoConta.cursor()
   cursoConta2 = bancoConta.cursor()
   cursoConta3 = bancoConta.cursor()
   cursoConta1.execute("CREATE TABLE IF NOT EXISTS semConta(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                            email TEXT, senha TEXT, tipo TEXT, nome TEXT)")
   cursoConta2.execute("CREATE TABLE IF NOT EXISTS contaGerenciamento(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                            email TEXT, senha TEXT, tipo TEXT, nome TEXT)")
   cursoConta3.execute("CREATE TABLE IF NOT EXISTS contaAdministrador(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                            email TEXT, senha TEXT, tipo TEXT, nome TEXT)")
   inserir1 = "INSERT INTO semConta(email, senha, tipo, nome) VALUES(?, ?, ?, ?)"
   inserir2 = "INSERT INTO contaGerenciamento(email, senha, tipo, nome) VALUES(?, ?, ?, ?)"
   inserir3 = "INSERT INTO contaAdministrador(email, senha, tipo, nome) VALUES(?, ?, ?, ?)"
   for i in range(1, num+1):
      if listaConta[i] == "1":
         cursoConta1.execute(inserir1, (listaEmails[i], listaSenha[i], "Funcionário", listaNomes[i],))
      elif listaConta[i] == "2":
         cursoConta2.execute(inserir2, (listaEmails[i], listaSenha[i], "Funcionário", listaNomes[i],))
      else:
         cursoConta3.execute(inserir3, (listaEmails[i], listaSenha[i], "Funcionário", listaNomes[i],))
      bancoConta.commit()
   cursoConta1.close()
   cursoConta2.close()
   cursoConta3.close()
   bancoConta.close() 
def funcionarioJanela(f):
   global num, rep, listaNomes, listaCpfs, listaRgs, listaSalarios, listaEmails, listaNascimento, listaEntrada, listaFuncao, listaConta, listaV, listaSenha, c, corPad, corPri, corL, funcionarioja, nasci, nome, cpf, rg, salario, email, entra, funcao, clickTD, btSC, btCS, btCA, variavelSC, variavelCS, variavelCA, senhaCS, senhaCA, scs, sca, buttCS, buttCA;
   c = 0
   rep = 1
   num = f
   corPad = "darkblue"
   corPri = "Ivory"
   corL = "gray18" 

   listaNomes = [""]
   listaCpfs = [""]
   listaRgs = [""]
   listaSalarios = [""]
   listaEmails = [""]
   listaNascimento = [""]
   listaEntrada = [""]
   listaFuncao = [""]
   listaConta = [""]
   listaSenha = [""]
   listaV = [""]
   
   funcionarioja = tix.Tk()
   xt = funcionarioja.winfo_screenwidth()
   yt = funcionarioja.winfo_screenheight()

   logo = Canvas(funcionarioja, bg=corPad, height=70, relief=FLAT, highlightcolor=corPad, highlightbackground=corPad)
   logo.pack(side=TOP, expand=False, anchor=N, fill=X)

   fundo = Canvas(funcionarioja, bg=corPad, height=20, relief=FLAT, highlightcolor=corPad, highlightbackground=corPad)
   fundo.pack(side=BOTTOM, expand=True, anchor=S, fill=X)

   status = tix.Label(fundo, text="para instruções passe o mause nos componentes!!", width=40, relief=FLAT, foreground="white", background=corPad, font=("Arial", 11))
   status.pack(anchor=CENTER, fill=Y)

   
   ttk.Label(logo, text="Formulário", background=corPad, font=("Klavika Med Caps", 40,"bold"), foreground="white").place(x=175, y=9)


   ttk.Label(funcionarioja, text="Nascimento:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=315, y=123)
   ttk.Label(funcionarioja, text="Entrada:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=315, y=163)
   ttk.Label(funcionarioja, text="Email:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=315, y=203)
   ttk.Label(funcionarioja, text="Função:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=315, y=243)
   ttk.Label(funcionarioja, text="Exercida", font=("Arial", 8,"bold"), foreground=corL, background=corPri).place(x=321, y=261)
   

   
   ttk.Label(funcionarioja, text="Nome:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=30, y=123)
   ttk.Label(funcionarioja, text="CPF:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=30, y=163)
   ttk.Label(funcionarioja, text="RG:", font=("Klavika Med Caps", 13,"bold"), foreground=corL,background=corPri).place(x=30, y=203)
   ttk.Label(funcionarioja, text="Salário:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=30, y=243)

   nome = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)
   nome.place(x=115, y=123)
   cpf = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)
   cpf.place(x=115, y=163)
   rg = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)
   rg.place(x=115, y=203)
   salario = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)
   salario.place(x=115, y=243)

   nasci = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)#validate="focusin", validatecommand=d)
   nasci.place(x=435, y=123)
   entra = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)
   entra.place(x=435, y=163)
   email = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)
   email.place(x=435, y=203)
   funcao = ttk.Entry(funcionarioja, font=("Arial", 12), width=20)
   funcao.place(x=435, y=243)
   

   def verificar():
      global listaV;
      try:
         for i in range(1, f+1):
            v = listaV[i]
         return True
      except:
         return False
   def verificarUnica(number):
      global listaV;
      try:
         v = listaV[number]
         return True
      except:
         return False
   #funções de dados
   def canc():
      global funcionarioja;
      funcionarioja.destroy()
   #############################################################
   def limpa():
      global nasci, nome, cpf, rg, salario, email, entra, funcao, variavelSC, variavelCS, variavelCA, btSC, btCS, btCA, clickTD, senhaCS, senhaCA;
      nome.delete(0, END)
      rg.delete(0, END)
      cpf.delete(0, END)
      salario.delete(0, END)
      email.delete(0, END)
      nasci.delete(0, END)
      entra.delete(0, END)
      funcao.delete(0, END)
      if variavelSC.get() == 1:
         btSC.deselect()
         disableSC()
      elif variavelCS.get() == 1:
         btCS.deselect()
         disableCS()
         senhaCS.delete(0, END)
      else:
         btCA.deselect()
         disableCA()
         senhaCA.delete(0, END)
      clickTD = 0
      
   def salvaDado(number):
      global listaNomes, listaCpfs, listaRgs, listaSalarios, listaEmails, listaNascimento, listaEntrada, listaFuncao, listaConta, listaV, listaSenha, c, nasci, nome, cpf, rg, salario, email, entra, funcao, variavelSC, variavelCS, variavelCA, btSC, btCS, btCA, clickTD, senhaCS, senhaCA;
      try:
         v = listaV[number]
      except:
         listaV.append(number)
         listaNomes.append(number)
         listaCpfs.append(number)
         listaRgs.append(number)
         listaSalarios.append(number)
         listaEmails.append(number)
         listaNascimento.append(number)
         listaEntrada.append(number)
         listaFuncao.append(number)
         listaConta.append(number)
         listaSenha.append(number)
         
      listaNomes[number] = nome.get()
      listaCpfs[number] = rg.get()
      listaRgs[number] = cpf.get()
      listaSalarios[number] = salario.get()
      listaEmails[number] = email.get()
      listaNascimento[number] = nasci.get()
      listaEntrada[number] = entra.get()
      listaFuncao[number] = funcao.get()
      if variavelSC.get() == 1:
         listaConta[number] = "1"
         listaSenha[number] = False
      elif variavelCS.get() == 1:
         listaConta[number] = "2"
         listaSenha[number] = senhaCS.get()
      else:
         listaConta[number] = "3"
         listaSenha[number] = senhaCA.get()
         
   def salv():
      global rep, listaNomes, listaCpfs, listaRgs, listaSalarios, listaEmails, listaNascimento, listaEntrada, listaFuncao, listaConta, listaV, listaSenha, c, nasci, nome, cpf, rg, salario, email, entra, funcao, variavelSC, variavelCS, variavelCA, btSC, btCS, btCA, clickTD, senhaCS, senhaCA;
      if c == f or (f == 1 and c == 0):
         if rep == 2:
            if nome.get() != "" and rg.get() != "" and cpf.get() != "" and salario.get() != "" and email.get() != "" and nasci.get() != "" and entra.get() != ""  and funcao.get() != "" and (variavelSC.get() == 1 or variavelCS.get() == 1 or variavelCA.get() == 1):
               salvaDado(f)
               guardarDados()
               criaConta()
               funcionarioja.destroy()
         else:
            if nome.get() != "" and rg.get() != "" and cpf.get() != "" and salario.get() != "" and email.get() != "" and nasci.get() != "" and entra.get() != ""  and funcao.get() != "" and (variavelSC.get() == 1 or variavelCS.get() == 1 or variavelCA.get() == 1): 
               salvaDado(f)
               labr = ttk.Label(funcionarioja, text="Pressione o botão denovo para fechar a janela", font=("Klavika Med Caps", 14), background="gray20", foreground="white", width=40)
               labr.place(x=109, y=391)
               funcionarioja.after(3500, labr.destroy)
               rep += 1
      else:
         if c == 0:
            salvaDado(1)
         else:
            salvaDado(c)
         #################################
   def prox():
      global listaNomes, listaCpfs, listaRgs, listaSalarios, listaEmails, listaNascimento, listaEntrada, listaFuncao, listaConta, listaV, listaSenha, c, nasci, nome, cpf, rg, salario, email, entra, funcao, variavelSC, variavelCS, variavelCA, btSC, btCS, btCA, clickTD, senhaCS, senhaCA;
      if c >= 0 and c < f and f != 1:
         if c == 0:
            v = verificarUnica(1)
         else:
            v = verificarUnica(c)
         if v == True and nome.get() != "" and rg.get() != "" and cpf.get() != "" and salario.get() != "" and email.get() != "" and nasci.get() != "" and entra != ""  and funcao != "" and (variavelSC.get() == 1 or variavelCS.get() == 1 or variavelCA.get() == 1):
            try:
               if c == 0:
                  lab.configure(text="Funcionário %dº"%(c+2))
                  c += 2
               else:
                  lab.configure(text="Funcionário %dº"%(c+1))
                  c += 1
                  
               nm = listaV[c]
               #######
               limpa()
               #######
               nome.insert(END, listaNomes[c])
               rg.insert(END, listaCpfs[c])
               cpf.insert(END, listaRgs[c])
               salario.insert(END, listaSalarios[c])
               email.insert(END, listaEmails[c])
               nasci.insert(END, listaNascimento[c])
               entra.insert(END, listaEntrada[c])
               funcao.insert(END, listaFuncao[c])
               if listaConta[c] == "1":
                  btSC.select()
                  disableSC()
               elif listaConta[c] == "2":
                  btCS.select()
                  disableCS()
                  senhaCS.insert(END, listaSenha[c])
               else:
                  btCA.select()
                  disableCA()
                  senhaCA.insert(END, listaSenha[c])
               if c == 1:
                  c += 1
            except:
               #######
               limpa()
               #######
               lab.configure(text="Funcionário %dº"%(c))
      else:
         v = verificarUnica(f)
         if v == True and nome.get() != "" and rg.get() != "" and cpf.get() != "" and salario.get() != "" and email.get() != "" and nasci.get() != "" and entra.get() != ""  and funcao.get() != "" and (variavelSC.get() == 1 or variavelCS.get() == 1 or variavelCA.get() == 1):
            lab.configure(text="Funcionário %dº"%(f))
            try:
               nm = listaV[f]
               #######
               limpa()
               #######
               nome.insert(END, listaNomes[f])
               rg.insert(END, listaCpfs[f])
               cpf.insert(END, listaRgs[f])
               salario.insert(END, listaSalarios[f])
               email.insert(END, listaEmails[f])
               nasci.insert(END, listaNascimento[f])
               entra.insert(END, listaEntrada[f])
               funcao.insert(END, listaFuncao[f])
         
               if listaConta[f] == "1":
                  btSC.select()
                  disableSC()
               elif listaConta[f] == "2":
                  btCS.select()
                  disableCS()
                  senhaCS.insert(END, listaSenha[f])
               else:
                  btCA.select()
                  disableCA()
                  senhaCA.insert(END, listaSenha[f])
            except:
               listaNomes[f] = nome.get()
               listaCpfs[f] = rg.get() 
               listaRgs[f] = cpf.get()
               listaSalarios[f] = salario.get()
               listaEmails[f] = email.get()
               listaNascimento[f] = nasci.get()
               listaEntrada[f] = entra.get()
               listaFuncao[f] = funcao.get()
               if variavelSC.get() == 1:
                  listaConta[f] = "1"
                  listaSenha[f] = False
               elif variavelCS.get() == 1:
                  listaConta[f] = "2"
                  listaSenha[f] = senhaCS.get()
               else:
                  listaConta[f] = "3"
                  listaSenha[f] = senhaCA.get()
                  
   #############################################################
   def ante():
      global rep, listaNomes, listaCpfs, listaRgs, listaSalarios, listaEmails, listaNascimento, listaEntrada, listaFuncao, listaConta, listaV, listaSenha, c, nasci, nome, cpf, rg, salario, email, entra, funcao, senhaCS, senhaCA;
      if c >= 1 and c <= f:
         v = verificar()
         if c == 1:
            if v == True and nome.get() != "" and rg.get() != "" and cpf.get() != "" and salario.get() != "" and email.get() != "" and nasci.get() != "" and entra.get() != ""  and funcao.get() != "" and (variavelSC.get() == 1 or variavelCS.get() == 1 or variavelCA.get() == 1):
               lab.configure(text="Funcionário %dº"%(c))
               #######
               limpa()
               ######
               nome.insert(END, listaNomes[c])
               cpf.insert(END, listaCpfs[c])
               rg.insert(END, listaRgs[c])
               salario.insert(END, listaSalarios[c])
               email.insert(END, listaEmails[c])
               nasci.insert(END, listaNascimento[c])
               entra.insert(END, listaEntrada[c])
               funcao.insert(END, listaFuncao[c])
               if listaConta[c] == "1":
                  btSC.select()
                  disableSC()
               elif listaConta[c] == "2":
                  btCS.select()
                  disableCS()
                  senhaCS.insert(END, listaSenha[c])
               else:
                  btCA.select()
                  disableCA()
                  senhaCA.insert(END, listaSenha[c])
               c = 0
         else:
            if v == True and nome.get() != "" and rg.get() != "" and cpf.get() != "" and salario.get() != "" and email.get() != "" and nasci.get() != "" and entra.get() != ""  and funcao.get() != "" and (variavelSC.get() == 1 or variavelCS.get() == 1 or variavelCA.get() == 1):
               if c == f:
                  rep = 1
               c -= 1
               lab.configure(text="Funcionário %dº"%(c))
               #######
               limpa()
               ######
               nome.insert(END, listaNomes[c])
               cpf.insert(END, listaCpfs[c])
               rg.insert(END, listaRgs[c])
               salario.insert(END, listaSalarios[c])
               email.insert(END, listaEmails[c])
               nasci.insert(END, listaNascimento[c])
               entra.insert(END, listaEntrada[c])
               funcao.insert(END, listaFuncao[c])
               if listaConta[c] == "1":
                  btSC.select()
                  disableSC()
               elif listaConta[c] == "2":
                  btCS.select()
                  disableCS()
                  senhaCS.insert(END, listaSenha[c])
               else:
                  btCA.select()
                  disableCA()
                  senhaCA.insert(END, listaSenha[c])
   def disableSC():
      global btCS, btCA, clickTD, senhaCS, senhaCA, sca, scs;
      if clickTD%2 == 0:
         btCS.config(state="disabled", disabledforeground=None)
         btCA.config(state="disabled", disabledforeground=None)
         senhaCA.delete(0, END)
         senhaCS.delete(0, END)
         senhaCA.configure(state="disabled")
         senhaCS.configure(state="disabled")
         scs.configure(foreground="gray50")
         sca.configure(foreground="gray50")
         buttCS.config(state="disabled")
         buttCA.config(state="disabled")
      else:
         btCS.configure(state="normal")
         btCA.configure(state="normal")
         senhaCA.configure(state="normal")
         senhaCS.configure(state="normal")
         sca.configure(foreground="gray18")
         scs.configure(foreground="gray18")
         buttCS.config(state="normal")
         buttCA.config(state="normal")
      clickTD += 1
   def disableCS():  
      global btSC, btCA, clickTD, senhaCA, sca;
      if clickTD%2 == 0:
         btSC.configure(state="disabled", disabledforeground=None)
         btCA.configure(state="disabled", disabledforeground=None)
         senhaCA.delete(0, END)
         senhaCA.configure(state="disabled")
         sca.configure(foreground="gray50")
         buttCA.config(state="disabled")
      else:
         btSC.configure(state="normal")
         btCA.configure(state="normal")
         senhaCA.configure(state="normal")
         sca.configure(foreground="gray18")
         buttCA.config(state="normal")
      clickTD += 1
   def disableCA():  
      global btSC, btCS, clickTD, senhaCS, scs, buttCS;
      if clickTD%2 == 0:
         btSC.configure(state="disabled", disabledforeground=None)
         btCS.configure(state="disabled", disabledforeground=None)
         senhaCS.delete(0 , END)
         senhaCS.configure(state="disabled")
         scs.configure(foreground="gray50")
         buttCS.config(state="disabled")
      else:
         btSC.configure(state="normal")
         btCS.configure(state="normal")
         senhaCS.configure(state="normal")
         scs.configure(foreground="gray18")
         buttCS.config(state="normal")
      clickTD += 1
      
   def mostraCS():
      global funcionarioja, senhaCS;
      senhaCS.configure(show="")
      def troca():
         senhaCS.configure(show="*")
      funcionarioja.after(600, troca)
   def mostraCA():
      global funcionarioja, senhaCA;
      senhaCA.configure(show="")
      def troca():
         senhaCA.configure(show="*")
      funcionarioja.after(600, troca)
      
   clickTD = 0
   variavelSC = IntVar()
   variavelCS = IntVar()
   variavelCA = IntVar()
   
   btSC = Checkbutton(funcionarioja, text="NÃO CRIAR CONTA?", takefocus=0, foreground=corL, background=corPri,\
                      font=("Klavika Med Caps", 11, "bold"), activeforeground=corL, variable=variavelSC, command=disableSC)
   btSC.place(x=30, y=290)
   btCS = Checkbutton(funcionarioja, text="CRIAR CONTA APENAS DE GERENCIAR?", takefocus=0, foreground=corL, background=corPri,\
                      font=("Klavika Med Caps", 11, "bold"), activeforeground=corL, variable=variavelCS, command=disableCS)
   btCS.place(x=30, y=320)
   btCA = Checkbutton(funcionarioja, text="CRIAR CONTA ADMINISTRADOR?", takefocus=0, foreground=corL, background=corPri,\
                      font=("Klavika Med Caps", 11, "bold"), activeforeground=corL, variable=variavelCA, command=disableCA)
   btCA.place(x=30, y=350)

   scs = ttk.Label(funcionarioja, text="Senha:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri)
   scs.place(x=325, y=320)
   sca = ttk.Label(funcionarioja, text="Senha:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri)
   sca.place(x=325, y=350)

   senhaCS = ttk.Entry(funcionarioja, font=("Arial", 12), width=10, takefocus=0, show="*")
   senhaCS.place(x=390, y=320)
   senhaCA = ttk.Entry(funcionarioja, font=("Arial", 12), width=10, takefocus=0, show="*")
   senhaCA.place(x=390, y=350)

   ima = PhotoImage(file="C:/ProgramData/TMS/Imagens/secs.png")
   buttCS = ttk.Button(funcionarioja, image=ima, takefocus=0, command=mostraCS)
   buttCS.place(x=486, y=319)
   buttCA = ttk.Button(funcionarioja, image=ima, takefocus=0, command=mostraCA)
   buttCA.place(x=486, y=349)
   
   #######
   cancela = Button(funcionarioja,text="Cancelar", command=canc, relief=GROOVE, background=corPri,\
                    font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                    takefocus=0)
   cancela.place(x=110, y=390)

   anterio = Button(funcionarioja, text="<< Anterior", command=ante, relief=GROOVE,  background=corPri,\
                    font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                    takefocus=0)
   anterio.place(x=220, y=390)

   proximo = Button(funcionarioja, text="Proximo >>", command=prox, relief=GROOVE,  background=corPri,\
                    font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                    takefocus=0)
   proximo.place(x=330, y=390)

   salva = Button(funcionarioja, text="Salvar",  command=salv, relief=GROOVE,  background=corPri,\
                  font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                  takefocus=0)
   salva.place(x=440, y=390)

   lab = ttk.Label(funcionarioja, text="Funcionário %dº"%(1), font=("Klavika Med Caps", 14,"bold"), foreground=corL, background=corPri)
   lab.place(x=290, y=80)

   instrucao = tix.Balloon(funcionarioja, status=status, initwait=100, state='both')
   ###
   instrucao.bind_widget(cancela, balloonmsg='clique',
   statusmsg='cancelar e fechar janela')
   ###
   instrucao.bind_widget(anterio, balloonmsg='clique',
   statusmsg='retornar para o anterior')
   ###
   instrucao.bind_widget(proximo, balloonmsg='clique',
   statusmsg='avançar para o proximo')
   ###
   instrucao.bind_widget(salva, balloonmsg='clique',
   statusmsg='salvar as alterções')
   ###
   instrucao.bind_widget(senhaCA, balloonmsg='inserir',
   statusmsg='a senha da conta')
   ###
   instrucao.bind_widget(senhaCS, balloonmsg='inserir',
   statusmsg='a senha da conta')
   ###
   instrucao.bind_widget(buttCA, balloonmsg='clique',
   statusmsg='visualizar senha')
   ###
   instrucao.bind_widget(buttCS, balloonmsg='clique',
   statusmsg='visualizar senha')
   ### 
   instrucao.bind_widget(nasci, balloonmsg='inserir',
   statusmsg='a data de nascimento')
   ###
   instrucao.bind_widget(nome, balloonmsg='inserir',
   statusmsg='o nome completo')
   ###
   instrucao.bind_widget(cpf, balloonmsg='inserir',
   statusmsg='o número do cpf')
   ###
   instrucao.bind_widget(rg, balloonmsg='inserir',
   statusmsg='o número do rg')
   ###
   instrucao.bind_widget(salario, balloonmsg='inserir',
   statusmsg='o salario')
   ###
   instrucao.bind_widget(email, balloonmsg='inserir',
   statusmsg='o email')
   ###
   instrucao.bind_widget(entra, balloonmsg='inserir',
   statusmsg='a data de entrada')
   ###
   instrucao.bind_widget(funcao, balloonmsg='inserir',
   statusmsg='a função exercida')
   ###
   instrucao.bind_widget(btSC, balloonmsg='selecione',
   statusmsg='para não criar conta')
   ###
   instrucao.bind_widget(btCS, balloonmsg='selecione',
   statusmsg='para criar conta gerenciamento')
   ###
   instrucao.bind_widget(btCA, balloonmsg='selecione',
   statusmsg='para criar conta administrador')
   ###
   instrucao.bind_widget(logo, balloonmsg='todas as alterações feitas nos dados\ndos funcionários devem ser salvas\n(clicando no botão "salvar")',
   statusmsg='siga as instruções de funcionamento')
   
   funcionarioja.config(bg=corPri)
   funcionarioja.geometry("%dx%d+%d+%d"%(xt/2.1, yt/1.7, xt/3.3, yt/5))
   funcionarioja.overrideredirect(1)
   funcionarioja.mainloop()
