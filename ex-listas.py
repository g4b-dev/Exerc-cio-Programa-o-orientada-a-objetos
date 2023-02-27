# Criar uma lista com 10 números inteiros aleatórios e imprimir o maior e o menor número da lista.
import random
    
numeros = list()
for i in range(10):
      numeros.append(random.randint(0, 50))
      
print(numeros)

print(f'O maior número é: {max(numeros)}'
      f'\nO menor número é: {min(numeros)}')

# Criar duas listas de números inteiros e mesclá-las em uma terceira lista em ordem crescente.
import random

lista1 = list()
for i in range(10):
      lista1.append(random.randint(0, 50))
lista2 = list()
for i in range(10):
      lista2.append(random.randint(0, 50))
lista3 = list()

lista3 = lista1 + lista2
lista3.sort()
print(lista3)

# Criar uma lista com nomes de pessoas e ordená-la alfabeticamente.

nomes = []
while (len(nomes) < 10):
      nome = input('Insira um nome ou digite 0 para parar:')
      if nome == '0':
            break
      if nome not in nomes:
            nomes.append(nome)
            
nomes.sort()
      
print(nomes)
