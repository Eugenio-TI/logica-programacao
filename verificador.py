import time
usuario = input('digite seu usuario: ')
time.sleep (0.50)
senha   = input('digite sua senha:   ')
time.sleep (0.50)
if usuario == 'eugenio' and senha == '123':
    print('acesso concedido!')
else:
    print('acesso negado!   ')
time.sleep (0.50)