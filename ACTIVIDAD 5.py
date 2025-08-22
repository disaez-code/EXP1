# Nombre de la empresa
print("========================================")
print("     SÁNDWICHES EXPRESS DELIVERY        ")
print("========================================")
print("Lista de precios:")
print("1. Churrasco      : $1500")
print("2. Completo       : $1000")
print("3. Vegetariano    : $2000")
print("4. Barros Luco    : $3000")
print("========================================")
print(" ")
print(" ")
print("¡Buen dia!, digame...")


churrascos = int(input("¿Cuantos churrascos va a querer?: "))
completos = int(input("Tambien tenemos completos: "))
vegetarianos = int(input("¿Va a querer algun vegetariano?: "))
barros_luco = int(input("¿Y va a querer algun barros luco?: "))


subtotal = (churrascos * 1500) + (completos * 1000) + (vegetarianos * 2000) + (barros_luco * 3000)


iva = subtotal * 0.19
total_con_iva = subtotal + iva


codigo = input("¿Tiene código de descuento? (s/n): ")

if codigo == "s" or codigo == "S":
    descuento = total_con_iva * 0.10
else:
    descuento = 0

# Total final
total_final = total_con_iva - descuento

# Mostrar resumen
print("\n========================================")
print("Resumen de la compra:")
print("Churrascos     x", churrascos, " = $", churrascos * 1500)
print("Completos      x", completos, " = $", completos * 1000)
print("Vegetarianos   x", vegetarianos, " = $", vegetarianos * 2000)
print("Barros Luco    x", barros_luco, " = $", barros_luco * 3000)
print("----------------------------------------")
print("Subtotal           : $", round(subtotal))
print("IVA (19%)          : $", round(iva))
print("Descuento (10%)    : -$", round(descuento))
print("----------------------------------------")
print("TOTAL A PAGAR      : $", round(total_final))
print("========================================")
print("¡Gracias por su compra!¡Vuelva pronto!")
