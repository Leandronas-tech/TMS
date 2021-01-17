from tkinter import*
from tkinter import ttk
from tkinter import tix
import sqlite3

def guardarDados():
   global num, listaTipos, listaNomes, listaPrecos;
   bancoProduto = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
   cursoProduto = bancoProduto.cursor()
   cursoProduto.execute("CREATE TABLE IF NOT EXISTS dadosProduto(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                     tipo TEXT, nome TEXT, preco TEXT)")
   inserir = "INSERT INTO dadosProduto(tipo, nome, preco) VALUES(?, ?, ?)"
   for i in range(1, num+1):
      cursoProduto.execute(inserir, (listaTipos[i], listaNomes[i], listaPrecos[i]))
      bancoProduto.commit()
      
   cursoProduto.close()
   bancoProduto.close()
def produtoJanela(f):
   global num, produtoja, rep, listaNomes, listaTipos, listaV, listaPrecos, c, tipo, nome, preco;
   c = 0
   num = f
   rep = 1
   corPad = "Olive"
   corPri = "Ghostwhite"
   corL = "gray18" 

   listaNomes = [""]
   listaTipos = [""]
   listaPrecos = [""]
   listaV = [""]
   
   produtoja = tix.Tk()
   xt = produtoja.winfo_screenwidth()
   yt = produtoja.winfo_screenheight()

   logo = Canvas(produtoja, bg=corPad, height=70, relief=FLAT, highlightcolor=corPad, highlightbackground=corPad)
   logo.pack(side=TOP, expand=False, anchor=N, fill=X)

   fundo = Canvas(produtoja, bg=corPad, height=20, relief=FLAT, highlightcolor=corPad, highlightbackground=corPad)
   fundo.pack(side=BOTTOM, expand=True, anchor=S, fill=X)

   status = tix.Label(fundo, text="para instruções passe o mause nos componentes!!", width=40, relief=FLAT, foreground="white", background=corPad, font=("Arial", 11))
   status.pack(anchor=CENTER, fill=Y)

   
   ttk.Label(logo, text="Formulário", background=corPad, font=("Klavika Med Caps", 40,"bold"), foreground="white").place(x=175, y=9)


   ttk.Label(produtoja, text="TIPO:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=305, y=123)
   ttk.Label(produtoja, text="NOME:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=302, y=203)
   ttk.Label(produtoja, text="PREÇO:", font=("Klavika Med Caps", 13,"bold"), foreground=corL, background=corPri).place(x=300, y=283)
   
   tipo_value = StringVar()
   tipo = ttk.Combobox(produtoja, font=("Arial", 12), width=20, textvariable=tipo_value)
   tipo["values"] = ("...", "Cerveja", "Refrigerante", "Salgado", "Salgadinho", "Bala", "Lanche", "Hamburgue", "Prato")
   tipo.place(x=228, y=160)
   nome = ttk.Entry(produtoja, font=("Arial", 12), width=22)
   nome.place(x=228, y=240)
   preco = ttk.Entry(produtoja, font=("Arial", 12), width=22)
   preco.place(x=228, y=320)


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
      global produtoja;
      produtoja.destroy()
   #############################################################
   def limpa():
      global tipo, nome, preco;
      tipo.delete(0, END)
      nome.delete(0, END)
      preco.delete(0, END)
      
   def salvaDado(number):
      global listaNomes, listaTipos, listaV, listaPrecos, tipo, nome, preco;
      try:
         v = listaV[number]
      except:
         listaV.append(number)
         listaNomes.append(number)
         listaTipos.append(number)
         listaPrecos.append(number)
         
         
      listaTipos[number] = tipo.get()
      listaNomes[number] = nome.get()
      listaPrecos[number] = preco.get()
   
   def salv():
      global rep, c, listaNomes, listaTipos, listaV, listaPrecos, tipo, nome, preco;
      if c == f or (f == 1 and c == 0):
         if rep == 2:
            if tipo.get() != "" and nome.get() != "" and preco.get() != "":
               salvaDado(f)
               guardarDados()
               produtoja.destroy()
         else:
            if tipo.get() != "" and nome.get() != "" and preco.get() != "":
               salvaDado(f)
               labr = ttk.Label(produtoja, text="Pressione o botão denovo para fechar a janela", font=("Klavika Med Caps", 14), background="gray20", foreground="white", width=40)
               labr.place(x=109, y=381.85)
               produtoja.after(3500, labr.destroy)
               rep += 1
      else:
         if c == 0:
            salvaDado(1)
         else:
            salvaDado(c)
         #################################
   def prox():
      global c, listaNomes, listaTipos, listaV, listaPrecos, tipo, nome, preco;
      if c >= 0 and c < f and f != 1:
         if c == 0:
            v = verificarUnica(1)
         else:
            v = verificarUnica(c)
         if v == True and tipo.get() != "" and nome.get() != "" and preco.get() != "":
            try:
               if c == 0:
                  lab.configure(text="Produto %dº"%(c+2))
                  c += 2
               else:
                  lab.configure(text="Produto %dº"%(c+1))
                  c += 1
                  
               nm = listaV[c]
               #######
               limpa()
               #######
               tipo.insert(END, listaTipos[c])
               nome.insert(END, listaNomes[c])
               preco.insert(END, listaPrecos[c])
               if c == 1:
                  c += 1
            except:
               #######
               limpa()
               #######
               lab.configure(text="Produto %dº"%(c))
      else:
         v = verificarUnica(f)
         if v == True and tipo.get() != "" and nome.get() != "" and preco.get() != "":
            lab.configure(text="Produto %dº"%(f))
            try:
               nm = listaV[f]
               #######
               limpa()
               #######
               tipo.insert(END, listaTipos[f])
               nome.insert(END, listaNomes[f])
               preco.insert(END, listaPrecos[f])
   
            except:
               listaTipos[f] = tipo.get()
               listaNomes[f] = nome.get() 
               listaPrecos[f] = preco.get()
              
   #############################################################
   def ante():
      global rep, listaNomes, listaTipos, listaV, listaPrecos, c, tipo, nome, preco;
      if c >= 1 and c <= f:
         v = verificar()
         if c == 1:
            if v == True and tipo.get() != "" and nome.get() != "" and preco.get() != "":
               lab.configure(text="Produto %dº"%(c))
               #######
               limpa()
               ######
               tipo.insert(END, listaTipos[c])
               nome.insert(END, listaNomes[c])
               preco.insert(END, listaPrecos[c])
               c = 0
         else:
            if  v == True and tipo.get() != "" and nome.get() != "" and preco.get() != "":
               if c == f:
                  rep = 1
               c -= 1
               lab.configure(text="Produto %dº"%(c))
               #######
               limpa()
               ######
               tipo.insert(END, listaTipos[c])
               nome.insert(END, listaNomes[c])
               preco.insert(END, listaPrecos[c])   

   
   #######
   cancela = Button(produtoja,text="Cancelar", command=canc, relief=GROOVE, background=corPri,\
                    font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                    takefocus=0)
   cancela.place(x=110, y=380)

   anterio = Button(produtoja, text="<< Anterior", command=ante, relief=GROOVE,  background=corPri,\
                    font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                    takefocus=0)
   anterio.place(x=220, y=380)

   proximo = Button(produtoja, text="Proximo >>", command=prox, relief=GROOVE,  background=corPri,\
                    font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                    takefocus=0)
   proximo.place(x=330, y=380)

   salva = Button(produtoja, text="Salvar",  command=salv, relief=GROOVE,  background=corPri,\
                  font=("Klavika Med Caps", 11, "bold"), width=11, foreground=corL, activeforeground=corL,\
                  takefocus=0)
   salva.place(x=440, y=380)
   
   lab = ttk.Label(produtoja, text="Produto %dº"%(1), font=("Klavika Med Caps", 14,"bold"), foreground=corL, background=corPri)
   lab.place(x=280, y=80)

   instrucao = tix.Balloon(produtoja, status=status, initwait=100, state='both')
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
   instrucao.bind_widget(tipo, balloonmsg='inserir',
   statusmsg='o tipo do produto; Exemplo: Cerveja')
   ###
   instrucao.bind_widget(nome, balloonmsg='inserir',
   statusmsg='o nome do produto; Exemplo: Skol')
   ###
   instrucao.bind_widget(preco, balloonmsg='inserir',
   statusmsg='o preço do produto; Exemplo: 3.40')
   ###
   
   produtoja.config(bg=corPri)
   produtoja.geometry("%dx%d+%d+%d"%(xt/2.1, yt/1.7, xt/3.3, yt/5))
   produtoja.overrideredirect(1)
   produtoja.mainloop()
