# Uso F-String
nome = 'Yuri'
print(f"Olá, {nome}")

num = 15
print(f'{num} + 10 = {num + 10}')

print(f"""Este é mais um exeplo de uso da {"F-String"}""")

print(f'5 {"{Estrelas}"}')
print(f'{{5}} {"Estrelas"}')

nome = 'Yuri'
idade = 27
print(f"""Olá!
...     Me chamo {nome}.
...     Tenho {idade} anos.""")


# Preenchimento
print(f'{"exemplo":15}')        # Determinando um tamanho
print(f'{"exemplo":*>15}')      # Preenchendo a esquerda
print(f'{"exemplo":*<15}')      # Preenchendo a direita
print(f'{"exemplo":*^15}')      # Centralizando
print(f'{12345:0>15}')          # Preenchendo com números

# Tipagem
print(f'{10:b}')            # binario
print(f'{10:o}')            # octal
print(f'{200:x}')           # hexadecimal
print(f'{200:X}')           # Hexadecimal
print(f'{345600000000:e}')  # notação científica
print(f'{65:c}')            # caractere
print(f'{10:#b}')           # binário com notação
print(f'{10:#o}')           
print(f'{10:#x}')
