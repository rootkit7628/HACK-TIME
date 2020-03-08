from tkinter.filedialog import *
import decrypt

class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('HACK TIME')
        self.root.geometry('1000x600+180+80')
        self.root.resizable(width=FALSE,height=FALSE)

    def corps(self):
        self.image = PhotoImage(file='image/background.png')
        self.background = Label(self.root, image = self.image ).place(relx =0 , rely =0)

        self.login_user = StringVar()
        self.login_input = Entry(self.root, textvariable=self.login_user, bg='white').place(relx=0.1243, rely=0.120,width=273,height=44)
        
        self.psd_user = StringVar()
        self.psd_input = Entry(self.root, textvariable=self.psd_user, bg='white').place(relx=0.1243, rely=0.237, width=273, height=44)

        self.sradio_var = StringVar()
        self.choix1 = Radiobutton(self.root, font=("Helvetica", 15), variable=self.sradio_var, value=decrypt.principale.psd_login_Nbr, text='Nom et Nombre ajouté', bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0).place(relx=0.06, rely=0.35)
        self.choix2 = Radiobutton(self.root, font=("Helvetica", 15), variable=self.sradio_var, value=decrypt.principale.psd_liste_Nbr, text='Liste de mots      et Nombres Ajoutés', bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0).place(relx=0.06, rely=0.40)
        self.choix3 = Radiobutton(self.root, font=("Helvetica", 15), variable=self.sradio_var, value=decrypt.principale.psd_login_voyelle, text='Changement voyelle / minuscule', bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0).place(relx=0.06, rely=0.45)
        self.choix4 = Radiobutton(self.root, font=("Helvetica", 15), variable=self.sradio_var, value=decrypt.principale.psd_2xliste, text='Liste de mots doublées', bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0).place(relx=0.06, rely=0.50)
        self.choix5 = Radiobutton(self.root, font=("Helvetica", 15), variable=self.sradio_var, value=decrypt.principale.psd_liste_reversex2, text='Liste de mots envers/doublées', bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0).place(relx=0.06, rely=0.55)

        self.file_name=StringVar

        self.file_list = PhotoImage(file='image/fichier.png')
        self.recupfichier_btn = Button(self.root, image=self.file_list, bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0,command=lambda:self.recupfichier("txt")).place(relx=0.22, rely=0.405)

        self.file_list1 = PhotoImage(file='image/fichier.png')
        self.recupfichier_btn1 = Button(self.root, image=self.file_list1, bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0,command=lambda:self.recupfichier("txt")).place(relx=0.31, rely=0.503)

        self.file_list2 = PhotoImage(file='image/fichier.png')
        self.recupfichier_btn2 = Button(self.root, image=self.file_list2, bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0,command=lambda:self.recupfichier("txt")).place(relx=0.375, rely=0.556)

        #Afficher la reponse
        self.reponse = Label(self.root, text='', bg="#0e73bb", font=("Arial", 12))
        self.reponse.place(relx=0.5, rely=0.65)

        self.search_psd = PhotoImage(file='image/search.png')
        self.search_btn = Button(self.root, image=self.search_psd, bg='#0e73bb', overrelief="flat", borderwidth='0c', activebackground='#0e73bb', highlightthickness=0,command=self.search).place(relx=0.1, rely=0.65)


    def recupfichier(self, extension):
        self.file_name=askopenfilename(filetypes=[(f".{extension}", f"*.{extension}")])

    def finale(self):
        self.root.mainloop()

    def search(self):
        print(self.file_name, type(self.file_name))
        a = decrypt.principale(self.login_user.get(),self.psd_user.get(),self.file_name)
        a1 = a.psd_2xliste()
        a2 = a.psd_Alogin_born()
        a3 = a.psd_list()
        a4 = a.psd_liste_Nbr()
        a5 = a.psd_liste_reversex2()
        a6 = a.psd_login_voyelle()
        a7 = a.psd_login_Nbr()
        psd_lista = [a1, a2, a3, a4, a5, a6, a7]

        for i in psd_lista:
            if i is not None:
                self.reponse.config(text="PASSWORD : "+i)
                self.reponse.update()

if __name__ == "__main__":
    fen = Interface()
    fen.corps()
    fen.finale()
