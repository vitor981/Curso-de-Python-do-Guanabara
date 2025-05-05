from os import system

system('cls')

reais = float(input('Digite o valor em reias na sua carteira: R$ '))
dolar = reais / 5.69

print()
print('='*40)
print()
print(f'Com: R$ {reais:.2f} \nVocê pode comprar: US$ {dolar:.2f}')
print()
print('='*40)
