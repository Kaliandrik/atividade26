# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

notas = []

for i in range(1,6):
    notas.append(int(input("Digite sua nota: ")))

maiornota = max(notas)
menornota = min(notas)
media = sum(notas) / len(notas)


print(media)
print(f"A menor nota é: {menornota}")
print(f"A maior nota é: {maiornota}")

