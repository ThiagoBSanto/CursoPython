# 
# OBS INICIAL
#
# Termos técnicos: Higher Order Functions e First-Class Functions
#
# Academicamente, os termos Higher Order Functions e First-Class 
# Functions têm significados diferentes.
#
# Higher Order Functions - Funções que podem receber e/ou retornar outras funções
#
# First-Class Functions - Funções que são tratadas como outros tipos de dados 
# comuns (strings, inteiros, etc...)
#
# Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.
#
# Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.

print('\nFIRST-CLASS FUNCTIONS E HIGHER ORDER FUNCTIONS EM PYTHON \n\n')
# *****************    FIRST-CLASS FUNCTIONS E HIGHER ORDER FUNCTIONS    ****************
#
# Em Python, funções são consideradas "first-class citizens" (cidadãs de primeira classe). Isso significa
# que as funções podem ser tratadas como qualquer outra entidade, como variáveis, strings ou números.
# Funções podem ser atribuídas a variáveis, passadas como argumentos para outras funções e retornadas como
# resultados de outras funções.
#
# Exemplo de atribuição de função a uma variável:
def quadrado(x):
    return x ** 2

funcao_referencia = quadrado
print(funcao_referencia(5))  # Saída: 25

# Exemplo de passagem de função como argumento:
def aplicar_operacao(func, valor):
    return func(valor)

resultado = aplicar_operacao(quadrado, 3)
print(resultado)  # Saída: 9

# Exemplo de retorno de função por outra função:
def criar_funcao_potencia(expoente):
    def potencia(x):
        return x ** expoente
    return potencia

quadrado_personalizado = criar_funcao_potencia(2)
print(quadrado_personalizado(4))  # Saída: 16

# *****************    HIGHER ORDER FUNCTIONS    ****************
#
# Uma Higher Order Function (Função de Ordem Superior) é aquela que aceita uma ou mais funções como
# argumentos ou retorna uma função como resultado. Exemplos de Higher Order Functions incluem map,
# filter e reduce.
#
# Exemplo de uso da função map:
numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x ** 2, numeros)
print(list(quadrados))  # Saída: [1, 4, 9, 16, 25]

# Exemplo de uso da função filter:
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4]

# Exemplo de uso da função reduce:
from functools import reduce
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 15