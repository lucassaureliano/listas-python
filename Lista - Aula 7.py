# Exercicios

# 1. Construa um programa no qual o usuário informe o nome, a estatura e o peso de vários alunos
# de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno ordenados
# pelo nome do aluno. Sabe-se que IMC = peso/altura**2

# 2. Faça um script que receba os valores do nome, idade e e-mail de uma pessoa
# e guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. 
# Exiba as informações desse dicionário
pessoa = {}

pessoa['nome'] = input("Digite o nome da pessoa: ")
pessoa['idade'] = input("Digite a idade da pessoa: ")
pessoa['email'] = input("Digite o e-mail da pessoa: ")

print("\nInformações da pessoa:")
print("Nome:", pessoa['nome'])
print("Idade:", pessoa['idade'])
print("E-mail:", pessoa['email'])

# 3. Faça um programa que leia 10 números do usuário e os coloque corretamente no dicionário D abaixo.
# D = {'pares': [], 'impares':[]}
D = {'pares': [], 'impares': []}

for _ in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        D['pares'].append(numero)
    else:
        D['impares'].append(numero)

print("\nDicionário D:")
print(D)

# 4. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos 
# de mercado e seus respectivos preços e os mostre na tela.
produtos = {}

for i in range(3):
    nome_produto = input(f"Digite o nome do produto {i+1}: ")
    preco_produto = float(input(f"Digite o preço do produto {i+1}: "))

    produtos[nome_produto] = preco_produto

print("\nProdutos cadastrados e seus preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R${preco:.2f}")

# 5. Escreva um programa que conta a quantidade de vogais em um 
# texto e armazena tal quantidade em um dicionário, onde a 
# chave é a vogal considerada.
texto = input("Digite um texto: ")

vogais = 'aeiouAEIOU'
vogais_contagem = {vogal: texto.count(vogal) for vogal in vogais}

print("\nQuantidade de vogais:")
for vogal, quantidade in vogais_contagem.items():
    print(f"{vogal}: {quantidade}")

# 6. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo
#  como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).
semana = {
    'segunda': ['Aula de Matemática', 'Aula de Português'],
    'terca': ['Aula de Ciências', 'Aula de História'],
    'quarta': ['Aula de Inglês', 'Aula de Educação Física'],
    'quinta': ['Aula de Geografia', 'Aula de Artes'],
    'sexta': ['Aula de Biologia', 'Aula de Química'],
    'sabado': [],
    'domingo': []
}

print(semana)