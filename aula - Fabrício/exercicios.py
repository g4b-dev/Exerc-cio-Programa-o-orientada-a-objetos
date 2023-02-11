# Escrever três programas.

# 1 - cálculo de média de 4 notas => 7 aprovado

# <7 >= 4 = Exame final <4 reprovado

notas = []
while len(notas) < 4:
    nota = float(input("Insira a nota do aluno"))
    notas.append(nota)

media = sum(notas)/4
print(f'A média do aluno foi: {media}')
if media >= 7:
    print("O aluno foi aprovado!")

elif media >= 4 and media < 7:
    print("O aluno está em exame final")

else:
    print("O aluno foi reprovado")


# 2 - criar um programa para organizar um array(lista/tupla)

# -> por ordem alfabética = NÂO PODE USAR O SORT SORTED e AFINS

# NÂO PODE USAR FUNÇÂO PRONTA DO PYTHON

palavras = ['bola','cachorro','arco','dado']

for i in range(len(palavras)-1):
    for j in range(len(palavras)-1): 
        if palavras[j] > palavras[j+1]:
            p = palavras[j]
            palavras[j] = palavras[j+1]
            palavras[j+1] = p

for palav in palavras:
    print(palav)

# 3 - criar uma função que vai receber algumas cidades(5)

# Organizar em ordem alfabética

# Podem subir no github e mandar o link aqui.

# Podem mandar o link de um google docs com as soluções também.

