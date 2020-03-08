
from tkinter import *
import interphace2 as ia
import os

class Demarage():
    def __init__(self):
        self.root = Tk()
        self.root.title('IHM')
        self.root.geometry('1366x768+500+500')


    def corps(self):
        self.image = PhotoImage(file='image/index.png')
        self.background = Label(self.root, image = self.image ).place(relx =0 , rely =0)

        self.title = PhotoImage(file='image/title.png')
        self.title_image = Label(self.root, image = self.title, bg='black' ).place(relx =0.10 , rely =0.2)

        self.play = PhotoImage(file="image/play.png")
        self.play_bton = Button(self.root, image=self.play, bg='black', overrelief="flat", borderwidth='0c', activebackground='black', highlightthickness=0,command=self.affiche).place(relx=0.218, rely=0.35)



    def finale(self):
        self.root.mainloop()

    def affiche(self):
        self.root.destroy()
        os.system("python3 interphace2.py")

if __name__ =='__main__':
    fen = Demarage()
    fen.corps()
    fen.finale()
