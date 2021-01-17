from reportlab.pdfgen import canvas
import datetime
import sqlite3
import os
def GeneratePDF(tab, total, dinheiro, troco):
    try:
        hora = datetime.datetime
        hora = hora.today()
        formato = ""
        formato += "mesa["+str(tab)+"]"
        formato += "-"
        formato += "data["+str(hora.date())+"]"
        formato += "-"
        formato += "hora["+str(hora.hour)+"-"+str(hora.minute)+"]"

        
        pdf = canvas.Canvas("C:/ProgramData/TMS/cumpomFiscal/{}.pdf".format(formato))

        
        bancoMesa = sqlite3.Connection("C:/ProgramData/TMS/bancoMesa/mesasDados.db")
        cursoMesa = bancoMesa.cursor()
        cursoMesa.execute("CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                            tipo TEXT, nome TEXT, qtd INTEGER, preco REAL)"%tab)
        cursoMesa.execute("SELECT * FROM %s"%tab)
        compras = cursoMesa.fetchall()

        lista = list(compras)
        x = 720
        for i in lista:
            pdf.drawString(200,x, '{}   {}   {}un   {}'.format(i[1], i[2], str(i[3]), str(i[4])))
            x -= 20

        pdf.drawString(200,x, '{}                {}'.format("Total", total))
        x -= 20
        pdf.drawString(200,x, '{}                {}'.format("Dinheiro", dinheiro))
        x -= 20
        pdf.drawString(200,x, '{}                {}'.format("Troco", troco))

        
        pdf.setTitle(formato)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,760, 'Cupom Fiscal')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(20,744, '===============================================================================')
        pdf.save()


        #abrir arquivo pdf
        ab = "start C:/ProgramData/TMS/cumpomFiscal/"+formato+".pdf"
        ##print(ab)
        os.system(ab)
    except:
        pass
