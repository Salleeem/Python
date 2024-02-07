import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Você clicou no botão!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Interface Gráfica")

# Criando um rótulo
rotulo = tk.Label(janela, text="Olá, mundo!")
rotulo.pack()

# Criando um botão
botao = tk.Button(janela, text="Clique Aqui", command=mostrar_mensagem)
botao.pack()

# Rodando o loop principal da aplicação
janela.mainloop()
