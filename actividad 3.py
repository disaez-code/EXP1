# Programa para mostrar la tabla de multiplicar de un número positivo

print("📌 Tabla de Multiplicar (1 al 10)")
print("-----------------------------------")

# Solicitar al usuario un número positivo
try:
    numero = int(input("🔢 Ingrese un número positivo: "))

    # Verificar que el número sea positivo
    if numero > 0:
        print(f"\n✅ Tabla de multiplicar del {numero}:")
        print("-----------------------------------")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero:2} x {i:2} = {resultado:3}")
    else:
        print("⚠️ Error: El número ingresado no es positivo.")
except ValueError:
    print("❌ Entrada no válida. Por favor, ingrese un número entero.")

