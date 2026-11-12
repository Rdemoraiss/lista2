from exercicio2 import livros

titulo_procurado = "Dom Casmurro"

for livro in livros:
    if livro[1] == titulo_procurado:
        print("Livro localizado!:", livro)
        break
