import requests
import json
import time
import random
import tkinter as tk


def cotar_dolar():
    sort = 'USD-BRL'
    cotar = requests.get(f'https://economia.awesomeapi.com.br/last/{sort}')
    resultado = cotar.json()
    mod = sort.replace('-', "")
    valor = resultado[f'{mod}']['bid']
    alta = resultado[f'{mod}']['high']
    baixa = resultado[f'{mod}']['low']
    taxa = resultado[f'{mod}']['pctChange']

    saida_v = tk.Label(text=valor, width=20, height=5, bg='black', fg='white', font=45)
    saida_v.grid(row=3, column=0, columnspan=3, sticky='NSEW')
    saidas_t = tk.Label(text=taxa, bg='black', fg='white').grid(row=5, column=2, sticky='NSEW')
    saida_b = tk.Label(text=baixa, bg='black', fg='white').grid(row=5, column=1, sticky='NSEW')
    saida_a = tk.Label(text=alta, bg='black', fg='white').grid(row=5, column=0, sticky='NSEW')


def cotar_euro():
    sort = 'EUR-BRL'
    cotar = requests.get(f'https://economia.awesomeapi.com.br/last/{sort}')
    resultado = cotar.json()
    mod = sort.replace('-', "")
    valor = resultado[f'{mod}']['bid']
    alta = resultado[f'{mod}']['high']
    baixa = resultado[f'{mod}']['low']
    taxa = resultado[f'{mod}']['pctChange']

    saida_v = tk.Label(text=valor, width=20, height=5, bg='black', fg='white', font=45)
    saida_v.grid(row=3, column=0, columnspan=3, sticky='NSEW')
    saidas_t = tk.Label(text=taxa, bg='black', fg='white').grid(row=5, column=2, sticky='NSEW')
    saida_b = tk.Label(text=baixa, bg='black', fg='white').grid(row=5, column=1, sticky='NSEW')
    saida_a = tk.Label(text=alta, bg='black', fg='white').grid(row=5, column=0, sticky='NSEW')


def cotar_btc():
    sort = 'BTC-BRL'
    cotar = requests.get(f'https://economia.awesomeapi.com.br/last/{sort}')
    resultado = cotar.json()
    mod = sort.replace('-', "")
    valor = resultado[f'{mod}']['bid']
    alta = resultado[f'{mod}']['high']
    baixa = resultado[f'{mod}']['low']
    taxa = resultado[f'{mod}']['pctChange']

    saida_v = tk.Label(text=valor, width=20, height=5, bg='black', fg='white', font=45)
    saida_v.grid(row=3, column=0, columnspan=3, sticky='NSEW')
    saidas_t = tk.Label(text=taxa, bg='black', fg='white').grid(row=5, column=2, sticky='NSEW')
    saida_b = tk.Label(text=baixa, bg='black', fg='white').grid(row=5, column=1, sticky='NSEW')
    saida_a = tk.Label(text=alta, bg='black', fg='white').grid(row=5, column=0, sticky='NSEW')
