import tkinter as tk
from collections import Counter
import string

class AnalisadorTexto(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analisador de Texto")
        self.geometry("400x300")

        # Interface
        self.label_instrucao = tk.Label(self, text="Digite o texto abaixo:")
        self.label_instrucao.pack(pady=10)

        self.texto_input = tk.Text(self, wrap=tk.WORD, width=40, height=10)
        self.texto_input.pack(pady=10)

        self.button_analisar = tk.Button(self, text="Analisar Texto", command=self.analisar_texto)
        self.button_analisar.pack(pady=10)

        # Resultados
        self.label_resultados = tk.Label(self, text="")
        self.label_resultados.pack(pady=10)

    def analisar_texto(self):
        texto = self.texto_input.get("1.0", tk.END).strip()

        # Número de palavras
        num_palavras = len(texto.split())

        # Número de caracteres (sem contar espaços em branco)
        num_caracteres = len(texto.replace(" ", "").replace("\n", ""))

        # Frequência de palavras
        palavras = [palavra.strip(string.punctuation).lower() for palavra in texto.split()]
        contagem_palavras = Counter(palavras)

        # Exibir resultados
        resultados = (
            f"Número de Palavras: {num_palavras}\n"
            f"Número de Caracteres: {num_caracteres}\n"
            "\nFrequência de Palavras:\n"
        )

        for palavra, frequencia in contagem_palavras.items():
            resultados += f"{palavra}: {frequencia}\n"

        self.label_resultados["text"] = resultados

if __name__ == "__main__":
    app = AnalisadorTexto()
    app.mainloop()
