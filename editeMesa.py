from tkinter import *
from tkinter import ttk
from tkinter import tix
import sqlite3
import os 

def criaDadoMesa(nMesa):
   bancoMesa = sqlite3.Connection("C:/ProgramData/TMS/bancoMesa/mesasDados.db")
   cursoMesa = bancoMesa.cursor()
   arquivo = open("C:/ProgramData/TMS/bancoMesa/mesaNumero.txt", "r")
   n = int(arquivo.read())+1
   arquivo.close()
   os.remove("C:/ProgramData/TMS/bancoMesa/mesaNumero.txt")
   bancoInfo = sqlite3.Connection("C:/ProgramData/TMS/bancoMeus/meusDados.db")
   cursoInfo = bancoInfo.cursor()
   edite = "UPDATE info SET informacao = ?, valor = ? WHERE valor = ?"
   if nMesa > 0:
      for i in range(n, nMesa+n):
         tab = "_"+str(i)+"_"
         cursoMesa.execute("CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                           tipo TEXT, nome TEXT, qtd INTEGER, preco REAL)"%tab)
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesaNumero.txt", "w")
      arquivo.write(str(nMesa+(n-1)))
      arquivo.close()
      cursoInfo.execute(edite, ("Quantidade de Mesa", str((nMesa+(n-1))), str(n-1),))
   else:
      nMesa = nMesa*(-1)
      ini = (n-nMesa)-1
      for i in range(ini, n):
         tab = "_"+str(i)+"_"
         cursoMesa.execute("DROP TABLE %s"%tab)          
      arquivo = open("C:/ProgramData/TMS/bancoMesa/mesaNumero.txt", "w")
      arquivo.write(str(ini))
      arquivo.close()
      cursoInfo.execute(edite, ("Quantidade de Mesa", str(ini), str(n-1),))

   bancoInfo.commit()
   cursoInfo.close()
   bancoInfo.close()
   bancoMesa.commit()
   cursoMesa.close()
   bancoMesa.close()

def mesajanela():
   global ent, nmesa;
   janelaM = Tk()
   nmesa = 0
   def adi():
      global ent, nmesa;
      nmesa += 1
      ent.configure(text="%s"%nmesa)
   def sub():
      global ent, nmesa;
      nmesa -= 1
      ent.configure(text="%s"%nmesa)
   def sal():
      global nmesa;
      if nmesa != 0:
         if nmesa > 0:
            l = Label(janelaM, text="Foram adicionadas %s mesas"%nmesa, font=("Klavika Med Caps", 14, "bold"))
            l.place(x=0, y=65)
         else:
            l = Label(janelaM, text="Foram removidas %s mesas"%(nmesa*(-1)), font=("Klavika Med Caps", 14, "bold"))
            l.place(x=0, y=65)
         def salter():
            criaDadoMesa(nmesa)
            janelaM.destroy()
         janelaM.after(1200, salter)
         
   but1 = ttk.Button(janelaM, text="+", padding=10, takefocus=0, command=adi)
   but1.pack(side=TOP,pady=6)
   ent = ttk.Label(janelaM, text="%s"%nmesa,padding=8)
   ent.pack(side=TOP,pady=3)
   but2 = ttk.Button(janelaM, text="-", padding=10, takefocus=0, command=sub)
   but2.pack(side=TOP,pady=5)
   but3 = ttk.Button(janelaM, text="Salvar", padding=10, takefocus=0, command=sal)
   but3.pack(side=TOP,pady=6)

   janelaM.resizable(width=False, height=False)
   janelaM.resizable(0, 0)
   janelaM.grab_set()
   janelaM.geometry("250x200")
   janelaM.title("Edite Mesa")
   janelaM.iconbitmap("C:/ProgramData/TMS/Imagens/unnamed.ico")
   janelaM.mainloop()
