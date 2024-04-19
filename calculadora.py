numero1 =float(input('informe seu valor'))
operacao =str(input('operacao'))
numero2 =float(input('informe seu valor'))
resultado = 0

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    operacao = numero1 / numero2
else:
    print('invalido')
print(resultado,'resultado final da sua conta')