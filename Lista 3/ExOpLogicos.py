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