#importa a biblioteca tkinter, que permite criar interfaces graficas 
import tkinter as tk
#importamos o modulo tkk (thamed widgets) do tkinter, que ofecere outros componentes com estilo mais moderno 
from tkinter import ttk

import sqlite3

#função para criar clientes no banco de dados 

def salvar_cliente():
    nome = entry_nome.get()
    whatsapp = entry_whatsapp.get()
    endereco = entry_endereco.get()
    print('Cliente salvo com sucesso!')

    if nome and whatsapp and endereco:  # Corrigir 'whatstapp' para 'whatsapp'
        conexao = sqlite3.connect("cadastros.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO clientes (nome, whatsapp, endereco) VALUES (?,?,?)", (nome, whatsapp, endereco))    
        conexao.commit()
        conexao.close()
        atualizar_tabela()
        entry_nome.delete(0, tk.END)
        entry_whatsapp.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
#funçao para carregar os clientes na tabela 
def atualizar_tabela():
    for row in tabela.get_children():
        tabela.delete(row)
    
    conexao = sqlite3.connect("cadastros.db") 
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    for row in cursor.fetchall():
        tabela.insert("","end", values=row)
    conexao.close() 


#cria a janela principal da palicação com a classe Tk()
janela = tk.Tk()

#titulo da janela, que vai apareer na barra de titulo
janela.title('Cadastro de clientes e serviços')

#define o tamanho da ajnela (largura x altura) em pixels 
janela.geometry('500x400')

#labels e entradas
tk.Label(janela,text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela,text="Whatsapp:").grid(row=1, column=0, padx=10, pady=5)
entry_whatsapp = tk.Entry(janela, width=40)
entry_whatsapp.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Endereço:").grid(row=2, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(janela, width=40)
entry_endereco.grid(row=2, column=1, padx=10, pady=5)

# **Botão para salvar**
botao_salvar = tk.Button(janela, text="Salvar Cliente", command=salvar_cliente, bg="green", fg="white")
botao_salvar.grid(row=3, column=1, padx=10, pady=10)

# **Tabela de Clientes**
colunas = ("ID", "Nome", "Whatsapp", "Endereço")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=120)

tabela.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Carregar clientes ao abrir o programa
atualizar_tabela()

# Rodar a interface gráfica
janela.mainloop()   