import tkinter as tk
from tkinter import messagebox

def fazer_login():

    usuario = entry_usuario.get()
    senha = entry_senha.get()

   
    if usuario == "admin" and senha == "admin123":
        messagebox.showinfo("Login", "Login bem sucedido!")
       
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos")

# Criar janela
janela = tk.Tk()
janela.title("Tela de Login")

# Criar rótulos e campos de entrada
label_usuario = tk.Label(janela, text="Nome de Usuário:")
label_usuario.pack()
entry_usuario = tk.Entry(janela)
entry_usuario.pack()

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(janela, show="*")  # O texto da senha será ocultado
entry_senha.pack()

# Botão de login
botao_login = tk.Button(janela, text="Login", command=fazer_login)
botao_login.pack()

# Executar a janela principal
janela.mainloop() 