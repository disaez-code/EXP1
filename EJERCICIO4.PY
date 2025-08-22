# -*- coding: utf-8 -*-
from typing import Dict

# Catálogo de productos con sus precios
CATALOGO: Dict[int, Dict[str, int]] = {
    1: {"nombre": "Mascarillas clínicas", "precio": 1000},
    2: {"nombre": "Guantes clínicos", "precio": 1000},
    3: {"nombre": "Delantal clínico", "precio": 2000},
    4: {"nombre": "Amonio Cuaternario", "precio": 3000},
}

EMPRESA = "Distribuidora Sanitaria Diego Ltda."
IVA = 0.19  # 19%


def mostrar_catalogo():
    """Muestra el catálogo con formato amigable."""
    print(f"\n{'-'*40}\n{EMPRESA}\n{'-'*40}")
    print("Listado de precios:\n")
    for codigo, info in CATALOGO.items():
        print(f"{codigo}) {info['nombre']:<25} ${info['precio']:>5}")
    print("-" * 40)


def calcular_total(compra: Dict[int, int], descuento: float = 0.0) -> float:
    """
    Calcula el total de la compra considerando IVA y descuento.
    :param compra: diccionario con {codigo_producto: cantidad}
    :param descuento: porcentaje de descuento (ej: 0.1 = 10%)
    :return: total final a pagar
    """
    subtotal = 0
    print("\nDetalle de compra:")
    for codigo, cantidad in compra.items():
        if codigo in CATALOGO and cantidad > 0:
            producto = CATALOGO[codigo]
            subtotal += producto["precio"] * cantidad
            print(f"- {producto['nombre']} x{cantidad}: ${producto['precio'] * cantidad}")

    if descuento > 0:
        print(f"\nDescuento aplicado: {int(descuento*100)}%")
        subtotal *= (1 - descuento)

    total = subtotal * (1 + IVA)
    return total


def ejecutar_tienda():
    """Flujo principal del programa."""
    mostrar_catalogo()

    compra = {}
    while True:
        try:
            codigo = int(input("Ingrese el código del producto (0 para finalizar): "))
            if codigo == 0:
                break
            if codigo not in CATALOGO:
                print("⚠️ Código inválido, intente nuevamente.")
                continue

            cantidad = int(input(f"Ingrese cantidad de '{CATALOGO[codigo]['nombre']}': "))
            compra[codigo] = compra.get(codigo, 0) + max(0, cantidad)

        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar números enteros.")

    aplicar_descuento = input("¿Tiene código de descuento? (s/n): ").strip().lower()
    descuento = 0.0
    if aplicar_descuento == "s":
        try:
            porcentaje = float(input("Ingrese porcentaje de descuento (ej: 10 para 10%): "))
            descuento = porcentaje / 100
        except ValueError:
            print("⚠️ Entrada inválida. No se aplicará descuento.")

    total = calcular_total(compra, descuento)
    print(f"\n{'='*40}\nTOTAL A PAGAR (IVA incluido): ${total:,.0f}\n{'='*40}")


if __name__ == "__main__":
    ejecutar_tienda()
