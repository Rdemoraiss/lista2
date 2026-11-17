livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"}
]

id_remover = 2

for indice, livro in enumerate(livros):
    if livro["id"] == id_remover:
        livros.pop(indice)
        break  

print(livros)
