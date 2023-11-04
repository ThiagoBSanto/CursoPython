#
#
# ****************   OPERADORES MATEMÁTICOS    ****************
#
# Os operadores são executados de acordo com a seguinte 
# precedência, da mais alta para a mais baixa:
#
# 1 - Parênteses: Operações dentro de parênteses têm a mais 
# alta precedência. Qualquer operação dentro de parênteses é 
# executada antes de qualquer outra operação.
#
# 2 - Exponenciação (**): O operador de exponenciação é usado 
#para calcular potências. Ele tem a segunda maior precedência.
#
# 3 - Multiplicação (*), Divisão (/), Divisão de Piso (//) e 
# Módulo (%): Esses operadores são usados para realizar operações 
# de multiplicação, divisão e módulo. Eles têm a mesma precedência 
# e são executados da esquerda para a direita.
#
# 4 - Adição (+) e Subtração (-): Os operadores de adição e 
# subtração têm a menor precedência. Eles também são executados 
# da esquerda para a direita.


resultado = 2 + 3 * 4  # A multiplicação tem precedência sobre a adição: 2 + 12 = 14
print(" resultado = 2 + 3 * 4 : ", resultado)
resultado = (2 + 3) * 4  # Os parênteses têm a mais alta precedência: 5 * 4 = 20
print(" resultado = (2 + 3) * 4 : ", resultado)
resultado = 2 ** 3 + 4  # A exponenciação tem precedência sobre a adição: 8 + 4 = 12
print(" resultado = 2 ** 3 + 4  : ", resultado)