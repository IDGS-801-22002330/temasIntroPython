import os

def funcion1():
    os.system('cls') 
    num1 = int(input('Ingrese un numero1: ')) 
    num2 = int(input('Ingrese un numero2: ')) 
    res = num1 + num2
    print(f'Resultado: {res}')

def funcion2():
    os.system('cls')  
    num1 = int(input('Ingrese un numero1: ')) 
    num2 = int(input('Ingrese un numero2: ')) 
    res = num1 - num2
    print(f'Resultado: {res}')
    
def funcion3():
    os.system('cls')  
    num1 = int(input('Ingrese un numero1: ')) 
    num2 = int(input('Ingrese un numero2: ')) 
    res = num1 * num2
    print(f'Resultado: {res}')
    
def funcion4():
    os.system('cls')  
    num1 = int(input('Ingrese un numero1: ')) 
    num2 = int(input('Ingrese un numero2: ')) 
    res = num1 / num2
    print(f'Resultado: {res}')

def run():
    while True:
        print(' ')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Salir') 
        op = int(input('Opcion: '))
        if op == 1:
            funcion1()
        if op == 2:
            funcion2()
        if op == 3:
            funcion3()
        if op == 4:
            funcion4()
        if op == 5:
            print("Saliendo...")
            break

if __name__ == "__main__":
    run()