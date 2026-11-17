funcionarios = [
    [1, "Ana Silva", "Analista de Sistemas", 4500.00],
    [2, "Carlos Souza", "Desenvolvedor Backend", 5800.50]
]

for indice, func in enumerate(funcionarios):
    if func[0] == 2:
        funcionarios[indice][3] += 500  
        print(f"Aumento aplicado! Novo salário de {func[1]}: R$ {funcionarios[indice][3]:.2f}")
        break
