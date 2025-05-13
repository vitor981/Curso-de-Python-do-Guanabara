from os import system

system('cls')

produto = float(input('Digite o valor do produto: R$ '))
desconto = produto - (produto * 5 / 100)

print()
print('='*40)
print()
print(f'Preço original: R$ {produto:.2f} \nDesconto de 5% aplicado: R$ {desconto:.2f}')
print()
print('='*40)
