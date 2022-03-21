from Token import Token
from Error import Error
from prettytable import PrettyTable
from tkinter import Radiobutton, Button, Label, Entry, Tk, END, W, IntVar, RAISED, Menubutton, Menu
import webbrowser

class AnalizadorLexico: 
    def __init__(self) -> None:
        self.listaTokens  = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 1
        self.i = 0
        self.x = []

    def s1(self,lexema):
        if lexema == 'f':
            self.buffer += lexema
            self.columna += 1
            self.estado = 2
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s2(self,lexema):
        if lexema == 'o':
            self.buffer += lexema
            self.columna += 1
            self.estado = 3
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s3(self,lexema):
        if lexema == 'r':
            self.buffer += lexema
            self.columna += 1
            self.estado = 4
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s4(self,lexema):
        if lexema == 'm':
            self.buffer += lexema
            self.columna += 1
            self.estado = 5
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s5(self,lexema):
        if lexema == 'u':
            self.buffer += lexema
            self.columna += 1
            self.estado = 6
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s6(self,lexema):
        if lexema == 'l':
            self.buffer += lexema
            self.columna += 1
            self.estado = 7
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s7(self,lexema):
        if lexema == 'a':
            self.buffer += lexema
            self.columna += 1
            self.estado = 8
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s8(self,lexema):
        if lexema == 'r':
            self.buffer += lexema
            self.columna += 1
            self.estado = 9
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s9(self,lexema):
        if lexema == 'i':
            self.buffer += lexema
            self.columna += 1
            self.estado = 10
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s10(self,lexema):
        if lexema == 'o':
            self.buffer += lexema
            self.columna += 1
            self.estado = 11
            self.listaTokens.append(
                Token(self.buffer,
                        self.linea,
                        self.columna,
                        'PALABRA RESERVADA'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error("ERROR lexema  {} desconocido".format(lexema),
                self.linea,
                self.columna))
    def s11(self, lexema):
        if lexema == '~':
            self.buffer += lexema
            self.columna += 1
            self.estado = 12
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def s12(self, lexema):
        if lexema == '>':
            self.buffer += lexema
            self.columna += 1
            self.estado = 13
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def s13(self, lexema):
        if lexema == '>':
            self.buffer += lexema
            self.columna += 1
            self.estado = 14
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'SIMBOLO ESPECIAL'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def analizar(self, cadena):
        self.listaErrores = []
        self.listaTokens = []
        
        self.i = 0

        while self.i < len(cadena):
            if cadena[self.i] == '\n':
                self.linea += 1
                self.columna = 0
            if self.estado == 1:
                self.s1(cadena[self.i])
            elif self.estado == 2:
                self.s2(cadena[self.i])
            elif self.estado == 3:
                self.s3(cadena[self.i])
            elif self.estado == 4:
                self.s4(cadena[self.i])
            elif self.estado == 5:
                self.s5(cadena[self.i])
            elif self.estado == 6:
                self.s6(cadena[self.i])
            elif self.estado == 7:
                self.s7(cadena[self.i])
            elif self.estado == 8:
                self.s8(cadena[self.i])
            elif self.estado == 9:
                self.s9(cadena[self.i])
            elif self.estado == 10:
                self.s10(cadena[self.i])
            elif self.estado == 11:
                self.s11(cadena[self.i])
            elif self.estado == 12:
                self.s12(cadena[self.i])
            elif self.estado == 13:
                self.s13(cadena[self.i])
            elif self.estado == 14:
                self.s14(cadena[self.i])
            elif self.estado == 15:
                self.s15(cadena[self.i])
            elif self.estado == 16:
                self.ts16(cadena[self.i])
            elif self.estado == 17:
                self.ts17(cadena[self.i])
            elif self.estado == 18:
                self.ts18(cadena[self.i])
            elif self.estado == 19:
                self.ts19(cadena[self.i])
            elif self.estado == 20:
                self.s20(cadena[self.i])
            elif self.estado == 21:
                self.s21(cadena[self.i])
            elif self.estado == 22:
                self.s22(cadena[self.i])
            elif self.estado == 23:
                self.s23(cadena[self.i])
            elif self.estado == 24:
                self.s24(cadena[self.i])
            elif self.estado == 25:
                self.s25(cadena[self.i])
            elif self.estado == 26:
                self.vs26(cadena[self.i])
            elif self.estado == 27:
                self.vs27(cadena[self.i])
            elif self.estado == 28:
                self.vs28(cadena[self.i])
            elif self.estado == 29:
                self.vs29(cadena[self.i])
            elif self.estado == 30:
                self.fs30(cadena[self.i])
            elif self.estado == 31:
                self.fs31(cadena[self.i])
            elif self.estado == 32:
                self.fs32(cadena[self.i])
            elif self.estado == 33:
                self.fs33(cadena[self.i])
            elif self.estado == 34:
                self.es34(cadena[self.i])
            elif self.estado == 35:
                self.es35(cadena[self.i])
            elif self.estado == 36:
                self.es36(cadena[self.i])
            elif self.estado == 37:
                self.es37(cadena[self.i])
            elif self.estado == 38:
                self.es38(cadena[self.i])
            elif self.estado == 39:
                self.vs39(cadena[self.i])
            self.i += 1 
        self.tokens()
        return self.x   
    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
        return x
    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["DEscripcion","linea","columna"]
        for error_ in self.listaErrores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        return x 
    def imprimirErrores2(self):
        reporte = open('Errores.html', 'w')
        dats = """<table border="1" style="width: 100%; border-collapse: collapse; border-style: double;">
    <tbody>
    <tr>
    <td style="width: 33%; text-align: center;">descripcion</td>
    <td style="width: 33%; text-align: center;">linea</td>
    <td style="width: 33%; text-align: center;">columna</td>
    </tr>"""
        for i in self.listaErrores:
            dats = dats+"""<tr>
        <td style="width: 33%; text-align: center;">"""+str(i.descripcion)+ """</td>
        <td style="width: 33%; text-align: center;">"""+str(i.linea)+"""</td>
        <td style="width: 33%; text-align: center;">"""+str(i.columna)+"""</td>
        </tr>
        <tr>"""
        reporte.write(dats)
        reporte.close()
        webbrowser.open_new_tab('Errores.html')
    def imprimirTokens2(self):
        reporte = open('Tokens.html', 'w')
        dats = """<table border="1" style="width: 100%; border-collapse: collapse; border-style: double;">
    <tbody>
    <tr>
    <td style="width: 25%; text-align: center;">lexema</td>
    <td style="width: 25%; text-align: center;">linea</td>
    <td style="width: 25%; text-align: center;">columna</td>
    <td style="width: 25%; text-align: center;">tipo</td>
    </tr>"""
        for i in self.listaTokens:
            dats = dats+"""<tr>
        <td style="width: 25%; text-align: center;">"""+str(i.lexema)+ """</td>
        <td style="width: 25%; text-align: center;">"""+str(i.linea)+"""</td>
        <td style="width: 25%; text-align: center;">"""+str(i.columna)+"""</td>
        <td style="width: 25%; text-align: center;">"""+str(i.tipo)+"""</td>
        </tr>
        <tr>"""
        reporte.write(dats)
        reporte.close()
        webbrowser.open_new_tab('Tokens.html')
    def s14(self, lexema):
        if lexema == '[':
            self.buffer += lexema
            self.columna += 1
            self.estado = 15
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def s15(self, lexema):
        if lexema == '<':
            self.buffer += lexema
            self.columna += 1
            self.estado = 16
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def ts16(self, lexema):
        if lexema == 't':
            self.buffer += lexema
            self.columna += 1
            self.estado = 17
        elif lexema == 'v':
            self.buffer += lexema
            self.columna += 1
            self.estado = 26
        elif lexema == 'f':
            self.buffer += lexema
            self.columna += 1
            self.estado = 30
        elif lexema == 'e':
            self.buffer += lexema
            self.columna += 1
            self.estado = 34
        elif lexema == '"':
            self.buffer += lexema
            self.columna += 1
            self.estado = 22
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def ts17(self, lexema):
        if lexema == 'i':
            self.buffer += lexema
            self.columna += 1
            self.estado = 18
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def ts18(self, lexema):
        if lexema == 'p':
            self.buffer += lexema
            self.columna += 1
            self.estado = 19
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def ts19(self, lexema):
        if lexema == 'o':
            self.buffer += lexema
            self.columna += 1
            self.estado = 20
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'IDENTIFICADOR'))
            self.buffer = ''

        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def s20(self, lexema):
        if lexema == ':':
            self.buffer += lexema
            self.columna += 1
            self.estado = 21
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        elif lexema == 'e':
            self.listaTokens.pop(len(self.listaTokens)-1)
            self.buffer == 'valore'
            self.columna += 1
            self.estado = 39
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def s21(self, lexema):
        if lexema == '"':
            self.buffer += lexema
            self.columna += 1
            self.estado = 22
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        elif lexema == '[':
            self.buffer += lexema
            self.columna += 1
            self.estado = 21
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def s22(self, lexema):
        if lexema != '"':
            self.buffer += lexema
            self.columna += 1
            self.estado = 22
        else:
            self.columna += 1
            self.estado = 24
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'CADENA'))
            self.buffer = ''
            self.columna += 1
            self.listaTokens.append(
                    Token('"',
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''    
    def s24(self, lexema):
        if lexema == '>':
            self.buffer += lexema
            self.columna += 1
            self.estado = 25
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        elif lexema == ',':
            self.buffer += lexema
            self.columna += 1
            self.estado = 16
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        elif lexema == ']':
            self.buffer += lexema
            self.columna += 1
            self.estado=24
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def s25(self, lexema):
        if lexema == ',':
            self.buffer += lexema
            self.columna += 1
            self.estado = 15
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
            self.buffer = ''
        elif lexema == ']':
            self.buffer += lexema
            self.columna += 1
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'DELIMITADOR'))
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def vs26(self, lexema):
        if lexema == 'a':
            self.buffer += lexema
            self.columna += 1
            self.estado = 27
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def vs27(self, lexema):
        if lexema == 'l':
            self.buffer += lexema
            self.columna += 1
            self.estado = 28
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def vs28(self, lexema):
        if lexema == 'o':
            self.buffer += lexema
            self.columna += 1
            self.estado = 29
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def vs29(self, lexema):
        if lexema == 'r':
            self.buffer += lexema
            self.columna += 1
            self.estado = 20
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'IDENTIFICADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def fs30(self, lexema):
        if lexema == 'o':
            self.buffer += lexema
            self.columna += 1
            self.estado = 31
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def fs31(self, lexema):
        if lexema == 'n':
            self.buffer += lexema
            self.columna += 1
            self.estado = 32
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def fs32(self, lexema):
        if lexema == 'd':
            self.buffer += lexema
            self.columna += 1
            self.estado = 33
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def fs33(self, lexema):
        if lexema == 'o':
            self.buffer += lexema
            self.columna += 1
            self.estado = 20
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'IDENTIFICADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def es34(self, lexema):
        if lexema == 'v':
            self.buffer += lexema
            self.columna += 1
            self.estado = 35
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def es35(self, lexema):
        if lexema == 'e':
            self.buffer += lexema
            self.columna += 1
            self.estado = 36
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def es36(self, lexema):
        if lexema == 'n':
            self.buffer += lexema
            self.columna += 1
            self.estado = 37
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def es37(self, lexema):
        if lexema == 't':
            self.buffer += lexema
            self.columna += 1
            self.estado = 38
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def es38(self, lexema):
        if lexema == 'o':
            self.buffer += lexema
            self.columna += 1
            self.estado = 20
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'IDENTIFICADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def vs39(self, lexema):
        if lexema == 's':
            self.buffer += lexema
            self.columna += 1
            self.estado = 20
            self.listaTokens.append(
                    Token('valores',
                        self.linea,
                        self.columna,
                        'IDENTIFICADOR'))
            self.buffer = ''
        else:
            self.columna += 1
            self.listaErrores.append(
                Error('ERROR caracter {} desconocido'.format(lexema),
                self.linea,
                self.columna))
    def tokens(self):
        for token in self.listaTokens:
            y = token.lexema
            self.x.append(y)
        return self.x
    def botones(self, tokens):
        y =[]
        for i in range(0,len(tokens)-1):
            token = tokens[i]
            if token != 'formulario' and token != '~>>' and token !='"' and token != ':' and token !=',':
                y.append(token)
        y.pop(0)
        z = []
        z1 = []
        z2 = []
        temp = 1
        for token in y:
            if token == '<':
                z = []
            elif token == '>':
                z1.append(z)
            else:
                if token == '[':
                    z2 = []
                    temp = 0
                elif token == ']':
                    z.append(z2)
                    temp = 1
                elif temp == 0:
                    z2.append(token)
                else:
                    z.append(token)
        temp = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0 
        root = Tk()
        
        for button in z1:
            temp = 0
            for token in button:
                if temp4 == 1:
                    var = IntVar()
                    contador = 1
                    for i in token:
                        R1 = Radiobutton(root, text=i, variable=var, value=contador)
                        R1.pack(anchor=W)
                        contador += 1
                    temp = 0
                    temp2 = 0 
                    temp3 = 0 
                    temp4 = 0
                elif temp4 == 2:
                    var = IntVar()
                    contador = 1
                    C = Menubutton(root, text='opciones', relief=RAISED,  bg='blue', fg='white',height=3, width=15)
                    C.pack(anchor=W)
                    C.menu = Menu( C, tearoff = 0)
                    C["menu"] =  C.menu
                    for i in token:
                        C.menu.add_checkbutton(label=i)
                    temp4 = 0
                ##################################################
                if temp3 == 1:
                    L = Label(root, text=token)
                    L.pack(anchor=W)
                    temp2 = 0
                    temp3 = 0
                elif temp3 == 2:
                    token+=': '
                    J = Label(root, text=token)
                    J.pack(anchor=W)
                    temp2 = 0
                    temp3 = 0
                elif temp3 == 3:
                    token += ': '
                    K = Label(root, text=token)
                    K.pack(anchor=W)
                    temp3 = 0
                elif temp3 == 4:
                    token += ': '
                    K = Label(root, text=token)
                    K.pack(anchor=W)
                    temp3 = 0
                elif temp3 == 5:
                    N = Button(root, text=token, bg='red', fg='white',height=3, width=14)
                    N.pack(anchor=W)
                #################################################
                if temp == 1:
                    if token == 'etiqueta' or token == 'label':
                        temp2 = 1
                    elif token == 'texto':
                        temp2 = 2
                    elif token == 'grupo-radio':
                        temp2 = 3
                    elif token == 'grupo-option':
                        temp2 = 4
                    elif token == 'boton':
                        temp2 = 5
                elif temp == 2:
                    J = Entry(root, width=40)
                    J.insert(END, token)
                    J.pack()
                    temp = 0
                
                #################################################
                if token == 'tipo':
                    temp = 1
                if token == 'fondo':
                    temp = 2
                #################################################
                if token == 'valor' and temp2 == 1 :
                    temp3 = 1
                if token == 'valor' and temp2 == 2:
                    temp3 = 2
                if token == 'valor' and temp2==3:
                    temp3 = 3
                if token == 'valores' and temp2 == 3:
                    temp4 = 1
                if token == 'valor' and temp2 == 4:
                    temp3 = 4
                if token == 'valores' and temp2 == 4:
                    temp4 = 2
                if token == 'valor' and temp2 == 5:
                    temp3 = 5
                #################################################
            O = Label(root, text='\n')
            O.pack()        
        root.mainloop()   