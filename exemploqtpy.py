import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

class CadastroPesoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Inicialize o banco de dados
        self.conexao = sqlite3.connect('dados_peso.db')
        self.criarTabela()

        # Chame o método para configurar a interface gráfica
        self.initUI()

    def initUI(self):
        # Crie widgets
        self.nome_label = QLabel('Nome:')
        self.nome_input = QLineEdit()
        self.peso_label = QLabel('Peso:')
        self.peso_input = QLineEdit()

        # Crie botões
        self.adicionar_button = QPushButton('Adicionar Dados')
        self.consultar_button = QPushButton('Consultar Dados')
        self.mostrar_button = QPushButton('Mostrar Dados')
        self.excluir_button = QPushButton('Excluir Dados')

        # Conecte os sinais aos slots (métodos)
        self.adicionar_button.clicked.connect(self.adicionarDados)
        self.consultar_button.clicked.connect(self.consultarDados)
        self.mostrar_button.clicked.connect(self.mostrarDados)
        self.excluir_button.clicked.connect(self.excluirDados)

        # Crie uma tabela para mostrar dados
        self.tabela = QTableWidget(self)
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(['Nome', 'Peso'])

        # Crie um layout vertical
        layout = QVBoxLayout()

        # Adicione widgets ao layout
        layout.addWidget(self.nome_label)
        layout.addWidget(self.nome_input)
        layout.addWidget(self.peso_label)
        layout.addWidget(self.peso_input)
        layout.addWidget(self.adicionar_button)
        layout.addWidget(self.consultar_button)
        layout.addWidget(self.mostrar_button)
        layout.addWidget(self.excluir_button)
        layout.addWidget(self.tabela)

        # Defina o layout do widget principal
        self.setLayout(layout)

        # Configure o tamanho e o título da janela
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Cadastro de Peso')

        # Exiba a janela
        self.show()

    def criarTabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados_peso (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                peso REAL
            )
        ''')
        self.conexao.commit()

    def adicionarDados(self):
        nome = self.nome_input.text()
        peso = float(self.peso_input.text())

        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO dados_peso (nome, peso) VALUES (?, ?)', (nome, peso))
        self.conexao.commit()

    def consultarDados(self):
        nome = self.nome_input.text()

        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM dados_peso WHERE nome = ?', (nome,))
        dados = cursor.fetchone()

        if dados:
            self.nome_input.setText(dados[1])
            self.peso_input.setText(str(dados[2]))
        else:
            self.nome_input.clear()
            self.peso_input.clear()

    def mostrarDados(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM dados_peso')
        dados = cursor.fetchall()

        self.tabela.setRowCount(0)

        for row, dado in enumerate(dados):
            self.tabela.insertRow(row)
            self.tabela.setItem(row, 0, QTableWidgetItem(dado[1]))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(dado[2])))

    def excluirDados(self):
        nome = self.nome_input.text()

        cursor = self.conexao.cursor()
        cursor.execute('DELETE FROM dados_peso WHERE nome = ?', (nome,))
        self.conexao.commit()

def main():
    app = QApplication(sys.argv)
    window = CadastroPesoApp()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
