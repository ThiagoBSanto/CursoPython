#
#
# *****************    CONVERTENDO TIPO    ****************
#
print()
print("CONVERTENDO TIPO")
print("\n")
# É conhecido também por conversão de tipo, coerção (coercion), typecasting
# type convertion.
# É o ato de converter um tipo em outro tipo imutáveis e primitivos:
# str, int, float, bool
# 
# 1 - Conversão de Tipo (Type Conversion): Refere-se ao processo de converter 
#um valor de um tipo de dados em outro tipo de dados. Isso pode ser feito de 
#maneira explícita ou implícita, dependendo da linguagem de programação e das 
#regras aplicáveis.
# 
print("Exemplo Conversão de Tipo")
print()
valor_texto = "42"
valor_inteiro = int(valor_texto)
print("tipo da variavel valor_texto = ",type(valor_texto))
print("tipo da variavel valor_inteiro = ",type(valor_inteiro))
print("valor inteiro = ", valor_inteiro)
print()
#
# 2 - Coerção (Coercion): A coerção de tipo é uma forma de conversão que ocorre 
# automaticamente, sem intervenção explícita do programador. Em algumas situações, 
# a linguagem de programação realiza a coerção de tipo para que as operações sejam 
# compatíveis. Por exemplo, converter um inteiro em um ponto flutuante para permitir 
# uma operação matemática.   
#
# Em Python a Coerção de tipo em operações matemáticas, onde um inteiro é 
# automaticamente convertido para um ponto flutuante para permitir a divisão:
print("Exemplo Coerção ")
print()
print("10 / 2  apesar de 10 e 2 serem int ")
resultado = 10 / 2  
print("O inteiro foi automaticamente convertido em float")
print("tipo da variável: ", type(resultado))
print(" 10 / 2 = ", resultado)
print()
# Aqui, a coerção converte 10 em 10.0
# 
# 3 - Type Casting (Typecasting): O termo "type casting" é frequentemente usado para 
# se referir à conversão explícita de um tipo de dado em outro. O programador realiza 
# uma "fundição" (casting) para especificar que um valor deve ser tratado como um tipo 
# diferente.
# 
#Type casting explícito de um ponto flutuante para um inteiro usando
print("Exemplo Typecasting ")
print()
valor_float1 = 3.14
valor_inteiro1 = int(valor_float1)
print("tipo da variavel valor_float1 = ",type(valor_float1))
print("tipo da variavel valor_inteiro1 = ",type(valor_inteiro1))
print("valor inteiro = ", valor_inteiro1)
