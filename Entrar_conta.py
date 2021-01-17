from tkinter import*
from tkinter import ttk
from tkinter import tix
import sqlite3
from InformacaoDono import donoJanela
from InformacaoFuncionario import funcionarioJanela
from InformacaoGerente import gerenteJanela
from InformacaoProduto import produtoJanela
from Cria_Configurações import configuraçaoJanela
from editeMesa import mesajanela

def entrarJanela():
   global us, sn, fn;
   from Cria_gerenciamento import gerenciarJanela
   janela = tix.Tk()
   tamX = janela.winfo_screenwidth()
   tamY = janela.winfo_screenheight()

   logo = Canvas(janela, bg="green4", height=100, relief=FLAT, highlightcolor="gray97")
   logo.pack(side=TOP, expand=False, fill=X)
   painel = Canvas(janela, bg="gray97", bd=0.0, relief=FLAT, highlightcolor="gray97")
   painel.pack(side=TOP, expand=True, fill=BOTH)
   borda = Canvas(painel, bg="green4", height=52, relief=FLAT, highlightcolor="gray97")
   borda.pack(side=BOTTOM, expand=True, fill=X, anchor=S)

   nomeP = Label(janela, text="Sistema de Gerenciamento Comercial", fg="white", background="green4", font=("Klavika Med Caps", 26, "bold"))
   nomeP.place(x=55, y=30)

   status = tix.Label(borda, text="para instruções passe o mause nos componentes!!", width=50, relief=FLAT, foreground="white", background="green4", font=("Klavika Med Caps", 14))
   status.place(x=160, y=15)

   ##############
   def fechar():
      janela.destroy()
   def editeM():
      global sen, sit;
      jan = Toplevel()
      def mostra():
         global sen, sit;
         s = sen.get()
         banco2 = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor2 = banco2.cursor()
         cursor2.execute("SELECT * FROM info")
         infor = cursor2.fetchall()
         sena = infor[0][2]
         if s == sena:
            jan.destroy()
            janela.destroy()
            mesajanela()
            entrarJanela()
         else:
            sit.destroy()
            sit = ttk.Label(jan, text="Senha Pin Incorreta\nTente Novamente", font=("Arial", 12, "bold"), padding=6)
            sit.pack(side=BOTTOM, anchor=CENTER)
      ttk.Label(jan, text="Senha Pin:", font=("Arial", 14, "bold"), padding=6).pack(side=TOP)
      sen = Entry(jan, font=("Arial", 13), width=37, show="*")
      sen.pack(side=TOP, anchor=CENTER, pady=4)
      buto = ttk.Button(jan, text="Entar", takefocus=0, padding=6, command=mostra)
      buto.pack(side=BOTTOM)
      sit = ttk.Label(jan, text="", font=("Arial", 12, "bold"), padding=6)
      sit.pack(side=BOTTOM, anchor=CENTER)          
      jan.resizable(0, 0)
      jan.title(" PIN")
      jan.geometry("355x200")
      jan.transient(janela)
      jan.grab_set()
      jan.wait_window()
      jan.mainloop()
   def editeP():
      global sen, sit;
      jan = Toplevel()
      def mostra():
         global sen, sit;
         s = sen.get()
         banco2 = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor2 = banco2.cursor()
         cursor2.execute("SELECT * FROM info")
         infor = cursor2.fetchall()
         sena = infor[0][2]
         if s == sena:
            jan.destroy()
            janela.destroy()
            produtoJanela(1)
            entrarJanela()
         else:
            sit.destroy()
            sit = ttk.Label(jan, text="Senha Pin Incorreta\nTente Novamente", font=("Arial", 12, "bold"), padding=6)
            sit.pack(side=BOTTOM, anchor=CENTER)
      ttk.Label(jan, text="Senha Pin:", font=("Arial", 14, "bold"), padding=6).pack(side=TOP)
      sen = Entry(jan, font=("Arial", 13), width=37, show="*")
      sen.pack(side=TOP, anchor=CENTER, pady=4)
      buto = ttk.Button(jan, text="Entar", takefocus=0, padding=6, command=mostra)
      buto.pack(side=BOTTOM)
      sit = ttk.Label(jan, text="", font=("Arial", 12, "bold"), padding=6)
      sit.pack(side=BOTTOM, anchor=CENTER)          
      jan.resizable(0, 0)
      jan.title(" PIN")
      jan.geometry("355x200")
      jan.transient(janela)
      jan.grab_set()
      jan.wait_window()
      jan.mainloop()
   def configure():
      global sen, sit;
      jan = Toplevel()
      def mostra():
         global sen, sit;
         s = sen.get()
         banco2 = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor2 = banco2.cursor()
         cursor2.execute("SELECT * FROM info")
         infor = cursor2.fetchall()
         sena = infor[0][2]
         if s == sena:
            jan.destroy()
            janela.destroy()
            configuraçaoJanela()
            entrarJanela()
         else:
            sit.destroy()
            sit = ttk.Label(jan, text="Senha Pin Incorreta\nTente Novamente", font=("Arial", 12, "bold"), padding=6)
            sit.pack(side=BOTTOM, anchor=CENTER)
      ttk.Label(jan, text="Senha Pin:", font=("Arial", 14, "bold"), padding=6).pack(side=TOP)
      sen = Entry(jan, font=("Arial", 13), width=37, show="*")
      sen.pack(side=TOP, anchor=CENTER, pady=4)
      buto = ttk.Button(jan, text="Entar", takefocus=0, padding=6, command=mostra)
      buto.pack(side=BOTTOM)
      sit = ttk.Label(jan, text="", font=("Arial", 12, "bold"), padding=6)
      sit.pack(side=BOTTOM, anchor=CENTER)          
      jan.resizable(0, 0)
      jan.title(" PIN")
      jan.geometry("355x200")
      jan.transient(janela)
      jan.grab_set()
      jan.wait_window()
      jan.mainloop()
   def novaCO():
      global fn, sen, sit;
      jan = Toplevel()
      
      def mostra():
         global sen, sit;
         s = sen.get()
         banco2 = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor2 = banco2.cursor()
         cursor2.execute("SELECT * FROM info")
         infor = cursor2.fetchall()
         sena = infor[0][2]
         if s == sena:
            jan.destroy()
            conta = fn.get()
            conta = conta.title()
            if conta == "Dono":
               janela.destroy()
               donoJanela(1)
               entrarJanela()
            elif conta == "Gerente":
               janela.destroy()
               gerenteJanela(1)
               entrarJanela()
            elif conta == "Funcionário":
               janela.destroy()
               funcionarioJanela(1)
               entrarJanela()
            else:
               label = Label(painel, text="Escolha um tipo para conta!!!", font=("Klavika Med Caps", 13))
               label.place(x=405, y=86)
               janela.after(3000, label.destroy)
         else:
            sit.destroy()
            sit = ttk.Label(jan, text="Senha Pin Incorreta\nTente Novamente", font=("Arial", 12, "bold"), padding=6)
            sit.pack(side=BOTTOM, anchor=CENTER)
      ttk.Label(jan, text="Senha Pin:", font=("Arial", 14, "bold"), padding=6).pack(side=TOP)
      sen = Entry(jan, font=("Arial", 13), width=37, show="*")
      sen.pack(side=TOP, anchor=CENTER, pady=4)
      buto = ttk.Button(jan, text="Entrar", takefocus=0, padding=6, command=mostra)
      buto.pack(side=BOTTOM)
      sit = ttk.Label(jan, text="", font=("Arial", 12, "bold"), padding=6)
      sit.pack(side=BOTTOM, anchor=CENTER)

      jan.resizable(0, 0)
      jan.title(" PIN")
      jan.geometry("355x200")
      jan.transient(janela)
      jan.grab_set()
      jan.wait_window()
      jan.mainloop()
   def rec():
      global us, fn, s, sen, sit, senU;
      try:
         usuario = us.get()
         tipo = fn.get()
         banco = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor = banco.cursor()
         if tipo == "Dono":
            conti ="dadosDono"
         elif tipo == "Gerente":
            conti = "infoGerente"
         elif tipo == "Funcionário":
            conti = "infoFuncionario"
         def mostra():
            global s, sen, sit, senU;
            s = sen.get()
            banco2 = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
            cursor2 = banco2.cursor()
            cursor2.execute("SELECT * FROM info")
            infor = cursor2.fetchall()
            sena = infor[0][2]
            if s == sena:
               sit.destroy()
               sit = ttk.Label(jan, text="Usuário:%s\nsenha:%s"%(usuario,senU), font=("Arial", 12, "bold"), padding=6)
               sit.pack(side=BOTTOM, anchor=CENTER)
            else:
               sit.destroy()
               sit = ttk.Label(jan, text="Senha Pin Incorreta\nTente Novamente", font=("Arial", 12, "bold"), padding=6)
               sit.pack(side=BOTTOM, anchor=CENTER)
         sele = "SELECT * FROM %s WHERE email = ?"%conti
         cursor.execute(sele, (usuario,))
         info = cursor.fetchall()
         c = info[0][9]
         print(c)
         bancoa = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/contaAcesso.db")
         cursora = bancoa.cursor()
         if c == "Conta administrador":
            cursora.execute("SELECT * FROM contaAdministrador WHERE email = ?", (usuario,))
            inf = cursora.fetchall()
            senU = inf[0][2]
         elif c == "Conta gerenciamento":
            cursora.execute("SELECT * FROM contaGerenciamento WHERE email = ?", (usuario,))
            inf = cursora.fetchall()
            senU = inf[0][2]
         jan = Toplevel()
         
         ttk.Label(jan, text="Senha Pin:", font=("Arial", 14, "bold"), padding=6).pack(side=TOP)
         sen = Entry(jan, font=("Arial", 13), width=37, show="*")
         sen.pack(side=TOP, anchor=CENTER, pady=4)
         buto = ttk.Button(jan, text="Obter Senha", takefocus=0, padding=6, command=mostra)
         buto.pack(side=BOTTOM)
         sit = ttk.Label(jan, text="", font=("Arial", 12, "bold"), padding=6)
         sit.pack(side=BOTTOM, anchor=CENTER)
                   
         jan.resizable(0, 0)
         jan.title(" PIN")
         jan.geometry("355x200")
         jan.transient(janela)
         jan.grab_set()
         jan.wait_window()
         jan.mainloop()
      except:
         label = Label(painel, text="Esse email não existe em nosso sistema!!", font=("Klavika Med Caps", 13))
         label.place(x=250, y=172)
         janela.after(3000, label.destroy)
         
   def entra():
      global us, sn, fn, senha;
      try:
         tipo = fn.get()
         usuario = us.get()
         senha = sn.get()
         banco1 = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/meusDados.db")
         cursor1 = banco1.cursor()
         banco2 = sqlite3.connect("C:/ProgramData/TMS/bancoMeus/contaAcesso.db")
         cursor2 = banco2.cursor()
         if tipo == "Dono":
            cursor1.execute("SELECT * FROM dadosDono WHERE email = ?", (usuario,))
            info = cursor1.fetchall()
            nconta = info[0][9]
         elif tipo == "Gerente":
            cursor1.execute("SELECT * FROM infoGerente WHERE email = ?", (usuario,))
            info = cursor1.fetchall()
            nconta = info[0][9]
         elif tipo == "Funcionário":
            cursor1.execute("SELECT * FROM infoFuncionario WHERE email = ?", (usuario,))
            info = cursor1.fetchall()
            nconta = info[0][9]
         if str(nconta) == "Não tem conta":
            label = Label(painel, text="Com esse email não foi criado conta de acesso!!", font=("Klavika Med Caps", 13))
            label.place(x=340, y=172)
            janela.after(3000, label.destroy)
         elif str(nconta) == "Conta gerenciamento":
            cursor2.execute("SELECT * FROM contaGerenciamento WHERE email = ?", (usuario,))
            info = cursor2.fetchall()
            sen = info[0][2]
            if sen == senha:
               janela.destroy()
               gerenciarJanela(info[0][4], info[0][1], "Gerenciador")
            else:
               label = Label(painel, text="Essa senha não confere com usuário!!", font=("Klavika Med Caps", 13))
               label.place(x=362, y=198)
               janela.after(3000, label.destroy)
         else:
            cursor2.execute("SELECT * FROM contaAdministrador WHERE email = ?", (usuario,))
            info = cursor2.fetchall()
            sen = info[0][2]
            if sen == senha:
               janela.destroy()
               gerenciarJanela(info[0][4], info[0][1], "Administrador")
            else:
               label = Label(painel, text="Essa senha não confere com usuário!!", font=("Klavika Med Caps", 13))
               label.place(x=362, y=198)
               janela.after(3000, label.destroy)
      except:
         label = Label(painel, text="Esse conta não existe em nosso sistema!!", font=("Klavika Med Caps", 13))
         label.place(x=334, y=168)
         janela.after(3000, label.destroy)
   
   #############
      
   #Cores burlywood, lightsalmon, 
   #barra de comfiguração
   imC = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/ImageConta.png")
   imM = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/imagemesa.png")
   imP = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/imageproduto.png")
   imCo = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/imageconfig.png")
   imS = PhotoImage(file="C:/ProgramData/TMS/Imagens/Menu Tms/ImageSair.png")
   # estilo de barra de ferramenta
   style = ttk.Style()
   style.configure("BW.TButton", background='gray89', relief=FLAT, foreground="green4")
   novaC = ttk.Button(painel, image=imC, underline=2, text="+ Nova Conta", style="BW.TButton", compound=LEFT, takefocus=False, command=novaCO)
   novaC.place(x=30, y=7)
   editarM = ttk.Button(painel, image=imM, underline=2, text="+ Editar Mesa", style="BW.TButton", compound=LEFT, takefocus=False, command=editeM)
   editarM.place(x=144, y=7)
   editarP = ttk.Button(painel, image=imP, underline=2, text="+ Editar Produto", style="BW.TButton", compound=LEFT, takefocus=False, command=editeP)
   editarP.place(x=256, y=7)
   config = ttk.Button(painel, image=imCo, underline=2, text="+ Configuração", style="BW.TButton", compound=LEFT, takefocus=False, command=configure)
   config.place(x=382, y=7)
   sair = ttk.Button(painel, image=imS, underline=2, text=" Fechar Janela", style="BW.TButton", compound=LEFT, takefocus=False, command=fechar)
   sair.place(x=505, y=7)

   ft = PhotoImage(file="C:/ProgramData/TMS/Imagens/ImageRes.png")
   ll = Label(logo, image=ft, bg="white")
   ll.place(x=700, y=15)

   im = PhotoImage(file="C:/ProgramData/TMS/Imagens/ImageResizer.net - uz0q9za9qxgmb9o.png")
   lb = Label(painel, image=im, bg="gray30")
   lb.place(x=30, y=46)


   # Conta da pessoa
   ttk.Label(painel, text="Conta:", font=("Klavika Med Caps", 13), background="gray97").place(x=145, y=85)
   ttk.Label(painel, text="Tipo", font=("Klavika Med Caps", 7, "bold"), background="gray97").place(x=158, y=102)
   variavel_fn = StringVar()
   fn = ttk.Combobox(painel, textvariable= variavel_fn, height=25, width=18, font=("Arial", 13))
   fn["values"] = ("", "Dono", "Gerente", "Funcionário")
   fn.current(0)
   fn.place(x=212, y=86)

   # separador 1
   separador1 = Frame(painel, height=2, bd=0.0, relief=FLAT, bg="black")
   separador1.pack(side=TOP, fill=X, padx=5, pady=2)

   # linha entre a barra e image
   painel.create_line(30, 39, tamX*0.6-30, 39)
   # linha entre a image e os campos de entrada
   painel.create_line(30, 157, tamX*0.6-30, 157)
   # linha entre a image e os botoes
   painel.create_line(30, 258, tamX*0.6-30, 258)
   # ultima linha
   painel.create_line(5, 297, tamX*0.6-5, 297, width=2, fill="black")

   def subus():
      global us;
      us.delete(0, END)
   def subsn():
      global sn; 
      sn.delete(0, END)
      sn.configure(show="*")
   def mostra():
      global sn; 
      sn.configure(show="")
      def troca():
            sn.configure(show="*")
      if sn.get() != " senha":   
         janela.after(600, troca)
   # dados de entrada
   ttk.Label(painel, text="Usuário:", background="gray97", font=("Klavika Med Caps", 12)).place(x=30, y=168)
   ttk.Label(painel, text="Senha:", background="gray97", font=("Klavika Med Caps", 12)).place(x=30, y=198)
   us = ttk.Entry(painel,  width=25, font=("Arial", 12), takefocus=False, validate="focusin", validatecommand=subus)
   sn = ttk.Entry(painel,  width=25, font=("Arial", 12), takefocus=False, validate="focusin", validatecommand=subsn)
   us.place(x=100, y=168)
   sn.place(x=100, y=198)
   us.insert(INSERT, " email")
   sn.insert(INSERT, " senha")
   # botões
   btE = ttk.Button(painel, text="Entrar", width=37, takefocus=False, command=entra)
   btE.place(x=100, y=225)

   ima = PhotoImage(file="C:/ProgramData/TMS/Imagens/secs.png")
   verse = ttk.Button(painel, image=ima, takefocus=0, command=mostra)
   verse.place(x=332, y=197)

   btS = ttk.Button(painel, text="Esqueceu a conta?", width=20, takefocus=False, command=rec)
   btCs = ttk.Button(painel, text="Nova conta?", width=15, takefocus=False, command=novaCO)
   btS.place(x=201, y=266)
   btCs.place(x=100, y=266)

   janela.geometry("%ix%i+%i+%i"%(tamX*0.6, tamY*0.6, tamX*0.19, tamY*0.18))
   janela.config(relief=FLAT)
   janela.config(bg="gray97")

   instrucao = tix.Balloon(janela, status=status, initwait=100, state='both')
   ###
   instrucao.bind_widget(btS, balloonmsg='clique',
   statusmsg='para recuperar senha')
   ###
   instrucao.bind_widget(btCs, balloonmsg='clique',
   statusmsg='para criar conta')
   ###
   instrucao.bind_widget(fn, balloonmsg='inserir',
   statusmsg='o tipo da conta')
   ###
   instrucao.bind_widget(btE, balloonmsg='clique',
   statusmsg='para entrar na conta')
   ###
   instrucao.bind_widget(verse, balloonmsg='clique',
   statusmsg='para visualizar senha')
   ### 
   instrucao.bind_widget(us, balloonmsg='inserir',
   statusmsg='o email usuário')
   ###
   instrucao.bind_widget(sn, balloonmsg='inserir',
   statusmsg='a senha do usuário')
   ###
   instrucao.bind_widget(novaC, balloonmsg='clique',
   statusmsg='para criar conta')
   ###
   instrucao.bind_widget(editarM, balloonmsg='clique',
   statusmsg='para editar mesa')
   ###
   instrucao.bind_widget(editarP, balloonmsg='clique',
   statusmsg='para editar produto')
   ### 
   instrucao.bind_widget(config, balloonmsg='clique',
   statusmsg='para configurações')
   ###
   instrucao.bind_widget(sair, balloonmsg='clique',
   statusmsg='para fechar janela')
   ###

   janela.minsize(int(tamX*0.6), int(tamY*0.6))
   janela.maxsize(int(tamX*0.6), int(tamY*0.6))
   janela.overrideredirect(1)
   janela.mainloop()
