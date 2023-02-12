'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

valorHora = float(input("Digite o valor que o usuário recebe por hora:"))
horas = float(input("Digite a quantidade de horas trabalhadas no mês:"))

salarioBruto = valorHora * horas
print("O seu salário Bruto é de:", salarioBruto)

if salarioBruto <= 900.0:
    print("O valor descontado pelo Imposto de renda será de: 0.0")
    sindicato = salarioBruto * 3 /100
    print("O valor descontado pelo sindicato será de:", sindicato)
    fgts = salarioBruto * 11 /100
    print("O valor descontado pelo fgts será de:", fgts)
    salarioLiquido = salarioBruto - sindicato - fgts
    print("O seu salário líquido será de:", salarioLiquido)

elif salarioBruto > 900.0 <= 1500.0:
    impostoRenda = salarioBruto *5 /100
    print("O valor descontado pelo Imposto de renda será de:", impostoRenda)
    sindicato = salarioBruto * 3 /100
    print("O valor descontado pelo sindicato será de:", salarioBruto)
    fgts = salarioBruto * 11 /100
    print("O valor descontado pelo fgts será de:", fgts)
    salarioLiquido = salarioBruto - sindicato - fgts - impostoRenda
    print("O seu salário líquido será de:", salarioLiquido)

elif salarioBruto > 1500.0 <= 2500.0:
    impostoRenda = salarioBruto *10 /100
    print("O valor descontado pelo Imposto de renda será de:", impostoRenda)
    sindicato = salarioBruto * 3 /100
    print("O valor descontado pelo sindicato será de:", sindicato)
    fgts = salarioBruto * 11 /100
    print("O valor descontado pelo fgts será de:", fgts)
    salarioLiquido = salarioBruto - sindicato - fgts - impostoRenda
    print("O seu salário líquido será de:", salarioLiquido)

elif salarioBruto > 2500.0:
    impostoRenda = salarioBruto *20 /100
    print("O valor descontado pelo Imposto de renda será de:", impostoRenda)
    sindicato = salarioBruto * 3 /100
    print("O valor descontado pelo sindicato será de:", sindicato)
    fgts = salarioBruto * 11 /100
    print("O valor descontado pelo fgts será de:", fgts)
    salarioLiquido = salarioBruto - sindicato - fgts - impostoRenda
    print("O seu salário líquido será de:", salarioLiquido)