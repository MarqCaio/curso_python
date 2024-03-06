"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) epaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
se nada dor digitado em nome ou idade:
    exiba "Desculpa, você deixou campos vazios.
"""

nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print (f'Seu nome é {nome}.')
    print (f'Seu nome invertido é {nome[::-1]}.')
    
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print ('Seu nome NÂO contém espaços.')
    print(f'O seu nome contém {len(nome)} letras.')
    print(f'A Primeira letra do seu nome é {nome[0]}.')
    print(f'A última letra do seu nome é {nome[-1]}.')

else:
    print('Desculpe, você deixou campos vazios.')