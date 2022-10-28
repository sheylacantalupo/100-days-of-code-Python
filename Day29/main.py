import math
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip as pyperclip


def gerador_senha():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letras_senha = [choice(letters) for _ in range(randint(8, 10))]
    simbolos_senha = [choice(symbols) for _ in range(randint(2, 4))]
    numeros_senha = [choice(numbers) for _ in range(randint(2, 4))]

    senha_lista = letras_senha + simbolos_senha + numeros_senha
    shuffle(senha_lista)

    senha = "".join(senha_lista)

    senha_entry.insert(0, senha)

    pyperclip.copy(senha)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def salvar():
    dados_website = website.get()
    dados_email = email.get()
    dados_senha = senha_entry.get()

    # messagebox.showinfo(title="title", message="mensagem")

    if website.get() == "" or senha_entry.get() == "":
        messagebox.showinfo(title="Atenção!", message="inserir dados");

    else:
        is_ok = messagebox.askokcancel(title=dados_website, message=f"Estes são os dados inseridos: \n{dados_website} \n"
                                                                    f"Senha: {dados_senha}\n\n OK para salvar ")
        if is_ok:
            with open("dados.txt", "a") as data:
                data.write(f"\n {dados_website} | {dados_email} | {dados_senha} ")
                website.delete(0, END)
                senha_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Gerenciador de Senhas")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)



website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/usuário")
email_label.grid(column=0, row=2)
senha_label = tkinter.Label(text="Senha:")
senha_label.grid(column=0, row=3)

# Entries
website = Entry(width=45)
website.grid(row=1, column=1, columnspan=2)
website.focus()
email = Entry(width=45)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "sheylacantalupo.sc@gmail.com")
senha_entry = Entry(width=31)
senha_entry.grid(row=3, column=1)

# botões
botao_gerador = Button(text="Gerar Senha", command=gerador_senha)
botao_gerador.grid(row=3, column=2)
botao_salvar = Button(text="Salvar", width=36, command=salvar)
botao_salvar.grid(row=4, column=1, columnspan=2)

window.mainloop()




