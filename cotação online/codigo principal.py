
# Código em manutenção.





import requests
import json
import time
import random
import tkinter as tk
from modular import cotar_dolar
from modular import cotar_euro
from modular import cotar_btc


# criar janela e estrutura e redimensiona
janela = tk.Tk()
janela.title('Cotação Online')
janela.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
janela.columnconfigure([0, 1, 2], weight=1)

# informações
info = tk.Label(text='COTAÇÃO ONLINE', bg='black', fg='#00FF00', width=5, height=1)
info.grid(row=0, column=0, columnspan=3, sticky='NSEW')
info2 = tk.Label(text='SELECIONE A MOEDA PARA COTAÇÃO:', bg='black', fg='white')
info2.grid(row=1, column=0, columnspan=3, sticky='NSEW')

# botões
dolar = tk.Button(text="DÓLAR", width=7, height=1, command=cotar_dolar).grid(row=2, column=0, sticky='nsew')
euro = tk.Button(text="EURO", width=7, height=1, command=cotar_euro).grid(row=2, column=1, sticky='NSEW')
btc = tk.Button(text='BITCOIN', width=7, height=1, command=cotar_btc).grid(row=2, column=2, sticky='NSEW')

# saídas de valor principal
valor = tk.Label(text='------', width=20, height=5).grid(row=3, column=0, columnspan=3)

# alta sub informação
alta = tk.Label(text='ALTA:', bg='black', fg='#00BFFF').grid(row=4, column=0, sticky='NSEW')
saidaAT = tk.Label(text='-----').grid(row=5, column=0)


# Baixa bud imformação
baixa = tk.Label(text='BAIXA:', bg='black', fg='red').grid(row=4, column=1, sticky='NSEW')
baixaB = tk.Label(text='-----').grid(row=5, column=1)

# Taxa de variação
taxa = tk.Label(text='VARIAÇÃO:', bg="black", fg='#FF00FF').grid(row=4, column=2, sticky='NSEW')
taxaT = tk.Label(text='-----').grid(row=5, column=2)


janela.mainloop()
