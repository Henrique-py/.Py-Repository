print("**********************************************")
print("*                                            *")
print("*           Restaurante Mosca Frita          *")
print("*                                            *")
print("**********************************************")
print("*                                            *")
print("*                                            *")
print("*  Escolha o cardápio que deseja visualizar  *")
print("*                                            *")
print("*Dia       Prato principal          Opção    *")
print("*Domingo   Macarronada              Dom      *")
print("*Quarta    Feijoada                 Qua      *")
print("*Sexta     Peixe Grelhado           Sex      *")
print("*Sábado    Churrasco                Sab      *")
print("*                                            *")
print("**********************************************")
opc = input("Digite a opção desejada: ")
if (opc == "Dom"):
    print("Opção escolhida: Domingo")
    print("Prato do dia: Macarronada")
    preco = print("R$12.90")
    qtde = int(input("Digite a quantidade: "))
    total = 12.90 * qtde
    desc = total * 0.10
    desc1 = total - desc
    print ("O valor a ser pago: ",total)
if (opc == "Qua"):
    print("Opção escolhida: Quarta")
    print("Prato do dia: Feijoada")
    preco = print("R$15.50")
    qtde = int(input("Digite a quantidade: "))
    total = 15.50 * qtde
    desc = total * 0.10
    desc1 = total - desc
    print("O valor a ser pago: ",total)
if (opc == "Sex"):
    print("Opção escolhida: Sexta")
    print("Prato do dia: Peixe Grelhado")
    preco = print("R$11.00")
    qtde = int(input("Digite a quantidade: "))
    total = 11 * qtde
    desc = total * 0.10
    desc1 = total - desc
    print ("O valor a ser pago: ",total)
if (opc == "Sab"):
    print("Opção escolhida: Sábado")
    print("Prato do dia: Churrasco")
    preco = print("R$14.30")
    qtde = int(input("Digite a quantidade: "))
    total = 14.30 * qtde
    desc = total * 0.10
    desc1 = total - desc
    print ("O valor a ser pago: ",total)
des = input("Desconto? (S/N): ")
if (des == "S" or "s"):
    print("Desconto concedido: 10%")
    print("Valor do desconto: ",0.10 *total)
    print("Valor a ser pago: ", desc1)
if des == "N" or "n":
    print ("Valor a ser pago sem desconto: ",total)