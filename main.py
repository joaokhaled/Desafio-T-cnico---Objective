from tkinter import Tk, Toplevel
from tkinter.ttk import Button, Label
from asks import Ask

g = Ask()

class Jogo(Toplevel):
    def __init__(self, master=None) -> None:
        self.master = master
        master.geometry("285x130")
        master.title("Jogo Gourmet")

        self.b = Label(master, text="Pense em um prato que gosta", font=("Arial", "9", "bold"))
        self.b.pack(pady=20)
        self.botaook = Button(master, text="OK", command=g.firstA)
        self.botaook.pack()


if __name__ == "__main__":
    raiz = Tk()
    main = Jogo(raiz)
    raiz.mainloop()