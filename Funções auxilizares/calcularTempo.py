# Calcular tempo de execução
import time

qtdd = 24387  # Repetições
tepu = 4.5  # Tempo de execução unitário
segt = qtdd * tepu
dias = int(segt / 86400)
hors = int((segt - (dias * 86400)) / 3600)
mins = int((segt - ((dias * 86400) + (hors * 3600)))/60)
segs = int(segt - (int(segt/60))*60)
if dias > 0:
    print(f'{dias}d {hors}h {mins}min {segs}seg')
elif dias ==  0 and hors > 0:
    print(f'{hors}h {mins}min {segs}seg')
elif dias ==  0 and hors == 0 and mins > 0:
    print(f'{mins:02}min {segs}seg')
else:
    print(f'{segs}seg')