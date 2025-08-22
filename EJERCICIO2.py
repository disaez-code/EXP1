# Programa divertido que muestra datos según el género de la persona

print("👋 ¡Bienvenida/o al sistema interactivo de registro de personas!")
print("      El objetivo de este registro es el que crea tu corazón  ")
print("-----------------------------------------------------------------")

# Ingreso de datos
nombre = input("👉 Por favor, ingresa tu nombre: ")

# Edad con validación
while True:
    edad_txt = input("👉 Ahora dinos tu edad: ")
    try:
        edad = int(edad_txt)
        if edad > 0:
            break
        else:
            print("❌ La edad debe ser un número positivo. Inténtalo nuevamente.")
    except ValueError:
        print("❌ Dato inválido: debes ingresar un valor numérico entero (por ejemplo, 23). ¡Inténtalo de nuevo!")

# Género con validación
while True:
    genero = input("👉 Ingresa tu género (M = Masculino, F = Femenino): ").upper()
    if genero in ["M", "F"]:
        break
    else:
        print("⚠ Entrada incorrecta: escribe 'M' para masculino o 'F' para femenino.")

# Celular con validación
while True:
    celular = input("👉 Finalmente, ingresa tu número de celular: ")
    if celular.isdigit() and len(celular) >= 7:
        break
    else:
        print("📵 Número inválido: el celular debe contener solo dígitos y tener al menos 7 números. Inténtalo otra vez.")

print("\n🔎 Procesando la información...\n")

# Lógica según el género
if genero == "M":
    print(f"🙋 Hola {nombre}, un hombre serio, maduro, responsable.")
    print(f"📌 Tu nombre es: {nombre}")
    print(f"📅 Tu edad es: {edad} años")
    print("✅ Información registrada con éxito, gracias por participar. 😁")

elif genero == "F":
    print(f"🙋‍♀️ Hola {nombre}, que lindo nombre *-*.")
    print(f"📌 Tu nombre es: {nombre}")
    print(f"📱 Tu número de celular es: {celular}")
    print("✅ Información registrada con éxito, gracias por participar. 💖")
