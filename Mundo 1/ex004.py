a = input('Digite algo: ')
print('O tipo primitivo de {} é:'.format(a),type(a),
      '\nSó tem espaços?',a.isspace(),
      '\nEle é um número?',a.isnumeric(),
      '\nÉ alfabético? ',a.isalpha(),
      '\nÉ alfanumérico?',a.isalnum(),
      '\nEstá em Maiúsculas?',a.isupper(),
      '\nEstá em Minúsculas?',a.islower(),
      '\nEstá Capitalizada?',a.istitle()
    )
