import math

def confereDelta(a, b, c):
    delta = (b**2)  - (4 * a * c)
    if delta < 0:
        return False
    return delta

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = confereDelta(a, b, c)

xv = -b/(2*a)
yv = -delta / (4*a)

if confereDelta == False:
    print("O delta é negativo, então a parabóla não encosta no eixo x, entretanto: ")
    print(f"O delta é {delta}, o x do vértice é {xv} e o y do vértice é {yv}")
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print(f"O x1 vale {x1} e o x2 vale {x2}")
    print(f"O x do vértice é {xv} e o y do vértice é {yv}")