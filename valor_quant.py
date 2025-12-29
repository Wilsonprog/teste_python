x = 0 # variável para armazenar

while True:
    cod = int(input("Digite o código do produto (1, 2, 3, 5 ou 9) ou se quiser parar insirá o 0: "))

    if cod == 0:
        print("Encerrando o programa...")
        break

# o While continuará solicitando o código caso o código do produto até que o usuário digite 0.

    quant = int(input("Digite a quantidade comprada: "))
    if cod == 1:
        prec = quant * 0.50
    elif cod == 2:
        prec = quant * 1.00
    elif cod == 3:
        prec = quant *  4.00
    elif cod == 5:
        prec = quant * 7.00
    elif cod == 9:
        prec = quant * 8.00
    else:
        print("Código inválido. Tente novamente.")
        continue

    x += prec

# Ao inserir os códigos, o sistema pede a quantidade irá calcular o preço dos produtos de acordo com o código inserido vezes a quantidade do produto.
# Se o código não for aquele que foi estabelecido no if ou elif, o else irá informar que o código é invalido e o loop irá continuar.

# Soma total dos valores dos produtos comprados.
print("Total a pagar: R$ {:.2f}".format(x))