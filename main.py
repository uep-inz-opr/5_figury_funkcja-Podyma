import math
liczba_figur = int(input())

suma_pol=0
for i in range(liczba_figur):
  dane_figury = input().split(" ") 
  if len(dane_figury)==3:
        p = (float(dane_figury[0]) + float(dane_figury[1]) + float(dane_figury[2])) / 2 #połowa obwodu figury
        pole_trojkata = math.sqrt(p*(p - float(dane_figury[0]))*(p - float(dane_figury[1]))*(p - float(dane_figury[2])))
        suma_pol = suma_pol + pole_trojkata
  elif len(dane_figury)==2:
        pole_prostokatu = float(dane_figury[0]) * float(dane_figury[1])
        suma_pol = suma_pol + pole_prostokatu
  elif len(dane_figury)==1:
        pole_kola = 2 * math.pi * float(dane_figury[0])
        suma_pol = suma_pol + pole_kola
  else: 
      continue
    
print(round(suma_pol,2))
