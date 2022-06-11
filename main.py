from conexao import criar_conexao, fechar_conexao
from tkinter import *
#import requests


def insere_cadastros(con, nome, idade, cpf, nacionalidade, sexo):
    cursor = con.cursor()
    sql = "INSERT INTO cadastros (nome, idade, cpf, nacionalidade, sexo) values (%s, %s, %s, %s, %s)"
    valores = (nome, idade, cpf, nacionalidade, sexo)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def main():
    con = criar_conexao("localhost", "kwaark1", "GFh@#0871", "funcionarios")

    insere_cadastros(con, "Matheus", 24, "12547852101", "BRASILEIRO", "MASCULINO")

    fechar_conexao(con)

if __name__ == "__main__":
    main()


janela = Tk()
janela.title("INSERIR NOVO CADASTRO.")

texto_orientacao = Label(janela, text="-INFORME OS DADOS PARA CADASTRO-")
texto_orientacao.grid(column=0, row=2)



janela.mainloop()
