print ("Cargos: ")
print ("10 - Ajudante")
print ("20 - Pedreiro")
print ("30 - Mestre de obras")
print ("40 - Arquiteto")
print ("50 - Engenheiro")
cod = input("Digite o código referente ao cargo: ")
salario = float(input("Digite o salário:"))
ajudante = float(salario) * 1.4
pedreiro = float(salario) * 1.35
mestre = float(salario) * 1.3
arquiteto = float(salario) * 1.25
eng = float(salario) * 1
if (cod == "10"):
    print(f'\nO percentual de aumento do Ajudante é de 40% e o novo salário é: {ajudante}\n')
if (cod == "20"):
    print(f'\nO percentual de aumento do Pedreiro é de 35% e o novo salário é: {pedreiro}\n')
if (cod == "30"):
    print(f'\nO percentual de aumento do Mestrede obras é de 30% e o novo salário é: {mestre}\n')
if (cod == "40"):
    print(f'\nO percentual de aumento do Arquiteto é de 25% e o novo salário é: {arquiteto}\n')
if (cod == "50"):
    print(f'\nO Engenheiro não terá aumento salarial!\n')
else:
    print("Código inválido!")