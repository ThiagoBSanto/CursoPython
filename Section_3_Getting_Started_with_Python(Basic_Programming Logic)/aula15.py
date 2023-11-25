#
print('\nLAÇO WHILE \n\n')
# *****    ESTRUTURA DE REPETIÇÃO - WHILE    *****
#
# NO VSCODE UTILIZE CTRL + / PARA DESCOMENTAR A
# A SELEÇÃO DO CODIGO DESEJADA
#
# A estrutura while em Python é utilizada para criar
# loops, ou seja, repetições de um bloco de código
# enquanto uma condição específica for verdadeira.
#
# A sintaxe básica é a seguinte:
# while condição:
# Repetição enquanto a condição for verdadeira
# ...
#
# O bloco de código dentro do while será executado
# repetidamente enquanto a condição especificada
# for avaliada como verdadeira. Se a condição se
# tornar falsa, a execução do loop é interrompida,
# e o controle do programa passa para o código após
# o bloco while.
#
#
############### INSTRUÇÕES DO WHILE ################
#
# 1 - break: Usada para sair imediatamente de um loop,
#     mesmo se a condição do loop não for falsa. Isso
#     é útil para interromper o loop com base em uma
#     condição específica.
#
# EXEMPLO

# contador = 0
# while True:
#     print(f"Contador: {contador}")
#     contador += 1
#     if contador == 5:
#         break

# print("\n-----------------------------\n")

# 2 - continue: A instrução continue é usada para pular
#     o restante do código dentro do loop e ir para a
#     próxima iteração. Isso pode ser útil quando é
#     desejável ignorar a execução de parte do código com
#     base em uma condição, mas ainda quer continuar o loop.
#
# Exemplo:

# contador = 0
# while contador < 5:
#     contador += 1
#     if contador == 3:
#         continue
#     print(f"Contador: {contador}")

# print("\n-----------------------------\n")

# 3 - else: O bloco else pode ser associado a um loop
#     while e é executado quando a condição do loop se
#     torna falsa. Isso é útil para executar código após
#     a conclusão bem-sucedida de um loop.
#
# Exemplo:

# contador = 0
# while contador < 5:
#     print(f"Contador: {contador}")
#     contador += 1
# else:
#     print("Loop concluído com sucesso.")
#
# print("\n-----------------------------\n")
#
#
########### Exercício 1 ####################
#
# Iterear string com while

# nome = "Thiago Barbosa Santos"
# indice = 0
# novo_nome = ''
# print(nome)
# while indice < len(nome):

#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1
# novo_nome += "*"
# print(novo_nome)
#
#
######## 2 - Exercicio - Calculadora #######

# print("CALCULADORA")
# sair = False
# while True:
#     print("Digite sair, para encerrar o programa a qualquer momento:")
#     if sair == True:
#         break
#     while True:
#         num1 = input("Informe o primeiro Valor:  ")
#         if num1.lower() == "sair":
#             sair = True
#             break

#         try:
#             num1 = int(num1)
#             if isinstance(num1, (int, float)):
#                 break

#         except:
#             print("Digite um valor válido")

#     while True:
#         if sair == True:
#             break
#         operador = input("Informe qual tipo de operação + - * /: ")
#         if operador.lower() == "sair":
#             sair = True
#             break

#         if ((operador == "+") or (operador == "-") or
#                 (operador == "*") or (operador == "/")):
#             break
#         else:
#             print("Digite um operador válido\n")

#     while True:
#         if sair == True:
#             break
#         num2 = input("Informe o segundo Valor:  ")
#         if num2.lower() == "sair":
#             sair = True
#             break
#         if operador == "/":
#             try:
#                 num2 = int(num2)
#                 if isinstance(num2, (int, float)):
#                     if (num2 != 0):
#                         break
#                     else:
#                         print("Não existe divisão por zero")

#             except:
#                 print("excpt1")
#         else:
#             try:
#                 num2 = int(num2)

#                 if isinstance(num2, (int, float)):
#                     break
#             except:
#                 print("Digite um valor válido")
#     print("\n")

#     if sair:
#         break

#     if operador == '+':
#         total = num1 + num2
#     elif operador == '-':
#         total = num1 - num2

#     elif operador == '*':
#         total = num1 * num2

#     else:
#         total = num1 / num2

#     print(f"{num1} {operador} {num2} = {total}")

#     print("\n----------------------")
# print("\nCALCULADORA FOI FINALIZADA")
