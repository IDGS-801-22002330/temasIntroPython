
x=0

while x<10:
    print(x)
    x=x+1

'''operacion de multiplicacion de a x b utilizando sumas
a=3
b=4
salida: 3+3+3+3=12
'''

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

resultado = 0
c = 0
suma = ""

while c < b:
    resultado = a*b
    suma += "{}+".format(a)
    c += 1
    if c == b:
        suma += "{}".format(a)

print("{}={}".format(suma, resultado))