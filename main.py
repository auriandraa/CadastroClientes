#importa a biblioteca tkinter, que permite criar interfaces graficas 
import tkinter as tk
#importamos o modulo tkk (thamed widgets) do tkinter, que ofecere outros componentes com estilo mais moderno 
from tkinter import ttk

#cria a janela principal da palicação com a classe Tk()
janela = tk.Tk()

#titulo da janela, que vai apareer na barra de titulo
janela.title('Cadastro de clientes e serviços')

#define o tamanho da ajnela (largura x altura) em pixels 
janela.geometry('500x400')

#cria uma label (rótulo) para mostrar uma mensagem de boas vindas na janela 
label = tk.Label(janela, text='Sistema de Cadastro', font=("Arial", 14) )
# a função 'pack()' posiciona o rotulo na janela. o argumento 'pady=20' adiciona um espaço de 20 pixels entre o rotulo e o topo da janela 
label.pack(pady=20)

#cria um botão para cadastrar um novo cliente 
botao_sair = ttk.Button(janela, text="Sair", command=janela.quit)
#a função 'pack()' posiciona o botão na janela. o botão será exibido na parte inferior da janela 
botao_sair.pack()

#inicia o loop da interface grafica. esse loop mantem a janela aberta e permite interação com os componentes 
#a janela só sera fecgada quando o usuário cliclar no botão 'sair' ou fechar a janela de forma manual.]

janela.mainloop()   