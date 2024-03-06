"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Caio'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %02X' % (15, 15))

# %.2 para formatar o tamanho depois da virgula
# %02 para formatar o tamanho do número hexadecimal