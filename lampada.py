problema = ('a lampada funciona')
print  ('a lampada estava plugada ?')
resposta = input('digite se sim ou não:  ')

if resposta == "não":
    print  ('plugar a lampada.')
else:
    print('o bulbo queimou?')
    resposta2 = input('digite se sim ou não: ')
    if resposta2 == 'sim':
        print('trocar bulbo.')
    else:
        print('trocar lampada.')
