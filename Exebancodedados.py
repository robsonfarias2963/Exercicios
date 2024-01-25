import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir o modelo de dados
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Conectar ao banco de dados SQLite
engine = create_engine('sqlite:///exemplo.db', echo=True)
Base.metadata.create_all(engine)

# Criar uma sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Função para adicionar um usuário ao banco de dados
def adicionar_usuario(nome, idade):
    novo_usuario = Usuario(nome=nome, idade=idade)
    session.add(novo_usuario)
    session.commit()

# Função para exibir todos os usuários na interface gráfica
def exibir_usuarios():
    resultados = session.query(Usuario).all()
    for usuario in resultados:
        tree.insert('', 'end', values=(usuario.id, usuario.nome, usuario.idade))

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Usuários")

# Criar uma árvore para exibir os usuários
tree = ttk.Treeview(root, columns=('ID', 'Nome', 'Idade'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Nome', text='Nome')
tree.heading('Idade', text='Idade')
tree.pack()

# Botão para adicionar um usuário
btn_adicionar = tk.Button(root, text="Adicionar Usuário", command=lambda: adicionar_usuario("Exemplo", 25))
btn_adicionar.pack()

# Botão para exibir usuários
btn_exibir = tk.Button(root, text="Exibir Usuários", command=exibir_usuarios)
btn_exibir.pack()

# Iniciar o loop principal
root.mainloop()
