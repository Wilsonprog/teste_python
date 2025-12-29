s = 0 # variável para armazenar o valor

while True: # se while for verdadeiro, o loop continuará a executar a variável v
    v = int(input("Digite um valor (até digitar 0 para parar): ")) # solicita ao usuário que insira o valor até inserir 0
    if v == 0: 
        break # se o valor v for igual á 0, o while será interrompido
    s += v #  soma a variável s com a variável v
    print("valor somado: {}".format(s)) # Exibe o quanto foi somado até o usuário inserir 0

print("Valor total somado é {}".format(s)) # Exibe o valor total que foi somado, assim que o usuuário inserir 0
