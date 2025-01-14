
texto1="Hola"
texto2="mundo"

textoFinal=texto1+" "+texto2
print(textoFinal)

print("El saludo es: %s %s" %(texto1, texto2))

saludoFinal2="Saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)

texto ="desarroyo web profecional utl"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("al"))
print(texto.count("e"))

print(texto.replace("y","ll"))
cadenaSeparada=texto.split(" ")
print(cadenaSeparada)
