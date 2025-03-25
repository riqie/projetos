# Criando a Interface/Front-End
from tkinter import *

# Variáveis de padding e largura da entrada
x_pad = 5
y_pad = 3
width_entry = 30

# Classe da Interface Gráfica
class Gui:
    def __init__(self):
        '''Classe da Interface Gráfica'''

        # Objeto da janela
        self.window = Tk()
        self.window.wm_title('PYSQL versão 1.0')

        # Definição das variáveis que recebem os dados inseridos pelo user
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Criando os objetos que farão parte das janelas
        self.lblnome = Label(self.window, text='Nome')
        self.lblsobrenome = Label(self.window, text='Sobrenome')
        self.lblemail = Label(self.window, text='Email')
        self.lblcpf = Label(self.window, text='Cpf')

        self.entNome = Entry(self.window, textvariable=self.txtNome, width=width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=width_entry)

        self.listClientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

        # Associando objetos ao grid da janela
        self.lblnome.grid(row=0, column=0)
        self.lblsobrenome.grid(row=1, column=0)
        self.lblemail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=3, rowspan=10)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        # União do scrollbar com a listbox
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Adicionar aparência à interface
        for child in self.window.winfo_children():
            widget_class = child.__class__.__name__

            if widget_class == 'Button':
                child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)

            elif widget_class == 'Listbox':
                child.grid_configure(padx=0, pady=0, sticky='NS')

            elif widget_class == 'Scrollbar':
                child.grid_configure(padx=0, pady=0, sticky='NS')

            else:
                child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        '''Executa a interface gráfica'''
        self.window.mainloop()

# Criação da interface gráfica removida
