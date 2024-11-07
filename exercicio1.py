import random

aposta1 = int(input('Digite o primeiro número da sua aposta (0 a 9): '))
aposta2 = int(input('Digite o segundo número da sua aposta (0 a 9): '))

if aposta1 < 0 or aposta1 > 9 or aposta2 < 0 or aposta2 > 9:
    print('Os números apostados devem estar entre os numeros 0 e 9')
else:
    numeros_sorteados = [random.randint(0, 9) for _ in range(4)]
    print('Números sorteados:', numeros_sorteados)

acertos = 0
if aposta1 in numeros_sorteados:
    acertos += 1
if aposta2 in numeros_sorteados:
    acertos += 1

if acertos == 1:
    premio = 1000
elif acertos == 2:
    premio = 2000
else: 
    premio = 0 

print('Premio: R$:', premio)