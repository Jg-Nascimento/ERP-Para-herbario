from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql.cursors


class userwindow():

    def MostarProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from exsicatas')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')



        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []
        for linha in resultado:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

    def PesquisarBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from exsicatas where familia LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()

        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def PesquisarBackEnd1(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from exsicatas where nomeVulgar LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()

        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def PesquisarBackEnd2(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from exsicatas where especie LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()
        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def __init__(self):
        self.user = Tk()
        self.user.resizable(True, True)
        self.user.protocol("WM_DELETE_WINDOW")
        self.user.title("Cadastrar Produtos")
        self.user['bg'] = '#524F4F'


        self.tree = ttk.Treeview(self.user, selectmode="browse",
                                 column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"),
                                 show='headings')

        scrollbar_horizontal = ttk.Scrollbar(self.user, orient='horizontal', command=self.tree.xview)
        scrollbar_vertical = ttk.Scrollbar(self.user, orient='vertical', command=self.tree.yview)

        self.tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)

        self.tree.column("column1", width=100, minwidth=50, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#2', text='Familia')

        self.tree.column("column3", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#3', text='Genero')

        self.tree.column("column4", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#4', text='Especie')

        self.tree.column("column5", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#5', text='Local')

        self.tree.column("column6", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#6', text='Coletor')

        self.tree.column("column7", width=100, minwidth=50, stretch=NO)
        self.tree.heading('#7', text='Data')


        self.tree.grid(row=7, column=0, padx=10, pady=10, columnspan=6, rowspan=6)

        self.pesquisar = Entry(self.user)
        self.pesquisar.grid(row=14, column=0, columnspan=1, padx=5, pady=5)

        Button(self.user, text='Pesquisar por Familia', width=15, bg='gray', command=self.PesquisarBackEnd,
               relief='flat', highlightbackground='#524F4F', fg='white').grid(row=14, column=1, padx=5, pady=5)

        Button(self.user, text='Pesquisar por Nome', width=15, bg='gray', command=self.PesquisarBackEnd1,
               relief='flat', highlightbackground='#524F4F', fg='white').grid(row=15, column=1, padx=5, pady=5)

        Button(self.user, text='Pesquisar por Especies', width=15, bg='gray', command=self.PesquisarBackEnd2,
               relief='flat', highlightbackground='#524F4F', fg='white').grid(row=16, column=1, padx=5, pady=5)

        Button(self.user, text='Atualizar', width=15, bg='gray', command=self.MostarProdutosBackEnd,
               relief='flat', highlightbackground='#524F4F', fg='white').grid(row=17, column=1, padx=5, pady=5)

        self.MostarProdutosBackEnd()

        self.user.mainloop()



class adminwindow():

    def GerarPDF(self):

        global contador
        contador += 1



        print(contador)

        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

        except:
            print('erro ao conectar no banco de dados')

        with conexao.cursor() as cursor:
            cursor.execute('select * from exsicatas where numeroTombamento = {};'.format(idDeletar))
            resultado = cursor.fetchone()



        from reportlab.pdfgen import canvas
        try:
            pdf = canvas.Canvas(f"Exsicata{contador}.pdf")
            pdf.setTitle('Herbario IFSP Barretos')



            pdf.drawString(10, 810, 'Nome vulvar: {}'.format(resultado['nomeVulgar']))

            pdf.drawString(10, 780, 'Familia: {}'.format(resultado['familia']))

            pdf.drawString(10, 750, 'Genero: {}'.format(resultado['genero']))

            pdf.drawString(10, 720, 'Especie: {}'.format(resultado['especie']))


            pdf.drawString(300, 810, 'Local: {}'.format(resultado['localColeta']))

            pdf.drawString(300, 780, 'Coletor: {}'.format(resultado['coletor']))

            pdf.drawString(300, 750, 'data: {}'.format(resultado['dataColeta']))

            pdf.drawString(300, 720, 'Tombamento: {}'.format(resultado['numeroTombamento']))


            pdf.drawString(10, 690, 'Observaçoes: {}'.format(resultado['observacoes']))


            pdf.save()

            messagebox.showinfo('PDF', 'PDF criado com sucesso')
        except:
            messagebox.showinfo('PDF', 'Erro ao criar PDF')

    def MostarProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from exsicatas')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')



        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []
        for linha in resultado:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])
            linhaV.append(linha['numeroTombamento'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

    def RemoverCadastrosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

        except:
            print('erro ao conectar no banco de dados')

        with conexao.cursor() as cursor:
            cursor.execute('delete from exsicatas where numeroTombamento = {};'.format(idDeletar))
            conexao.commit()

        self.MostarProdutosBackEnd()

    def LimparCadastrosBackEnd(self):

        if messagebox.askokcancel('Limpar dados CUIDADO!!', 'DESEJA EXCLUIR TODOS OS DADOS DA TABELA ? NAO HÁ VOLTA!!'):

            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Caio@lemos12',
                    db='herbario',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

            except:
                print('erro ao conectar no banco de dados')

            with conexao.cursor() as cursor:
                cursor.execute('truncate table exsicatas;')
                conexao.commit()

            self.MostarProdutosBackEnd()

    def CadastrarProdutoBackEnd(self):
        nome = self.nomeVulgar.get()
        familia = self.familia.get()
        genero = self.genero.get()
        especie = self.especie.get()
        localColeta = self.localColeta.get()
        coletor = self.coletor.get()
        data = self.dataColeta.get()

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        with conexao.cursor() as cursor:
            cursor.execute('insert into exsicatas (familia, genero, especie, nomeVulgar, localColeta, coletor, dataColeta) values (%s, %s, %s, %s, %s, %s, %s)', (familia, genero, especie, nome, localColeta, coletor, data))
            conexao.commit()



        self.MostarProdutosBackEnd()
        self.LimparEntry()

    def LimparEntry(self):
        self.nomeVulgar.delete(0, END)
        self.coletor.delete(0, END)
        self.localColeta.delete(0, END)
        self.especie.delete(0, END)
        self.genero.delete(0, END)
        self.familia.delete(0, END)
        self.dataColeta.delete(0, END)

    def PesquisarBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from exsicatas where familia LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()

        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def PesquisarBackEnd1(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from exsicatas where nomeVulgar LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()

        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def PesquisarBackEnd2(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from exsicatas where especie LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()
        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nomeVulgar'])
            linhaV.append(linha['familia'])
            linhaV.append(linha['genero'])
            linhaV.append(linha['especie'])
            linhaV.append(linha['localColeta'])
            linhaV.append(linha['coletor'])
            linhaV.append(linha['dataColeta'])


            self.tree.insert("", END, values=linhaV, iid=linha['numeroTombamento'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def CadastrarExsicatas(self):
        self.cadastrar = Tk()
        self.cadastrar.resizable(True, True)
        self.cadastrar.protocol("WM_DELETE_WINDOW")
        self.cadastrar.title("Cadastrar Produtos")
        self.cadastrar['bg'] = '#524F4F'


        Label(self.cadastrar, text='Cadastre as exsicatas', font='arial, 12', bg='#524F4F', fg='white').grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        Label(self.cadastrar, text='Nome Vulgar', bg='#524F4F', fg='white').grid(row=1, column=0, padx=5, pady=5)
        self.nomeVulgar = Entry(self.cadastrar)
        self.nomeVulgar.grid(row=1, column=1, padx=5)

        Label(self.cadastrar, text='Familia', bg='#524F4F', fg='white').grid(row=1, column=2, padx=5, pady=5)
        self.familia = Entry(self.cadastrar)
        self.familia.grid(row=1, column=3, padx=5, pady=5)

        Label(self.cadastrar, text='Genero', bg='#524F4F', fg='white').grid(row=1, column=4, padx=5, pady=5)
        self.genero = Entry(self.cadastrar)
        self.genero.grid(row=1, column=5, padx=5, pady=5)


        Label(self.cadastrar, text='Especies', bg='#524F4F', fg='white').grid(row=2, column=0, padx=5, pady=5)
        self.especie = Entry(self.cadastrar)
        self.especie.grid(row=2, column=1, padx=5)

        Label(self.cadastrar, text='Local de coleta', bg='#524F4F', fg='white').grid(row=2, column=2, padx=5, pady=5)
        self.localColeta = Entry(self.cadastrar)
        self.localColeta.grid(row=2, column=3, padx=5, pady=5)

        Label(self.cadastrar, text='Coletor', bg='#524F4F', fg='white').grid(row=2, column=4, padx=5, pady=5)
        self.coletor = Entry(self.cadastrar)
        self.coletor.grid(row=2, column=5, padx=5, pady=5)

        Label(self.cadastrar, text='Data da coleta', bg='#524F4F', fg='white').grid(row=3, column=2, padx=5, pady=5)
        self.dataColeta = Entry(self.cadastrar)
        self.dataColeta.grid(row=3, column=3, padx=5, pady=20)




        self.tree = ttk.Treeview(self.cadastrar, selectmode="browse",
                                 column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8"),
                                 show='headings')

        scrollbar_horizontal = ttk.Scrollbar(self.cadastrar, orient='horizontal', command=self.tree.xview)
        scrollbar_vertical = ttk.Scrollbar(self.cadastrar, orient='vertical', command=self.tree.yview)

        self.tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)

        self.tree.column("column1", width=100, minwidth=50, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#2', text='Familia')

        self.tree.column("column3", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#3', text='Genero')

        self.tree.column("column4", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#4', text='Especie')

        self.tree.column("column5", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#5', text='Local')

        self.tree.column("column6", width=200, minwidth=50, stretch=NO)
        self.tree.heading('#6', text='Coletor')

        self.tree.column("column7", width=100, minwidth=50, stretch=NO)
        self.tree.heading('#7', text='Data')

        self.tree.column("column8", width=40, minwidth=40, stretch=NO)
        self.tree.heading('#8', text='Numero')

        Button(self.cadastrar, text='Cadastrar', width=15, bg='gray', command=self.CadastrarProdutoBackEnd, relief='flat', highlightbackground='#524F4F', fg='white').grid(row=3, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir', width=15, bg='gray' , relief='flat', highlightbackground='#524F4F', command=self.RemoverCadastrosBackEnd, fg='white').grid(row=3, column=4, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar', width=15, bg='gray', relief='flat', command=self.MostarProdutosBackEnd, highlightbackground='#524F4F', fg='white').grid(row=4, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar produtos', width=15, bg='red4', relief='flat', highlightbackground='#524F4F', command=self.LimparCadastrosBackEnd, fg='white').grid(row=4, column=4, padx=5, pady=5)
        Button(self.cadastrar)


        self.tree.grid(row=7, column=0, padx=10, pady=10, columnspan=6, rowspan=6)




        self.pesquisar = Entry(self.cadastrar)
        self.pesquisar.grid(row=14, column=0, columnspan=1, padx=5, pady=5)



        Button(self.cadastrar, text='Pesquisar por Familia', width=15, bg='gray', command=self.PesquisarBackEnd,
                  relief='flat', highlightbackground='#524F4F', fg='white').grid(row=14, column=1, padx=5, pady=5)

        Button(self.cadastrar, text='Gerar pdf', width=15, bg='gray', command=self.GerarPDF,
               relief='flat', highlightbackground='#524F4F', fg='white').grid(row=14, column=2, padx=5, pady=5)

        Button(self.cadastrar, text='Pesquisar por Nome', width=15, bg='gray', command=self.PesquisarBackEnd1,
               relief='flat', highlightbackground='#524F4F', fg='white').grid(row=15, column=1, padx=5, pady=5)

        Button(self.cadastrar, text='Pesquisar por Especies', width=15, bg='gray', command=self.PesquisarBackEnd2,
               relief='flat', highlightbackground='#524F4F', fg='white').grid(row=16, column=1, padx=5, pady=5)


        self.MostarProdutosBackEnd()


        self.cadastrar.mainloop()

    def Sobre(self):
        messagebox.showinfo('caio.h.sampaio@outlook.com', 'APP feito em Python e Tkinter por Caio Sampaio')

    def Update(self):

            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Caio@lemos12',
                    db='herbario',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                print('erro')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from cadastros')
                    resultado = cursor.fetchall()
            except:
                print('erro no banco de dados')

            self.tree.delete(*self.tree.get_children())

            i = 0
            linhaV = []
            for linha in resultado:
                linhaV.append(linha['id'])
                linhaV.append(linha['nome'])
                linhaV.append(linha['senha'])
                linhaV.append(linha['nivel'])

                self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')

                linhaV.clear()

                i += 1

    def VisualizarCadastros(self):
            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Caio@lemos12',
                    db='herbario',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                print('erro ao conectar no banco de dados')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from cadastros')
                    resultado = cursor.fetchall()
            except:
                print('erro no banco de dados')

            self.VC = Toplevel()
            self.VC.resizable(False, False)
            self.VC.protocol("WM_DELETE_WINDOW")
            self.VC.title("Visualizar Cadastros")

            self.tree = ttk.Treeview(self.VC, selectmode="browse", column=("column1", "column2", "column3", "column4"),
                                     show='headings')

            self.tree.column("column1", width=40, minwidth=500, stretch=NO)
            self.tree.heading('#1', text='ID')

            self.tree.column("column2", width=100, minwidth=500, stretch=NO)
            self.tree.heading('#2', text='Usuario')

            self.tree.column("column3", width=100, minwidth=180, stretch=NO)
            self.tree.heading('#3', text='Senha')

            self.tree.column("column4", width=40, minwidth=180, stretch=NO)
            self.tree.heading('#4', text='nivel')

            self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

            Button(self.VC, text='Atualizar', command=self.Update).grid(row=1, column=0, sticky=W + E, columnspan=2,
                                                                          padx=5, pady=5)

            Button(self.VC, text='Excluir', command=self.Remover).grid(row=1, column=2, sticky=W + E, columnspan=1,
                                                                          padx=5, pady=5)
            self.Update()

            self.VC.mainloop()

    def Remover(self):

            idDeletar = int(self.tree.selection()[0])

            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Caio@lemos12',
                    db='herbario',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

            except:
                print('erro ao conectar no banco de dados')

            with conexao.cursor() as cursor:
                cursor.execute('delete from cadastros where id = {};'.format(idDeletar))
                conexao.commit()

            self.Update()

    def __init__(self):
        self.admin = Tk()
        self.admin.resizable(True, True)
        self.admin.protocol("WM_DELETE_WINDOW")
        self.admin.title("Painel Admnistrativo")



        self.menubar = Menu(self.admin)
        self.menubar.add_separator()

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="Sobre",command=self.Sobre)
        self.menubar.add_cascade(label="Ajuda", menu=self.help_menu)
        self.menubar.add_separator()

        self.produtos_menu = Menu(self.menubar, tearoff=0)
        self.produtos_menu.add_command(label='Cadastrar Exsicatas', command=self.CadastrarExsicatas)
        self.menubar.add_cascade(label='Exsicatas', menu=self.produtos_menu)
        self.menubar.add_separator()

        self.pedidos_menu = Menu(self.menubar, tearoff=0)
        self.pedidos_menu.add_command(label='Visualizar cadastros', command=self.VisualizarCadastros)
        self.menubar.add_cascade(label='Cadastros', menu=self.pedidos_menu)
        self.menubar.add_separator()

        self.estatistica_menu = Menu(self.menubar, tearoff=0)
        self.estatistica_menu.add_command(label='***')
        self.menubar.add_cascade(label='***', menu=self.estatistica_menu)
        self.menubar.add_separator()


        self.admin.configure(menu=self.menubar)

        self.admin.geometry('1000x600')
        self.admin.mainloop()


class mainwindow():

    def VerificaLogin(self):
        autenticado = False
        usuarioMaster = False

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='herbario',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar no banco de dados')

        usuario = self.usuario.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')

        for linha in resultado:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            messagebox.showinfo('Login', 'Email ou senha invalido')



        if autenticado:
            self.root.destroy()
            if usuarioMaster:
                adminwindow()
            elif not usuarioMaster:
                userwindow()


        conexao.close()

    def CadastroBackEnd(self):

        codigoPadrao = '123@h'

        if self.codigoSeguranca.get() == codigoPadrao:
            if len(self.usuario.get()) <= 20:
                if len(self.senha.get()) <= 50:
                    nome = self.usuario.get()

                    senha = self.senha.get()
                    try:
                        conexao = pymysql.connect(
                            host='localhost',
                            user='root',
                            password='Caio@lemos12',
                            db='herbario',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )
                    except:
                        print('erro ao conectar no banco de dados')

                    try:
                        with conexao.cursor() as cursor:
                            cursor.execute('insert into cadastros (nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                            conexao.commit()

                        messagebox.showinfo('Cadastro', 'Usuario cadastrado com sucesso reinicie o programa para fazer login')
                        self.root.destroy()

                    except:
                        print('erro no banco de dados')



                else:
                    messagebox.showinfo('ERRO', 'POR FAVOR INSIRA UM NOME COM 50 OU MENOS CARACTERES')
            else:
                messagebox.showinfo('ERRO', 'POR FAVOR INSIRA UM NOME COM 20 OU MENOS CARACTERES')
        else:
            messagebox.showinfo('ERRO', 'CODIGO DE SEGURANÇA ERRADO REINICIE O PROGRAMA')
            self.root.destroy()

    def Cadastro(self):

        Label(self.root, text='Chave de segurança').grid(row=3, column=0, pady=5, padx=10)
        self.codigoSeguranca = Entry(self.root, show='*')
        self.codigoSeguranca.grid(row=3, column=1, pady=5, padx=10)
        Button(self.root, text='Confirmar cadastro', width=15, bg='blue1', command=self.CadastroBackEnd).grid(row=4, column=0, columnspan=3, pady=5, padx=10)

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW")
        self.root.title("Login")
        Label(self.root, text='Login').grid(row=0, column=0, columnspan=2, pady=5, padx=10)

        Label(self.root, text='Usuario').grid(row=1, column=0, pady=5, padx=10 )
        self.usuario = Entry(self.root)
        self.usuario.grid(row=1, column=1, pady=5, padx=10)

        Label(self.root, text='Senha').grid(row=2, column=0, pady=5, padx=10)
        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, pady=5, padx=10)


        Button(self.root, text='Logar', width=15, bg='green', command=self.VerificaLogin).grid(row=5, column=0, pady=5, padx=10)
        Button(self.root, text='Cadastrar', width=15, bg='orange', command=self.Cadastro).grid(row=5, column=1, pady=5, padx=1)





        self.root.mainloop()


try:
    contador = 0
    mainwindow()
except:
    print('erro')