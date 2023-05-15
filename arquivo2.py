a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de a: "))
c = float(input("Informe o valor de a: "))

# Listas Python
i = -100
x = [] # Lista vazia
y = [] # Lista vazia

while i < 10:
    x.append(i) # Append = adicione isso na minha lista
    f = a*i**2 + b*i +c
    y.append(f)
    i+=1
    print(f"x = {x} \n y = {y}")