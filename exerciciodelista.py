"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
vetor a média de cada aluno, imprima o número de alunos com média maior ou
igual a 7.0.
"""
median7 = 0
notas = []
media7 = []
for c in range (10):
    media = 0

    print(f"Aluno {c+1}")

    for i in range(4):
        notas.append(float(input(f"Digite a {i+1}ª nota: ")))
        media += notas[i]
    
    media = media / 4
    print(media)

    if media >= 7:
        media7.append(media)
        median7+=1


print(f"Tivemos {median7} que tiraram media maior ou igual a sete")


        

        
        



