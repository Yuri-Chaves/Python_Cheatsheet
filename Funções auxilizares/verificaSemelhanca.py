# Verificar a semelhança entre duas Strings
import unicodedata
from difflib import SequenceMatcher
def str_normalized(string):
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()
# retorna a string decodificada seguindo o padrão ascii
def similaridade(str1, str2):
    str1 = str_normalized(str1)
    str2 = str_normalized(str2)
    return SequenceMatcher(None, str1, str2).ratio()
# retorna um valor entre 0 e 1 indicando a porcentagem de semelhança entre as strings

print(similaridade('frases iguais', 'frases iguais'))
print(similaridade('frases diferentes', 'frases iguais'))
print(similaridade('esta frase é completamente diferente', 'não está nada igual'))
