import tkinter as tk
import os
import definicoes_janela

numeroClientes = len(definicoes_janela.carregaListaClientes())
icon = "./assets/gaynor.ico"

janela = tk.Tk()
janela.title("Conta Clientes")  
janela.geometry("250x50")
janela["bg"] = "#fecdd0"
#setting icon
img_icon = tk.PhotoImage(file=os.path.join(icon))
janela.tk.call('wm', 'iconphoto', janela._w, img_icon)

#button
btSair = tk.Button(text="Sair", bg="#FFF", relief="flat")
btSair["command"] = janela.destroy

#label
lblNumeroClietntes = tk.Label(text="Número de clientes:  "+str(numeroClientes), bg="#FFF", font=("Roboto", 12))

#placing
lblNumeroClietntes.place(y=12,x=7)
btSair.place(y=12, x=200)

janela.mainloop()
