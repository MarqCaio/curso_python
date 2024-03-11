"""
EXERCÍCIO 01
Faça um programa que peça ao usuário para digitar um número,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
 
if numero.isdigit(): # Checa se o usuário digitou só números
    numero_int = int(numero) # Converte para um número inteiro
    par_impar = numero_int % 2 == 0 # Resto da divisão = a 0, resposta PAR
    par_impar_texto = 'ímpar' # define a msg ímpar

    if par_impar:
        par_impar_texto = 'par' # Define a msg par

    print(f'O número {numero_int} é {par_impar_texto}.')
else:
    print(f'{numero}, não é um número inteiro.')


"""
EXERCÍCIO 02
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
horario = input('Digite a hora, apenas números inteiros. ')

try:
    hora = int(horario)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Hora não reconhecida')
except:
    print('Digite apenas valores inteiros.')
"""

"""
EXERCÍCIO 03
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome) #len retorna o tamanho

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite mais de uma letra.')
"""