import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from pywin.Demos import toolbar


class MainWindow(QMainWindow):
    def __init__(self,button_action1=None):
        super().__init__()

        self.setWindowTitle("Meu Primeiro Programa")


        button_action = QAction(QIcon("bug.png"), "&Nova", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)


        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_submenu=file_menu.addMenu("Adicionar")
        file_submenu=file_menu.addMenu("Inserir")
        file_menu.addAction(button_action)
        file_menu.addSeparator()


       ## button_action.triggered.connect(self.onMyToolBarButtonClick)
       ## button_action.setCheckable(True)



        file_menu =menu.addMenu("&Edit")
        file_submenu=file_menu.addMenu("Coletar")
        file_submenu=file_menu.addMenu("Novos Dados")
        file_menu.addAction(button_action)
        file_menu.addSeparator()


        file_menu = menu.addMenu("&View")
        file_submenu=file_menu.addMenu("Ajustar")
        file_menu.addAction(button_action)
        file_menu.addSeparator()


    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()