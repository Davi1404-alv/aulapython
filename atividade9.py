# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função principal
def main():
    # Solicitar o nome do aluno
    nome = input("Digite o nome do aluno: ")

    # Solicitar as notas
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)

    # Calcular a média
    media = calcular_media(notas)

    # Determinar a situação do aluno
    if media < 3:
        situacao = "Reprovado"
    elif 3 <= media < 6:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"

    # Exibir o resultado
    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

# Executar o programa
if __name__ == "__main__":
    main()