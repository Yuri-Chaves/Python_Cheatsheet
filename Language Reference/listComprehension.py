precos = [50, 500, 1500, 2000, 3000, 4000, 785]

# Caso 1
novo_preco = []
for preco in precos:
    novo_preco.append(preco * 1.025)
print(novo_preco)

# Caso 2
imposto = []
for preco in precos:
    if preco >= 2000:
        imposto.append(preco * 1.1)
print(imposto)

#  com List Comprehension

# Caso 1
novo_preco = [preco * 1.025 for preco in precos]
print(novo_preco)

# Caso 2
imposto = [preco * 1.1 for preco in precos if preco >= 2000]
print(imposto)