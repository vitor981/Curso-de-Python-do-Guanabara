from os import system

system('cls')

altura = float(input('Digite a altura da parede: '))
largura = float (input('Digite a largura: '))
area = altura * largura
tinta = area / 2

print()
print('='*60)
print()
print(f'Sua parede tem a dimensão de {altura} X {largura} e uma área de {area}m². \nPara Pintar essa parede você precisará de {tinta}L de tinta.')
print()
print('='*60)