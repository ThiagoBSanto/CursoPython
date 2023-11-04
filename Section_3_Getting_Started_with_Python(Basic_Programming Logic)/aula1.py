#
#
# *****************    INTERPRETADOR PYTHON    ****************
#
# O interpretador Python é um programa que executa código Python,
# traduzindo-o em instruções compreensíveis pelo computador.
#
#
# *****************    COMENTÁRIO EM PYTHON    ****************
#
print("COMENTÁRIOS")
print()
#
# Comentários em Python são trechos de texto inseridos em seu 
# código fonte para fornecer informações ou explicações úteis. 
# Comentários não têm impacto na execução do programa; eles são 
# ignorados pelo interpretador Python. Os comentários são usados 
# para documentar o código, torná-lo mais legível e facilitar a 
# compreensão do que está acontecendo em um programa. Aqui estão 
# alguns detalhes importantes sobre comentários em Python:
#
# 1 - Sintaxe de Comentário: 
# Em Python, você pode criar um comentário colocando um # (hashtag)
# no início de uma linha. Tudo que segue o # na mesma linha é tratado
# como um comentário e não é interpretado pelo Python.
#
print("Exemplo 1:")
# Isto é um comentário
print("Isso é um código real")
print()
#
# 2 - Comentários de Múltiplas Linhas: Python não tem suporte nativo 
# a comentários de múltiplas linhas no estilo de /* ... */ que algumas 
# outras linguagens possuem. Em vez disso, você pode criar comentários 
# de várias linhas usando várias linhas de comentários de linha única.
#
# Exemplo 2:
# Este é um comentário de múltiplas linhas
# que é dividido em várias linhas.
#
# 3 - Boas Práticas de Comentários: É importante usar comentários para 
# tornar o código mais claro, mas não exagere. Comentários devem explicar
# o "por quê" e não o "o quê" (a menos que o código não seja óbvio). 
# Mantenha os comentários concisos e relevantes.
#
# 4 - Remoção de Comentários: Comentários não são executados, mas permanecem 
# no código-fonte. Portanto, é importante manter os comentários atualizados e 
# remover comentários desnecessários, pois podem tornar o código desordenado.
#
# OBS -> COMENTÁRIO
#   Comentários bem escritos são uma prática recomendada no desenvolvimento 
#   de software, pois ajudam os desenvolvedores a entender e manter o código, 
#   facilitam a colaboração e a depuração, e melhoram a legibilidade do código.
#
#
# *****************    DOCSTRING EM PYTHON    ****************
#
# OBS -> DOCSTRING
#   EMBORA AS FUNÇÕES SEJAM MAIS AVANÇADAS DO QUE O CONTEÚDO ESTUDADO ATÉ  O 
#   MOMENTO, ESTOU INCLUINDO-AS AQUI PARA REFERÊNCIA FUTURA E FACILITAR CONSULTAS. 
# 
# Uma docstring (document string) em Python é uma convenção usada para fornecer 
# documentação embutida em um programa, módulo, classe ou função. A docstring é 
# uma string (cadeia de caracteres) que descreve o que a entidade documentada faz, 
# como ela deve ser usada e outras informações relevantes. Ela é colocada dentro de
# aspas triplas (simples ou duplas) como o primeiro item do corpo de um módulo, 
# classe ou função, e é opcional, mas altamente recomendada para documentar seu 
# código de maneira clara e compreensível.
# 
# 1 - Docstrings de Módulo:
# Colocadas no início de um módulo para descrever seu propósito e funcionalidade geral.
#
# Exemplo 3:
"""
Este é um exemplo de docstring de módulo.
Ele descreve o objetivo geral do módulo.
Pode conter informações sobre como usar o módulo ou qualquer outra informação 
relevante.
"""
#   # Código do módulo continua aqui
#
# 2 - Docstrings de Função/Classe: 
# Colocadas no início de uma função ou classe para descrever o que a função 
# ou classe faz, seus parâmetros e seu retorno.
#
# Exemplo 4:
# def minha_funcao(parametro1, parametro2): (cria uma função)
"""
Esta é a docstring de uma função.
Descreve o que a função faz, seus parâmetros e o que ela retorna.
"""
#   # Código da função continua aqui
#
# As docstrings são usadas não apenas para documentar o código, mas 
# também podem ser acessadas programaticamente, tornando-as úteis 
# para a geração automática de documentação ou para uso em IDEs e 
# ferramentas de desenvolvimento.
#
# pode usar a função help() ou acessar o atributo __doc__ para obter 
# informações da docstring de um módulo, função ou classe em tempo 
# de execução.
# Aqui está um exemplo de uso da função help() em um módulo ou 
# função com uma docstring:
#
# def minha_funcao(parametro1, parametro2):
#
"""
Esta é a docstring de uma função.
Descreve o que a função faz, seus parâmetros e o que ela retorna.
"""
#
# Código da função continua aqui
#
# help(minha_funcao)
#
# Quando você executa help(minha_funcao), a docstring será exibida na 
# saída, fornecendo informações úteis sobre a função.