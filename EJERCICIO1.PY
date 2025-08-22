def obtener_mayor_de_tres():
    """
    Solicita tres números enteros al usuario y retorna el mayor de ellos.
    """
    try:
        numeros = []
        for i in range(1, 4):
            num = int(input(f"Ingrese el número {i}: "))
            numeros.append(num)

        mayor = max(numeros)
        print(f"\nEl número mayor es: {mayor}")

    except ValueError:
        print("⚠️ Error: debe ingresar solo números enteros.")


if __name__ == "__main__":
    obtener_mayor_de_tres()
