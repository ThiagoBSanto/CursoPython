#
#
# *****************    try e except    ****************
#
#O try e except são blocos de código em Python que são 
#usados para lidar com exceções, ou seja, situações 
#imprevistas ou erros durante a execução de um programa. 
#A ideia é tentar executar um bloco de código dentro do 
#try, e se ocorrer uma exceção, o controle é transferido 
#para o bloco except, onde você pode lidar com o erro de 
#maneira adequada.
#
# A estrutura básica é a seguinte:
'''
try:
    # Código que pode gerar uma exceção
    # ...
except ExcecaoTipo1 as e:
    # Código a ser executado se ocorrer uma exceção do tipo ExcecaoTipo1
    # A variável 'e' contém informações sobre a exceção
    # ...
except ExcecaoTipo2 as e:
    # Código a ser executado se ocorrer uma exceção do tipo ExcecaoTipo2
    # ...
else:
    # Código a ser executado se NÃO ocorrer nenhuma exceção no bloco try
    # ...
finally:
    # Código a ser executado sempre, independente de ter ocorrido exceção ou não
    # ...



'''
