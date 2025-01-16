'''
range(20) #0, 1, 2, ..., 19
x=range(10, 20) # Desde el 10 = 10, 11, 12, ..., 20
y=range(1, 20, 2)

for i in range(20):
    print(i)
'''   
    
# Usando FOR y pidiendo al usuarioun numero, que imprima la tabla de multiplicar del numero como:
# 7 x 1 = 7
# 7 x 2 = 14

num=int(input("ingrese el numero a multiplicar:"))
for i in range(1, 11):
    res=num*i
    print(f"{num} x {i} = {res}")
