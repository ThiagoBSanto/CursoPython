#
import random
print('\nLAÇO FOR \n\n')
# *****    ESTRUTURA DE REPETIÇÃO - FOR    *****
#
# A estrutura for em Python é utilizada para iterar
# sobre uma sequência (como uma lista, tupla, string
# ou range) ou outros objetos iteráveis. Diferentemente
# do while, o for é utilizado quando o número de
# iterações é conhecido antecipadamente.
#
# A sintaxe básica é a seguinte:
# for variavel in sequencia:
#     Bloco de código a ser repetido para cada item
#     da sequência
#
# A variável assume o valor de cada item da sequência
# em cada iteração do loop.
#
#
############### INSTRUÇÕES DO FOR ################
#
# 1 - break: Usada para sair imediatamente de um loop,
#     mesmo se a condição do loop não for falsa. Isso
#     é útil para interromper o loop com base em uma
#     condição específica.
#
# EXEMPLO

# for contador in range(5):
#     print(f"Contador: {contador}")
#     if contador == 2:
#         break

# print("\n-----------------------------\n")

# 2 - continue: A instrução continue é usada para pular
#     o restante do código dentro do loop e ir para a
#     próxima iteração. Isso pode ser útil quando é
#     desejável ignorar a execução de parte do código com
#     base em uma condição, mas ainda quer continuar o loop.
#
# Exemplo:

# for contador in range(1, 6):
#     if contador == 3:
#         continue
#     print(f"Contador: {contador}")

# print("\n-----------------------------\n")

# 3 - else: A cláusula else em um loop for é executada
#     quando o loop é concluído, mas não foi interrompido
#     por uma instrução break.

# EXEMPLO

# for item in range(5):
#     print(f"Item: {item}")
# else:
#     print("Loop concluído sem interrupções.")

# print("\n-----------------------------\n")

# 4 - pass: A instrução pass é usada como um espaço
#     reservado, indicando que nenhum código deve ser
#     executado. É útil quando a sintaxe exige um bloco
#     de código, mas você não deseja executar nada.

# EXEMPLO

# for i in range(3):
#     pass  # Nenhuma ação é realizada neste loop

# print("\n-----------------------------\n")

# 5 - enumerate: A função enumerate() é usada para
#     obter tanto o índice quanto o valor de cada item
#     em uma sequência. Pode ser útil quando você
#     precisa do índice e do valor simultaneamente.

# EXEMPLO

# lista = ['a', 'b', 'c']
# for indice, valor in enumerate(lista):
#     print(f"Índice: {indice}, Valor: {valor}")
#
#
############   A FUNÇÃO RANGE EM PYTHON  #############

# A função range() em Python é uma função integrada que
# gera uma sequência de números em uma progressão
# aritmética. É comumente usada em estruturas de repetição,
# como loops for, para iterar sobre uma sequência de
# valores específicos.

# *****    SINTAXE DA FUNÇÃO RANGE    *****
#
# A sintaxe básica da função range() é a seguinte:
# range(início, fim, passo)
#
# - início: O valor inicial da sequência (inclusive).
# - fim: O valor final da sequência (exclusivo).
# - passo: O intervalo entre os valores (opcional, padrão 1).

# *****    EXEMPLOS DE USO    *****
#
# 1. Geração de uma sequência de números:
#    A função range() pode ser utilizada para gerar
#    uma sequência de números dentro de um intervalo.

# Exemplo:
# for numero in range(1, 6):
#     print(numero)
# Output: 1, 2, 3, 4, 5

# 2. Especificando um passo na sequência:
#    O parâmetro passo define o intervalo entre os
#    números na sequência gerada.

# Exemplo:
# for numero in range(1, 10, 2):
#     print(numero)
# Output: 1, 3, 5, 7, 9

# 3. Utilizando a função range() em conjunto com len():
#    A função len() pode ser utilizada para obter o
#    comprimento de uma sequência, e assim, a função
#    range() pode ser usada para iterar sobre índices.

# Exemplo:
# lista = ['a', 'b', 'c', 'd']
# for indice in range(len(lista)):
#     print(f"Índice: {indice}, Valor: {lista[indice]}")

# 4. Criando uma lista a partir da função range():
#    A função range() também pode ser usada para
#    gerar uma lista de números.

# Exemplo:
# lista_numeros = list(range(5))
# print(lista_numeros)
# Output: [0, 1, 2, 3, 4]

