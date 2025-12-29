x = 0
sum = 0

while True:
    n = int(input("Digite os valores (até digitar 0): "))
    if n == 0:
        break
    x += n
    sum += 1
    média = x / sum

print("Total será de {} | Média é de {:.2f}".format(x, média))