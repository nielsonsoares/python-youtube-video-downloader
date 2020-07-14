from pytube import YouTube
from tkinter import *

root = Tk()
larguraJanela = 400
alturaJanela = 150

posicaoDireita = int(root.winfo_screenwidth()/2 - larguraJanela/2)
posicaoAbaixo = int(root.winfo_screenheight()/2 - alturaJanela/2)

root.geometry("{}x{}+{}+{}".format(larguraJanela, alturaJanela, posicaoDireita, posicaoAbaixo))

root.title("Baixar Videos do YouTube")

myVar = StringVar()
myVar.set("Entre com a url abaixo:")
link = StringVar()

def baixar():
    try:
        myVar.set("Baixando...")
        root.update()
        YouTube(link.get()).streams.first().download();
        link.set("Video baixado com sucesso!")
    except Exception as e:
        myVar.set("Error")
        root.update()
        link.set("Entre com o link correto")

#Label(root).pack()

Label(root, textvariable=myVar, width=40, font="Consolas 15 bold").pack(pady=10)

Entry(root, textvariable=link, width=40).pack(pady=10)

Button(root, text="Baixar Video", command=baixar).pack()

root.mainloop()