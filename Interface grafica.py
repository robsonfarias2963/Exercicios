from tkinter import *
def mostrar_texto():
    valor = entrada.get()
    labelsaida['text'] = valor
janela = Tk()
janela.title("Aplicação em Tkinter")
janela.geometry("300x70")

frame = Frame(master=janela)
frame.pack()

labelentrada = Label(master=frame, text="Digite um número:")
labelentrada.grid(row=0, column=0)

entrada=Entry(master=frame,width=10)
entrada.grid(row=0, column=1)
botao = Button(master=frame, text="Mostrar",command=mostrar_texto)
botao.grid(row=1, column=0)

labelsaida = Label(master=frame)
labelsaida.grid(row=2, column=0)

janela.mainloop()