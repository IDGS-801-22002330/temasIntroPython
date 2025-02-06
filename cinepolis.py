import os
from io import open

class VentaBoletos:
    def __init__(self):
        self.registro_compras = {}
        self.corte_total = 0.0
        self.archivo_ventas = "ventas_cinepolis.txt"
        self.precio_boletos = 12
        self.descuento_tarjeta = 0.1
        self.max_boletos = 7

    def iniciar(self):
        while True:
            print("\nSISTEMA DE VENTA DE BOLETOS")
            print("1. Comprar boletos")
            print("2. Finalizar y borrar historial")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.procesar_compra()
            elif opcion == "2":
                self.mostrar_historial()
                self.limpiar_historial()
                break
            else:
                print("\nOpción inválida, intenta nuevamente.")

    def validar_entrada(self, mensaje, min_val=1, max_val=100):
        while True:
            try:
                valor = int(input(mensaje))
                if min_val <= valor <= max_val:
                    return valor
                else:
                    print(f"Por favor, ingresa un número entre {min_val} y {max_val}.")
            except ValueError:
                print("Entrada inválida, intenta de nuevo.")

    def procesar_compra(self):
        cliente = input("\nIngrese su nombre: ")
        num_personas = self.validar_entrada("¿Cuántas personas asistirán? (Máximo 7): ", 1, self.max_boletos)
        num_boletos = self.validar_entrada("¿Cuántos boletos desea comprar? (Máximo 7 por persona): ", 1, self.max_boletos)

        while num_boletos != num_personas:
            print("\nEl número de boletos no coincide con la cantidad de personas.")
            print("1. Ajustar la cantidad de personas")
            print("2. Ajustar la cantidad de boletos")
            seleccion = input("Seleccione una opción: ")
            if seleccion == "1":
                num_personas = self.validar_entrada("Nueva cantidad de personas: ", 1, self.max_boletos)
            elif seleccion == "2":
                num_boletos = self.validar_entrada("Nueva cantidad de boletos: ", 1, self.max_boletos)
            else:
                print("Opción inválida, intenta nuevamente.")

        total_compra = num_boletos * self.precio_boletos
        usa_tarjeta = input("¿Pagarás con tarjeta del cine? (si/no): ").strip().lower() == "si"
        descuento = self.calcular_descuento(num_boletos, total_compra, usa_tarjeta)
        total_pagar = total_compra - descuento

        self.corte_total += total_pagar

        if cliente in self.registro_compras:
            self.registro_compras[cliente][0] += num_boletos
            self.registro_compras[cliente][1] += total_pagar
        else:
            self.registro_compras[cliente] = [num_boletos, total_pagar]

        print("\nResumen de compra:")
        print(f"Comprador: {cliente}")
        print(f"Personas: {num_personas}, Boletos: {num_boletos}")
        print(f"Subtotal: ${total_compra:.2f}")
        print(f"Descuento aplicado: -${descuento:.2f}")
        print(f"Total a pagar: ${total_pagar:.2f}\n")

        self.guardar_compra()

    def calcular_descuento(self, total_boletos, precio_total, usa_tarjeta):
        descuento = 0
        if total_boletos > 5:
            descuento += precio_total * 0.15
        elif 3 <= total_boletos <= 5:
            descuento += precio_total * 0.1
        if usa_tarjeta:
            descuento += (precio_total - descuento) * self.descuento_tarjeta
        return descuento

    def guardar_compra(self):
        with open(self.archivo_ventas, "w") as archivo:
            for cliente, (boletos, total) in self.registro_compras.items():
                archivo.write(f"{cliente},{boletos},{total}\n")

    def mostrar_historial(self):
        print("\nResumen de compras:\n")
        print(f"{'Cliente':<15}{'Boletos':<10}{'Total':<10}")
        print("-" * 35)
        for cliente, (boletos, total) in self.registro_compras.items():
            print(f"{cliente:<15}{boletos:<10}${total:<10.2f}")
        print("-" * 35)
        print(f"TOTAL GENERAL: --------- ${self.corte_total:.2f}")

        print("\nSaliendo del sistema. ¡Gracias por tu compra!")

    def limpiar_historial(self):
        with open(self.archivo_ventas, "w") as archivo:
            archivo.write("")
        print("Historial de compras borrado.")

if __name__ == "__main__":
    sistema = VentaBoletos()
    sistema.iniciar()
