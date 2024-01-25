import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class App():
    def __init__(self, toplevel):
        self.raiz = toplevel
        self.raiz.title('AquaPython App')
        # define tamanho da janela
        self.raiz.geometry("300x300")


        # impede redimensionar a janela
        self.raiz.resizable(False, False)

    def create_widgets(self) :
        pass


def calcular_caixa_dagua_necessaria(self,
    volume_necessario):


    dimensoes = [300, 500,1000,1500,2000,3000,5000]
    for dimensao in dimensoes:
        if dimensao > volume_necessario:
            return dimensao

def calcular_volume_necessario(self, consumo_per_capita,
numero_de_pessoas):


    volume = consumo_per_capita*numero_de_pessoas*1.2
    return volume
def obter_resultados(self):
    consumo_per_capita = float(self.consumo_entry.get())
    numero_de_pessoas = int(self.n_pessoas_entry.get())
    volume = self.calcular_volume_necessario(consumo_per_capita,numero_de_pessoas)

    caixa = self.calcular_caixa_dagua_necessaria(volume)
    msg = f"Consumo diário {volume}L"
    msg += f"\nUtilizar caixa d'água de {caixa}L"
    messagebox.showinfo("Caixa d'água", msg)
def create_widgets(self):
# Cria os frames
    self.frame1 = tk.Frame(self.raiz)
    self.frame1.pack(fill=tk.BOTH)
    self.frame2 = tk.Frame(self.raiz)
    self.frame2.pack(fill=tk.BOTH, padx=10, pady=5)
    self.frame3 = tk.Frame(self.raiz)
    self.frame3.pack(fill=tk.BOTH, padx=10, pady=5)
    self.frame4 = tk.Frame(self.raiz)
    self.frame4.pack(fill=tk.BOTH, padx=10, pady=5)
    self.img = ImageTk.PhotoImage(Image.open("caixa_3d.png"))
    self.panel = ttk.Label(self.frame1, image = self.img)
    self.panel.pack(side=tk.LEFT)



# Consumo
    self.consumo_label = ttk.Label(self.frame2,
    text="Consumo per capita (L/dia):")
    self.consumo_label.pack(side=tk.LEFT)
    self.consumo_entry = ttk.Entry(self.frame2, width=11)
    self.consumo_entry.pack(side=tk.RIGHT)
# Numero de pessoas
    self.n_pessoas_label = ttk.Label(self.frame3,
    text="No de pessoas:")
    self.n_pessoas_label.pack(side=tk.LEFT)
    self.n_pessoas_entry = ttk.Entry(self.frame3, width=11)
    self.n_pessoas_entry.pack(side=tk.RIGHT)
# login button
    button = ttk.Button(self.frame4, text="Calcular",
    command=self.obter_resultados)

    button.pack(side=tk.RIGHT)
if __name__ == '__main__':
    raiz = tk.Tk()
    app = App(raiz)
    app.create_widgets()
    raiz.mainloop()