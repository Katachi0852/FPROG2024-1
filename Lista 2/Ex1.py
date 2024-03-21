#Ler a quantidade de minutos para converter
minutos = float(input('Digite o tempo em minutos: '))

segundos = minutos * 60

print('\n',minutos, ' minuto(s) é igual a ',segundos, ' segundos\n')

#Conversão de doláres para real
dolar = float(input('Digite a quantidade de dólares que deseja converter: '))

real = dolar * 4.97

print(dolar, ' doláres equivale a ',real, 'reais.\n')

#

peso = float (input('Digite em gramas o peso do prato: '))

valor = peso / 100 * 40

print('O valor total do prato é igual a R$ ',valor,'\n')

#

grauA = float (input('Digite sua nota do grau A: '))

print('')

grauB = float (input('Digite sua nota do grau B: '))

media = (grauA + grauB) / 2

print('\nSua média final é ',media,'\n')

#

litroGasulina = float (input('Digite o preço da gasolina: '))

reais = float (input('Quantos reais você tem par abastecer o carro? '))

abastecido = reais / litroGasulina

print('Você conseguira abastecer',abastecido,'litros de gasolina')

#

celular = int (input('Digite a quantidade de smartphones que foram vendidos no dia de hoje: '))

tablets = int (input('Digite a quantidade de tablets que foram vendidos no dia de hoje: '))

totalCelular = celular * 1000

totalTablets = tablets * 1500

print('\nO faturamento com a venda de celulares no dia de hoje foi de',totalCelular,'\n')

print('O faturamento com a venda de tablets no dia de hoje foi de',totalTablets,'\n')

FaturamentoTotal = totalTablets + totalCelular

print('O faturamento total do dia de hoje foi de: ', FaturamentoTotal,'\n')

#

passaros = int (input('Digite a quantidade de pássaros: '))

racao = passaros * 0.30

print('A quantidade de ração necessária para hoje é',racao,'gramas\n')

#

grauCelsius = float (input('Digite a temperatura em graus celsius: '))

grausF = (grauCelsius * 9/5) + 32

print(grauCelsius,'grau(s) Celsius equivale a',grausF,'graus fahrenheit\n')

#

compra = float(input('Digite o valor da compra: '))

desconto = compra * 0.15

total = compra - desconto

print('O valor total da compra com o desconto ficou',total,'\n')

#

camisetas = int (input('Digite a quantidade de camisetas compradas: '))

calcas = int (input('\nDigite a quantidade de calças compradas: '))

cintos = int (input('\nDigite a quantidade de cintos comprados: '))

totalCamisetas = camisetas * 25

totalCalcas = calcas * 100

totalCintos = cintos * 40

total = totalCalcas + totalCamisetas + totalCintos

desconto = total * 0.1

totalDesconto = total - desconto

print('\nO valor total de compra com o desconto ficou R$',totalDesconto,'\n')