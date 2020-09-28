# Creando lista vacia
RegistroVentas =[]

# El usuario ingresa si quiere o no ingresar un cliente
opcion = 0
opcion = input("¿Deseas ingresar un cliente?: ")

#El usuario ingresa los datos de la venta
while opcion == "si":
    Cliente = input("Nombre del cliente: ")
    Producto = input("producto: ")
    Costo = float(input("costo ($0.00): "))

# Los datos ingresados se guardan en un diccionario    
    Registro = dict(Cliente=Cliente, Producto=Producto, Costo=Costo)

# los datos del diccionario son ingresados en una lista    
    RegistroVentas.append(Registro)

# Se le pregunta si desea ingresar otra venta
    opcion = input("¿Deseas ingresar otro cliente?: ")

# Se devuelven los datos ingresados    
for Registro in RegistroVentas:
    print(Registro)
CostosTotales = "Los costos totales obtenidos hasta el momento son: "
for Registro in RegistroVentas:
    print(Registro.get(Costo))