print('\nFUNÇÕES EM PYTHON \n\n')
# *****************    FUNÇÕES    ****************
#
# Em Python, funções são blocos de código reutilizáveis projetados para realizar tarefas específicas.
# Elas são definidas usando a palavra-chave 'def' seguida pelo nome da função e uma lista de parâmetros
# entre parênteses. A estrutura básica de uma função é a seguinte:
#
# def nome_da_funcao(parametro1, parametro2, ...):
#     # corpo da função
#     # operações a serem realizadas
#     return resultado
#
# Parâmetros: São variáveis usadas para receber valores que a função utilizará durante sua execução.
# No exemplo acima, 'parametro1' e 'parametro2' são parâmetros.
#
# Retorno de Valor: Uma função pode ou não retornar um valor. A palavra-chave 'return' é usada para
# especificar o valor que a função deve retornar. Caso a função não tenha um 'return', ela retorna 'None'.
#
# Escopo de Variáveis: Variáveis definidas dentro de uma função são chamadas de variáveis locais e existem
# apenas dentro do escopo da função. Elas não são acessíveis fora da função, a menos que seja utilizado o
# valor retornado pela função.
#
# Exemplo:
#
'''
print("Exemplo - Função de Soma")
def soma(a, b):
    # Esta função recebe dois parâmetros, 'a' e 'b', realiza a operação de soma e retorna o resultado.
    resultado = a + b
    return resultado

# Chamada da função
numero1 = 3
numero2 = 5
resultado_soma = soma(numero1, numero2)
print(f"Resultado da soma de {numero1} e {numero2}: {resultado_soma}")  # Saída: Resultado da soma de 3 e 5: 8

# *****************    ESCOPO DE VARIÁVEIS    ****************
#
# Em Python, o escopo de uma variável refere-se à região do código onde a variável é acessível.
# Existem dois principais tipos de escopo em Python: escopo global e escopo local.
#
#      **************    ESCOPO GLOBAL    *************
#
# Variáveis definidas fora de qualquer função têm escopo global. Elas podem ser acessadas em qualquer
# parte do código, incluindo dentro de funções. No entanto, se uma variável global for modificada dentro
# de uma função, é necessário usar a palavra-chave 'global'.
#
# Exemplo:
variavel_global = 10  # Esta variável tem escopo global


def funcao_global():
    print("Acessando variável global dentro da função:", variavel_global)


funcao_global()  # Saída: Acessando variável global dentro da função: 10

#      **************    ESCOPO LOCAL    *************
#
# Variáveis definidas dentro de uma função têm escopo local. Elas são acessíveis apenas dentro da função.
# Se uma variável local tiver o mesmo nome que uma variável global, a variável local terá precedência dentro
# da função.
#
# Exemplo:
variavel_global = 10  # Variável global com o mesmo nome


def funcao_local():
    variavel_local = 5  # Esta variável tem escopo local
    print("Acessando variável local dentro da função:", variavel_local)


funcao_local()  # Saída: Acessando variável local dentro da função: 5

# Tentando acessar uma variável local fora de sua função resultará em erro:
# print(variavel_local)  # Comentado para evitar erro

# Escopo de Variáveis em Funções:
# Quando uma função é chamada, ela cria seu próprio escopo local. As variáveis locais existem apenas durante
# a execução da função e são destruídas quando a função é concluída. Variáveis locais não são acessíveis
# fora da função.
#
# Exemplo:


def funcao_com_variavel_local():
    variavel_local = 20
    print("Dentro da função:", variavel_local)


funcao_com_variavel_local()  # Saída: Dentro da função: 20

# Tentando acessar a variável local fora da função resultará em erro:
# print(variavel_local)  # Comentado para evitar erro
#
#
# *****************    PARÂMETROS E ARGUMENTOS    ****************
#
# Em Python, parâmetros são as variáveis utilizadas em uma função para receber valores durante sua execução.
# Esses valores são chamados de argumentos quando a função é chamada. Parâmetros são definidos na declaração
# da função, enquanto argumentos são passados para a função durante sua chamada.
#
# Exemplo de definição de função com parâmetros:


def saudacao(nome, saudacao_personalizada):
    mensagem = f"{saudacao_personalizada}, {nome}!"
    return mensagem


# Exemplo de chamada da função com argumentos:
nome_usuario = "Maria"
saudacao_usuario = "Olá"
mensagem_saudacao = saudacao(nome_usuario, saudacao_usuario)
print(mensagem_saudacao)  # Saída: Olá, Maria!

# Parâmetros podem ter valores padrão, tornando-os opcionais durante a chamada da função.
# Se um valor padrão for fornecido, o parâmetro se torna opcional, e caso não seja passado um
# argumento para ele, o valor padrão será utilizado.
#
# Exemplo:


def potencia(base, expoente=2):
    resultado = base ** expoente
    return resultado


# Chamada da função com um argumento (expoente usa o valor padrão):
resultado_potencia_1 = potencia(3)
# Saída: 3 elevado à potência 2: 9
print("3 elevado à potência 2:", resultado_potencia_1)

# Chamada da função com dois argumentos (expoente é fornecido):
resultado_potencia_2 = potencia(3, 3)
# Saída: 3 elevado à potência 3: 27
print("3 elevado à potência 3:", resultado_potencia_2)

'''

# EXERCICIO

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
'''
def mostrar(*args):
    resultado = 1
    for _ in args:
        resultado *= _
    #print(f'Resutado = {resultado}')
    return resultado


valor = mostrar(1,2,3,4,5)
print(valor)
#
'''
'''
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(numero):
    try:
        if int(numero) % 2 == 0:
            return  print(f"O NUMERO {numero} é PAR")
        else:
            return  print(f"O NUMERO {numero} IMPAR")
    except:
        return print(f'Valor não valido!')
    
par_impar(0)
par_impar(1)
par_impar('2')
par_impar('3')
par_impar(4)
par_impar('a')

'''