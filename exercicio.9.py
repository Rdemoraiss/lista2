funcionarios = []

funcionarios.append([1, "Ana Silva", "Analista de Sistemas", 4500.00])
funcionarios.append([2, "Carlos Souza", "Desenvolvedor Backend", 5800.50])

for func in funcionarios:
    print(f"ID: {func[0]} | Nome: {func[1]} | Cargo: {func[2]} | Salário: R$ {func[3]:.2f}")
