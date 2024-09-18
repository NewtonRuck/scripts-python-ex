from datetime import date
birthyear = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - birthyear
anoalistamento = 18 + birthyear
print('Quem nasceu em {} tem {} em {}.'.format(birthyear, idade, anoatual))
if idade < 18:
    print('Ainda \033[1;34mfaltam {} anos\033[m  para o alistamento.'.format(anoalistamento - anoatual))
    print('Seu alistamento será em \033[1;34m{}\033[m.'.format(anoalistamento))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(anoalistamento))
else:
    print('Você deve se alistar \033[1;31mIMEDIATAMENTE\033[m!')