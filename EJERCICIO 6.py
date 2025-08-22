# 🛍️ Tienda de Mascarillas Lavables - Cálculo del Total con Envío

# Precio de cada mascarilla
precio_mascarilla = 500

# Comunas aledañas a Maipú
comunas_aledanas = ["cerrillos", "estación central", "pudahuel", "la cisterna"]

print("🔹 Bienvenido a la tienda de mascarillas lavables")
print("📍 Ventas desde la comuna de Maipú")
print("---------------------------------------------------")

try:
    # Solicitar datos al usuario
    cantidad = int(input("🔢 Ingrese la cantidad de mascarillas que desea comprar: "))
    comuna_cliente = input("🏠 Ingrese su comuna: ").strip().lower()

    # Calcular subtotal
    subtotal = cantidad * precio_mascarilla

    # Determinar costo de envío
    if subtotal > 15000:
        costo_envio = 0
        tipo_envio = "🚚 Envío gratis por compras sobre $15.000"
    elif comuna_cliente == "maipú":
        costo_envio = 1000
        tipo_envio = "📦 Envío en la misma comuna (Maipú)"
    elif comuna_cliente in comunas_aledanas:
        costo_envio = 2000
        tipo_envio = "📦 Envío a comuna aledaña"
    else:
        costo_envio = 3000
        tipo_envio = "📦 Envío a otra comuna"

    # Calcular total
    total = subtotal + costo_envio

    # Mostrar el detalle de la compra
    print("\n🧾 --- Detalle de la Compra ---")
    print(f"📍 Comuna del cliente  : {comuna_cliente.title()}")
    print(f"🛒 Mascarillas compradas: {cantidad}")
    print(f"💵 Precio unitario      : ${precio_mascarilla}")
    print(f"🧮 Subtotal             : ${subtotal}")
    print(f"{tipo_envio}")
    print(f"🚚 Costo de envío       : ${costo_envio}")
    print(f"💰 Total a pagar        : ${total}")
    print("-----------------------------------")

    # Confirmación de compra
    confirmar = input("❓ ¿Desea confirmar su compra? (sí/no): ").strip().lower()

    if confirmar in ["sí", "si"]:
        print("✅ ¡Compra confirmada! Gracias por preferirnos.")
    else:
        print("❌ Compra cancelada. Puede volver cuando lo desee.")

except ValueError:
    print("❌ Error: Ingrese un número válido para la cantidad.")

