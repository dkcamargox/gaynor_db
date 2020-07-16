from definicoes_janela import define_janela, define_maior_str, espacoNoFinal, salva, carrega, define_tam_janela, buscap_nome, buscap_sapato,busca_multiplos_nomes
from tkinter import Tk, Button, Label, Entry, PhotoImage, CENTER, W, Frame
from os import startfile, listdir, getenv
from os.path import isfile, isdir, join, abspath
import subprocess
from scrollable_frame import ScrollableFrame
import asyncio
# @ FEITO POR DOGÃO
# @ DATA 27.09.2019
# @ TODOS DIREITOS RESERVADOS


class Programa_Win(Tk):
    cliente = []
    lista_clientes = []
    W = []
    nome_exclui_g: str
    lista_label_clientes = []

    # Terminada Abaixo
    def janela_clear(self):
        for wid in self.W:
            if type(wid) is list:
                for x in range(0, len(wid)):
                    wid[x].place_forget()
            else:
                wid.place_forget()
        self.W = []
        define_tam_janela(self, "1400x800")

    # Terminada Abaixo
    def voltar_menu_principal_bt_clk(self):
        self.janela_clear()
        self.janela_principal()

    # Terminada Abaixo
    def Confirma_cadastra_bt_clk(self):
        self.lista_clientes.append(self.cliente)
        salva(self.lista_clientes)
        self.janela_clear()
        self.janela_principal()

    # Terminada Abaixo
    def Voltar_cadastra_bt_clk(self):
        self.janela_clear()

        nome = str(self.Nome_cadastro.get()).upper()
        sapato = str(self.Sapato_cadastro.get()).upper()
        LargPe = str(self.LarguraPeCadastroEntry.get()).upper()
        NomeResp: str = str(self.NomeResponsavelCadastroEntry.get()).upper()
        CpfResp: str = str(self.CpfResposavelCadastroEntry.get()).upper()
        CompriPe: str = str(self.ComprimentoPeCadastroEntry.get()).upper()
        CalcMed: str = str(self.CalcanharMedidaCadastroEntry.get()).upper()
        Ponteira: str = str(self.PonteiraCadastroEntry.get()).upper()
        Idade: str = str(self.IdadeCadastroEntry.get()).upper()
        TempBal: str = str(self.TempoBalletCadastroEntry.get()).upper()
        CargHor: str = str(self.CargaHorariaCadastroEntry.get()).upper()
        Escola: str = str(self.EscolaCadastroEntry.get()).upper()
        CodSapatilha: str = str(self.CodigoSapatilhaCadastroEntry.get()).upper()
        Rua: str = str(self.RuaCadastroEntry.get()).upper()
        Numero = str(self.NumeroCadastroEntry.get()).upper()
        Cidade: str = str(self.CidadeCadastroEntry.get()).upper()
        UF: str = str(self.UFCadastroEntry.get()).upper()
        

        self.cliente = [nome, sapato, LargPe, NomeResp, CpfResp, CompriPe, CalcMed, Ponteira, Idade,
                        TempBal, CargHor, Escola, CodSapatilha, Rua, Numero, Cidade, UF]
        self.janela_cadastrar()

        self.Nome_cadastro.insert(0, self.cliente[0])
        self.Sapato_cadastro.insert(0, self.cliente[1])
        self.LarguraPeCadastroEntry.insert(0, self.cliente[2])
        self.NomeResponsavelCadastroEntry.insert(0, self.cliente[3])
        self.CpfResposavelCadastroEntry.insert(0, self.cliente[4])
        self.ComprimentoPeCadastroEntry.insert(0, self.cliente[5])
        self.CalcanharMedidaCadastroEntry.insert(0, self.cliente[6])
        self.PonteiraCadastroEntry.insert(0, self.cliente[7])
        self.IdadeCadastroEntry.insert(0, self.cliente[8])
        self.TempoBalletCadastroEntry.insert(0, self.cliente[9])
        self.CargaHorariaCadastroEntry.insert(0, self.cliente[10])
        self.EscolaCadastroEntry.insert(0, self.cliente[11])
        self.CodigoSapatilhaCadastroEntry.insert(0, self.cliente[12])
        self.RuaCadastroEntry.insert(0, self.cliente[13])
        self.NumeroCadastroEntry.insert(0, self.cliente[14])
        self.CidadeCadastroEntry.insert(0, self.cliente[15])
        self.UFCadastroEntry.insert(0, self.cliente[16])

    # Terminada Abaixo
    def janela_confirma_cadastro(self):
        self.janela_clear()

        nome = espacoNoFinal(str(self.Nome_cadastro.get()).upper())
        sapato = espacoNoFinal(str(self.Sapato_cadastro.get()).upper())
        LargPe = espacoNoFinal(str(self.LarguraPeCadastroEntry.get()).upper())
        NomeResp: str = espacoNoFinal(str(self.NomeResponsavelCadastroEntry.get()).upper())
        CpfResp: str = espacoNoFinal(str(self.CpfResposavelCadastroEntry.get()).upper())
        CompriPe: str = espacoNoFinal(str(self.ComprimentoPeCadastroEntry.get()).upper())
        CalcMed: str = espacoNoFinal(str(self.CalcanharMedidaCadastroEntry.get()).upper())
        Ponteira: str = espacoNoFinal(str(self.PonteiraCadastroEntry.get()).upper())
        Idade: str = espacoNoFinal(str(self.IdadeCadastroEntry.get()).upper())
        TempBal: str = espacoNoFinal(str(self.TempoBalletCadastroEntry.get()).upper())
        CargHor: str = espacoNoFinal(str(self.CargaHorariaCadastroEntry.get()).upper())
        Escola: str = espacoNoFinal(str(self.EscolaCadastroEntry.get()).upper())
        CodSapatilha: str = espacoNoFinal(str(self.CodigoSapatilhaCadastroEntry.get()).upper())
        Rua: str = espacoNoFinal(str(self.RuaCadastroEntry.get()).upper())
        Numero = espacoNoFinal(str(self.NumeroCadastroEntry.get()).upper())
        Cidade: str = espacoNoFinal(str(self.CidadeCadastroEntry.get()).upper())
        UF: str = espacoNoFinal(str(self.UFCadastroEntry.get()).upper())
        Observacao: str = espacoNoFinal(str(self.ObservacaoCadastroEntry.get()).upper())

        self.cliente = [nome, sapato, LargPe, NomeResp, CpfResp, CompriPe, CalcMed, Ponteira, Idade,
                        TempBal, CargHor, Escola, CodSapatilha, Rua, Numero, Cidade, UF, Observacao]


        Tamanhos = []
        LabelName = ["Nome:                \t\t", "Tamanho do pé:       \t", "Largura do pé:       \t",
                     "Nome do responsável: \t", "CPF do responsável:  \t", "Comprimento do pé:   \t",
                     "Medida do calcanhar: \t", "Ponteira:            \t\t", "Idade:               \t\t",
                     "Tempo de ballet:     \t", "Carga horária:       \t\t", "Escola:              \t\t",
                     "Código da sapatilha: \t", "Rua:                 \t\t", "Telefone:              \t\t",
                     "Cidade:              \t\t", "UF:                  \t\t", "Observação:          \t\t"]

        for i in range(0, len(LabelName)):
            Tamanhos.append((10 + len(LabelName[i] + self.cliente[i])))

        Tamanhos.sort(reverse=True)

        # Labels

        self.titulo_confirma = Label(self, font=("Times New Roman", 24), text="Confirma?", bg="#fff",
                                     width=30, anchor=CENTER, bd=20)

        self.nome_confirma = Label(self, font=("Times New Roman", 14), text=LabelName[0] + nome, bg="#fff",
                                   width=Tamanhos[0], anchor=W, bd=4)

        self.sapato_confirma = Label(self, font=("Times New Roman", 14), text=LabelName[1] + sapato, bg="#fff",
                                     width=Tamanhos[0], anchor=W, bd=4)

        self.LarguraPeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[2] + LargPe, bg="#fff",
                                       width=Tamanhos[0], anchor=W, bd=4)

        self.NomeResponsavelConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[3] + NomeResp,
                                             bg="#fff", width=Tamanhos[0], anchor=W,
                                             bd=4)

        self.CpfResposavelConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[4] + CpfResp,
                                           bg="#fff", width=Tamanhos[0], anchor=W,
                                           bd=4)
        
        self.ComprimentoPeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[5] + CompriPe,
                                           bg="#fff", width=Tamanhos[0], anchor=W,
                                           bd=4)

        self.CalcanharMedidaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[6] + CalcMed,
                                             bg="#fff", width=Tamanhos[0],
                                             anchor=W, bd=4)

        self.PonteiraConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[7] + Ponteira, bg="#fff"
                                      , width=Tamanhos[0], anchor=W, bd=4)

        self.IdadeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[8] + Idade, bg="#fff",
                                   width=Tamanhos[0], anchor=W, bd=4)

        self.TempoBalletConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[9] + TempBal,
                                         bg="#fff", width=Tamanhos[0], anchor=W,
                                         bd=4)

        self.CargaHorariaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[10] + CargHor,
                                          bg="#fff", width=Tamanhos[0], anchor=W,
                                          bd=4)

        self.EscolaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[11] + Escola, bg="#fff",
                                    width=Tamanhos[0], anchor=W, bd=4)

        self.CodigoSapatilhaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[12] + CodSapatilha,
                                             bg="#fff", width=Tamanhos[0],
                                             anchor=W, bd=4)

        self.RuaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[13] + Rua, bg="#fff",
                                 width=Tamanhos[0], anchor=W, bd=4)

        self.NumeroConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[14] + Numero, bg="#fff",
                                    width=Tamanhos[0], anchor=W, bd=4)

        self.CidadeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[15] + Cidade, bg="#fff",
                                    width=Tamanhos[0], anchor=W, bd=4)

        self.UFConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[16] + UF, bg="#fff",
                                width=Tamanhos[0], anchor=W, bd=4)

        self.ObservacaoConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[17] + Observacao, bg="#fff",
                                width=Tamanhos[0], anchor=W, bd=4)

        # Buttons

        self.Cadastra = Button(self, font=("Times New Roman", 16), text="Confirma", bd=0, bg="white", fg=THECOLOR, width=10,
                               activebackground=THECOLOR, activeforeground="white", highlightcolor="white", cursor="hand2",
                               highlightbackground="white")

        self.Voltar_cadastra = Button(self, font=("Times New Roman", 16), text="Voltar", bd=0, width=10,
                                      bg="white", fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                      highlightcolor="white", highlightbackground="white", cursor="hand2")

        self.W = [self.titulo_confirma, self.Cadastra, self.nome_confirma, self.sapato_confirma, self.Voltar_cadastra,
                  self.LarguraPeConfirma, self.NomeResponsavelConfirma, self.CpfResposavelConfirma,
                  self.ComprimentoPeConfirma, self.CalcanharMedidaConfirma, self.PonteiraConfirma, self.IdadeConfirma,
                  self.TempoBalletConfirma, self.CargaHorariaConfirma, self.EscolaConfirma,
                  self.CodigoSapatilhaConfirma, self.RuaConfirma, self.NumeroConfirma, self.CidadeConfirma,
                  self.UFConfirma, self.ObservacaoConfirma]
        # comandos

        self.Cadastra["command"] = self.Confirma_cadastra_bt_clk
        self.Voltar_cadastra["command"] = self.Voltar_cadastra_bt_clk

        # binds

        self.Cadastra.bind('<Return>', lambda event: self.Confirma_cadastra_bt_clk())
        self.Voltar_cadastra.bind('<Return>', lambda event: self.Voltar_cadastra_bt_clk())

        # Layout

        TamX: int = 20

        TamY: int = 97
        # Labels

        self.titulo_confirma.place(x=430, y=15)
        
        
        self.nome_confirma.place(x=TamX, y=TamY)
        self.CodigoSapatilhaConfirma.place(x=TamX, y=TamY + (34 * 1))
        self.sapato_confirma.place(x=TamX, y=TamY + (34 * 2))
        self.LarguraPeConfirma.place(x=TamX, y=TamY + (34 * 3))
        self.ComprimentoPeConfirma.place(x=TamX, y=TamY + (34 * 4))
        self.CalcanharMedidaConfirma.place(x=TamX, y=TamY + (34 * 5))
        self.PonteiraConfirma.place(x=TamX, y=TamY + (34 * 6))
        self.IdadeConfirma.place(x=TamX, y=TamY + (34 * 7))
        self.TempoBalletConfirma.place(x=TamX, y=TamY + (34 * 8))
        self.CargaHorariaConfirma.place(x=TamX, y=TamY + (34 * 9))
        self.EscolaConfirma.place(x=TamX, y=TamY + (34 * 10))
        self.ObservacaoConfirma.place(x=TamX, y=TamY + (34 * 11))
        self.NomeResponsavelConfirma.place(x=TamX, y=TamY + (34 * 12))
        self.CpfResposavelConfirma.place(x=TamX, y=TamY + (34 * 13))
        self.NumeroConfirma.place(x=TamX, y=TamY + (34 * 14))
        self.RuaConfirma.place(x=TamX, y=TamY + (34 * 15))
        self.CidadeConfirma.place(x=TamX, y=TamY + (34 * 16))
        self.UFConfirma.place(x=TamX, y=TamY + (34 * 17))

        # Buttons

        self.Cadastra.place(x=1175, y=260)
        self.Voltar_cadastra.place(x=1175, y=310)

    # Terminada Abaixo
    def janela_cadastrar(self):
        self.janela_clear()
        # widgets

        # Criação Labels
        self.titulo_cadastro = Label(self, font=("Times New Roman", 24), text="Cadastro de Cliente", bg="#fff",
                                     width=30, anchor=CENTER, bd=20)

        self.nome_cadastro = Label(self, font=("Times New Roman", 14), text="Nome:", bg="#fff", width=40,
                                   anchor=CENTER, bd=5)

        self.sapato_cadastro = Label(self, font=("Times New Roman", 14), text="Tamanho do pé:", bg="#fff", width=40,
                                     anchor=CENTER, bd=5)

        self.LarguraPeCadastro = Label(self, font=("Times New Roman", 14), text="Lárgura do pé:", bg="#fff",
                                       width=40, anchor=CENTER, bd=5)

        self.NomeResponsavelCadastro = Label(self, font=("Times New Roman", 14), text="Nome do Responsável:",
                                             bg="#fff", width=40, anchor=CENTER, bd=5)

        self.CpfResposavelCadastro = Label(self, font=("Times New Roman", 14), text="CPF do responsável:", bg="#fff",
                                           width=40, anchor=CENTER, bd=5)

        self.ComprimentoPeCadastro = Label(self, font=("Times New Roman", 14), text="Comprimento do pé:", bg="#fff",
                                           width=40, anchor=CENTER, bd=5)

        self.CalcanharMedidaCadastro = Label(self, font=("Times New Roman", 14), text="Medida do calcanhar:",
                                             bg="#fff", width=40, anchor=CENTER, bd=5)

        self.PonteiraCadastro = Label(self, font=("Times New Roman", 14), text="Ponteira:", bg="#fff", width=40,
                                      anchor=CENTER, bd=5)

        self.IdadeCadastro = Label(self, font=("Times New Roman", 14), text="Idade:", bg="#fff", width=40,
                                   anchor=CENTER, bd=5)

        self.TempoBalletCadastro = Label(self, font=("Times New Roman", 14), text="Tempo de Ballet:", bg="#fff",
                                         width=40, anchor=CENTER, bd=5)

        self.CargaHorariaCadastro = Label(self, font=("Times New Roman", 14), text="Carga Horária:", bg="#fff",
                                          width=40, anchor=CENTER, bd=5)

        self.EscolaCadastro = Label(self, font=("Times New Roman", 14), text="Escola:", bg="#fff", width=40,
                                    anchor=CENTER, bd=5)

        self.CodigoSapatilhaCadastro = Label(self, font=("Times New Roman", 14), text="Código da sapatilha:",
                                             bg="#fff", width=40, anchor=CENTER, bd=5)

        self.RuaCadastro = Label(self, font=("Times New Roman", 14), text="Rua:", bg="#fff", width=40,
                                 anchor=CENTER, bd=5)

        self.NumeroCadastro = Label(self, font=("Times New Roman", 14), text="Telefone:", bg="#fff", width=40,
                                    anchor=CENTER, bd=5)

        self.CidadeCadastro = Label(self, font=("Times New Roman", 14), text="Cidade:", bg="#fff", width=40,
                                    anchor=CENTER, bd=5)

        self.UFCadastro = Label(self, font=("Times New Roman", 14), text="UF:", bg="#fff", width=40,
                                anchor=CENTER, bd=5)

        self.ObservacaoCadastro = Label(self, font=("Times New Roman", 14), text="Observação:", bg="#fff", width=40,
                                anchor=CENTER, bd=5)
        
        # Entrys

        self.Nome_cadastro = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CodigoSapatilhaCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.Sapato_cadastro = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.LarguraPeCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.ComprimentoPeCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CalcanharMedidaCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.PonteiraCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.IdadeCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.TempoBalletCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CargaHorariaCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.EscolaCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.ObservacaoCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.NomeResponsavelCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CpfResposavelCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.NumeroCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.RuaCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CidadeCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.UFCadastroEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        

        # Criação Buttons
        self.Cadastra = Button(self, font=("Times New Roman", 16), text="Confirma", width=10, bg="white",
                                      fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                      highlightcolor="white", highlightbackground="white", bd=0, cursor="hand2")

        

        self.voltar_menu_principal = Button(self, font=("Times New Roman", 16), text="Voltar", width=10, cursor="hand2",
                                    bg="white", fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                    highlightcolor="white", highlightbackground="white", bd=0)
        

        self.W = [self.titulo_cadastro, self.nome_cadastro, self.sapato_cadastro, self.LarguraPeCadastro,
                  self.NomeResponsavelCadastro, self.CpfResposavelCadastro, self.ComprimentoPeCadastro,
                  self.CalcanharMedidaCadastro, self.PonteiraCadastro, self.IdadeCadastro, self.TempoBalletCadastro,
                  self.CargaHorariaCadastro, self.EscolaCadastro, self.CodigoSapatilhaCadastro, self.RuaCadastro,
                  self.NumeroCadastro, self.CidadeCadastro, self.UFCadastro, self.ObservacaoCadastro, self.Nome_cadastro, self.Sapato_cadastro,
                  self.LarguraPeCadastroEntry, self.NomeResponsavelCadastroEntry, self.CpfResposavelCadastroEntry,
                  self.ComprimentoPeCadastroEntry, self.CalcanharMedidaCadastroEntry, self.PonteiraCadastroEntry,
                  self.IdadeCadastroEntry, self.TempoBalletCadastroEntry, self.CargaHorariaCadastroEntry,
                  self.EscolaCadastroEntry, self.CodigoSapatilhaCadastroEntry, self.RuaCadastroEntry,
                  self.NumeroCadastroEntry, self.CidadeCadastroEntry, self.UFCadastroEntry, self.ObservacaoCadastroEntry,
                  self.voltar_menu_principal, self.Cadastra]

        # comandos

        self.Cadastra["command"] = self.janela_confirma_cadastro
        self.Cadastra.bind('<Return>', lambda event: self.janela_confirma_cadastro())

        self.voltar_menu_principal["command"] = self.voltar_menu_principal_bt_clk
        self.voltar_menu_principal.bind('<Return>', lambda event: self.voltar_menu_principal_bt_clk())
        # Layout Labels
        LabelsX: int = 20
        LabelsY: int = 110

        Labels2X: int = 430
        Labels3X: int = 840

        # Layout Entry
        EntryX: int = LabelsX + 25
        EntryY: int = 143

        Entry2X: int = Labels2X + 25
        Entry3X: int = Labels3X + 25

        # Titulo
        self.titulo_cadastro.place(x=430, y=15)

        # Labels desenho

        self.nome_cadastro.place(x=LabelsX, y=LabelsY + (70 * 0))
        self.CodigoSapatilhaCadastro.place(x=LabelsX, y=LabelsY + (70 * 1))
        self.sapato_cadastro.place(x=LabelsX, y=LabelsY + (70 * 2))
        self.LarguraPeCadastro.place(x=LabelsX, y=LabelsY + (70 * 3))
        self.ComprimentoPeCadastro.place(x=LabelsX, y=LabelsY + (70 * 4))
        self.CalcanharMedidaCadastro.place(x=LabelsX, y=LabelsY + (70 * 5))
        self.PonteiraCadastro.place(x=LabelsX, y=LabelsY + (70 * 6))
        self.IdadeCadastro.place(x=LabelsX, y=LabelsY + (70 * 7))

        self.TempoBalletCadastro.place(x=Labels2X, y=LabelsY + (70 * 0))
        self.CargaHorariaCadastro.place(x=Labels2X, y=LabelsY + (70 * 1))
        self.EscolaCadastro.place(x=Labels2X, y=LabelsY + (70 * 2))
        self.ObservacaoCadastro.place(x=Labels2X, y=LabelsY + (70 * 3))
        self.NomeResponsavelCadastro.place(x=Labels2X, y=LabelsY + (70 * 4))
        self.CpfResposavelCadastro.place(x=Labels2X, y=LabelsY + (70 * 5))
        self.NumeroCadastro.place(x=Labels2X, y=LabelsY + (70 * 6))
        self.RuaCadastro.place(x=Labels2X, y=LabelsY + (70 * 7))

        self.CidadeCadastro.place(x=Labels3X, y=LabelsY + (70 * 0))
        self.UFCadastro.place(x=Labels3X, y=LabelsY + (70 * 1))


        # Entry desenho

        self.Nome_cadastro.place(x=EntryX, y=EntryY)
        self.CodigoSapatilhaCadastroEntry.place(x= EntryX, y=EntryY + (70 * 1))
        self.Sapato_cadastro.place(x=EntryX, y=EntryY + (70 * 2))
        self.LarguraPeCadastroEntry.place(x=EntryX, y=EntryY + (70 * 3))
        self.ComprimentoPeCadastroEntry.place(x=EntryX, y=EntryY + (70 * 4))
        self.CalcanharMedidaCadastroEntry.place(x=EntryX, y=EntryY + (70 * 5))
        self.PonteiraCadastroEntry.place(x=EntryX, y=EntryY + (70 * 6))
        self.IdadeCadastroEntry.place(x= EntryX, y=EntryY + (70 * 7))

        self.TempoBalletCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 0))
        self.CargaHorariaCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 1))
        self.EscolaCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 2))
        self.ObservacaoCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 3))
        self.NomeResponsavelCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 4))
        self.CpfResposavelCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 5))
        self.NumeroCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 6))
        self.RuaCadastroEntry.place(x=Entry2X, y=EntryY + (70 * 7))

        self.CidadeCadastroEntry.place(x= Entry3X, y=EntryY + (70 * 0))
        self.UFCadastroEntry.place(x=Entry3X, y=EntryY + (70 * 1))

        # Buttons desenho

        self.Cadastra.place(x=900, y=250)
        self.voltar_menu_principal.place(x=1090, y=250)

    # Terminada Abaixo
    def editar_confirma(self, cliente_para_editar):
        pos = buscap_nome(cliente_para_editar.upper(), self.lista_clientes)
        pos = int(pos)
        self.lista_clientes[pos][0] = espacoNoFinal(str(self.Nome_editar.get()).upper())
        self.lista_clientes[pos][1] = espacoNoFinal(str(self.Sapato_editar.get()).upper())
        self.lista_clientes[pos][2] = espacoNoFinal(str(self.LarguraPeEditarEntry.get()).upper())
        self.lista_clientes[pos][3] = espacoNoFinal(str(self.NomeResponsavelEditarEntry.get()).upper())
        self.lista_clientes[pos][4] = espacoNoFinal(str(self.CpfResposavelEditarEntry.get()).upper())
        self.lista_clientes[pos][5] = espacoNoFinal(str(self.ComprimentoPeEditarEntry.get()).upper())
        self.lista_clientes[pos][6] = espacoNoFinal(str(self.CalcanharMedidaEditarEntry.get()).upper())
        self.lista_clientes[pos][7] = espacoNoFinal(str(self.PonteiraEditarEntry.get()).upper())
        self.lista_clientes[pos][8] = espacoNoFinal(str(self.IdadeEditarEntry.get()).upper())
        self.lista_clientes[pos][9] = espacoNoFinal(str(self.TempoBalletEditarEntry.get()).upper())
        self.lista_clientes[pos][10] = espacoNoFinal(str(self.CargaHorariaEditarEntry.get()).upper())
        self.lista_clientes[pos][11] = espacoNoFinal(str(self.EscolaEditarEntry.get()).upper())
        self.lista_clientes[pos][12] = espacoNoFinal(str(self.CodigoSapatilhaEditarEntry.get()).upper())
        self.lista_clientes[pos][13] = espacoNoFinal(str(self.RuaEditarEntry.get()).upper())
        self.lista_clientes[pos][14] = espacoNoFinal(str(self.NumeroEditarEntry.get()).upper())
        self.lista_clientes[pos][15] = espacoNoFinal(str(self.CidadeEditarEntry.get()).upper())
        self.lista_clientes[pos][16] = espacoNoFinal(str(self.UFEditarEntry.get()).upper())
        self.lista_clientes[pos][17] = espacoNoFinal(str(self.ObservacaoEditarEntry.get()).upper())

        salva(self.lista_clientes)
        self.janela_clear()
        self.janela_principal()

    # Terminada Abaixo
    def janela_editar(self, cliente_para_editar, SapatoOuNome):
        
        self.janela_clear()

        define_tam_janela(self, "1400x800")
        pos = buscap_nome(cliente_para_editar.upper(), self.lista_clientes)
        pos = int(pos)

        # Widgets

        # Labels

        self.titulo_editar = Label(self, font=("Times New Roman", 24), text="Edição de Cliente", bg="#fff", width=30,
                                   anchor=CENTER, bd=20)

        self.nome_editar = Label(self, font=("Times New Roman", 14), text="Nome:", bg="#fff", width=40,
                                 anchor=CENTER, bd=5)

        self.sapato_editar = Label(self, font=("Times New Roman", 14), text="Tamanho do pé:", bg="#fff", width=40,
                                   anchor=CENTER, bd=5)

        self.LarguraPeEditar = Label(self, font=("Times New Roman", 14), text="Lárgura do pé:", bg="#fff", width=40,
                                     anchor=CENTER, bd=5)

        self.NomeResponsavelEditar = Label(self, font=("Times New Roman", 14), text="Nome do Responsável:",
                                           bg="#fff", width=40, anchor=CENTER, bd=5)

        self.CpfResposavelEditar = Label(self, font=("Times New Roman", 14), text="CPF do responsável:", bg="#fff",
                                         width=40, anchor=CENTER, bd=5)

        self.ComprimentoPeEditar = Label(self, font=("Times New Roman", 14), text="Comprimento do pé:", bg="#fff",
                                         width=40, anchor=CENTER, bd=5)

        self.CalcanharMedidaEditar = Label(self, font=("Times New Roman", 14), text="Medido do calcanhar:",
                                           bg="#fff", width=40, anchor=CENTER, bd=5)

        self.PonteiraEditar = Label(self, font=("Times New Roman", 14), text="Ponteira:", bg="#fff", width=40,
                                    anchor=CENTER, bd=5)

        self.IdadeEditar = Label(self, font=("Times New Roman", 14), text="Idade:", bg="#fff", width=40,
                                 anchor=CENTER, bd=5)

        self.TempoBalletEditar = Label(self, font=("Times New Roman", 14), text="Tempo de Ballet:", bg="#fff",
                                       width=40, anchor=CENTER, bd=5)

        self.CargaHorariaEditar = Label(self, font=("Times New Roman", 14), text="Carga Horária:", bg="#fff",
                                        width=40, anchor=CENTER, bd=5)

        self.EscolaEditar = Label(self, font=("Times New Roman", 14), text="Escola:", bg="#fff", width=40,
                                  anchor=CENTER, bd=5)

        self.CodigoSapatilhaEditar = Label(self, font=("Times New Roman", 14), text="Código da sapatilha:",
                                           bg="#fff", width=40, anchor=CENTER, bd=5)

        self.RuaEditar = Label(self, font=("Times New Roman", 14), text="Rua:", bg="#fff", width=40,
                               anchor=CENTER, bd=5)

        self.NumeroEditar = Label(self, font=("Times New Roman", 14), text="Telefone:", bg="#fff", width=40,
                                  anchor=CENTER, bd=5)

        self.CidadeEditar = Label(self, font=("Times New Roman", 14), text="Cidade:", bg="#fff", width=40,
                                  anchor=CENTER, bd=5)

        self.UFEditar = Label(self, font=("Times New Roman", 14), text="UF:", bg="#fff", width=40,
                              anchor=CENTER, bd=5)

        self.ObservacaoEditar = Label(self, font=("Times New Roman", 14), text="Observação:", bg="#fff", width=40,
                              anchor=CENTER, bd=5)
                              
        # Entrys

        self.Nome_editar = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )

        self.CodigoSapatilhaEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )

        self.Sapato_editar = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )

        self.LarguraPeEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )

        self.ComprimentoPeEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CalcanharMedidaEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.PonteiraEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.IdadeEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.TempoBalletEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CargaHorariaEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.EscolaEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.ObservacaoEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.NomeResponsavelEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CpfResposavelEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.NumeroEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.RuaEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.CidadeEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        self.UFEditarEntry = Entry(
            self, 
            width = 40, 
            justify = CENTER, 
            font = ("Times New Roman", 14), 
            bd = 0, 
            fg = ENTRY_FG_COLOR, 
            bg = ENTRY_BG_COLOR
        )
        
        # Buttons

        self.Confirma_editar = Button(self, font=("Times New Roman", 16), text="Confirma", width=10, bg="white",
                                      fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                      highlightcolor="white", highlightbackground="white", bd=0, cursor="hand2")

        self.Voltar_editar = Button(self, font=("Times New Roman", 16), text="Voltar", width=10, cursor="hand2",
                                    bg="white", fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                    highlightcolor="white", highlightbackground="white", bd=0)

        self.W = [self.titulo_editar, self.nome_editar, self.sapato_editar, self.LarguraPeEditar,
                  self.NomeResponsavelEditar, self.CpfResposavelEditar, self.ComprimentoPeEditar,
                  self.CalcanharMedidaEditar, self.PonteiraEditar, self.IdadeEditar, self.TempoBalletEditar,
                  self.CargaHorariaEditar, self.EscolaEditar, self.CodigoSapatilhaEditar, self.RuaEditar,
                  self.NumeroEditar, self.CidadeEditar, self.UFEditar, self.ObservacaoEditar, self.LarguraPeEditarEntry,
                  self.NomeResponsavelEditarEntry, self.CpfResposavelEditarEntry, self.ComprimentoPeEditarEntry,
                  self.CalcanharMedidaEditarEntry, self.PonteiraEditarEntry, self.IdadeEditarEntry,
                  self.TempoBalletEditarEntry, self.CargaHorariaEditarEntry, self.EscolaEditarEntry,
                  self.CodigoSapatilhaEditarEntry, self.RuaEditarEntry, self.NumeroEditarEntry, self.CidadeEditarEntry,
                  self.UFEditarEntry, self.ObservacaoEditarEntry, self.Nome_editar, self.Sapato_editar, self.Voltar_editar, self.Confirma_editar]

        # Comandos

        if SapatoOuNome == 'nome':
            self.Voltar_editar['command'] = lambda: self.janela_usuario_escolhido(pos, 0, SapatoOuNome)
            self.Voltar_editar.bind('<Return>', lambda event: self.janela_usuario_escolhido(pos, 0, SapatoOuNome))
            self.Confirma_editar["command"] = lambda: self.janela_usuario_escolhido(pos, 0, SapatoOuNome)
            self.Confirma_editar.bind('<Return>', lambda event: self.janela_usuario_escolhido(pos, 0, SapatoOuNome))
        
        else:
            self.Voltar_editar['command'] = lambda: self.janela_usuario_escolhido(pos, 0, SapatoOuNome)
            self.Voltar_editar.bind('<Return>', lambda event: self.janela_usuario_escolhido(pos, 0, SapatoOuNome))
            self.Confirma_editar["command"] = lambda: self.janela_usuario_escolhido(pos, 0, SapatoOuNome)
            self.Confirma_editar.bind('<Return>', lambda event: self.janela_usuario_escolhido(pos, 0, SapatoOuNome))
            
        

        # Inserts

        self.Nome_editar.insert(0, self.lista_clientes[pos][0])
        self.Sapato_editar.insert(0, self.lista_clientes[pos][1])
        self.LarguraPeEditarEntry.insert(0, self.lista_clientes[pos][2])
        self.NomeResponsavelEditarEntry.insert(0, self.lista_clientes[pos][3])
        self.CpfResposavelEditarEntry.insert(0, self.lista_clientes[pos][4])
        self.ComprimentoPeEditarEntry.insert(0, self.lista_clientes[pos][5])
        self.CalcanharMedidaEditarEntry.insert(0, self.lista_clientes[pos][6])
        self.PonteiraEditarEntry.insert(0, self.lista_clientes[pos][7])
        self.IdadeEditarEntry.insert(0, self.lista_clientes[pos][8])
        self.TempoBalletEditarEntry.insert(0, self.lista_clientes[pos][9])
        self.CargaHorariaEditarEntry.insert(0, self.lista_clientes[pos][10])
        self.EscolaEditarEntry.insert(0, self.lista_clientes[pos][11])
        self.CodigoSapatilhaEditarEntry.insert(0, self.lista_clientes[pos][12])
        self.RuaEditarEntry.insert(0, self.lista_clientes[pos][13])
        self.NumeroEditarEntry.insert(0, self.lista_clientes[pos][14])
        self.CidadeEditarEntry.insert(0, self.lista_clientes[pos][15])
        self.UFEditarEntry.insert(0, self.lista_clientes[pos][16])
        self.ObservacaoEditarEntry.insert(0, self.lista_clientes[pos][17])

        # Layout Labels
        LabelsY: int = 110

        LabelsX: int = 20
        Labels2X: int = 430
        Labels3X: int = 840

        # Layout Entry
        EntryY: int = 143

        EntryX: int = LabelsX + 25
        Entry2X: int = Labels2X + 25
        Entry3X: int = Labels3X + 25
        
        
        # Desenha Titulo

        self.titulo_editar.place(x=430, y=15)

        #  Desenha Labels

        self.nome_editar.place(x=LabelsX, y=LabelsY + ( 70 * 0))
        self.CodigoSapatilhaEditar.place(x=LabelsX, y=LabelsY + ( 70 * 1))
        self.sapato_editar.place(x=LabelsX, y=LabelsY + ( 70 * 2))
        self.LarguraPeEditar.place(x=LabelsX, y=LabelsY + ( 70 * 3))
        self.ComprimentoPeEditar.place(x=LabelsX, y=LabelsY + ( 70 * 4))
        self.CalcanharMedidaEditar.place(x=LabelsX, y=LabelsY + ( 70 * 5))
        self.PonteiraEditar.place(x=LabelsX, y=LabelsY + ( 70 * 6))
        self.IdadeEditar.place(x=LabelsX, y=LabelsY + ( 70 * 7))
        
        self.TempoBalletEditar.place(x=Labels2X, y=LabelsY + ( 70 * 0))
        self.CargaHorariaEditar.place(x=Labels2X, y=LabelsY + ( 70 * 1))
        self.EscolaEditar.place(x=Labels2X, y=LabelsY + ( 70 * 2))
        self.ObservacaoEditar.place(x=Labels2X, y=LabelsY + ( 70 * 3))
        self.NomeResponsavelEditar.place(x=Labels2X, y=LabelsY + ( 70 * 4))
        self.CpfResposavelEditar.place(x=Labels2X, y=LabelsY + ( 70 * 5))
        self.NumeroEditar.place(x=Labels2X, y=LabelsY + ( 70 * 6))
        self.RuaEditar.place(x=Labels2X, y=LabelsY + ( 70 * 7))

        self.CidadeEditar.place(x=Labels3X,  y=LabelsY + ( 70 * 0))
        self.UFEditar.place(x=Labels3X,  y=LabelsY + ( 70 * 1))

        # Desenha Entrys

        self.Nome_editar.place(x=EntryX, y=EntryY + ( 70 * 0))
        self.CodigoSapatilhaEditarEntry.place(x=EntryX, y=EntryY + ( 70 * 1))
        self.Sapato_editar.place(x=EntryX, y=EntryY + ( 70 * 2))
        self.LarguraPeEditarEntry.place(x=EntryX, y=EntryY + ( 70 * 3))
        self.ComprimentoPeEditarEntry.place(x=EntryX, y=EntryY + ( 70 * 4))
        self.CalcanharMedidaEditarEntry.place(x=EntryX, y=EntryY + ( 70 * 5))
        self.PonteiraEditarEntry.place(x=EntryX, y=EntryY + ( 70 * 6))
        self.IdadeEditarEntry.place(x=EntryX, y=EntryY + (70 * 7))
        
        self.TempoBalletEditarEntry.place(x=Entry2X, y=EntryY + ( 70 * 0))
        self.CargaHorariaEditarEntry.place(x=Entry2X, y=EntryY + ( 70 * 1))
        self.EscolaEditarEntry.place(x=Entry2X, y=EntryY + ( 70 * 2))
        self.ObservacaoEditarEntry.place(x=Entry2X, y=EntryY + ( 70 * 3))
        self.NomeResponsavelEditarEntry.place(x=Entry2X, y=EntryY + ( 70 * 4))
        self.CpfResposavelEditarEntry.place(x=Entry2X, y=EntryY + ( 70 * 5))
        self.NumeroEditarEntry.place(x=Entry2X, y=EntryY + (70 * 6))
        self.RuaEditarEntry.place(x=Entry2X, y=EntryY + ( 70 * 7))
        
        self.CidadeEditarEntry.place(x=Entry3X, y=EntryY + (70 * 0))
        self.UFEditarEntry.place(x=Entry3X, y=EntryY + (70 * 1))

        # Desenha Buttons

        self.Confirma_editar.place(x=900, y=250)
        self.Voltar_editar.place(x=1090, y=250)

    # Terminada Abaixo
    def janela_listagem_mesmo_tamanho_pe(self, Initial):

        self.janela_clear()

        # layout align

        self.Aling: int = 30


        self.lista_multiplo_pe = []
        self.sapato_busca_g = str(self.Sapato_janela_buscar_entry.get()).upper()
        self.lista_multiplo_pe = buscap_sapato(self.sapato_busca_g, self.lista_clientes)
        Initial

        # se a lista de clientes com o mesmo pé estiver vazia
        if self.lista_multiplo_pe == []:

            self.janela_clear()

            self.titulo_buscar_E = Label(
                self, 
                font=("Times New Roman", 24),
                text="Nenhuma cliente com \n   esse tamanho de pé", 
                bg="#fff", 
                width=30,
                anchor=CENTER, 
                bd=20
            )

            self.Voltar_buuscar_E = Button(
                self, 
                font=("Times New Roman", 20), 
                text="Voltar", 
                cursor="exchange",
                command=self.janela_buscar, 
                highlightbackground=THECOLOR,
                highlightcolor=THECOLOR, 
                fg=THECOLOR, 
                bg="white", 
                activebackground=THECOLOR,
                activeforeground="white", 
                bd=0
            )

            self.Voltar_buuscar_E.bind('<Return>', lambda event: self.janela_buscar())
            
            self.W = [self.titulo_buscar_E, self.Voltar_buuscar_E]

            self.titulo_buscar_E.place(x=430, y=15)
            self.Voltar_buuscar_E.place(x=660, y=240)
        
        else:

            self.janela_clear()

            lista_tam_nomes = []
            for x in range(0, len(self.lista_multiplo_pe)):
                lista_tam_nomes.append(len(self.lista_clientes[x][0]))
            m_tam = define_maior_str(lista_tam_nomes)

            # width general
            geral_width_label = 80

            # definindo widgets

            # label titulo

            self.titulo_buscar = Label(
                self, 
                font=("Times New Roman", 20),
                text="  " + "Nome:" + (m_tam) * "  " + "Sapato:",
                width=geral_width_label + 6, 
                bg="#fff", 
                anchor=W
            )

            # scrollable frame

            self.ScrollableFrameSapatos = ScrollableFrame(
                self,
                self, 
                width=1316, 
                height=512,
                bg=BGCOLOR,
                highlightbackground='#facacd'
            )

            
            # adiciona clientes no frame arrastavel
            def adicionaBlocosClientesNoScrollableFrame(frame: ScrollableFrame, listaClientes: list):
                
                # se ja tiver carregado um numero igual ao tamanho da lista retorna
                if frame.numberOfChilds == len(listaClientes):
                    return
                
                # corta a lista entre o numero de clientes que ja foram adicionadas e umintervalo de 10 clientes
                listaClientesAdicionaraNoFrame = listaClientes[frame.numberOfChilds:frame.numberOfChilds + 10]
                
                for cliente in listaClientesAdicionaraNoFrame:
                    
                    # bloco para cada cliente
                    FrameCLienteSapatos = Frame(
                        self.ScrollableFrameSapatos.scrollable_frame,
                        bg=BGCOLOR
                    )
                    FrameCLienteSapatos.columnconfigure(0, weight=1)
                    FrameCLienteSapatos.columnconfigure(1, weight=2)

                    # label da cliente
                    LabelClientesSapatos = Label(
                        FrameCLienteSapatos,
                        font=("Times New Roman", 20),
                        text=f"  {self.lista_clientes[cliente][0]}" + (m_tam - len(self.lista_clientes[cliente][0])) * "  "+f"\t{self.lista_clientes[cliente][1]}",
                        width=geral_width_label,
                        bg="#fff",
                        anchor=W
                    )
                    
                    # botao da cliente
                    BotaoClienteSapatos = Button(
                        FrameCLienteSapatos,
                        font=("Times New Roman", 14),
                        text="Ver Mais", bg="#ffebff",
                        highlightcolor="white", 
                        cursor='hand2',
                        highlightbackground="white", 
                        fg=THECOLOR, 
                        height=1,
                        activebackground=THECOLOR, 
                        activeforeground="white", 
                        bd=0
                    )

                    # comando e binds
                    BotaoClienteSapatos["command"] = lambda Salvo=cliente: self.janela_usuario_escolhido(Salvo, Initial, 'sapato')
                    BotaoClienteSapatos.bind('<Return>', lambda event, Salvo=cliente: self.janela_usuario_escolhido(Salvo, Initial, 'sapato'))

                    # desenho dentro do frame
                    LabelClientesSapatos.grid(column=0, row=0, pady=10,sticky="wens")
                    BotaoClienteSapatos.grid(column=1, row=0, pady=10, sticky="wens")

                    # desenho do bloco de cliente  dentroframe arrastavel
                    FrameCLienteSapatos.grid(padx=5)
                
                # atualiza o numero de clientes carregadas
                frame.numberOfChilds = frame.numberOfChilds + len(listaClientesAdicionaraNoFrame)
            
            # se é a primeria vez que carrega o frame arrastavel
            if self.ScrollableFrameSapatos.scrollbar.get()[1] == 0.0:
                adicionaBlocosClientesNoScrollableFrame(self.ScrollableFrameSapatos, self.lista_multiplo_pe)
            
            # setando a função para evento onEnd do Frame Arrastavel
            self.ScrollableFrameSapatos.setOnEnd(lambda : adicionaBlocosClientesNoScrollableFrame(self.ScrollableFrameSapatos, self.lista_multiplo_pe))



            # definindo botão de voltar
            self.Voltar_buuscar = Button(
                self,
                font=("Times New Roman", 18), 
                text="Voltar",
                cursor="hand2", 
                highlightbackground="white", 
                highlightcolor="white",
                bd=0, 
                bg="white", 
                fg=THECOLOR, 
                activebackground=THECOLOR,
                activeforeground="white"
            )

            #comandos de botões voltar
            self.Voltar_buuscar["command"] = lambda: self.janela_buscar()

            # bind botão voltar
            self.Voltar_buuscar.bind('<Return>', lambda event: self.janela_buscar())

            # self.W
            self.W = [ self.titulo_buscar, self.ScrollableFrameSapatos, self.Voltar_buuscar ]

            # placing widgets
            self.ScrollableFrameSapatos.place(x = 30, y = 60 )
            self.titulo_buscar.place(x=self.Aling + 5, y=15)
            self.Voltar_buuscar.place(x=100, y=600)

    # Terminada Abaixo
    def janela_listagem_mesmo_nome(self, Initial):

        self.janela_clear()
            
        # layout align 

        self.Aling: int = 30
        
        
        self.lista_multiplo_nome = []
        self.nome_buscar_g = str(self.Nome_janela_buscar_entry.get()).upper()
        self.lista_multiplo_nome = busca_multiplos_nomes(self.nome_buscar_g, self.lista_clientes)
        Initial

        # se não tem nenhuma cliente com esse nome ou com essas iniciais
        if self.lista_multiplo_nome == []:
            
            self.janela_clear()
            
            self.titulo_buscar_E = Label(
                self, 
                font=("Times New Roman", 24), 
                text="Cliente não Cadastrada",
                bg="#fff",
                width=30, 
                anchor=CENTER, 
                bd=20
            )

            self.Voltar_buuscar_E = Button(
                self, 
                font=("Times New Roman", 20), 
                text="Voltar", 
                cursor="hand2",
                command=self.janela_buscar, 
                highlightbackground=THECOLOR,
                highlightcolor=THECOLOR, 
                fg=THECOLOR, bg="white", 
                activebackground=THECOLOR,
                activeforeground="white", 
                bd=0
            )

            # bind
            self.Voltar_buuscar_E.bind('<Return>', lambda event: self.janela_buscar())
            
            self.W = [self.titulo_buscar_E, self.Voltar_buuscar_E]

            self.titulo_buscar_E.place(x=430, y=15)
            self.Voltar_buuscar_E.place(x=660, y=240)

        # caso contrario
        else:
            # layout
            lista_tam_nomes = []
            for x in range(0, len(self.lista_multiplo_nome)):
                lista_tam_nomes.append(len(self.lista_clientes[x][0]))
            m_tam = define_maior_str(lista_tam_nomes)
            
            # width general
            geral_width_label = 80

            
            # definindo os widgets

            # label titulo

            self.titulo_buscar = Label(
                self,
                font=("Times New Roman", 20),
                text="  " + "Nome:" + (m_tam) * "  " + "Sapato:",
                width=geral_width_label + 6,
                bg="#fff",
                anchor=W
            )

        
            # scrollable frame

            self.ScrollableFrameNomes = ScrollableFrame(
                self,
                self, 
                width=1316, 
                height=512,
                bg=BGCOLOR,
                highlightbackground='#facacd'
            )

            # adiciona clientes no frame arrastavel
            def adicionaBlocosClientesNoScrollableFrame(frame: ScrollableFrame, listaClientes: list):
                
                # se ja tiver carregado um numero igual ao tamanho da lista retorna
                if frame.numberOfChilds == len(listaClientes):
                    return
                
                # corta a lista entre o numero de clientes que ja foram adicionadas e umintervalo de 10 clientes
                listaClientesAdicionaraNoFrame = listaClientes[frame.numberOfChilds:frame.numberOfChilds + 10]
                
                for cliente in listaClientesAdicionaraNoFrame:
                    
                    # bloco para cada cliente
                    FrameCLienteNomes = Frame(
                        self.ScrollableFrameNomes.scrollable_frame,
                        bg=BGCOLOR
                    )
                    FrameCLienteNomes.columnconfigure(0, weight=1)
                    FrameCLienteNomes.columnconfigure(1, weight=2)

                    # label da cliente
                    LabelClienteNomes = Label(
                        FrameCLienteNomes,
                        font=("Times New Roman", 20),
                        text=f"  {self.lista_clientes[cliente][0]}" + (m_tam - len(self.lista_clientes[cliente][0])) * "  "+f"\t{self.lista_clientes[cliente][1]}",
                        width=geral_width_label,
                        bg="#fff",
                        anchor=W
                    )
                    
                    # botao da cliente
                    BotaoClienteNomes = Button(
                        FrameCLienteNomes,
                        font=("Times New Roman", 14),
                        text="Ver Mais", bg="#ffebff",
                        highlightcolor="white", 
                        cursor='hand2',
                        highlightbackground="white", 
                        fg=THECOLOR, 
                        height=1,
                        activebackground=THECOLOR, 
                        activeforeground="white", 
                        bd=0
                    )

                    # comando e binds
                    BotaoClienteNomes["command"] = lambda Salvo=cliente: self.janela_usuario_escolhido(Salvo, Initial, 'nome')
                    BotaoClienteNomes.bind('<Return>', lambda event, Salvo=cliente: self.janela_usuario_escolhido(Salvo, Initial, 'nome'))

                    # desenho dentro do frame
                    LabelClienteNomes.grid(column=0, row=0, pady=10,sticky="wens")
                    BotaoClienteNomes.grid(column=1, row=0, pady=10, sticky="wens")

                    # desenho do bloco de cliente  dentroframe arrastavel
                    FrameCLienteNomes.grid(padx=5)
                
                # atualiza o numero de clientes carregadas
                frame.numberOfChilds = frame.numberOfChilds + len(listaClientesAdicionaraNoFrame)
            
            # se é a primeria vez que carrega o frame arrastavel
            if self.ScrollableFrameNomes.scrollbar.get()[1] == 0.0:
                adicionaBlocosClientesNoScrollableFrame(self.ScrollableFrameNomes, self.lista_multiplo_nome)
            
            # setando a função para evento onEnd do Frame Arrastavel
            self.ScrollableFrameNomes.setOnEnd(lambda : adicionaBlocosClientesNoScrollableFrame(self.ScrollableFrameNomes, self.lista_multiplo_nome))


            # definindo botão de voltar

            self.Voltar_buuscar = Button(
                self,
                font=("Times New Roman", 18), 
                text="Voltar",
                cursor="hand2", 
                highlightbackground="white", 
                highlightcolor="white",
                bd=0, 
                bg="white", 
                fg=THECOLOR, 
                activebackground=THECOLOR,
                activeforeground="white"
            )
            
            #comandos de botões voltar
            self.Voltar_buuscar["command"] = lambda: self.janela_buscar()

            # bind botão voltar
            self.Voltar_buuscar.bind('<Return>', lambda event: self.janela_buscar())

            # self.W
            self.W = [ self.titulo_buscar, self.ScrollableFrameNomes, self.Voltar_buuscar ]

            # placing widgets
            self.ScrollableFrameNomes.place(x = 30, y = 60 )
            self.titulo_buscar.place(x=self.Aling + 5, y=15)
            self.Voltar_buuscar.place(x=100, y=600)

    # Terminada Abaixo
    def janela_buscar(self):
        self.janela_clear()
        self.ContadorSapato = 0
        define_tam_janela(self, "1400x800")

        # layout

        ButtonAling: int = 880
        AllAling: int = 410
        LabelAling: int = 450
        EntryAling: int = 465
        # widgets
        self.titulo_buscar = Label(self, font=("Times New Roman", 24), text="Busca de Cliente", bg="#fff",
                                   width=35, anchor=CENTER, bd=20)

        self.nome_buscar = Label(self, font=("Times New Roman", 18), text="Nome:", bg="#fff",
                                 width=30, anchor=CENTER, bd=5)

        self.sapato_buscar = Label(self, font=("Times New Roman", 18), text="Sapato:", bg="#fff",
                                   width=30, anchor=CENTER, bd=5)


        self.Nome_janela_buscar_entry = Entry(self, width=34, justify=CENTER, font=("Times New Roman", 16), fg=THECOLOR,
                                 highlightbackground=THECOLOR, bd=0, highlightcolor=THECOLOR, bg="#f0f0f8")

        self.Sapato_janela_buscar_entry = Entry(self, width=34, justify=CENTER, font=("Times New Roman", 16), fg=THECOLOR,
                                   highlightbackground=THECOLOR, bd=0, highlightcolor=THECOLOR, bg="#f0f0f8")

        self.Busca_p_nome = Button(self, font=("Times New Roman", 14), text="Busca por Nome", width=13,
                                        highlightcolor="white", highlightbackground="white", bg="white",
                                        fg=THECOLOR, activebackground=THECOLOR, activeforeground="white", bd=0,
                                        cursor="hand2")

        self.Busca_p_sapato = Button(self, font=("Times New Roman", 14), text="Busca por Sapato", width=13,
                                        highlightcolor="white", highlightbackground="white", bg="white",
                                        fg=THECOLOR, activebackground=THECOLOR, activeforeground="white", bd=0,
                                        cursor="hand2")

        self.voltar_menu_principal = Button(self, font=("Times New Roman", 14), text="Voltar", width=13,
                                            highlightcolor="white", highlightbackground="white", bg="white",
                                            fg=THECOLOR, activebackground=THECOLOR, activeforeground="white", bd=0,
                                            cursor="hand2")


        self.W = [self.voltar_menu_principal, self.titulo_buscar, self.nome_buscar, self.sapato_buscar,
                  self.Nome_janela_buscar_entry,
                  self.Sapato_janela_buscar_entry, self.Busca_p_nome, self.Busca_p_sapato]

        # comandos

        self.voltar_menu_principal["command"] = self.voltar_menu_principal_bt_clk
        self.Busca_p_sapato["command"] = lambda: self.janela_listagem_mesmo_tamanho_pe(0)
        self.Busca_p_nome["command"] = lambda: self.janela_listagem_mesmo_nome(0)


        # binds
        self.voltar_menu_principal.bind('<Return>', lambda event: self.voltar_menu_principal_bt_clk())
        self.Busca_p_sapato.bind('<Return>', lambda event: self.janela_listagem_mesmo_tamanho_pe(0))
        self.Busca_p_nome.bind('<Return>', lambda event: self.janela_listagem_mesmo_nome(0))
        

        # desenhos

        self.titulo_buscar.place(x=AllAling, y=15)
        self.nome_buscar.place(x=LabelAling, y=125)
        self.sapato_buscar.place(x=LabelAling, y=250)
        self.Nome_janela_buscar_entry.place(x=EntryAling, y=164)
        self.Sapato_janela_buscar_entry.place(x=EntryAling, y=289)
        self.Busca_p_nome.place(x=ButtonAling, y=162)
        self.Busca_p_sapato.place(x=ButtonAling, y=287)
        self.voltar_menu_principal.place(x=ButtonAling, y=350)

    # Terminada Abaixo
    def Exclui_bt_clk(self):
        pos = int(buscap_nome(self.nome_exclui_g, self.lista_clientes))
        self.lista_clientes.pop(pos)
        salva(self.lista_clientes)
        self.janela_clear()
        self.janela_principal()

    # Terminada Abaixo
    def Voltar_exclui_bt_clk(self):
        self.janela_clear()
        self.janela_excluir()
        self.Nome_janela_excluir_entry.insert(0, self.nome_exclui_g)

    # Terminada Abaixo
    def exclui_bt_clk(self):

        self.nome_exclui_g = str(self.Nome_janela_excluir_entry.get()).upper()
        pos = buscap_nome(self.nome_exclui_g, self.lista_clientes)

        if None != pos:

            pos = int(pos)

            self.janela_clear()

            self.titulo_confirma = Label(self, font=("Times New Roman", 24), text="Confirma?", bg="#fff", width=30,
                                         anchor=CENTER, bd=20)

            Tamanhos = []
            LabelName = ["Nome:                \t\t", "Tamanho do pé:       \t", "Largura do pé:       \t",
                         "Nome do responsável: \t", "CPF do responsável:  \t", "Comprimento do pé:   \t",
                         "Medida do calcanhar: \t", "Ponteira:            \t\t", "Idade:               \t\t",
                         "Tempo de ballet:     \t", "Carga horária:       \t\t", "Escola:              \t\t",
                         "Código da sapatilha: \t", "Rua:                 \t\t", "Telefone:              \t\t",
                         "Cidade:              \t\t", "UF:                  \t\t", "Observação:          \t\t"]

            for c in range(0, len(LabelName)):
                Tamanhos.append(10 + len(LabelName[c] + self.lista_clientes[pos][c]))

            Tamanhos.sort(reverse=True)

            # Labels

            self.nome_confirma = Label(self, font=("Times New Roman", 14), text=LabelName[0] + self.lista_clientes[pos][0],
                                       bg="#fff", width=Tamanhos[0], anchor=W, bd=4)

            self.sapato_confirma = Label(self, font=("Times New Roman", 14),
                                         text=LabelName[1] + self.lista_clientes[pos][1], bg="#fff",
                                         width=Tamanhos[0], anchor=W, bd=4)

            self.LarguraPeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                 text=LabelName[2] + self.lista_clientes[pos][2], bg="#fff",
                                                 width=Tamanhos[0], anchor=W, bd=4)

            self.NomeResponsavelExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                       text=LabelName[3] + self.lista_clientes[pos][3],
                                                       bg="#fff", width=Tamanhos[0], anchor=W, bd=4)

            self.CpfResponsavelExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                      text=LabelName[4] + self.lista_clientes[pos][4],
                                                      bg="#fff", width=Tamanhos[0], anchor=W, bd=4)

            self.ComprimentoPeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                     text=LabelName[5] + self.lista_clientes[pos][5],
                                                     bg="#fff", width=Tamanhos[0], anchor=W, bd=4)

            self.CalcanharMedidaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                       text=LabelName[6] + self.lista_clientes[pos][6],
                                                       bg="#fff", width=Tamanhos[0], anchor=W, bd=4)

            self.PonteiraExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                text=LabelName[7] + self.lista_clientes[pos][7], bg="#fff",
                                                width=Tamanhos[0], anchor=W, bd=4)

            self.IdadeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                             text=LabelName[8] + self.lista_clientes[pos][8], bg="#fff",
                                             width=Tamanhos[0], anchor=W, bd=4)

            self.TempoBalletExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                   text=LabelName[9] + self.lista_clientes[pos][9],
                                                   bg="#fff",
                                                   width=Tamanhos[0], anchor=W, bd=4)

            self.CargaHorariaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                    text=LabelName[10] + self.lista_clientes[pos][10],
                                                    bg="#fff",
                                                    width=Tamanhos[0], anchor=W, bd=4)

            self.EscolaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                              text=LabelName[11] + self.lista_clientes[pos][11], bg="#fff",
                                              width=Tamanhos[0], anchor=W, bd=4)

            self.CodigoSapatilhaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                       text=LabelName[12] + self.lista_clientes[pos][12],
                                                       bg="#fff", width=Tamanhos[0], anchor=W, bd=4)

            self.RuaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                           text=LabelName[13] + self.lista_clientes[pos][13], bg="#fff",
                                           width=Tamanhos[0], anchor=W, bd=4)

            self.NumeroExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                              text=LabelName[14] + self.lista_clientes[pos][14], bg="#fff",
                                              width=Tamanhos[0], anchor=W, bd=4)

            self.CidadeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                              text=LabelName[15] + self.lista_clientes[pos][15], bg="#fff",
                                              width=Tamanhos[0], anchor=W, bd=4)

            self.UFExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                          text=LabelName[16] + self.lista_clientes[pos][16], bg="#fff",
                                          width=Tamanhos[0], anchor=W, bd=4)

            self.ObservacaoExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                          text=LabelName[17] + self.lista_clientes[pos][17], bg="#fff",
                                          width=Tamanhos[0], anchor=W, bd=4)

            # Buttons

            self.Exclui_bt = Button(self, font=("Times New Roman", 19), text="Confirma", bg="white", fg=THECOLOR, bd=0,
                                    activebackground=THECOLOR, activeforeground="white", highlightbackground="white",
                                    highlightcolor="white", cursor="hand2", width=10)

            self.Voltar_exclui_cadastra = Button(self, font=("Times New Roman", 19), text="Voltar", cursor="exchange",
                                                 bg="white", fg=THECOLOR, bd=0, activebackground=THECOLOR,
                                                 activeforeground="white", highlightbackground="white", width=10,
                                                 highlightcolor="white")

            self.W = [self.titulo_confirma, self.nome_confirma, self.sapato_confirma, self.LarguraPeExcluiConfirma,
                      self.NomeResponsavelExcluiConfirma, self.CpfResponsavelExcluiConfirma,
                      self.ComprimentoPeExcluiConfirma, self.CalcanharMedidaExcluiConfirma, self.PonteiraExcluiConfirma,
                      self.IdadeExcluiConfirma, self.TempoBalletExcluiConfirma, self.CargaHorariaExcluiConfirma,
                      self.EscolaExcluiConfirma, self.CodigoSapatilhaExcluiConfirma, self.RuaExcluiConfirma,
                      self.NumeroExcluiConfirma, self.CidadeExcluiConfirma, self.UFExcluiConfirma, self.ObservacaoExcluiConfirma,
                      self.Voltar_exclui_cadastra, self.Exclui_bt]
            # comandos

            self.Voltar_exclui_cadastra["command"] = self.Voltar_exclui_bt_clk
            self.Exclui_bt["command"] = self.Exclui_bt_clk

            # binds

            self.Voltar_exclui_cadastra.bind('<Return>', lambda event: self.Voltar_exclui_bt_clk())
            self.Exclui_bt.bind('<Return>', lambda event: self.Exclui_bt_clk())
            
            # Layout

            TamX: int = 20
            TamY: int = 97

            # Labels

            self.titulo_confirma.place(x=430, y=15)
            
            self.nome_confirma.place(x=TamX, y=TamY)
            self.CodigoSapatilhaExcluiConfirma.place(x=TamX, y=TamY + (34 * 1))
            self.sapato_confirma.place(x=TamX, y=TamY + (34 * 2))
            self.LarguraPeExcluiConfirma.place(x=TamX, y=TamY + (34 * 3))
            self.ComprimentoPeExcluiConfirma.place(x=TamX, y=TamY + (34 * 4))
            self.CalcanharMedidaExcluiConfirma.place(x=TamX, y=TamY + (34 * 5))
            self.PonteiraExcluiConfirma.place(x=TamX, y=TamY + (34 * 6))
            self.IdadeExcluiConfirma.place(x=TamX, y=TamY + (34 * 7))
            self.TempoBalletExcluiConfirma.place(x=TamX, y=TamY + (34 * 8))
            self.CargaHorariaExcluiConfirma.place(x=TamX, y=TamY + (34 * 9))
            self.EscolaExcluiConfirma.place(x=TamX, y=TamY + (34 * 10))
            self.ObservacaoExcluiConfirma.place(x=TamX, y=TamY + (34 * 11))
            self.NomeResponsavelExcluiConfirma.place(x=TamX, y=TamY + (34 * 12))
            self.CpfResponsavelExcluiConfirma.place(x=TamX, y=TamY + (34 * 13))
            self.NumeroExcluiConfirma.place(x=TamX, y=TamY + (34 * 14))
            self.RuaExcluiConfirma.place(x=TamX, y=TamY + (34 * 15))
            self.CidadeExcluiConfirma.place(x=TamX, y=TamY + (34 * 16))
            self.UFExcluiConfirma.place(x=TamX, y=TamY + (34 * 17))

            # Buttons

            self.Exclui_bt.place(x=1018, y=300)
            self.Voltar_exclui_cadastra.place(x=1018, y=350)

        else:  # Caso não encontre a cliente
            self.janela_clear()
            self.titulo_confirma_exclui_E = Label(self, font=("Times New Roman", 24), text="Cliente não cadastrada",
                                                  bg="#fff",
                                                  width=30, anchor=CENTER, bd=20)
            self.Voltar_exclui_confirma_exclui_E = Button(self, font=("Times New Roman", 20), text="Voltar",
                                                        command=self.Voltar_exclui_bt_clk, highlightcolor="white", 
                                                        highlightbackground="white", bg="white", fg=THECOLOR, 
                                                        activebackground=THECOLOR, activeforeground="white",
                                                        bd=0, cursor="hand2" )


            self.W = [self.titulo_confirma_exclui_E, self.Voltar_exclui_confirma_exclui_E]

            self.titulo_confirma_exclui_E.place(x=430, y=15)
            self.Voltar_exclui_confirma_exclui_E.place(x=650, y=240)

    # Terminada Abaixo
    def janela_excluir(self):
        self.janela_clear()

        # layout
        
        LabelAling: int = 450
        EntryAling: int = 465

        # widgets
        self.titulo_exclui = Label(self, font=("Times New Roman", 24), text="Exclusão de Cliente", bg="#fff",
                                   width=30, anchor=CENTER, bd=20)

                                   
        self.nome_janela_ecluir_label = Label(self, font=("Times New Roman", 18), text="Nome:", bg="#fff",
                                 width=30, anchor=CENTER, bd=5)
                                 
                                 
        self.Nome_janela_excluir_entry = Entry(self, width=34, justify=CENTER, font=("Times New Roman", 16), fg=THECOLOR,
                                            highlightbackground=THECOLOR, bd=0, highlightcolor=THECOLOR, bg="#f0f0f8")
                                  
                                  
        self.Exclui = Button(self, font=("Times New Roman", 18), text="Excluir", highlightcolor="white", highlightbackground="white",
                            bg="white", fg=THECOLOR, activebackground=THECOLOR, activeforeground="white", bd=0, cursor="hand2")

        
        self.voltar_menu_principal = Button(self, font=("Times New Roman", 18), text="Voltar", highlightcolor="white", 
                                            highlightbackground="white", bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                            activeforeground="white", bd=0, cursor="hand2" )

        self.W = [self.titulo_exclui, self.nome_janela_ecluir_label, self.Nome_janela_excluir_entry, self.Exclui, self.voltar_menu_principal]
        
        
        # comandos

        self.Exclui["command"] = self.exclui_bt_clk
        self.voltar_menu_principal["command"] = self.voltar_menu_principal_bt_clk

        #binds

        self.Exclui.bind('<Return>', lambda event: self.exclui_bt_clk())

        
        # desenhos

        self.titulo_exclui.place(x=415, y=15)
        self.nome_janela_ecluir_label.place(x=LabelAling, y=125)
        self.Nome_janela_excluir_entry.place(x=EntryAling, y=164)
        self.Exclui.place(x=600, y=240)
        self.voltar_menu_principal.place(x=700, y=240)

    # Terminada Abaixo
    def janela_usuario_escolhido(self, IndiceUsuario, Auxiliar, SapatoOuNome):
        self.janela_clear()

        self.Name: str = self.lista_clientes[IndiceUsuario][0].capitalize()
        self.Sapato: str = self.lista_clientes[IndiceUsuario][1]
        self.LarguraPe: str = self.lista_clientes[IndiceUsuario][2]
        self.NomeResponsavel: str = self.lista_clientes[IndiceUsuario][3]
        self.CpfResponsavel: str = self.lista_clientes[IndiceUsuario][4]
        self.ComprimentoPe: str = self.lista_clientes[IndiceUsuario][5]
        self.CalcanharMedida: str = self.lista_clientes[IndiceUsuario][6]
        self.Ponteira: str = self.lista_clientes[IndiceUsuario][7]
        self.Idade: str = self.lista_clientes[IndiceUsuario][8]
        self.TempoBallet: str = self.lista_clientes[IndiceUsuario][9]
        self.CargaHoraria: str = self.lista_clientes[IndiceUsuario][10]
        self.Escola: str = self.lista_clientes[IndiceUsuario][11]
        self.CodigoSapatilha: str = self.lista_clientes[IndiceUsuario][12]
        self.Rua: str = self.lista_clientes[IndiceUsuario][13]
        self.Numero: str = self.lista_clientes[IndiceUsuario][14]
        self.Cidade: str = self.lista_clientes[IndiceUsuario][15]
        self.UF: str = self.lista_clientes[IndiceUsuario][16]
        self.Observacao: str = self.lista_clientes[IndiceUsuario][17]


        Tamanhos = []
        LabelName = ["Tamanho do pé:       \t", "Largura do pé:       \t", "Nome do responsável: \t",
                     "CPF do responsável:  \t", "Comprimento do pé:   \t", "Medida do calcanhar: \t",
                     "Ponteira:            \t\t", "Idade:               \t\t", "Tempo de ballet:     \t",
                     "Carga horária:       \t\t", "Escola:              \t\t", "Código da sapatilha: \t",
                     "Rua:                 \t\t", "Telefone:              \t\t", "Cidade:              \t\t",
                     "UF:                  \t\t", "Observação:          \t\t"]

        for c in range(0, len(LabelName)):
            Tamanhos.append(10 + len(LabelName[c] + self.lista_clientes[IndiceUsuario][c]))

        Tamanhos.sort(reverse=True)

        # Labels

        self.Titulo = Label(self, font=("Times New Roman", 24), text=f"Cliente:\t{self.Name}", bg="#fff",
                            width=len(self.Name) + 10, anchor=CENTER, bd=20)

        self.SapatoUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[0]+self.Sapato,
                                   bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.LarguraPeUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[1]+self.LarguraPe,
                                      bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.NomeResponsavelUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[2]+self.NomeResponsavel, 
                                            bg="#fff", bd=4,
                                            width=Tamanhos[0], anchor=W)

        self.CpfResponsavelUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[3]+self.CpfResponsavel, 
                                           bg="#fff", bd=4,
                                           width=Tamanhos[0], anchor=W)

        self.ComprimentoPeUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[4]+self.ComprimentoPe, 
                                          bg="#fff", bd=4,
                                          width=Tamanhos[0], anchor=W)

        self.CalcanharMedidaUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[5]+self.CalcanharMedida,
                                            bg="#fff", bd=4,
                                            width=Tamanhos[0], anchor=W)

        self.PonteiraUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[6]+self.Ponteira,
                                     bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.IdadeUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[7]+self.Idade,
                                  bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.TempoBalletUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[8]+self.TempoBallet,
                                        bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.CargaHorariaUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[9]+self.CargaHoraria,
                                         bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.EscolaUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[10]+self.Escola,
                                   bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.CodigoSapatilhaUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[11]+self.CodigoSapatilha, 
                                            bg="#fff", bd=4,
                                            width=Tamanhos[0], anchor=W)

        self.RuaUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[12]+self.Rua,
                                bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.NumeroUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[13]+self.Numero,
                                   bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.CidadeUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[14]+self.Cidade,
                                   bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.UFUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[15]+self.UF,
                               bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

        self.ObservacaoUsuario = Label(self, font=("Times New Roman", 14), text=LabelName[16]+self.Observacao,
                               bg="#fff", bd=4, width=Tamanhos[0], anchor=W)

                               
        
        self.EditarBotao = Button(self, font=("Times New Roman", 18), text="Editar", bd=0, bg="white", fg=THECOLOR, width=10,
                               activebackground=THECOLOR, activeforeground="white", highlightcolor="white", cursor="hand2",
                               highlightbackground="white")

        self.VoltaBotao = Button(self, font=("Times New Roman", 18), text="Voltar", bd=0, bg="white", fg=THECOLOR, width=10,
                               activebackground=THECOLOR, activeforeground="white", highlightcolor="white", cursor="hand2",
                               highlightbackground="white")
        
        self.EditarBotao['command'] = lambda: self.janela_editar(self.Name, SapatoOuNome)
        self.EditarBotao.bind('<Return>', lambda event: self.janela_editar(self.Name, SapatoOuNome))
        
        if SapatoOuNome == 'nome':
            self.VoltaBotao['command'] = lambda: self.janela_listagem_mesmo_nome(0)
            self.VoltaBotao.bind('<Return>', lambda event: self.janela_listagem_mesmo_nome(0))
        
        else:
            self.VoltaBotao['command'] = lambda: self.janela_listagem_mesmo_tamanho_pe(0)
            self.VoltaBotao.bind('<Return>', lambda event: self.janela_listagem_mesmo_tamanho_pe(0))

        self.Titulo.place(x=430, y=15)

        # Layout

        TamX: int = 20
        TamY: int = 125

        # Labels

        
        self.CodigoSapatilhaUsuario.place(x=TamX, y=TamY)
        self.SapatoUsuario.place(x=TamX, y=TamY + (34 * 1))
        self.LarguraPeUsuario.place(x=TamX, y=TamY + (34 * 2))
        self.ComprimentoPeUsuario.place(x=TamX, y=TamY + (34 * 3))
        self.CalcanharMedidaUsuario.place(x=TamX, y=TamY + (34 * 4))
        self.PonteiraUsuario.place(x=TamX, y=TamY + (34 * 5))
        self.IdadeUsuario.place(x=TamX, y=TamY + (34 * 6))
        self.TempoBalletUsuario.place(x=TamX, y=TamY + (34 * 7))
        self.CargaHorariaUsuario.place(x=TamX, y=TamY + (34 * 8))
        self.EscolaUsuario.place(x=TamX, y=TamY + (34 * 9))
        self.ObservacaoUsuario.place(x=TamX, y=TamY + (34 * 10))
        self.NomeResponsavelUsuario.place(x=TamX, y=TamY + (34 * 11))
        self.CpfResponsavelUsuario.place(x=TamX, y=TamY + (34 * 12))
        self.NumeroUsuario.place(x=TamX, y=TamY + (34 * 13))
        self.RuaUsuario.place(x=TamX, y=TamY + (34 * 14))
        self.CidadeUsuario.place(x=TamX, y=TamY + (34 * 15))
        self.UFUsuario.place(x=TamX, y=TamY + (34 * 16))

        # Buttons

        self.EditarBotao.place(x=900, y=350)
        self.VoltaBotao.place(x=900, y=400)

        self.W = [self.Titulo, self.SapatoUsuario, self.SapatoUsuario, self.LarguraPeUsuario,
                    self.NomeResponsavelUsuario, self.CpfResponsavelUsuario, self.ComprimentoPeUsuario,
                    self.CalcanharMedidaUsuario, self.PonteiraUsuario, self.IdadeUsuario, self.TempoBalletUsuario,
                    self.CargaHorariaUsuario, self.EscolaUsuario, self.CodigoSapatilhaUsuario, self.RuaUsuario,
                    self.NumeroUsuario, self.CidadeUsuario, self.UFUsuario, self.ObservacaoUsuario, self.VoltaBotao, self.EditarBotao]
    
    # Terminada Abaixo
    def janela_planilhas(self, diretorio: str):
        def geraFrameDeArchivos(diretorio: str, conteudo: [str]):
            listaFramesArchivos: list = []
            for archivo in conteudo:
               
                # creations
                frameArchivo = Frame(
                    scrollableFrame.scrollable_frame,
                    bg=BGCOLOR
                )
                frameArchivo.columnconfigure(0, weight=1)
                frameArchivo.columnconfigure(1, weight=2)

                if isdir(join(diretorio, archivo)):
                    img = PhotoImage(file='./assets/pasta.png')
                    textLabelArchivo = f' {archivo} '
                else:
                    img = PhotoImage(file=join('./assets/arquivo.png'))
                    archivoSemExtensao = archivo.split('.')
                    textLabelArchivo = f' {archivoSemExtensao[0]} '

                labelArchivo = Label(
                    frameArchivo,
                    font = ( 'Roboto', 20 ),
                    text = textLabelArchivo,
                    width = 78,
                    bg = '#FFF',
                    anchor = 'w'
                )

                labelTipoArchivo = Label(
                    frameArchivo,
                    font = ( 'Roboto', 20 ),
                    image = img,
                    bg = '#FFF',
                    anchor = 'center'
                )
                labelTipoArchivo.image = img
                
                botaoArchivo = Button(
                    frameArchivo,
                    font=("Times New Roman", 14),
                    text="Abrir", bg="#ffebff",
                    highlightcolor="white", 
                    cursor='hand2',
                    highlightbackground="white", 
                    fg=THECOLOR, 
                    height=1,
                    width = 8,
                    activebackground=THECOLOR, 
                    activeforeground="white", 
                    bd=0
                )

                if isfile(join(diretorio, archivo)):
                    botaoArchivo['command'] = lambda archivo=join(diretorio, archivo): startfile(abspath(archivo))
                elif isdir(join(diretorio, archivo)):
                    botaoArchivo['command'] = lambda diretorio=f'{diretorio}{archivo}/': botaoArchivo_onClick(diretorio)
                    def botaoArchivo_onClick(diretorio):
                        wrapJanelaPlanilhas.place_forget()
                        self.janela_planilhas(diretorio)   


                # draws
                labelTipoArchivo.grid(column=0, row=0, pady=10, ipadx=5, sticky='wens')
                labelArchivo.grid(column=1, row=0, pady=10, sticky='wens')
                botaoArchivo.grid(column=2, row=0, pady=10, sticky="wens")

                listaFramesArchivos.append(frameArchivo)
            return listaFramesArchivos


        def botaoVoltar_onClick(diretorio: str):
            def concatAgain(arrayDir: list):
                stringDir = 'C:/'
                for diretorio in arrayDir[1:]:
                    stringDir = f'{stringDir}{diretorio}/'
                return stringDir

            arrayDir: list = diretorio.split('/')
            if diretorio == self.initialDir:
                self.W = [wrapJanelaPlanilhas]
                self.janela_clear()
                self.janela_principal()
            else:
                del arrayDir[len(arrayDir)-2:]
                backDir: str = concatAgain(arrayDir)
                wrapJanelaPlanilhas.place_forget()
                self.janela_planilhas(backDir)

        def botaoAbrirNoExplorer_onClick(diretorio: str):
            startfile(diretorio)
        # creations
        wrapJanelaPlanilhas = Frame(
            self,
            bg = BGCOLOR
        )

        wrapBotoesHeader = Frame(
            wrapJanelaPlanilhas,
            bg = BGCOLOR
        )

        botaoVoltar = Button(
            wrapBotoesHeader,
            font=("Roboto", 14),
            text="Voltar", bg='#FFF',
            cursor='hand2',
            height=1,
            bd=0
        )

        botaoAbrirNoExplorer = Button(
            wrapBotoesHeader,
            font=("Roboto", 14),
            text="Abrir no Explorador de Arquivos", bg='#FFF',
            cursor='hand2',
            height=1,
            bd=0
        )

        scrollableFrame = ScrollableFrame(
            self,
            wrapJanelaPlanilhas,
            width=1316, 
            height=512,
            bg=BGCOLOR,
            highlightbackground='#facacd'
        )
        
        listaFramesArchivos = geraFrameDeArchivos(diretorio, listdir(diretorio))

        # commands
        scrollableFrame.adicionarListaFrames(listaFramesArchivos)
        scrollableFrame.setOnEnd(lambda: scrollableFrame.adicionarListaFrames(listaFramesArchivos))
        botaoVoltar['command'] = lambda dir=diretorio: botaoVoltar_onClick(dir)
        botaoAbrirNoExplorer['command'] = lambda dir=diretorio: botaoAbrirNoExplorer_onClick(dir)

        # draws
        wrapBotoesHeader.grid(
            row = 0,
            padx = (38, 0),
            pady = ( 30, 0),
            sticky="wens"
        )
        botaoAbrirNoExplorer.grid(
            row = 0,
            column = 1,
            padx = (947, 0),
            sticky = 'ns'
        )
        botaoVoltar.grid(
            row = 0,
            column = 0,
            sticky = 'ns'
        )
        scrollableFrame.grid(
            row = 1,
            padx = 30,
            pady = 30
        )
        wrapJanelaPlanilhas.place(
            x = 0,
            y =0
        )

    # Terminada Abaixo
    def janela_principal(self):  # CHECK

        Espaçamento: int = 150
        TamX: int = 445
        self.W = []
        self.Verify = False

        # fundo

        # widgets
        self.titulo = Label(self, font=("Times New Roman", 24), text="Clientes Gaynor", bg="#fff", width=75,
                            anchor=CENTER, bd=20)

        self.cadastrar_bt = Button(
            self, 
            font=("Times New Roman", 16), 
            text="Cadastrar", 
            width=40, 
            fg="black",
            bg="white", 
            bd=0, 
            cursor="hand2", 
            highlightbackground=THECOLOR
        )
                                    
        self.buscar_bt = Button(
            self, 
            font=("Times New Roman", 16), 
            text="Buscar", 
            width=40, 
            fg="black",
            bg="white", 
            bd=0, 
            cursor="hand2", 
            highlightbackground=THECOLOR
        )

        self.excluir_bt = Button(
            self, 
            font=("Times New Roman", 16), 
            text="Excluir", 
            width=40, 
            fg="black",
            bg="white", 
            bd=0, 
            cursor="hand2", 
            highlightbackground=THECOLOR
        )

        self.planilhas_bt = Button(
            self, 
            font=("Times New Roman", 16), 
            text="Administrativo", 
            width=40, 
            fg="black",
            bg="white", 
            bd=0, 
            cursor="hand2", 
            highlightbackground=THECOLOR
        )
        
        self.W = [self.cadastrar_bt, self.excluir_bt, self.buscar_bt, self.planilhas_bt, self.titulo]

        # comando dos botoes
        self.cadastrar_bt["command"] = self.janela_cadastrar
        self.buscar_bt["command"] = self.janela_buscar
        self.excluir_bt["command"] = self.janela_excluir
        self.planilhas_bt['command'] = lambda: botaoListarArchives_onClick()
        def botaoListarArchives_onClick():
            self.janela_clear()
            self.janela_planilhas(self.initialDir)
        
        # binds

        self.cadastrar_bt.bind('<Return>', lambda event: self.janela_cadastrar())
        self.buscar_bt.bind('<Return>', lambda event: self.janela_buscar())
        self.excluir_bt.bind('<Return>', lambda event: self.janela_excluir())
        self.planilhas_bt.bind('<Return>', lambda event: self.botaoListarArchives_onClick())


        # desenho dos botoes
        self.titulo.place(x=0, y=15)
        self.cadastrar_bt.place(x=TamX, y=Espaçamento)
        self.buscar_bt.place(x=TamX, y=Espaçamento + 90)
        self.excluir_bt.place(x=TamX, y=Espaçamento + 180)
        self.planilhas_bt.place(x=TamX, y=Espaçamento + 270)

    # Terminada Abaixo
    def __init__(self):
        # cria janela do programa 
        define_janela(self, "./assets/gaynor.ico", "Clientes Gaynor ", "300x200", BGCOLOR)

        try:
            self.lista_clientes = carrega()
        except EOFError:
            self.lista_clientes = []
        else:
            self.lista_clientes = carrega()
        
        # enerar tela de splash
        self.janela_clear()
        
        self.state('zoomed')
        user = getenv('username')
        self.initialDir: str = f'C:/Users/{user}/OneDrive/Planilhas/'
        
        self.bind('<Escape>', lambda event: self.state('normal'))
        self.bind('<F11>', lambda event: self.state('zoomed'))

        
        self.janela_principal()
        
        self.mainloop()

        
        
        
BGCOLOR: str = '#fecdd0'
THECOLOR: str = "#f2c7c9"
ENTRY_FG_COLOR: str = '#000'
ENTRY_BG_COLOR: str = '#f0f0f8'
lclappdata = getenv('localappdata')
program = f'{lclappdata}\\Microsoft\\OneDrive\\onedrive.exe'
args = '/background'

subprocess.Popen([program, args]).pid
gaynor_db = Programa_Win()

