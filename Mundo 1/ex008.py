from os import system

system('cls')

metros = int(input('Quantos metros você quer converter? '))
milimetros = (metros*1000)
centimetros = (metros*100)
decimetros = (metros*10)
quilometros = float(metros/1000)
hectometros = float(metros/100)
decametros = float(metros/10)

print('='*50)
print()
print(f'A medida de {metros} Metros corresponde a:')
print(f'Milímetros: {milimetros} mm'
      f'\nCentímetros: {centimetros} cm'
      f'\nDecímetros: {decimetros} dm'
      f'\nQuilômetros: {quilometros} km'
      f'\nHectómetros: {hectometros} hm'
      f'\nDecâmetros: {decametros} dam'
    )
print()
print('='*50)
