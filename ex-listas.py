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

# Remover todas as ocorrências de um determinado número de uma lista de números inteiros


# Criar uma lista com números inteiros e contar quantos números pares e quantos números ímpares existem na lista.
import random

numeros = list()
for i in range(10):
      numeros.append(random.randint(0, 50))

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'{numeros}\nA lista contém", {pares}, "números pares e", {impares}, "números ímpares.')

# Criar uma lista com números inteiros e verificar se um determinado número está na lista ou não.

import random

numeros = list()
for i in range(10):
      numeros.append(random.randint(0, 50))
      
print(numeros)

valinum = int(input('Digite um número para validarmos se o mesmo está na lista:'))
if valinum not in numeros:
      print(f'O número {valinum} não está na lista.')
else:
      print(f'O número {valinum} está na lista.')
      
# Criar uma lista com nomes de frutas e verificar se uma determinada fruta está na lista ou não.

frutas = ["banana", "maçã", "laranja", "abacaxi", "uva", "manga", "morango"]

valifru = int(input('Insira uma fruta para validarmos se a mesma está na lista:'))
if valifru not in frutas:
      print(f'A fruta {valifru} não está na lista.')
else:
      print(f'A fruta {valifru} está na lista.')
      
# Criar uma lista de números inteiros e calcular a soma de todos os números na lista.

import random

numeros = list()
for i in range(10):
      numeros.append(random.randint(0, 50))
      
print(f'{numeros}\nA soma é {sum(numeros)}')

# Criar uma lista de números inteiros e calcular a média dos números na lista.

import random

numeros = list()
for i in range(10):
      numeros.append(random.randint(0, 50))
      
print(f'{numeros}\nA média é ({sum(numeros)/len(numeros)})')

# Criar uma lista com nomes de pessoas e imprimir o primeiro e o último nome da lista.

nomes = []
while (len(nomes) < 100):
      nome = (input('Digite um nome próprio ou parar para parar de adicionar:'))
      if nome == '0':
            break
      else:
            nomes.append(nome)
            
print(f'O primeiro nome é {nomes[0]}\nO último nome é {nomes[len(nomes) - 1]}')
