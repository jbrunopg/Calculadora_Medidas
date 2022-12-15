from tkinter import *
from tkinter import ttk

# cores
cor1 = '#3b3b3b' # preto
cor2 = '#ffffff' # branco

janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=cor1)

# frame janelas

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerdo = Frame(janela, width=450, height=220, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerdo.place(x=2, y=54)

frame_direita = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)

# estilo janelas

estilo = ttk.Style(janela)
estilo.theme_use("clam")




janela.mainloop()
