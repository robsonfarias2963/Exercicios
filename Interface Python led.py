import pyfirmata
from tkinter import *
# Especifique a Porta Serial onde o Arduino
# está conectado, por exemplo, COM3

PORTA = 'especificar_porta_serial'
arduino = pyfirmata.Arduino(PORTA)
arduino.digital[13].mode = pyfirmata.OUTPUT

def controle(valor):
   arduino.digital[13].write(valor)

janela = Tk()
janela.title("Acender e apagar LED com botão")
janela.geometry("350x60")

frame = Frame(master=janela)
frame.pack()

botaoacende = Button(master=frame, text="Acender",command=lambda:controle(1))
botaoacende.grid(row=0, column=0)
botaoapaga = Button(master=frame, text="Apagar",command=lambda:controle(0))
botaoapaga.grid(row=0, column=1)

janela.mainloop()