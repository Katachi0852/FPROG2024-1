sexo = 'F'
idade = 60

if sexo == 'F' : #testa se a var sexo é feminino
    #aqui estarão as ações que devem executar se a avaliação if for verdadeiro
    print('É do sexo feminino')
    if idade >= 65:
        print('Possui 65 anos ou mais de idade')
    else:
        print('Possui menos de 65 anos de idade')
    
#aqui estarão as ações que devem executar se a avaliação if for falsa
else:
    print('É do sexo masculino')


if sexo == 'F' and idade >= 65:
    print('É uma pessoa do sexo feminino com mais de 65 anos.')

###

mediaFinal = 6.0
frequencia = 0.75

if mediaFinal < 6.0:
    print('Reprovado por média inferior a 6.0!')
elif frequencia < 0.75:
    print('Reprovado por faltas!')
else:
    print('Aprovado!')

if (mediaFinal < 6.0 or frequencia < 0.75):
    print('Reprovado!')
    if mediaFinal < 6.0:
        print('Reprovado por média baixa!')