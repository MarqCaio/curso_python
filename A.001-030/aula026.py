"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - Força o número a aparecer antes dos zeros
sinal - + ou -
Ex.: 0>-100,.1f
conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.34729384729:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:04X}')
print(f'{variavel!r}')
