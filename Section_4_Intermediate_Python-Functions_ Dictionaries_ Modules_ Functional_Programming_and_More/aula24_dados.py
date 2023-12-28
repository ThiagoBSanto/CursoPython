import copy
from aula24 import produtos

novos_produtos = copy.deepcopy(produtos)

print(*produtos,sep='\n')
print()
print(*novos_produtos,sep='\n')