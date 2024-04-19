ano_nascimento = int(input('digite o ano de seu nascimento'))
ano_atual = 2024
idade = ano_atual - ano_nascimento
if idade >=16:
    print('pode votar esse ano.')
else:
    print('nao pode votar esse ano.')