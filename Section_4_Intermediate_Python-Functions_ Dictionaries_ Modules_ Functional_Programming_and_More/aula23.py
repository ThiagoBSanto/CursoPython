print('\nCLOSURES E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES EM PYTHON \n\n')
# *****************    CLOSURES E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES    ****************
#
# Em Python, um closure ocorre quando uma função aninhada (função interna) referencia uma variável
# da função externa (função externa). O closure "captura" o estado da variável, mesmo após a função
# externa ter concluído sua execução.
#
# Exemplo de closure:
def criar_funcao_multiplicadora(fator):
    def multiplicar(x):
        return x * fator
    return multiplicar

# Criando uma função que multiplica por 3
triplicar = criar_funcao_multiplicadora(3)
print(triplicar(5))  # Saída: 15

# Criando uma função que multiplica por 7
multiplicar_por_sete = criar_funcao_multiplicadora(7)
print(multiplicar_por_sete(4))  # Saída: 28

# *****************    FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES    ****************
#
# Em Python, é possível definir funções que retornam outras funções. Isso é útil para criar
# funções personalizadas com comportamentos específicos.
#
# Exemplo de função que retorna outra função:
'''
def criar_funcao_exponencial(expoente):
    def exponencial(x):
        return x ** expoente
    return exponencial

# Criando uma função que calcula o quadrado
quadrado = criar_funcao_exponencial(2)
print(quadrado(3))  # Saída: 9

# Criando uma função que calcula o cubo
cubo = criar_funcao_exponencial(3)
print(cubo(2))  # Saída: 8

'''

def multiplicador(vezes):
    def mult(x):
        return vezes * x
    return mult

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadriplicar(5))
