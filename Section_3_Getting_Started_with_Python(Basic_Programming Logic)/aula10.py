#
print('\nOPERADOR LOGICOS \n\n')
# *****************    OPERADOR LOGICOS    ****************
#
# Operadores: and, or, not, in, not in
#
#      **************    OPERADOR AND    *************
#
# O operador lógico and é utilizado para realizar uma operação de 
# "E lógico" em Python. Ele retorna True se e somente se ambos os 
# operandos forem verdadeiros. Se pelo menos um dos operandos for 
# falso, a expressão com o operador and será avaliada como False.
#
print("Exemplo 1 - Op. AND")
print("a = True\nb = True")
a = True
b = True
resultado = a and b
print("Resultado a 'and' b = ", resultado )
print()
print("a = True\nb = False")
a = True
b = False
resultado = a and b
print("Resultado a 'and' b = ", resultado )
print()
print("a = False\nb = False")
a = False
b = False
resultado = a and b
print("Resultado a 'and' b = ", resultado )
print()
#
# O operador and é frequentemente usado em expressões 
# condicionais para combinar múltiplas condições. 
#
print("Exemplo 2 - Op. AND")
print("Idade = 25\nCNH = True")
idade = 25
tem_carteira_de_motorista = True

if idade >= 18 and tem_carteira_de_motorista:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")
print()    
#
#      **************    OPERADOR OR    *************
#
# O operador lógico or é utilizado para realizar uma operação de 
# "OU lógico" em Python. Ele retorna True se pelo menos 1 
# operando for True. Se  ambos  operandos forem False, a 
# expressão com o operador and será avaliada como False.
#
print("Exemplo 1 - Op. OR")
print("a = True\nb = True")
a = True
b = True
resultado = a or b
print("Resultado a 'or' b = ", resultado )
print()
print("a = True\nb = False")
a = True
b = False
resultado = a or b
print("Resultado a 'or' b = ", resultado )
print()
print("a = False\nb = False")
a = False
b = False
resultado = a or b
print("Resultado a 'or' b = ", resultado )
print()
#
#      **************    OPERADOR NOT    *************
#
# Basicamente, o operador "not" inverte o valor de verdade 
# (verdadeiro ou falso) de uma expressão lógica. Se a 
# expressão for verdadeira, o "not" a tornará falsa, e se a 
# expressão for falsa, o "not" a tornará verdadeira.
print()
print("Exemplo 1 - Op. NOT")
print("Condicao = True")
print("if 'not' condicao:")
condicao = True
if not condicao:
    print("A condição é falsa.")
else:
    print("A condição é verdadeira.")
print()
#
#
#      **************    OPERADOR IN    *************
#
# O operador lógico in é usado para verificar se um elemento 
# está presente em uma sequência, como uma lista, uma tupla, 
# uma string, entre outros. Ele retorna True se o elemento 
# estiver presente na sequência e False caso contrário.
#
#
print()
print("Exemplo 1 - Op. IN")
print("Lista = [1, 2, 3, 4, 5]")
print("Verificar se o 3 esta na lista")
minha_lista = [1, 2, 3, 4, 5]

if 3 in minha_lista:
    print("O elemento 3 está na lista.")
else:
    print("O elemento 3 não está na lista.")
#
#
#      **************    OPERADOR NOT IN    *************
#
# O operador lógico not in (em português) é usado para verificar 
# se um elemento NÃO está presente em uma sequência, como uma 
# lista, uma tupla, uma string, entre outros. Ele retorna True se o
# elemento NÃO estiver presente na sequência e False caso contrário.
print()
print("Exemplo 1 - Op. NOT IN")
print("Lista = [1, 2, 3, 4, 5, 6]")
print("Verificar se o 6 esta na lista")
minha_lista = [1, 2, 3, 4, 5, 6]
if 6 not in minha_lista:
    print("O elemento 6 não está na lista.")
else:
    print("O elemento 6 está na lista.")