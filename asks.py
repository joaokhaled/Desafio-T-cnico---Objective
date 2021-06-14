from tkinter import messagebox, simpledialog
from tkinter import Toplevel

class Ask(Toplevel):
    def __init__(self) -> None:
        pass

    def firstA(self):
        global fword
        answer = messagebox.askyesno("Confirm","O prato que você pensou é massa?")
        if answer == True:
            fword = "Lasanha"
            self.secondA()
        else:
            fword = "Bolo de Chocolate"
            a = messagebox.askyesno("Confirm", f"O prato que você pensou é {fword}?")
            if a is not True:
                self.inputString()
            else:
                self.acertei()

    def secondA(self):
        global fword
        mb = messagebox.askyesno("Confirm", f"O prato que você pensou é {fword}?")
        if mb is not True:
            self.inputString()
        else:
            self.acertei()

    def inputString(self):
        global sd
        sd = simpledialog.askstring("Desisto", "Qual prato que você pensou?")
        if sd is not None:
            self.secondString()

    def secondString(self):
        simpledialog.askstring("Complete", f"{sd} é _______ mas {fword} não.")

    def acertei(self):
        messagebox.showinfo("Jogo Gourmet", "Acertei de novo!")


ad = Ask()