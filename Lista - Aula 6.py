# Exercicios

# 1.Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.
palavra = input("Digite uma palavra: ")
for letra in palavra:
    print(letra)

# 2.Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, depois imprima a nova string: Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "
palavra = input("Digite uma palavra: ")
nova_string = " ".join(palavra)
print(nova_string)

# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'
entrada = input("Digite uma string: ")
nova_string = entrada.replace('a', '4').replace('e', '3').replace('I', '1').replace('t', '7')
print("Nova string:", nova_string)

# 4.Faça um programa que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".
entrada = input("Digite uma string: ")
string_invertida = entrada[::-1]
print("String invertida:", string_invertida)

# 5. Escreva um programa que duas strings e gere uma terceira na qual os caracteres da segunda foram retirados da primeira.
string_original = input("Digite a primeira string: ")
caracteres_remover = input("Digite a segunda string (caracteres a serem removidos): ")
traducao = str.maketrans('', '', caracteres_remover)
nova_string = string_original.translate(traducao)
print("Nova string:", nova_string)

# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto..
texto = input("Digite um texto: ")
palavra = input("Digite uma palavra: ")

if palavra in texto:
    print("A palavra está presente no texto.")
else:
    print("A palavra não está presente no texto.")