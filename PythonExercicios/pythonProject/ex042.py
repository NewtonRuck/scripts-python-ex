A = float(input('Medida da viga 1: '))
B = float(input('Medida da viga 2: '))
C = float(input('Medida da viga 3: '))
A, B, C = sorted([A, B, C], reverse=True)
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
    else:
        print("TRIANGULO ESCALENO")