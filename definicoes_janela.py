import os
from tkinter import Tk, Button, Label, Entry, PhotoImage, CENTER
import pickle
db = "database.txt"

def define_icon(a: object, icon) -> object:
    img_icon = PhotoImage(file=os.path.join(icon))
    a.tk.call('wm', 'iconphoto', a._w, img_icon)


def define_tam_janela(janela: object, size):
    janela.geometry(size)


def define_janela(janela: object, icone, title, size, bg_color):
    Tk.__init__(janela)
    janela.geometry(size)
    janela.title(title)
    janela["bg"] = bg_color
    define_icon(janela, icone)


def salva(lista):
    with open("./"+ db, "wb") as file:
        pickle.dump(lista, file)
        file.close()



def carrega():
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


def define_maior_str(tamanhos):
    maior_tamanho = tamanhos[0]
    for x in range(1, len(tamanhos)):
        if maior_tamanho < tamanhos[x]:
            maior_tamanho = tamanhos[x]
    return maior_tamanho
