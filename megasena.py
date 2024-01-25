import tkinter as tk
from random import sample

class SimuladorMegaSena(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador da Mega Sena")
        self.geometry("400x300")

        # Números sorteados
        self.numeros_sorteados = []

        # Interface
        self.label_resultado = tk.Label(self, text="", font=('Arial', 16))
        self.label_resultado.pack(pady=20)

        self.button_sortear = tk.Button(self, text="Sortear Números", command=self.sortear_numeros)
        self.button_sortear.pack()

    def sortear_numeros(self):
        # Simula o sorteio de 6 números entre 1 e 60
        self.numeros_sorteados = sorted(sample(range(1, 61), 6))
        resultado = f"Números Sorteados: {', '.join(map(str, self.numeros_sorteados))}"
        self.label_resultado["text"] = resultado

if __name__ == "__main__":
    app = SimuladorMegaSena()
    app.mainloop()
