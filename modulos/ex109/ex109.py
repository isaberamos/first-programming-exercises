import moeda


p = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Aumentando 10% sobre o preço temos {moeda.aumento(p, 10, True)}")
print(f"Reduzindo 13% sobre o preço temos {moeda.desconto(p, 13, True)}")
