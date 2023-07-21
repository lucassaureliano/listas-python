# 1. Adicione os números de 1 a 10 à lista "minha_lista" utilizando um loop, em seguida imprima esses valores na tela e por fim
# mostre o tamanho dessa lista.
minha_lista = []

for i in range(1, 11):
    minha_lista.append(i)

print("Valores da lista minha_lista:", minha_lista)
print("Tamanho da lista minha_lista:", len(minha_lista))

# 2. Crie uma lista com os números pares de 0 a 20 e em seguida atenda os seguintes comandos:
# a) Inverta a ordem dos elementos da lista.
# b) Remova os números múltimos de 5 da lista.
numeros_pares = [i for i in range(0, 21) if i % 2 == 0]
print("Números pares de 0 a 20:")
print(numeros_pares)
numeros_pares.reverse()
print("Números pares de 20 a 0:")
print(numeros_pares)
numeros_pares = [num for num in numeros_pares if num % 5 != 0]
print("Lista com números pares, invertida e sem múltiplos de 5:")
print(numeros_pares)

# 3. Crie uma lista chamada "lista_concatenada" que seja a concatenação das listas criadas na questão 1 e na questão 2.
lista_concatenada = minha_lista + numeros_pares

# 4. Remova todos os elementos da lista "lista_concatenada".
lista_concatenada.clear()
print(lista_concatenada)

# 5. Crie uma lista chamada "lista_repetida" com 5 repetições da lista "lista_concatenada".
lista_repetida = lista_concatenada * 5
print("Lista repetida com 5 repetições da lista_concatenada:")
print(lista_repetida)

# 6. Copie a lista "lista_concatenada" para uma nova lista chamada "copia_lista_concatenada" sem utilizar o operador de atribuição direta.
import copy
copia_lista_concatenada = copy(lista_concatenada)

# 7. Faça um programa que leia nome e idade de 5 pessoas e coloque os nomes em uma lista e as idades em outra. 
# Apresente as duas listas preenchidas.
nomes = []
idades = []

for i in range(5):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    nomes.append(nome)
    idades.append(idade)

print("\nLista de nomes:")
print(nomes)

print("\nLista de idades:")
print(idades)


# 8.Faça um script que leia números do usuário, enquanto ele não digitar 0. 
# Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0, 
# o valor máximo e o valor mínimo.
numeros = []
numero = int(input("Digite um número (digite 0 para parar): "))

while numero != 0:
    numeros.append(numero)
    numero = int(input("Digite um número (digite 0 para parar): "))

if len(numeros) == 0:
    print("Nenhum número foi digitado.")
else:
    numeros_sem_zero = [num for num in numeros if num != 0]

    if len(numeros_sem_zero) > 0:
        print("Números digitados (ignorando o 0):", numeros_sem_zero)
        print("Quantidade de números digitados (ignorando o 0):", len(numeros_sem_zero))
        print("Valor máximo (ignorando o 0):", max(numeros_sem_zero))
        print("Valor mínimo (ignorando o 0):", min(numeros_sem_zero))
    else:
        print("Apenas o valor 0 foi digitado.")

# 9.Faça um script que informe o fatorial de um número.
# Utilize obrigatoriamente o comando for
numero = int(input("Digite um número inteiro: "))

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é: {fatorial}")

# 10.Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.
# Se N for par, ele também deve ser incluído no output (vide exemplo para N = 2)
numero = int(input("Digite um número inteiro: "))

n_absoluto = abs(numero)

numeros_pares = []

for i in range(n_absoluto, -n_absoluto - 1, -1):
    if i % 2 == 0:
        numeros_pares.append(i)

print("Números pares entre", -n_absoluto, "e", n_absoluto, "em ordem decrescente:")
print(numeros_pares)


# 11. Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.
numero = int(input("Digite um número inteiro: "))

soma = 0
for i in range(1, numero + 1):
    soma += i

print(f"A soma dos números de 1 a {numero} é: {soma}")


# 12. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade 
# de divisores desse número e quais são eles.
numero = int(input("Digite um número inteiro: "))

divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print(f"O número {numero} possui {len(divisores)} divisores:")
print(divisores)