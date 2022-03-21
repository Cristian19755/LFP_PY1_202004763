from tkinter import  RAISED,Button, Menu, Menubutton, Text, Tk, filedialog,END
from easygui import msgbox
from Analizador import AnalizadorLexico
import webbrowser
class main:
    def __init__(self):
        self.archivo = ''

    def abrirArchivo(self):
        self.archivo = filedialog.askopenfilename(title='Abrir')
        self.archivo = open(self.archivo,'r')
        self.archivo = self.archivo.read()
        D.insert(END ,self.archivo)

    def reporteTokens(self):
        al = AnalizadorLexico()
        archivo = D.get('1.0','end')
        al.analizar(archivo)
        Tokens = al.imprimirTokens()
        msgbox(Tokens, 'Reporte de Tokens')
        al.imprimirTokens2()

    def reporteErrores(self):
        al = AnalizadorLexico()
        archivo = D.get('1.0','end')
        al.analizar(archivo)
        Errores = al.imprimirErrores()
        msgbox(Errores, 'Reporte de Errores')
        al.imprimirErrores2()

    def manualUsuario(self):
        webbrowser.open('MANUAL DE USUARIO.pdf')

    def manualTecnico(self):
        webbrowser.open('MANUAL TECNICO.pdf')
    def analizar(self):
        al = AnalizadorLexico()
        archivo = D.get('1.0','end')
        x = al.analizar(archivo)
        al.botones(x)
al = AnalizadorLexico()
M = main()
root = Tk()
root.geometry('645x600')
#########################################################################
B = Button(root, text ='CARGAR ARCHIVO', command=M.abrirArchivo, bg='blue', fg='white',height=3, width=15)
B.grid(row = 0 , column = 0, sticky= 'W')

##########################################################################
C = Menubutton(root, text='REPORTES', relief=RAISED,  bg='blue', fg='white',height=3, width=15)
C.grid(row=0, column=0, sticky='E')
C.menu = Menu( C, tearoff = 0)
C["menu"] =  C.menu

C.menu.add_command(label='Reporte de Tokens', command=M.reporteTokens)
C.menu.add_command(label='Reporte de Errores', command=M.reporteErrores)
C.menu.add_command(label='Manual de Usuario', command=M.manualUsuario)
C.menu.add_command(label='Manual Tecnico', command=M.manualTecnico)

###########################################################################
D = Text(root, bg = "light yellow")
D.grid(row=1, column=0)
D.insert(END ,M.archivo)

###########################################################################
E = Button(root, text ='ANALIZAR', command=M.analizar, bg='blue', fg='white',height=3, width=15)
E.grid(row=2, column=0)
root.mainloop()

