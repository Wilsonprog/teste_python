deposit_start = float(input("Digite o depósito inicial: ")) #depósito inicial
deposito_mounth = float(input("Digite o valor do depósito mensal: ")) #depósito mensal
feels = float(input("Digite a taxa de juros mensal (%): ")) #taxa de juros mensal

balance = deposit_start #saldo inicial
month = 1 #variável para contar os meses

while month <= 12:
    balance += deposito_mounth        #adiciona o depósito mensal 
    balance += balance * (feels / 100)          #adiciona os juros ao saldo
    print(f"Mês {month}: saldo = R$ {balance:.2f}") #exibe o saldo do mês
    month += 1 #incrementa o mês

total_deposit = deposit_start + deposito_mounth * 12 #total depositado no ano
total_feels = balance - total_deposit #total ganho com juros

print(f"Total deposit: R$ {total_deposit:.2f}")
print(f"Final balance: R$ {balance:.2f}")
print(f"total earned with interest: R$ {total_feels:.2f}")