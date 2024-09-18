#Informe do sexo onde r irá vir com letra maiúscula, sem espaços
#e apenas a primeira letra contará
r = str(input('Digite seu sexo: ')).upper().strip()[0]
while r not in 'MmFf':
    r = str(input('Dados inválidos, por favor informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(r))