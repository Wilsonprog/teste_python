debt = float(input("Digite o valor da dívida: R$ ")) #valor da dívida
taxa_juros = float(input("Digite a taxa de juros mensal (%): ")) #taxa de juros mensal
meses = int(input("Digite o número de meses para pagar a dívida: ")) #número de meses para pagar a dívida   

saldo_divida = debt

x = 1
cont = 0

while x <= meses:
    saldo_divida += saldo_divida * (taxa_juros / 100)  #adiciona os juros ao saldo da dívida
    pagamento = saldo_divida / (meses - cont)          #calcula o pagamento mensal
    saldo_divida -= pagamento                           #subtrai o pagamento do saldo da dívida
    print(f"Mês {x}: saldo da dívida = R$ {saldo_divida:.2f}") #exibe o saldo da dívida do mês
    x += 1                                              #incrementa o mês
    cont += 1                                           #incrementa o contador de meses pagos


print(f"Total pago após {meses} meses: R$ {divida + (saldo_divida - divida):.2f}")