# *****    OBSERVAÇÕES IMPORTANTES    *****
#
# - A função range() é inclusiva no valor inicial e
#   exclusiva no valor final, ou seja, o último valor
#   da sequência não é incluído.
#
# - Se o valor inicial não for fornecido, ele é
#   assumido como 0.
#
# - Se o passo não for fornecido, ele é assumido como 1.
#
# A função range() é uma ferramenta versátil em Python,
# proporcionando uma maneira eficiente de gerar sequências
# numéricas para diversos propósitos, principalmente em
# contextos de controle de fluxo e iteração.
#
#

############### JOGO DA FORCA ###############################

facil = ["Kiwi", "Nota", "Uva", "Vela", "Xale",
         "Dado", "Fada", "Limao", "Sapo", "Vento",
         "Amor", "Bola", "Casa", "Gato", "Luz",
         "Mesa", "Noite", "Olho", "Pato", "Rato"]

medio = ["Banana", "Cachorro", "Estrela", "Janela", "Liquido",
         "Magico", "Palavra", "Queijo", "Sorvete", "Tomate",
         "Ceu", "Girafa", "Fantasma", "Vitoria", "Folha",
         "Barco", "Chave", "Medico", "Silencio", "Pessoa"]

dificil = ["Elefante", "Aventura", "Abacaxi", "Melancia", "Hipopotamo",
           "Universo", "Biblioteca", "Chocolate", "Magnifico", "Caminhada",
           "Incrivel", "Fenomenal", "Explorador", "Especialista", "Escultura",
           "Prodigioso", "Colaboracao", "Deslumbrante", "Extraordinario", "Adoravel"]


facil = ["Kiwi", "Nota", "Uva", "Vela", "Xale",
         "Dado", "Fada", "Limao", "Sapo", "Vento",
         "Amor", "Bola", "Casa", "Gato", "Luz",
         "Mesa", "Noite", "Olho", "Pato", "Rato"]

medio = ["Banana", "Cachorro", "Estrela", "Janela", "Liquido",
         "Magico", "Palavra", "Queijo", "Sorvete", "Tomate",
         "Ceu", "Girafa", "Fantasma", "Vitoria", "Folha",
         "Barco", "Chave", "Medico", "Silencio", "Pessoa"]

dificil = ["Elefante", "Aventura", "Abacaxi", "Melancia", "Hipopotamo",
           "Universo", "Biblioteca", "Chocolate", "Magnifico", "Caminhada",
           "Incrivel", "Fenomenal", "Explorador", "Especialista", "Escultura",
           "Prodigioso", "Colaboracao", "Deslumbrante", "Extraordinario", "Adoravel"]

print("************** JOGO DA FORCA *******************")
print("************************************************")
print("\n\n")
print("Dificuldade 1 - até 5 letras e 6 vidas")
print("Dificuldade 2 - 6 ou 7 letras e 5 vidas")
print("Dificuldade 3 - + de 8 letras e 4 vidas\n")
dificuldade = input("Qual o nível de dificuldade 1, 2 ou 3: ")
letras_certa = ''
palavra = ""
if dificuldade == "1":
    vida = 6
    i = random.randint(0, 19)
    palavra = facil[i]

elif dificuldade == "2":
    vida = 5
    i = random.randint(0, 19)
    palavra = medio[i]
else:
    vida = 4
    i = random.randint(0, 19)
    palavra = dificil[i]

print("\n")

asterisco = "*" * len(palavra)
print(asterisco)
chutes = []

while vida > 0:
    if '*' not in asterisco:
        print(
            f"Parabéns, você acertou '{palavra}' com {vida} vidas restantes.")
        break

    print(f"Você possui {vida} chances:")
    print(f"Letras digitadas: {chutes}")
    letra = input("\nInforme uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra válida.\n")
        continue

    if letra in chutes:
        print("Essa letra já foi usada.")
        continue

    chutes.append(letra)

    letra_encontrada = False
    for i in range(len(palavra)):
        if letra == palavra[i].lower():
            asterisco = asterisco[:i] + letra + asterisco[i + 1:]
            letra_encontrada = True

    if not letra_encontrada:
        print(f"Essa palavra não possui essa letra.")
        vida -= 1
    else:
        print("Possui essa letra:")

    print(asterisco)
if vida == 0:
    print("GAME OVER. A palavra correta era:", palavra)
