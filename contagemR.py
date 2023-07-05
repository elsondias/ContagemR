import tkinter as tk
import time


def iniciar_contagem(event=None):
    tempo = int(tempo_entry.get())

    minutos = tempo // 60
    segundos = tempo % 60
    horas = minutos // 60
    minutos = minutos % 60

    while tempo > 0:
        tempo_label.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
        tempo -= 1
        segundos -= 1
        if segundos < 0:
            minutos -= 1
            segundos = 59
        if minutos < 0:
            horas -= 1
            minutos = 59
        root.update()
        time.sleep(1)

    tempo_label.config(text="Tempo esgotado!")


root = tk.Tk()
root.title("Contagem Regressiva")

instrucao_label = tk.Label(root, text="Coloque algum número para começar: ", font=("Helvetica", 16))
instrucao_label.pack(pady=10)

tempo_label = tk.Label(root, font=("Helvetica", 15))
tempo_label.pack(pady=15)

tempo_entry = tk.Entry(root, font=("Helvetica", 14))
tempo_entry.pack(pady=10)
tempo_entry.bind("<Return>", iniciar_contagem)

iniciar_button = tk.Button(root, text="Iniciar", font=("Helvetica", 14), command=iniciar_contagem)
iniciar_button.pack(pady=8)

root.mainloop()
