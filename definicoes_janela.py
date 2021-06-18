import os
from tkinter import Tk, Button, Label, Entry, PhotoImage, CENTER
import pickle
db: str = "database.txt"
sessaoArch: str = "sessao.txt"

def define_icon(janela: object, icon) -> object:
    img_icon = PhotoImage(file=os.path.join(icon))
    janela.tk.call('wm', 'iconphoto', janela._w, img_icon)


def define_tam_janela(janela: object, size):
    janela.geometry(size)


def define_janela(janela: object, icone, title, size, bg_color):
    Tk.__init__(janela)
    janela.geometry(size)
    janela.title(title)
    janela["bg"] = bg_color
    define_icon(janela, icone)


def salvaSessao(sessao: bool):
    with open("./"+ sessaoArch, "wb") as file:
        pickle.dump(sessao, file)
        file.close()
    return


def carregaSessao():
    try:
        with open("./" + sessaoArch, "rb") as file:
            sessao = pickle.load(file)
            file.close()
    except EOFError:
        sessao: bool = False 
    else:
        with open("./" + sessaoArch, "rb") as file:
            sessao = pickle.load(file)
            file.close()
    return sessao


def salvaListaClientes(lista):
    with open("./"+ db, "wb") as file:
        pickle.dump(lista, file)
        file.close()


def carregaListaClientes():  
    try:
        with open("./" + db, "rb") as file:
            lista = pickle.load(file)
            file.close()
    except EOFError:
        lista = []
    else:
        with open("./" + db, "rb") as file:
            lista = pickle.load(file)
            file.close()
    
    return lista


def espacoNoFinal(nome_buscar):
    if(len(nome_buscar) > 0):    
        while nome_buscar[len(nome_buscar) - 1] == " ":
            nome_buscar = nome_buscar[:len(nome_buscar) - 1]
    return (nome_buscar)


def buscap_nome(nome, clientes):
    for x in range(0, len(clientes)):
        if clientes[x][0] == nome:
            return x
    return None

def busca_multiplos_nomes(nome, clientes):
    return_list = []
    contador_char_iguais = 0
    for i in range(0 , len(clientes)):
        for j in range(0, len(nome)):
            if(len(nome) <= len(clientes[i][0])):
                if(nome[j] == clientes[i][0][j]):
                    contador_char_iguais += 1
        if(contador_char_iguais == len(nome)):
            return_list.append(i)
        contador_char_iguais = 0
    return(return_list)

def buscap_sapato(pe, clientes):
    lista = []
    for x in range(0, len(clientes)):
        if clientes[x][1] == pe:
            lista.append(x)
    return lista


def buscap_codigo(codigo, clientes):
    lista = []
    for x in range(0, len(clientes)):
        if codigo in clientes[x][12]:
            lista.append(x)
    return lista


def define_maior_str(tamanhos):
    maior_tamanho = tamanhos[0]
    for x in range(1, len(tamanhos)):
        if maior_tamanho < tamanhos[x]:
            maior_tamanho = tamanhos[x]
    return maior_tamanho
