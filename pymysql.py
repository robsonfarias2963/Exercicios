import tkinter as tk
from tkinter import messagebox
import pymysql

class ProgramaMySQLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Programa com PyMySQL")

        # Layout da interface gráfica
        self.label_instrucao = tk.Label(root, text="Insira as informações de conexão com o banco de dados:")
        self.label_instrucao.pack(pady=10)

        self.label_host = tk.Label(root, text="Host:")
        self.label_host.pack(pady=5)
        self.entry_host = tk.Entry(root)
        self.entry_host.pack(pady=5)

        self.label_usuario = tk.Label(root, text="Usuário:")
        self.label_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack(pady=5)

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack(pady=5)

        self.label_banco = tk.Label(root, text="Banco de Dados:")
        self.label_banco.pack(pady=5)
        self.entry_banco = tk.Entry(root)
        self.entry_banco.pack(pady=5)

        self.botao_conectar = tk.Button(root, text="Conectar ao Banco de Dados", command=self.conectar_banco_dados)
        self.botao_conectar.pack(pady=10)

        self.texto_resultado = tk.Text(root, height=10, width=50)
        self.texto_resultado.pack(pady=10)

    def conectar_banco_dados(self):
        try:
            # Obter informações de conexão do usuário
            host = self.entry_host.get()
            usuario = self.entry_usuario.get()
            senha = self.entry_senha.get()
            banco_dados = self.entry_banco.get()

            # Conectar ao banco de dados
            conexao = pymysql.connect(host=host, user=usuario, password=senha, db=banco_dados)
            cursor = conexao.cursor()

            # Executar uma consulta simples
            consulta = "SELECT * FROM exemplo"
            cursor.execute(consulta)

            # Obter os resultados e exibi-los na interface gráfica
            resultados = cursor.fetchall()
            self.texto_resultado.delete("1.0", tk.END)  # Limpar o texto anterior
            for resultado in resultados:
                self.texto_resultado.insert(tk.END, f"{resultado}\n")

            # Fechar a conexão com o banco de dados
            cursor.close()
            conexao.close()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro na conexão ao banco de dados: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramaMySQLApp(root)
    root.mainloop()
