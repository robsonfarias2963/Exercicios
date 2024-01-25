import tkinter as tk


def exibir_tabuada() :
    valor=int(entry.get())
    resultado.config(state=tk.NORMAL)
    resultado.delete(1.0,tk.END)

    if valor < 0 :
        resultado.insert(tk.END,"Por favor, insira um valor positivo.")
    else :
        resultado.insert(tk.END,'-'*30+'\n')
        for c in range(1,11) :
            resultado.insert(tk.END,f'{valor} x {c} = {valor*c}\n')
        resultado.insert(tk.END,'-'*30+'\n')

    resultado.config(state=tk.DISABLED)


app=tk.Tk()
app.title("Tabuada")

label=tk.Label(app,text="Quer ver a tabuada de qual valor:")
label.pack(pady=10)

entry=tk.Entry(app)
entry.pack(pady=10)

botao=tk.Button(app,text="Exibir Tabuada",command=exibir_tabuada)
botao.pack(pady=10)

resultado=tk.Text(app,height=10,width=40,state=tk.DISABLED)
resultado.pack(pady=10)

app.mainloop()
