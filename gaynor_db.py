from definicoes_janela import define_janela, define_maior_str, espacoNoFinal, salva, carrega, define_tam_janela, buscap_nome, buscap_sapato,busca_multiplos_nomes
from tkinter import Tk, Button, Label, Entry, PhotoImage, CENTER, W

# @ FEITO POR DOGÃO
# @ DATA 27.09.2019
# @ TODOS DIREITOS RESERVADOS

THECOLOR: str = "#f538c3"





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
        LabelName = ["Nome:                \t\t", "Tamanho do pé:       \t", "Largura do pé:       \t\t",
                     "Nome do responsável: \t", "CPF do responsável:  \t", "Comprimento do pé:   \t",
                     "Medida do calcanhar: \t", "Ponteira:            \t\t", "Idade:               \t\t",
                     "Tempo de ballet:     \t", "Carga horária:       \t\t", "Escola:              \t\t",
                     "Código da sapatilha: \t", "Rua:                 \t\t", "Número:              \t\t",
                     "Cidade:              \t\t", "UF:                  \t\t", "Observação:          \t\t"]

        for c in range(0, len(LabelName)):
            Tamanhos.append((10 + len(LabelName[c] + self.cliente[c])))

        Tamanhos.sort(reverse=True)

        # Labels

        self.titulo_confirma = Label(self, font=("Times New Roman", 24), text="Confirma?", bg="#f7cbf7",
                                     width=30, anchor=CENTER, bd=20)

        self.nome_confirma = Label(self, font=("Times New Roman", 14), text=LabelName[0] + nome, bg="#f7cbf7",
                                   width=Tamanhos[0], anchor=W, bd=4)

        self.sapato_confirma = Label(self, font=("Times New Roman", 14), text=LabelName[1] + sapato, bg="#f7cbf7",
                                     width=Tamanhos[0], anchor=W, bd=4)

        self.LarguraPeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[2] + LargPe, bg="#f7cbf7",
                                       width=Tamanhos[0], anchor=W, bd=4)

        self.NomeResponsavelConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[3] + NomeResp,
                                             bg="#f7cbf7", width=Tamanhos[0], anchor=W,
                                             bd=4)

        self.CpfResposavelConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[4] + CpfResp,
                                           bg="#f7cbf7", width=Tamanhos[0], anchor=W,
                                           bd=4)
        
        self.ComprimentoPeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[5] + CompriPe,
                                           bg="#f7cbf7", width=Tamanhos[0], anchor=W,
                                           bd=4)

        self.CalcanharMedidaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[6] + CalcMed,
                                             bg="#f7cbf7", width=Tamanhos[0],
                                             anchor=W, bd=4)

        self.PonteiraConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[7] + Ponteira, bg="#f7cbf7"
                                      , width=Tamanhos[0], anchor=W, bd=4)

        self.IdadeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[8] + Idade, bg="#f7cbf7",
                                   width=Tamanhos[0], anchor=W, bd=4)

        self.TempoBalletConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[9] + TempBal,
                                         bg="#f7cbf7", width=Tamanhos[0], anchor=W,
                                         bd=4)

        self.CargaHorariaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[10] + CargHor,
                                          bg="#f7cbf7", width=Tamanhos[0], anchor=W,
                                          bd=4)

        self.EscolaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[11] + Escola, bg="#f7cbf7",
                                    width=Tamanhos[0], anchor=W, bd=4)

        self.CodigoSapatilhaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[12] + CodSapatilha,
                                             bg="#f7cbf7", width=Tamanhos[0],
                                             anchor=W, bd=4)

        self.RuaConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[13] + Rua, bg="#f7cbf7",
                                 width=Tamanhos[0], anchor=W, bd=4)

        self.NumeroConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[14] + Numero, bg="#f7cbf7",
                                    width=Tamanhos[0], anchor=W, bd=4)

        self.CidadeConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[15] + Cidade, bg="#f7cbf7",
                                    width=Tamanhos[0], anchor=W, bd=4)

        self.UFConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[16] + UF, bg="#f7cbf7",
                                width=Tamanhos[0], anchor=W, bd=4)

        self.ObservacaoConfirma = Label(self, font=("Times New Roman", 14), text=LabelName[17] + Observacao, bg="#f7cbf7",
                                width=Tamanhos[0], anchor=W, bd=4)

        # Buttons

        self.Voltar_cadastra = Button(self, font=("Times New Roman", 16), text="Voltar", cursor="exchange", bd=0,
                                      bg="white", fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                      highlightcolor="white", highlightbackground="white")

        self.Cadastra = Button(self, font=("Times New Roman", 16), text="Confirma", bd=0, bg="white", fg=THECOLOR,
                               activebackground=THECOLOR, activeforeground="white", highlightcolor="white",
                               highlightbackground="white", cursor="hand1")

        self.W = [self.titulo_confirma, self.Cadastra, self.nome_confirma, self.sapato_confirma, self.Voltar_cadastra,
                  self.LarguraPeConfirma, self.NomeResponsavelConfirma, self.CpfResposavelConfirma,
                  self.ComprimentoPeConfirma, self.CalcanharMedidaConfirma, self.PonteiraConfirma, self.IdadeConfirma,
                  self.TempoBalletConfirma, self.CargaHorariaConfirma, self.EscolaConfirma,
                  self.CodigoSapatilhaConfirma, self.RuaConfirma, self.NumeroConfirma, self.CidadeConfirma,
                  self.UFConfirma, self.ObservacaoConfirma]
        # comandos

        self.Cadastra["command"] = self.Confirma_cadastra_bt_clk
        self.Voltar_cadastra["command"] = self.Voltar_cadastra_bt_clk

        # Layout

        TamX: int = 20

        TamY: int = 91
        # Labels

        self.titulo_confirma.place(x=430, y=15)
        self.nome_confirma.place(x=TamX, y=TamY)
        self.sapato_confirma.place(x=TamX, y=TamY + 34)
        self.LarguraPeConfirma.place(x=TamX, y=TamY + (34 * 2))
        self.NomeResponsavelConfirma.place(x=TamX, y=TamY + (34 * 3))
        self.CpfResposavelConfirma.place(x=TamX, y=TamY + (34 * 4))
        self.ComprimentoPeConfirma.place(x=TamX, y=TamY + (34 * 5))
        self.CalcanharMedidaConfirma.place(x=TamX, y=TamY + (34 * 6))
        self.PonteiraConfirma.place(x=TamX, y=TamY + (34 * 7))
        self.IdadeConfirma.place(x=TamX, y=TamY + (34 * 8))
        self.TempoBalletConfirma.place(x=TamX, y=TamY + (34 * 9))
        self.CargaHorariaConfirma.place(x=TamX, y=TamY + (34 * 10))
        self.EscolaConfirma.place(x=TamX, y=TamY + (34 * 11))
        self.CodigoSapatilhaConfirma.place(x=TamX, y=TamY + (34 * 12))
        self.RuaConfirma.place(x=TamX, y=TamY + (34 * 13))
        self.NumeroConfirma.place(x=TamX, y=TamY + (34 * 14))
        self.CidadeConfirma.place(x=TamX, y=TamY + (34 * 15))
        self.UFConfirma.place(x=TamX, y=TamY + (34 * 16))
        self.ObservacaoConfirma.place(x=TamX, y=TamY + (34 * 17))

        # Buttons

        self.Cadastra.place(x=1160, y=260)
        self.Voltar_cadastra.place(x=1175, y=310)

    # Terminada Abaixo
    def janela_cadastrar(self):
        self.janela_clear()
        # widgets

        # Criação Labels
        self.titulo_cadastro = Label(self, font=("Times New Roman", 24), text="Edição de Cliente", bg="#f7cbf7",
                                     width=30, anchor=CENTER, bd=20)

        self.nome_cadastro = Label(self, font=("Times New Roman", 14), text="Nome:", bg="#f7cbf7", width=40,
                                   anchor=CENTER, bd=5)

        self.sapato_cadastro = Label(self, font=("Times New Roman", 14), text="Tamanho do pé:", bg="#f7cbf7", width=40,
                                     anchor=CENTER, bd=5)

        self.LarguraPeCadastro = Label(self, font=("Times New Roman", 14), text="Lárgura do pé:", bg="#f7cbf7",
                                       width=40, anchor=CENTER, bd=5)

        self.NomeResponsavelCadastro = Label(self, font=("Times New Roman", 14), text="Nome do Responsável:",
                                             bg="#f7cbf7", width=40, anchor=CENTER, bd=5)

        self.CpfResposavelCadastro = Label(self, font=("Times New Roman", 14), text="CPF do responsável:", bg="#f7cbf7",
                                           width=40, anchor=CENTER, bd=5)

        self.ComprimentoPeCadastro = Label(self, font=("Times New Roman", 14), text="Comprimento do pé:", bg="#f7cbf7",
                                           width=40, anchor=CENTER, bd=5)

        self.CalcanharMedidaCadastro = Label(self, font=("Times New Roman", 14), text="Medido do calcanhar:",
                                             bg="#f7cbf7", width=40, anchor=CENTER, bd=5)

        self.PonteiraCadastro = Label(self, font=("Times New Roman", 14), text="Ponteira:", bg="#f7cbf7", width=40,
                                      anchor=CENTER, bd=5)

        self.IdadeCadastro = Label(self, font=("Times New Roman", 14), text="Idade:", bg="#f7cbf7", width=40,
                                   anchor=CENTER, bd=5)

        self.TempoBalletCadastro = Label(self, font=("Times New Roman", 14), text="Tempo de Ballet:", bg="#f7cbf7",
                                         width=40, anchor=CENTER, bd=5)

        self.CargaHorariaCadastro = Label(self, font=("Times New Roman", 14), text="Carga Horária:", bg="#f7cbf7",
                                          width=40, anchor=CENTER, bd=5)

        self.EscolaCadastro = Label(self, font=("Times New Roman", 14), text="Escola:", bg="#f7cbf7", width=40,
                                    anchor=CENTER, bd=5)

        self.CodigoSapatilhaCadastro = Label(self, font=("Times New Roman", 14), text="Código da sapatilha:",
                                             bg="#f7cbf7", width=40, anchor=CENTER, bd=5)

        self.RuaCadastro = Label(self, font=("Times New Roman", 14), text="Rua:", bg="#f7cbf7", width=40,
                                 anchor=CENTER, bd=5)

        self.NumeroCadastro = Label(self, font=("Times New Roman", 14), text="Número:", bg="#f7cbf7", width=40,
                                    anchor=CENTER, bd=5)

        self.CidadeCadastro = Label(self, font=("Times New Roman", 14), text="Cidade:", bg="#f7cbf7", width=40,
                                    anchor=CENTER, bd=5)

        self.UFCadastro = Label(self, font=("Times New Roman", 14), text="UF:", bg="#f7cbf7", width=40,
                                anchor=CENTER, bd=5)

        self.ObservacaoCadastro = Label(self, font=("Times New Roman", 14), text="Observação:", bg="#f7cbf7", width=40,
                                anchor=CENTER, bd=5)
        
        # Entrys

        self.Nome_cadastro = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                   highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.Sapato_cadastro = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                     highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.LarguraPeCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                            highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.NomeResponsavelCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                  highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CpfResposavelCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.ComprimentoPeCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CalcanharMedidaCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                  highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.PonteiraCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                           highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.IdadeCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                        highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.TempoBalletCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                              highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CargaHorariaCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                               highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.EscolaCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                         highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CodigoSapatilhaCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                  highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.RuaCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                      highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.NumeroCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                         highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CidadeCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                         highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.UFCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                     highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR, bg="gray90")

        self.ObservacaoCadastroEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                     highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR, bg="gray90")


        # Criação Buttons
        self.Cadastra = Button(self, font=("Times New Roman", 16), text="Cadastrar", bd=0, bg="white", fg=THECOLOR,
                               activebackground=THECOLOR, activeforeground="white", highlightcolor="white",
                               highlightbackground="white", cursor="hand1")

        self.voltar_menu_principal = Button(self, font=("Times New Roman", 16), text="Voltar", bd=0, bg="white",
                                            fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                            highlightcolor="white", highlightbackground="white", cursor="exchange")

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
        self.voltar_menu_principal["command"] = self.voltar_menu_principal_bt_clk

        # Layout Labels
        LabelsX: int = 20
        LabelsY: int = 110

        Labels2X: int = 430
        Labels3X: int = 840

        # Layout Entry
        EntryX: int = LabelsX + 25
        EntryY: int = 144

        Entry2X: int = Labels2X + 25
        Entry3X: int = Labels3X + 25

        # Titulo
        self.titulo_cadastro.place(x=430, y=15)

        # Labels desenho
        self.nome_cadastro.place(x=LabelsX, y=LabelsY + (70 * 0))
        self.sapato_cadastro.place(x=LabelsX, y=LabelsY + (70 * 1))
        self.LarguraPeCadastro.place(x=LabelsX, y=LabelsY + (70 * 2))
        self.NomeResponsavelCadastro.place(x=LabelsX, y=LabelsY + (70 * 3))
        self.CpfResposavelCadastro.place(x=LabelsX, y=LabelsY + (70 * 4))
        self.ComprimentoPeCadastro.place(x=LabelsX, y=LabelsY + (70 * 5))
        self.CalcanharMedidaCadastro.place(x=LabelsX, y=LabelsY + (70 * 6))
        self.PonteiraCadastro.place(x=LabelsX, y=LabelsY + (70 * 7))

        self.IdadeCadastro.place(x=Labels2X, y=LabelsY + (70 * 0))
        self.TempoBalletCadastro.place(x=Labels2X, y=LabelsY + (70 * 1))
        self.CargaHorariaCadastro.place(x=Labels2X, y=LabelsY + (70 * 2))
        self.EscolaCadastro.place(x=Labels2X, y=LabelsY + (70 * 3))
        self.CodigoSapatilhaCadastro.place(x=Labels2X, y=LabelsY + (70 * 4))
        self.RuaCadastro.place(x=Labels2X, y=LabelsY + (70 * 5))
        self.NumeroCadastro.place(x=Labels2X, y=LabelsY + (70 * 6))
        self.CidadeCadastro.place(x=Labels2X, y=LabelsY + (70 * 7))
        self.UFCadastro.place(x=Labels3X, y=LabelsY + (70 * 0))
        self.ObservacaoCadastro.place(x=Labels3X, y=LabelsY + (70 * 1))

        # Entry desenho
        self.Nome_cadastro.place(x=EntryX, y=EntryY)
        self.Sapato_cadastro.place(x=EntryX, y=EntryY + 70)
        self.LarguraPeCadastroEntry.place(x=EntryX, y=EntryY + (70 * 2))
        self.NomeResponsavelCadastroEntry.place(x=EntryX, y=EntryY + (70 * 3))
        self.CpfResposavelCadastroEntry.place(x=EntryX, y=EntryY + (70 * 4))
        self.ComprimentoPeCadastroEntry.place(x=EntryX, y=EntryY + (70 * 5))
        self.CalcanharMedidaCadastroEntry.place(x=EntryX, y=EntryY + (70 * 6))
        self.PonteiraCadastroEntry.place(x=EntryX, y=EntryY + (70 * 7))

        self.IdadeCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 0))
        self.TempoBalletCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 1))
        self.CargaHorariaCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 2))
        self.EscolaCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 3))
        self.CodigoSapatilhaCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 4))
        self.RuaCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 5))
        self.NumeroCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 6))
        self.CidadeCadastroEntry.place(x= Entry2X, y=EntryY + (70 * 7))
        self.UFCadastroEntry.place(x=Entry3X, y=EntryY + (70 * 0))
        self.ObservacaoCadastroEntry.place(x=Entry3X, y=EntryY + (70 * 1))

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

        self.titulo_editar = Label(self, font=("Times New Roman", 24), text="Edição de Cliente", bg="#f7cbf7", width=30,
                                   anchor=CENTER, bd=20)

        self.nome_editar = Label(self, font=("Times New Roman", 14), text="Nome:", bg="#f7cbf7", width=40,
                                 anchor=CENTER, bd=5)

        self.sapato_editar = Label(self, font=("Times New Roman", 14), text="Tamanho do pé:", bg="#f7cbf7", width=40,
                                   anchor=CENTER, bd=5)

        self.LarguraPeEditar = Label(self, font=("Times New Roman", 14), text="Lárgura do pé:", bg="#f7cbf7", width=40,
                                     anchor=CENTER, bd=5)

        self.NomeResponsavelEditar = Label(self, font=("Times New Roman", 14), text="Nome do Responsável:",
                                           bg="#f7cbf7", width=40, anchor=CENTER, bd=5)

        self.CpfResposavelEditar = Label(self, font=("Times New Roman", 14), text="CPF do responsável:", bg="#f7cbf7",
                                         width=40, anchor=CENTER, bd=5)

        self.ComprimentoPeEditar = Label(self, font=("Times New Roman", 14), text="Comprimento do pé:", bg="#f7cbf7",
                                         width=40, anchor=CENTER, bd=5)

        self.CalcanharMedidaEditar = Label(self, font=("Times New Roman", 14), text="Medido do calcanhar:",
                                           bg="#f7cbf7", width=40, anchor=CENTER, bd=5)

        self.PonteiraEditar = Label(self, font=("Times New Roman", 14), text="Ponteira:", bg="#f7cbf7", width=40,
                                    anchor=CENTER, bd=5)

        self.IdadeEditar = Label(self, font=("Times New Roman", 14), text="Idade:", bg="#f7cbf7", width=40,
                                 anchor=CENTER, bd=5)

        self.TempoBalletEditar = Label(self, font=("Times New Roman", 14), text="Tempo de Ballet:", bg="#f7cbf7",
                                       width=40, anchor=CENTER, bd=5)

        self.CargaHorariaEditar = Label(self, font=("Times New Roman", 14), text="Carga Horária:", bg="#f7cbf7",
                                        width=40, anchor=CENTER, bd=5)

        self.EscolaEditar = Label(self, font=("Times New Roman", 14), text="Escola:", bg="#f7cbf7", width=40,
                                  anchor=CENTER, bd=5)

        self.CodigoSapatilhaEditar = Label(self, font=("Times New Roman", 14), text="Código da sapatilha:",
                                           bg="#f7cbf7", width=40, anchor=CENTER, bd=5)

        self.RuaEditar = Label(self, font=("Times New Roman", 14), text="Rua:", bg="#f7cbf7", width=40,
                               anchor=CENTER, bd=5)

        self.NumeroEditar = Label(self, font=("Times New Roman", 14), text="Número:", bg="#f7cbf7", width=40,
                                  anchor=CENTER, bd=5)

        self.CidadeEditar = Label(self, font=("Times New Roman", 14), text="Cidade:", bg="#f7cbf7", width=40,
                                  anchor=CENTER, bd=5)

        self.UFEditar = Label(self, font=("Times New Roman", 14), text="UF:", bg="#f7cbf7", width=40,
                              anchor=CENTER, bd=5)

        self.ObservacaoEditar = Label(self, font=("Times New Roman", 14), text="Observação:", bg="#f7cbf7", width=40,
                              anchor=CENTER, bd=5)
                              
        # Entrys

        self.Nome_editar = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                 highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.Sapato_editar = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                   highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.LarguraPeEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                          highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.NomeResponsavelEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CpfResposavelEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                              highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.ComprimentoPeEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                              highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CalcanharMedidaEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.PonteiraEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                         highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.IdadeEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                      highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.TempoBalletEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                            highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CargaHorariaEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                             highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.EscolaEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                       highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CodigoSapatilhaEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                                highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.RuaEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                    highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.NumeroEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                       highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.CidadeEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                       highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR)

        self.UFEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                   highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR, bg="gray90")

        self.ObservacaoEditarEntry = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 14), bd=0,
                                   highlightbackground=THECOLOR, highlightcolor=THECOLOR, fg=THECOLOR, bg="gray90")

        # Buttons

        self.Confirma_editar = Button(self, font=("Times New Roman", 16), text="Confirma", width=10, bg="white",
                                      fg=THECOLOR, activebackground=THECOLOR, activeforeground="white",
                                      highlightcolor="white", highlightbackground="white", bd=0, cursor="hand1")

        self.Voltar_editar = Button(self, font=("Times New Roman", 16), text="Voltar", width=10, cursor="exchange",
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
            self.Voltar_editar['command'] = lambda: self.Busca_p_nome_bt_clk(0)
        
        else:
            self.Voltar_editar['command'] = lambda: self.Busca_p_sapato_bt_clk(0)
        
        self.Confirma_editar["command"] = lambda: self.editar_confirma(cliente_para_editar)

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

        # Layout

        TamX: int = 20
        Tam2X: int = 430
        Tam3X: int = 840

        EntryY: int = 144

        # Desenha Titulo

        self.titulo_editar.place(x=430, y=15)

        #  Desenha Labels

        self.nome_editar.place(x=TamX, y=110)
        self.sapato_editar.place(x=TamX, y=180)
        self.LarguraPeEditar.place(x=TamX, y=250)
        self.NomeResponsavelEditar.place(x=TamX, y=320)
        self.CpfResposavelEditar.place(x=TamX, y=390)
        self.ComprimentoPeEditar.place(x=TamX, y=460)
        self.CalcanharMedidaEditar.place(x=TamX, y=530)
        self.PonteiraEditar.place(x=TamX, y=600)
        self.IdadeEditar.place(x=Tam2X, y=110)
        self.TempoBalletEditar.place(x=Tam2X, y=180)
        self.CargaHorariaEditar.place(x=Tam2X, y=250)
        self.EscolaEditar.place(x=Tam2X, y=320)
        self.CodigoSapatilhaEditar.place(x=Tam2X, y=390)
        self.RuaEditar.place(x=Tam2X, y=460)
        self.NumeroEditar.place(x=Tam2X, y=530)
        self.CidadeEditar.place(x=Tam2X, y=600)
        self.UFEditar.place(x=Tam3X, y=110)
        self.ObservacaoEditar.place(x=Tam3X, y=180)

        # Desenha Entrys

        self.Nome_editar.place(x=45, y=EntryY + (70 * 0))
        self.Sapato_editar.place(x=45, y=EntryY + (70 * 1))
        self.LarguraPeEditarEntry.place(x=TamX + 25, y=EntryY + (70 * 2))
        self.NomeResponsavelEditarEntry.place(x=TamX + 25, y=EntryY + (70 * 3))
        self.CpfResposavelEditarEntry.place(x=TamX + 25, y=EntryY + (70 * 4))
        self.ComprimentoPeEditarEntry.place(x=TamX + 25, y=EntryY + (70 * 5))
        self.CalcanharMedidaEditarEntry.place(x=TamX + 25, y=EntryY + (70 * 6))
        self.PonteiraEditarEntry.place(x=TamX + 25, y=EntryY + (70 * 7))
        self.IdadeEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 0))
        self.TempoBalletEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 1))
        self.CargaHorariaEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 2))
        self.EscolaEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 3))
        self.CodigoSapatilhaEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 4))
        self.RuaEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 5))
        self.NumeroEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 6))
        self.CidadeEditarEntry.place(x=Tam2X + 25, y=EntryY + (70 * 7))
        self.UFEditarEntry.place(x=Tam3X + 25, y=EntryY + (70 * 0))
        self.ObservacaoEditarEntry.place(x=Tam3X + 25, y=EntryY + (70 * 1))

        # Desenha Buttons

        self.Confirma_editar.place(x=900, y=300)
        self.Voltar_editar.place(x=900, y=350)

    # Terminada Abaixo
    def Busca_p_sapato_bt_clk(self, Initial):

        self.janela_clear()
        # layoutjhgf

        self.Aling: int = 30


        self.lista_mesmo_p = []
        self.sapato_busca_g = str(self.Sapato_buscar.get()).upper()
        self.lista_mesmo_p = buscap_sapato(self.sapato_busca_g, self.lista_clientes)
        Initial
        if self.lista_mesmo_p == []:

            self.janela_clear()

            self.titulo_buscar_E = Label(self, font=("Times New Roman", 24),
                                         text="Nenhuma cliente com \n   esse tamanho de pé", bg="#f7cbf7", width=30,
                                         anchor=CENTER, bd=20)

            self.Voltar_buuscar_E = Button(self, font=("Times New Roman", 20), text="Voltar", cursor="exchange",
                                           command=self.janela_buscar, highlightbackground=THECOLOR,
                                           highlightcolor=THECOLOR, fg=THECOLOR, bg="white", activebackground=THECOLOR,
                                           activeforeground="white", bd=0)

            self.W = [self.titulo_buscar_E, self.Voltar_buuscar_E]

            self.titulo_buscar_E.place(x=430, y=15)
            self.Voltar_buuscar_E.place(x=660, y=240)

        else:

            self.janela_clear()

            lista_tam_nomes = []
            self.TodosBotoes = []
            self.lista_label_clientes = []

            for x in range(0, len(self.lista_mesmo_p)):
                lista_tam_nomes.append(len(self.lista_clientes[x][0]))
            m_tam = define_maior_str(lista_tam_nomes)

            self.titulo_buscar = Label(self, font=("Times New Roman", 20),
                                       text="  " + "Nome:" + (m_tam) * "  " + "Sapato:",
                                       width=len("  " + "Nome:" + (m_tam) * "  " + " Sapato:"), bg="#f7cbf7", anchor=W)

            self.Voltar_buuscar = Button(self, font=("Times New Roman", 18), text="Voltar",
                                         cursor="exchange", highlightbackground="white", highlightcolor="white",
                                         bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                         activeforeground="white")

            self.Voltar_buuscar["command"] = lambda: self.janela_buscar()

            for n in self.lista_mesmo_p:
                self.lista_label_clientes.append(Label(self, font=("Times New Roman", 20),
                                                       text="  " + self.lista_clientes[n][0] + (m_tam - len(
                                                           self.lista_clientes[n][0])) * "  " + "\t" +
                                                            self.lista_clientes[n][1],
                                                       width=len("  " + "Nome:" + (m_tam) * "  " + "\tSapato:"),
                                                       bg="#f7cbf7",
                                                       anchor=W))

                self.BotaoUsuario = Button(self, font=("Times New Roman", 14), text="Ver Mais",
                                           highlightcolor="white",
                                           highlightbackground="white", bg="white", fg=THECOLOR,
                                           activebackground=THECOLOR, activeforeground="white", bd=0,
                                           cursor="hand1")

                self.BotaoUsuario["command"] = lambda Salvo=n: self.janela_usuario_escolhido(Salvo, Initial, 'sapato')

                self.TodosBotoes.append(self.BotaoUsuario)
            if len(self.lista_mesmo_p) <= 11:
                for y in range(0, len(self.lista_mesmo_p)):
                    self.lista_label_clientes[y].place(x=self.Aling, y=(60 + (45 * y)))
                    self.TodosBotoes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                              y=(60 + (45 * y)))
                self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes, self.TodosBotoes]
            else:
                for y in range(0, 11):
                    self.lista_label_clientes[y].place(x=self.Aling, y=(60 + (45 * y)))
                    self.TodosBotoes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                              y=(60 + (45 * y)))
                self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes, self.TodosBotoes]
                self.ProxPage = Button(self,font=("Times New Roman", 20),  text="Proxima Página", cursor="hand1", highlightbackground="white",
                                       highlightcolor="white", bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                       activeforeground="white")
                self.ProxPage["command"] = lambda: self.ProxPageFuncSapato(11)
                self.ProxPage.place(x=1100, y=600)
                self.W.append(self.ProxPage)


            self.titulo_buscar.place(x=self.Aling, y=15)
            self.geometry("1400x800")
            self.Voltar_buuscar.place(x=100, y=600)

    # Terminada Abaixo
    def PrevPageFuncSapato(self, Numero):
        self.PrevPage.place_forget()
        Numero -= 11
        self.ProxPageFuncSapato(Numero)

    # Terminada Abaixo
    def ProxPageFuncSapato(self, numero):
        self.janela_clear()
        self.titulo_buscar.place(x=self.Aling, y=15)
        self.geometry("1400x800")
        self.Voltar_buuscar.place(x=100, y=600)
        lista_tam_nomes = []
        for x in range(0, len(self.lista_mesmo_p)):
            lista_tam_nomes.append(len(self.lista_clientes[x][0]))
        m_tam = define_maior_str(lista_tam_nomes)
        if len(self.lista_mesmo_p)-numero <= 11:
            for y, x in zip(range(numero, len(self.lista_mesmo_p)), range(0 , (len(self.lista_mesmo_p)-numero))):

                self.lista_label_clientes[y].place(x=self.Aling, y=(60 + (45 * x)))
                self.TodosBotoes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                          y=(60 + (45 * x)))
            self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes, self.TodosBotoes]

        else:

            for y, x in zip(range(numero, numero+11) , range(0,11) ):
                self.lista_label_clientes[y].place(x=self.Aling, y=(60 + (45 * x)))
                self.TodosBotoes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                          y=(60 + (45 * x)))
            self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes, self.TodosBotoes]
            self.ProxPage = Button(self,font=("Times New Roman", 20), text="Proxima Página", cursor="hand1", highlightbackground="white",
                                   highlightcolor="white", bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                   activeforeground="white")
            self.ProxPage["command"] = lambda: self.ProxPageFuncSapato(numero+11)
            self.ProxPage.place(x=1100, y=600)
            self.W.append((self.ProxPage))
        if numero != 0:

            self.PrevPage = Button(self,font=("Times New Roman", 20), text="Página Anterior", cursor="exchange", highlightbackground="white",
                                   highlightcolor="white", bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                   activeforeground="white")
            self.PrevPage["command"] = lambda: self.PrevPageFuncSapato(numero)
            self.W.append(self.PrevPage)
            self.PrevPage.place(x=900, y=600)

    # Terminada Abaixo
    def Busca_p_nome_bt_clk(self, Initial):
        self.janela_clear()
            
        self.lista_multiplo_nome = []
        self.nome_buscar_g = str(self.Nome_buscar.get()).upper()
        self.lista_multiplo_nome = busca_multiplos_nomes(self.nome_buscar_g, self.lista_clientes)
        Initial

        # se não tem nenhuma cliente com esse nome ou com essas iniciais
        if self.lista_multiplo_nome == []:
            self.janela_clear()
            self.titulo_buscar_E = Label(self, font=("Times New Roman", 24), text="Cliente não Cadastrada",
                                            bg="#f7cbf7",
                                            width=30, anchor=CENTER, bd=20)
            self.Voltar_buuscar_E = Button(self, font=("Times New Roman", 20), text="Voltar", cursor="exchange",
                                            command=self.janela_buscar, highlightbackground=THECOLOR,
                                            highlightcolor=THECOLOR, fg=THECOLOR, bg="white", activebackground=THECOLOR,
                                            activeforeground="white", bd=0)

            self.W = [self.titulo_buscar_E, self.Voltar_buuscar_E]

            self.titulo_buscar_E.place(x=430, y=15)
            self.Voltar_buuscar_E.place(x=660, y=240)

        # caso contrario
        else:
            # layout
            self.Aling: int = 30
            lista_tam_nomes = []
            self.lista_label_clientes_nomes = []
            self.BotoesUsuarios_nomes = []
            for x in range(0, len(self.lista_multiplo_nome)):
                lista_tam_nomes.append(len(self.lista_clientes[x][0]))
            m_tam = define_maior_str(lista_tam_nomes)


            # definindo os widgets
            self.titulo_buscar = Label(self, font=("Times New Roman", 20),
                                       text="  " + "Nome:" + (m_tam) * "  " + "Sapato:",
                                       width=len("  " + "Nome:" + (m_tam) * "  " + " Sapato:"), bg="#f7cbf7", anchor=W)

            self.Voltar_buuscar = Button(self, font=("Times New Roman", 18), text="Voltar",
                                         cursor="exchange", highlightbackground="white", highlightcolor="white",
                                         bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                         activeforeground="white")
            # definindo lista de clientes label e botão 
            for n in self.lista_multiplo_nome:
                self.lista_label_clientes_nomes.append(Label(self, font=("Times New Roman", 20),
                                                       text="  " + self.lista_clientes[n][0] + (m_tam - len(
                                                           self.lista_clientes[n][0])) * "  " + "\t" +
                                                            self.lista_clientes[n][1],
                                                       width=len("  " + "Nome:" + (m_tam) * "  " + "\tSapato:"),
                                                       bg="#f7cbf7",
                                                       anchor=W))

                self.BotaoUsuario_nomes = Button(self, font=("Times New Roman", 14), text="Ver Mais",
                                           highlightcolor="white",
                                           highlightbackground="white", bg="white", fg=THECOLOR,
                                           activebackground=THECOLOR, activeforeground="white", bd=0,
                                           cursor="hand1")

                self.BotaoUsuario_nomes["command"] = lambda Salvo=n: self.janela_usuario_escolhido(Salvo, Initial, 'nome')

                self.BotoesUsuarios_nomes.append(self.BotaoUsuario_nomes)
            #comandos de botões
            self.Voltar_buuscar["command"] = lambda: self.janela_buscar()

            #self.W
            self.W = [self.Voltar_buuscar, self.titulo_buscar]
            # placing
            if len(self.lista_multiplo_nome) <= 11:
                for y in range(0, len(self.lista_multiplo_nome)):
                    self.lista_label_clientes_nomes[y].place(x=self.Aling, y=(60 + (45 * y)))
                    self.BotoesUsuarios_nomes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                              y=(60 + (45 * y)))
                self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes_nomes, self.BotoesUsuarios_nomes]
            else:
                for y in range(0, 11):
                    self.lista_label_clientes_nomes[y].place(x=self.Aling, y=(60 + (45 * y)))
                    self.BotoesUsuarios_nomes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                              y=(60 + (45 * y)))
                self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes_nomes, self.BotoesUsuarios_nomes]
                self.ProxPage = Button(self,font=("Times New Roman", 20),  text="Proxima Página", cursor="hand1", highlightbackground="white",
                                       highlightcolor="white", bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                       activeforeground="white")
                self.ProxPage["command"] = lambda: self.ProxPageFuncNome(11)
                self.ProxPage.place(x=1100, y=600)
                self.W.append(self.ProxPage)

            
            self.titulo_buscar.place(x=self.Aling, y=15)
            self.geometry("1400x800")
            self.Voltar_buuscar.place(x=100, y=600)

    # Terminada Abaixo
    def ProxPageFuncNome(self, numero):
        self.janela_clear()
        self.titulo_buscar.place(x=self.Aling, y=15)
        self.geometry("1400x800")
        self.Voltar_buuscar.place(x=100, y=600)
        lista_tam_nomes = []
        for x in range(0, len(self.lista_multiplo_nome)):
            lista_tam_nomes.append(len(self.lista_clientes[x][0]))
        m_tam = define_maior_str(lista_tam_nomes)


        if len(self.lista_multiplo_nome)-numero <= 11:
            for y, x in zip(range(numero, len(self.lista_multiplo_nome)), range(0 , (len(self.lista_multiplo_nome)-numero))):

                self.lista_label_clientes_nomes[y].place(x=self.Aling, y=(60 + (45 * x)))
                self.BotoesUsuarios_nomes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                          y=(60 + (45 * x)))
            self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes_nomes, self.BotoesUsuarios_nomes]

        else:

            for y, x in zip(range(numero, numero+11) , range(0,11) ):
                self.lista_label_clientes_nomes[y].place(x=self.Aling, y=(60 + (45 * x)))
                self.BotoesUsuarios_nomes[y].place(x=(len("  " + "Nome:" + (m_tam) * "  " + " Sapato:")) * 11,
                                          y=(60 + (45 * x)))
            self.W = [self.titulo_buscar, self.Voltar_buuscar, self.lista_label_clientes_nomes, self.BotoesUsuarios_nomes]
            self.ProxPage = Button(self,font=("Times New Roman", 20), text="Proxima Página", cursor="hand1", highlightbackground="white",
                                   highlightcolor="white", bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                   activeforeground="white")
            self.ProxPage["command"] = lambda: self.ProxPageFuncNome(numero+11)
            self.ProxPage.place(x=1100, y=600)
            self.W.append((self.ProxPage))
        if numero != 0:

            self.PrevPage = Button(self,font=("Times New Roman", 20), text="Página Anterior", cursor="exchange", highlightbackground="white",
                                   highlightcolor="white", bd=0, bg="white", fg=THECOLOR, activebackground=THECOLOR,
                                   activeforeground="white")
            self.PrevPage["command"] = lambda: self.PrevPageFuncNome(numero)
            self.W.append(self.PrevPage)
            self.PrevPage.place(x=900, y=600)

    # Terminada Abaixo
    def PrevPageFuncNome(self, Numero):
        self.PrevPage.place_forget()
        Numero -= 11
        self.ProxPageFuncNome(Numero)

    # Terminada Abaixo
    def janela_buscar(self):
        self.janela_clear()
        self.ContadorSapato = 0
        define_tam_janela(self, "1400x800")

        # layout

        ButtonAling: int = 880
        AllAling: int = 410
        LabelAling: int = 450

        # widgets
        self.titulo_buscar = Label(self, font=("Times New Roman", 24), text="Busca de Cliente", bg="#f7cbf7",
                                   width=35, anchor=CENTER, bd=20)

        self.nome_buscar = Label(self, font=("Times New Roman", 18), text="Nome:", bg="#f7cbf7",
                                 width=30, anchor=CENTER, bd=5)

        self.sapato_buscar = Label(self, font=("Times New Roman", 18), text="Sapato:", bg="#f7cbf7",
                                   width=30, anchor=CENTER, bd=5)

        self.Nome_buscar = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 16), fg=THECOLOR,
                                 highlightbackground=THECOLOR, bd=0, highlightcolor=THECOLOR)

        self.Sapato_buscar = Entry(self, width=40, justify=CENTER, font=("Times New Roman", 16), fg=THECOLOR,
                                   highlightbackground=THECOLOR, bd=0, highlightcolor=THECOLOR)

        self.Busca_p_nome = Button(self, font=("Times New Roman", 14), text="Busca por Nome", width=13,
                                   cursor="question_arrow", bg=THECOLOR, fg="white", bd=0, activebackground="white",
                                   activeforeground=THECOLOR, highlightbackground="white", highlightcolor="white")

        self.Busca_p_sapato = Button(self, font=("Times New Roman", 14), text="Busca por Sapato", width=13,
                                     cursor="question_arrow", bg=THECOLOR, fg="white", bd=0, activebackground="white",
                                     activeforeground=THECOLOR, highlightbackground="white", highlightcolor="white")

        self.voltar_menu_principal = Button(self, font=("Times New Roman", 14), text="Voltar", width=13,
                                            cursor="exchange", bg=THECOLOR, fg="white", bd=0, activebackground="white",
                                            activeforeground=THECOLOR, highlightbackground="white",
                                            highlightcolor="white")

        self.W = [self.voltar_menu_principal, self.titulo_buscar, self.nome_buscar, self.sapato_buscar,
                  self.Nome_buscar,
                  self.Sapato_buscar, self.Busca_p_nome, self.Busca_p_sapato]

        # comandos

        self.voltar_menu_principal["command"] = self.voltar_menu_principal_bt_clk
        self.Busca_p_sapato["command"] = lambda: self.Busca_p_sapato_bt_clk(0)
        self.Busca_p_nome["command"] = lambda: self.Busca_p_nome_bt_clk(0)

        # desenhos

        self.nome_buscar.place(x=LabelAling, y=125)
        self.sapato_buscar.place(x=LabelAling, y=250)
        self.titulo_buscar.place(x=AllAling, y=15)
        self.Nome_buscar.place(x=AllAling, y=165)
        self.Sapato_buscar.place(x=AllAling, y=290)
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
        self.Nome_excluir.insert(0, self.nome_exclui_g)

    # Terminada Abaixo
    def exclui_bt_clk(self):

        self.nome_exclui_g = str(self.Nome_excluir.get()).upper()
        pos = buscap_nome(self.nome_exclui_g, self.lista_clientes)

        if None != pos:

            pos = int(pos)

            self.janela_clear()

            self.titulo_confirma = Label(self, font=("Times New Roman", 24), text="Confirma?", bg="#f7cbf7", width=30,
                                         anchor=CENTER, bd=20)

            Tamanhos = []
            LabelName = ["Nome:                \t\t", "Tamanho do pé:       \t", "Largura do pé:       \t\t",
                         "Nome do responsável: \t", "CPF do responsável:  \t", "Comprimento do pé:   \t",
                         "Medida do calcanhar: \t", "Ponteira:            \t\t", "Idade:               \t\t",
                         "Tempo de ballet:     \t", "Carga horária:       \t\t", "Escola:              \t\t",
                         "Código da sapatilha: \t", "Rua:                 \t\t", "Número:              \t\t",
                         "Cidade:              \t\t", "UF:                  \t\t", "Observação:          \t\t"]

            for c in range(0, len(LabelName)):
                Tamanhos.append(10 + len(LabelName[c] + self.lista_clientes[pos][c]))

            Tamanhos.sort(reverse=True)

            # Labels

            self.nome_confirma = Label(self, font=("Times New Roman", 14), text="Nome:\t" + self.lista_clientes[pos][0],
                                       bg="#f7cbf7", width=Tamanhos[0], anchor=CENTER, bd=4)

            self.sapato_confirma = Label(self, font=("Times New Roman", 14),
                                         text="Tamanho do pé:\t" + self.lista_clientes[pos][1], bg="#f7cbf7",
                                         width=Tamanhos[0], anchor=CENTER, bd=4)

            self.LarguraPeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                 text="Largura do pé:\t" + self.lista_clientes[pos][2], bg="#f7cbf7",
                                                 width=Tamanhos[0], anchor=CENTER, bd=4)

            self.NomeResponsavelExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                       text="Nome do responsável:\t" + self.lista_clientes[pos][3],
                                                       bg="#f7cbf7", width=Tamanhos[0], anchor=CENTER, bd=4)

            self.CpfResponsavelExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                      text="Cpf do responsável:\t" + self.lista_clientes[pos][4],
                                                      bg="#f7cbf7", width=Tamanhos[0], anchor=CENTER, bd=4)

            self.ComprimentoPeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                     text="Comprimento do pé:\t" + self.lista_clientes[pos][5],
                                                     bg="#f7cbf7", width=Tamanhos[0], anchor=CENTER, bd=4)

            self.CalcanharMedidaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                       text="Medida do calcanhar:\t" + self.lista_clientes[pos][6],
                                                       bg="#f7cbf7", width=Tamanhos[0], anchor=CENTER, bd=4)

            self.PonteiraExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                text="Ponteira:\t" + self.lista_clientes[pos][7], bg="#f7cbf7",
                                                width=Tamanhos[0], anchor=CENTER, bd=4)

            self.IdadeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                             text="Idade:\t" + self.lista_clientes[pos][8], bg="#f7cbf7",
                                             width=Tamanhos[0], anchor=CENTER, bd=4)

            self.TempoBalletExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                   text="Tempo de ballet:\t" + self.lista_clientes[pos][9],
                                                   bg="#f7cbf7",
                                                   width=Tamanhos[0], anchor=CENTER, bd=4)

            self.CargaHorariaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                    text="Carga Horária:\t" + self.lista_clientes[pos][10],
                                                    bg="#f7cbf7",
                                                    width=Tamanhos[0], anchor=CENTER, bd=4)

            self.EscolaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                              text="Escola:\t" + self.lista_clientes[pos][11], bg="#f7cbf7",
                                              width=Tamanhos[0], anchor=CENTER, bd=4)

            self.CodigoSapatilhaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                                       text="Código da sapatilha:\t" + self.lista_clientes[pos][12],
                                                       bg="#f7cbf7", width=Tamanhos[0], anchor=CENTER, bd=4)

            self.RuaExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                           text="Rua:\t" + self.lista_clientes[pos][13], bg="#f7cbf7",
                                           width=Tamanhos[0], anchor=CENTER, bd=4)

            self.NumeroExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                              text="Número:\t" + self.lista_clientes[pos][14], bg="#f7cbf7",
                                              width=Tamanhos[0], anchor=CENTER, bd=4)

            self.CidadeExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                              text="Cidade:\t" + self.lista_clientes[pos][15], bg="#f7cbf7",
                                              width=Tamanhos[0], anchor=CENTER, bd=4)

            self.UFExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                          text="UF:\t" + self.lista_clientes[pos][16], bg="#f7cbf7",
                                          width=Tamanhos[0], anchor=CENTER, bd=4)

            self.ObservacaoExcluiConfirma = Label(self, font=("Times New Roman", 14),
                                          text="Observação:\t" + self.lista_clientes[pos][17], bg="#f7cbf7",
                                          width=Tamanhos[0], anchor=CENTER, bd=4)

            # Buttons

            self.Exclui_bt = Button(self, font=("Times New Roman", 19), text="Confirma", bg="white", fg=THECOLOR, bd=0,
                                    activebackground=THECOLOR, activeforeground="white", highlightbackground="white",
                                    highlightcolor="white", cursor="pirate")

            self.Voltar_exclui_cadastra = Button(self, font=("Times New Roman", 19), text="Voltar", cursor="exchange",
                                                 bg="white", fg=THECOLOR, bd=0, activebackground=THECOLOR,
                                                 activeforeground="white", highlightbackground="white",
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

            # Layout

            TamX: int = 20
            TamY: int = 91

            # Labels

            self.titulo_confirma.place(x=430, y=15)
            self.nome_confirma.place(x=TamX, y=TamY + (34 * 0))
            self.sapato_confirma.place(x=TamX, y=TamY + (34 * 1))
            self.LarguraPeExcluiConfirma.place(x=TamX, y=TamY + (34 * 2))
            self.NomeResponsavelExcluiConfirma.place(x=TamX, y=TamY + (34 * 3))
            self.CpfResponsavelExcluiConfirma.place(x=TamX, y=TamY + (34 * 4))
            self.ComprimentoPeExcluiConfirma.place(x=TamX, y=TamY + (34 * 5))
            self.CalcanharMedidaExcluiConfirma.place(x=TamX, y=TamY + (34 * 6))
            self.PonteiraExcluiConfirma.place(x=TamX, y=TamY + (34 * 7))
            self.IdadeExcluiConfirma.place(x=TamX, y=TamY + (34 * 8))
            self.TempoBalletExcluiConfirma.place(x=TamX, y=TamY + (34 * 9))
            self.CargaHorariaExcluiConfirma.place(x=TamX, y=TamY + (34 * 10))
            self.EscolaExcluiConfirma.place(x=TamX, y=TamY + (34 * 11))
            self.CodigoSapatilhaExcluiConfirma.place(x=TamX, y=TamY + (34 * 12))
            self.RuaExcluiConfirma.place(x=TamX, y=TamY + (34 * 13))
            self.NumeroExcluiConfirma.place(x=TamX, y=TamY + (34 * 14))
            self.CidadeExcluiConfirma.place(x=TamX, y=TamY + (34 * 15))
            self.UFExcluiConfirma.place(x=TamX, y=TamY + (34 * 16))
            self.ObservacaoExcluiConfirma.place(x=TamX, y=TamY + (34 * 17))

            # Buttons

            self.Exclui_bt.place(x=1000, y=300)
            self.Voltar_exclui_cadastra.place(x=1018, y=350)

        else:  # Caso não encontre a cliente
            self.janela_clear()
            self.titulo_confirma_exclui_E = Label(self, font=("Times New Roman", 24), text="Cliente não Cadastrada",
                                                  bg="#f7cbf7",
                                                  width=30, anchor=CENTER, bd=20)
            self.Voltar_exclui_confirma_exclui_E = Button(self, font=("Times New Roman", 20), text="Voltar",
                                                          command=self.Voltar_exclui_bt_clk, cursor="exchange",
                                                          bg=THECOLOR, fg="white", bd=0, activebackground="white",
                                                          activeforeground=THECOLOR, highlightbackground=THECOLOR,
                                                          highlightcolor=THECOLOR)

            self.W = [self.titulo_confirma_exclui_E, self.Voltar_exclui_confirma_exclui_E]

            self.titulo_confirma_exclui_E.place(x=430, y=15)
            self.Voltar_exclui_confirma_exclui_E.place(x=650, y=240)

    # Terminada Abaixo
    def janela_excluir(self):
        self.janela_clear()

        # layout
        Alinhamento: int = 500

        # widgets
        self.titulo_exclui = Label(self, font=("Times New Roman", 24), text="Exclusão de Cliente", bg="#f7cbf7",
                                   width=30, anchor=CENTER, bd=20)
        self.nome_exclui = Label(self, font=("Times New Roman", 18), text="Nome:", bg="#f7cbf7",
                                 width=30, anchor=CENTER, bd=5)
        self.Nome_excluir = Entry(self, width=35, justify=CENTER, font=("Times New Roman", 14),
                                  highlightbackground="#f538c3", highlightcolor=THECOLOR, bd=0, fg="#f538c3")
        self.Exclui = Button(self, font=("Times New Roman", 18), text="Excluir", fg="white", bg="#f538c3", bd=0,
                             activebackground="white", activeforeground="#f538c3", cursor="pirate")
        self.voltar_menu_principal = Button(self, font=("Times New Roman", 18), text="Voltar", fg="white", bg="#f538c3",
                                            bd=0, activebackground="white", activeforeground="#f538c3",
                                            cursor="exchange")

        self.W = [self.titulo_exclui, self.nome_exclui, self.Nome_excluir, self.Exclui, self.voltar_menu_principal]
        # comandos
        self.Exclui["command"] = self.exclui_bt_clk
        self.voltar_menu_principal["command"] = self.voltar_menu_principal_bt_clk
        # desenhos
        self.titulo_exclui.place(x=415, y=15)
        self.Nome_excluir.place(x=Alinhamento + 27, y=165)
        self.Exclui.place(x=600, y=240)
        self.voltar_menu_principal.place(x=700, y=240)
        self.nome_exclui.place(x=Alinhamento, y=125)

    # Terminada Abaixo
    def janela_principal(self):  # CHECK

        Espaçamento: int = 150
        TamX: int = 445
        self.W = []
        self.Verify = False

        # fundo
        self.fundo = Label(self, width=100, height=100, bg="white")

        # widgets
        self.cadastrar_bt = Button(self, font=("Times New Roman", 16), text="Cadastrar", width=40, fg="black",
                                   bg="white", bd=0, cursor="hand1", highlightbackground=THECOLOR)
        self.excluir_bt = Button(self, font=("Times New Roman", 16), text="Excluir", width=40, fg="black", bg="white",
                                 bd=0, cursor="hand1", highlightbackground=THECOLOR)
        self.buscar_bt = Button(self, font=("Times New Roman", 16), text="Buscar", width=40, fg="black", bg="white",
                                bd=0, cursor="hand1", highlightbackground=THECOLOR)
        self.titulo = Label(self, font=("Times New Roman", 24), text="Clientes Gaynor", bg="#f7cbf7", width=30,
                            anchor=CENTER, bd=20)
        self.W = [self.cadastrar_bt, self.excluir_bt, self.buscar_bt, self.titulo]

        # comando dos botoes
        self.cadastrar_bt["command"] = self.janela_cadastrar
        self.buscar_bt["command"] = self.janela_buscar
        self.excluir_bt["command"] = self.janela_excluir

        # desenho dos botoes
        self.titulo.place(x=415, y=15)
        self.cadastrar_bt.place(x=TamX, y=Espaçamento)
        self.buscar_bt.place(x=TamX, y=Espaçamento + 90)
        self.excluir_bt.place(x=TamX, y=Espaçamento + 180)
        self.fundo.place(x=0, y=0)
        self.mainloop()

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
        LabelName = ["Tamanho do pé:       \t", "Largura do pé:       \t\t", "Nome do responsável: \t",
                     "CPF do responsável:  \t", "Comprimento do pé:   \t", "Medida do calcanhar: \t",
                     "Ponteira:            \t\t", "Idade:               \t\t", "Tempo de ballet:     \t",
                     "Carga horária:       \t\t", "Escola:              \t\t", "Código da sapatilha: \t",
                     "Rua:                 \t\t", "Número:              \t\t", "Cidade:              \t\t",
                     "UF:                  \t\t", "Observação:          \t\t"]

        for c in range(0, len(LabelName)):
            Tamanhos.append(10 + len(LabelName[c] + self.lista_clientes[IndiceUsuario][c]))

        Tamanhos.sort(reverse=True)

        # Labels

        self.Titulo = Label(self, font=("Times New Roman", 24), text=f"Cliente: {self.Name}", bg="#f7cbf7",
                            width=len(self.Name) + 10, anchor=CENTER, bd=20)

        self.SapatoUsuario = Label(self, font=("Times New Roman", 14), text=f"Tamanho do pé: {self.Sapato}",
                                   bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.LarguraPeUsuario = Label(self, font=("Times New Roman", 14), text=f"Largura do pé: {self.LarguraPe}",
                                      bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.NomeResponsavelUsuario = Label(self, font=("Times New Roman", 14),
                                            text=f"Nome do responsável: {self.NomeResponsavel}", bg="#f7cbf7", bd=4,
                                            width=Tamanhos[0], anchor=CENTER)

        self.CpfResponsavelUsuario = Label(self, font=("Times New Roman", 14),
                                           text=f"CPF do responsável: {self.CpfResponsavel}", bg="#f7cbf7", bd=4,
                                           width=Tamanhos[0], anchor=CENTER)

        self.ComprimentoPeUsuario = Label(self, font=("Times New Roman", 14),
                                          text=f"Comprimento do pé: {self.ComprimentoPe}", bg="#f7cbf7", bd=4,
                                          width=Tamanhos[0], anchor=CENTER)

        self.CalcanharMedidaUsuario = Label(self, font=("Times New Roman", 14),
                                            text=f"Medida do calcanhar: {self.CalcanharMedida}", bg="#f7cbf7", bd=4,
                                            width=Tamanhos[0], anchor=CENTER)

        self.PonteiraUsuario = Label(self, font=("Times New Roman", 14), text=f"Ponteira: {self.Ponteira}",
                                     bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.IdadeUsuario = Label(self, font=("Times New Roman", 14), text=f"Idade: {self.Idade}",
                                  bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.TempoBalletUsuario = Label(self, font=("Times New Roman", 14), text=f"Tempo de ballet: {self.TempoBallet}",
                                        bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.CargaHorariaUsuario = Label(self, font=("Times New Roman", 14), text=f"Carga horária: {self.CargaHoraria}",
                                         bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.EscolaUsuario = Label(self, font=("Times New Roman", 14), text=f"Escola: {self.Escola}",
                                   bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.CodigoSapatilhaUsuario = Label(self, font=("Times New Roman", 14),
                                            text=f"Código da sapatilha: {self.CodigoSapatilha}", bg="#f7cbf7", bd=4,
                                            width=Tamanhos[0], anchor=CENTER)

        self.RuaUsuario = Label(self, font=("Times New Roman", 14), text=f"Rua: {self.Rua}",
                                bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.NumeroUsuario = Label(self, font=("Times New Roman", 14), text=f"Número: {self.Numero}",
                                   bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.CidadeUsuario = Label(self, font=("Times New Roman", 14), text=f"Cidade: {self.Cidade}",
                                   bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.UFUsuario = Label(self, font=("Times New Roman", 14), text=f"UF: {self.UF}",
                               bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.ObservacaoUsuario = Label(self, font=("Times New Roman", 14), text=f"Observação: {self.Observacao}",
                               bg="#f7cbf7", bd=4, width=Tamanhos[0], anchor=CENTER)

        self.VoltaBotao = Button(self, font=("Times New Roman", 18), text="Voltar", fg="white", bg="#f538c3",
                                 bd=0, activebackground="white", activeforeground="#f538c3",
                                 cursor="exchange")
        
        self.EditarBotao = Button(self, font=("Times New Roman", 18), text="Editar", fg="white", bg="#f538c3",
                                 bd=0, activebackground="white", activeforeground="#f538c3",
                                 cursor="exchange")
        
        self.EditarBotao['command'] = lambda: self.janela_editar(self.Name, SapatoOuNome)
        
        if SapatoOuNome == 'nome':
            self.VoltaBotao['command'] = lambda: self.Busca_p_nome_bt_clk(0)
        
        else:
            self.VoltaBotao['command'] = lambda: self.Busca_p_sapato_bt_clk(0)

        self.Titulo.place(x=430, y=15)

        # Layout

        TamX: int = 20
        TamY: int = 91

        # Labels

        self.SapatoUsuario.place(x=TamX, y=TamY + (34 * 0))
        self.SapatoUsuario.place(x=TamX, y=TamY + (34 * 1))
        self.LarguraPeUsuario.place(x=TamX, y=TamY + (34 * 2))
        self.NomeResponsavelUsuario.place(x=TamX, y=TamY + (34 * 3))
        self.CpfResponsavelUsuario.place(x=TamX, y=TamY + (34 * 4))
        self.ComprimentoPeUsuario.place(x=TamX, y=TamY + (34 * 5))
        self.CalcanharMedidaUsuario.place(x=TamX, y=TamY + (34 * 6))
        self.PonteiraUsuario.place(x=TamX, y=TamY + (34 * 7))
        self.IdadeUsuario.place(x=TamX, y=TamY + (34 * 8))
        self.TempoBalletUsuario.place(x=TamX, y=TamY + (34 * 9))
        self.CargaHorariaUsuario.place(x=TamX, y=TamY + (34 * 10))
        self.EscolaUsuario.place(x=TamX, y=TamY + (34 * 11))
        self.CodigoSapatilhaUsuario.place(x=TamX, y=TamY + (34 * 12))
        self.RuaUsuario.place(x=TamX, y=TamY + (34 * 13))
        self.NumeroUsuario.place(x=TamX, y=TamY + (34 * 14))
        self.CidadeUsuario.place(x=TamX, y=TamY + (34 * 15))
        self.UFUsuario.place(x=TamX, y=TamY + (34 * 16))
        self.ObservacaoUsuario.place(x=TamX, y=TamY + (34 * 17))

        # Buttons

        self.VoltaBotao.place(x=900, y=350)
        self.EditarBotao.place(x=900, y=400)

        self.W = [self.Titulo, self.SapatoUsuario, self.SapatoUsuario, self.LarguraPeUsuario,
                    self.NomeResponsavelUsuario, self.CpfResponsavelUsuario, self.ComprimentoPeUsuario,
                    self.CalcanharMedidaUsuario, self.PonteiraUsuario, self.IdadeUsuario, self.TempoBalletUsuario,
                    self.CargaHorariaUsuario, self.EscolaUsuario, self.CodigoSapatilhaUsuario, self.RuaUsuario,
                    self.NumeroUsuario, self.CidadeUsuario, self.UFUsuario, self.ObservacaoUsuario, self.VoltaBotao, self.EditarBotao]

    # Terminada Abaixo
    def __init__(self):
        try:
            self.lista_clientes = carrega()
        except EOFError:
            self.lista_clientes = []
        else:
            self.lista_clientes = carrega()
        define_janela(self, "gaynor.ico", "Clientes Gaynor Minden", "1400x800", "#f538c3")

        self.janela_principal()


gaynor_db = Programa_Win()
