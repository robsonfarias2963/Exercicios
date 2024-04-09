from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Barra de navegação
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Botao voltar
        voltar_btn = QAction('<-', self)
        voltar_btn.triggered.connect(self.browser.back)
        navbar.addAction(voltar_btn)

        # Botao refresh
        refresh_btn = QAction('Recarregar', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

app = QApplication(sys.argv)
QApplication.setApplicationName('Novo_browser')
windows = MainWindow()

app.exec_()
