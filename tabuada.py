lista = [1,2,3,4,5,6,7,8,9,10]

for item, in lista:
    print(f'tabuada de {item} \n')

    numero = item
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')    
