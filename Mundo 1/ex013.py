from os import system

system('cls')

salario = float(input('Digite o salario do funcionario: R$ '))
aumento = salario + (salario * 15 / 100)

print()
print('='*40)
print(f'Salario sem aumento: R$ {salario:.2f} \nSalario com aumento de 15%: R$ {aumento:.2f}')
print()
print('='*40)