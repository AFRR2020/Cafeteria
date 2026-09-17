def calcular_total(precio,cantidad):
    return precio*cantidad

print("================================")
print("SISTEMA PEDIDOS CAFETRIA-EL MONO")
print("================================")

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese cantidada: "))

valor_total = calcular_total(precio,cantidad)
print()
print("Pedido registrado: ")
print("Producto: ", producto)
print("Precio: $ ", precio)
print("Valor Subtotal: $ ",valor_total)
print("El producto tiene un descuento del 10%")
descuento = valor_total*0.9
print("Valor total: $ ", descuento)
