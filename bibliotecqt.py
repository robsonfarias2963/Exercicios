import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser

class TabuadaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tabuada App')

        # Widgets
        self.label = QLabel('Quer ver a tabuada de qual valor:')
        self.input_box = QLineEdit()
        self.result_browser = QTextBrowser()
        self.calc_button = QPushButton('Calcular Tabuada')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_browser)
        self.setLayout(layout)

        # Connect Signals
        self.calc_button.clicked.connect(self.calcular_tabuada)

    def calcular_tabuada(self):
        try:
            valor = int(self.input_box.text())
            if valor < 0:
                self.result_browser.setPlainText("Por favor, insira um valor positivo.")
            else:
                resultado = '-' * 30 + '\n'
                for c in range(1, 11):
                    resultado += f'{valor} x {c} = {valor * c}\n'
                resultado += '-' * 30
                self.result_browser.setPlainText(resultado)

        except ValueError:
            self.result_browser.setPlainText("Por favor, insira um valor válido.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabuadaApp()
    window.show()
    sys.exit(app.exec_())
