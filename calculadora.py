import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")

        # Variável para armazenar a expressão
        self.expressao = ""

        # Criação da tela
        self.tela = tk.Entry(self, font=('Arial', 24), justify="right")
        self.tela.grid(row=0, column=0, columnspan=4)

        # Botões
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (texto, linha, coluna) in botoes:
            tk.Button(self, text=texto, font=('Arial', 18), command=lambda t=texto: self.clique(t)).grid(row=linha, column=coluna)

    def clique(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.expressao)
                self.expressao = str(resultado)
            except Exception as e:
                self.expressao = "Erro"
        elif valor == 'C':
            self.expressao = ""
        else:
            self.expressao += valor

        self.atualizar_tela()

    def atualizar_tela(self):
        self.tela.delete(0, tk.END)
        self.tela.insert(0, self.expressao)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
