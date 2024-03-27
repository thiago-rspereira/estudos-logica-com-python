# Programa para realizar a soma entre dois números
x = 50
y = 30

print("Soma de x e y:", x + y)

# Programa para ler uma variável e retornar informações sobre ela
print("\nAnálise de uma variável:")
variavel = input("Digite uma variável: ")

print("Tipo da variável:", type(variavel))

# Verificar se a variável pode ser convertida para um número
if variavel.isnumeric():
    variavel = int(variavel)
    print("Conteúdo da variável como número inteiro:", variavel)
elif variavel.replace('.', '', 1).isdigit():
    variavel = float(variavel)
    print("Conteúdo da variável como número de ponto flutuante:", variavel)
else:
    print("Conteúdo da variável como string:", variavel)