"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'seu nome é {nome}.')

    if nome == 'Sair':
        break
print('Acabou.')
