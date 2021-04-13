num = input("Informe um número: ")
if(num < "0"):
    print("Numero Negativo é invalido!!")
raiz = float(num) ** 0.5
qua =  float(num) ** 2
cub = float(num) * 3
soma =  float(raiz) + (qua) + (cub)
print ("Opções: ")
print ("1-  Raiz Quadrada")
print ("2- Quadrado")
print ("3- Cubo")
print ("4-  Soma de  todas as  operações acima")
opc = (input("Digite sua opção:"))
if (opc == "1"):
    print(f'\nA raiz quadrada de {num} é {raiz}\n')
if (opc ==  "2"):
    print(f'\nO quadrado de {num} é {qua}\n')
if  (opc ==  "3"):
    print(f'\nO cubo de {num} é {cub}\n')
if (opc == "4"):
    print(f'\nA soma de todas as operações é  {soma}\n')
elif (opc > "4" or opc < "1"):
    print("Opção inválida!!!")


