def calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos):
    # Cálculo do salário fixo
    salario_final = salario_fixo
    
    # Caso o vendedor vendeu carros
    if carros_vendidos > 0:
        # Adiciona a comissão pelos carros vendidos com base na comissao oferecida pela empresa
        salario_final += carros_vendidos * comissao_por_carro
        # Adiciona 5% sobre o total das vendas dos carros
        salario_final += 0.05 * total_vendas
        
        # Verifica se há bônus caso o vendendor tenha vendido mais de 10 carros
        if carros_vendidos > 10:
            salario_final += 0.10 * total_vendas
    
    return salario_final

while True:
    try:
        # Coleta de dados do usuário com base no banco de dados da empresa
        salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
        comissao_por_carro = float(input("Digite a comissão fixa por carro vendido: R$ "))
        total_vendas = float(input("Digite o valor total das vendas: R$ "))
        carros_vendidos = int(input("Digite o número de carros vendidos: "))

        # Resultado do salario
        salario = calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos)
        print(f"O salário final do vendedor é: R$ {salario:.2f}")

        # Pergunta se o usuário deseja inserir novos dados de outros vendedores
        continuar = input("Deseja inserir novos dados? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa finalizado.")
            break

    except ValueError:
        print("Por favor, insira valores válidos.")