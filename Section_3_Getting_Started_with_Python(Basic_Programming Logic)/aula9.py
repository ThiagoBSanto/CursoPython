#
#
# *****************    IF-ELIF-ELSE    ****************
#
# if, elif e else são estruturas de controle condicional 
# em Python que permitem que você tome decisões com base 
# em condições.
#
# FUNCIONAMENTO
#
# if: A estrutura if é usada para executar um bloco de 
# código somente se uma determinada condição for 
# verdadeira. 
print()
print("EXEMPLO 1")
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
#
# Neste exemplo, o código dentro do bloco if será executado 
# apenas se a variável idade for maior ou igual a 18.
#
# elif (abreviação de "else if"): A estrutura elif é usada 
# quando você deseja testar várias condições em sequência. 
# Ela segue um if e permite que você especifique uma nova 
# condição a ser verificada se a condição anterior não for 
# verdadeira. elif -> existe a partir de 3 condições, em 
# caso de duas usa o if-else, e de uma so, somente o if.
#
# else: A estrutura else é usada para especificar o que 
# fazer quando nenhuma das condições anteriores for 
# verdadeira.
# #
#  
print()
print("EXEMPLO COM ELIF")
nota = 75
if nota >= 90:
    print("Aprovado com nota A")
elif nota >= 80:
    print("Aprovado com nota B")
elif nota >= 70:
    print("Aprovado com nota C")
else:
    print("Reprovado")
#
print()
print("EXEMPLO ELSE")
idade = 15
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
print()
print()    
#
#
# *****************    EXERCICIO    ****************
#
primeiro_valor = input('Digite um valor ')
segundo_valor  = input('Digite outro valor ') 
#
if primeiro_valor == segundo_valor :
    print("Os valores são iguais: = ", primeiro_valor)
elif primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} > {segundo_valor}: O primeiro valor é maior")
else:
    print(f"{primeiro_valor} < {segundo_valor}: O segundo  valor é maior")    
