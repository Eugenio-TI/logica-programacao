aluno = input('digite o nome do aluno: ')
serie = input('infome a série do aluno:')
quantidade_notas = int(input('digite a quatidade de notas'))
soma_notas = 0
media_escola = 6

for i in range(1 , quantidade_notas +1 ):
    nota = float(input(f'digite a nota {i}.: '))
    soma_notas += nota

media = soma_notas / quantidade_notas
print(f'a media das notas é {media:.2f}.')

if media >= media_escola:
    print('aprovado.')
else:
    print('reprovado.')