import tkinter as tk
from tkinter import ttk
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('financas.db')
cursor = conn.cursor()

# Criar a tabela de contas se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data_vencimento DATE NOT NULL,
        status TEXT
    )
''')
conn.commit()

# Função para adicionar uma conta ao banco de dados
def adicionar_conta(descricao, valor, data_vencimento, status):
    cursor.execute('INSERT INTO contas (descricao, valor, data_vencimento, status) VALUES (?, ?, ?, ?)',
                   (descricao, valor, data_vencimento, status))
    conn.commit()
    exibir_contas()

# Função para excluir uma conta do banco de dados
def excluir_conta():
    item_selecionado = tree.selection()
    if item_selecionado:
        conta_id = tree.item(item_selecionado)['values'][0]
        cursor.execute('DELETE FROM contas WHERE id = ?', (conta_id,))
        conn.commit()
        exibir_contas()

# Função para exibir todas as contas na interface gráfica
def exibir_contas():
    for item in tree.get_children():
        tree.delete(item)
    resultados = cursor.execute('SELECT * FROM contas').fetchall()
    for conta in resultados:
        tree.insert('', 'end', values=(conta[0], conta[1], conta[2], conta[3], conta[4]))

# Criar a janela principal
root = tk.Tk()
root.title("Gerenciador de Finanças")

# Criar uma árvore para exibir as contas
tree = ttk.Treeview(root, columns=('ID', 'Descrição', 'Valor', 'Data de Vencimento', 'Status'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Descrição', text='Descrição')
tree.heading('Valor', text='Valor')
tree.heading('Data de Vencimento', text='Data de Vencimento')
tree.heading('Status', text='Status')
tree.pack()

# Entradas de texto para adicionar conta
entrada_descricao = tk.Entry(root)
entrada_descricao.pack()

entrada_valor = tk.Entry(root)
entrada_valor.pack()

entrada_data_vencimento = tk.Entry(root)
entrada_data_vencimento.pack()

entrada_status = tk.Entry(root)
entrada_status.pack()

# Botão para adicionar uma conta
btn_adicionar = tk.Button(root, text="Adicionar Conta", command=lambda: adicionar_conta(
    entrada_descricao.get(),
    float(entrada_valor.get()),
    entrada_data_vencimento.get(),
    entrada_status.get()
))
btn_adicionar.pack()

# Botão para excluir uma conta
btn_excluir = tk.Button(root, text="Excluir Conta", command=excluir_conta)
btn_excluir.pack()

# Botão para exibir contas
btn_exibir = tk.Button(root, text="Exibir Contas", command=exibir_contas)
btn_exibir.pack()

# Iniciar o loop principal
root.mainloop()

# Fechar a conexão com o banco de dados quando o programa encerrar
conn.close()
