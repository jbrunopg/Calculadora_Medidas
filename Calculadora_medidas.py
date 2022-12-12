#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import ttk


# In[6]:


# cores
cor1 = '#3b3b3b' # preto



# In[9]:


janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=cor1)

# frame janelas

frame_cima = Frame(janela, width=450, height=50, bg='red', pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerdo = Frame(janela, width=450, height=220, bg='green', pady=0, padx=3, relief='flat')
frame_esquerdo.place(x=2, y=54)

frame_direita = Frame(janela, width=198, height=260, bg='white', pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)






janela.mainloop()


# In[ ]:




