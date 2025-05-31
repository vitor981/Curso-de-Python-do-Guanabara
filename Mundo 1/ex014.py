from os import system

system('cls')

celsius = float(input('Digite uma temperatura em °C: '))
fahrenheit = celsius * 9 / 5 + 32

print()
print('='*40)
print()
print(f'{celsius}°C corresponde a: {fahrenheit}°F')
print()
print('='*40)
