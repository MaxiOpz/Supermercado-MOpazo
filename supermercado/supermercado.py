def productoMasCaro(productos): #Crea la funcion productoMasCaro con el parametro productos
  Lineas = productos.readlines() #Guarda en Lineas el contendio que lee con .readlines()
  Pcaro = "" #Guarda un string vacio en la variable Pcaro
  Mprice = 0 #Guarda el valor 0 en la variavle Mprice
  for l in Lineas: #Recorre cada linea de la variable Lineas y lo guarda en l
    idProducto, nombre, precio, cantidad = l.strip().split(",") #Separa cada dato correspondientemente con .strip para evitar espacios o cosas innecesarias y lo separa por , con .split
    if float(precio) > Mprice: #si el precio es mayor a la variable Mprice...
      Mprice = float(precio) #Se actualiza la variable con el valor de precio y...
      Pcaro = nombre #Guarda en Pcaro el nombre del producto
    return Pcaro #Devuelve Pcaro, el nombre del producto

with open('productos.csv', 'r') as productos:
  print(productoMasCaro(productos))

def valorTotalBodega(productos): #Crea la funcion valorTotalBodega con el parametro productos
  Lineas = productos.readlines() #Guarda en Lineas las lineas que lee con .readlines()
  TValue = 0 #Establece en 0 la variable TValue
  for l in Lineas: #Recorre cada linea de la variable Lineas y lo guarda en l
    idProducto, nombre, precio, cantidad = l.strip().split(",") #Separa cada dato correspondientemente con .strip para evitar espacios o cosas innecesarias y lo separa por , con .split
    TValue += float(precio) * float(cantidad) #Suma a TValue la multiplicacion del precio y la cantidad
  return TValue #Devuelve TValue

with open('productos.csv', 'r') as productos:
  print(valorTotalBodega(productos))

  import csv #Importa la libreria csv
def productoConMasIngresos(items, productos): #Crea la funcion productoConMasIngresos con los parametros items y productos
    productosD = list(csv.reader(productos, delimiter=',')) #Guarda en la variable productosD la lectura del archivo con csv.reader utilzando , como separador y lo convierte en una lista

    InfoProductos = {} #Crea un diccionario vacio
    for Prod in productosD: #Recorre productosD y lo guarda en Prod
            IdProducto = Prod[0] #Guarda en IdProducto el dato que aparece al principio de cada linea en Prod
            Nombre = Prod[1] #Guarada en Nombre el dato que aparece de segundo en cada linea en Prod
            Precio = float(Prod[2]) #Guarda en Precio el dato que esta en la tercera posicion de la linea y lo convierte a decimal con float
            InfoProductos[IdProducto] = {"nombre" : Nombre, "precio" : Precio} #Crea una entrada al diccionario con la id como clave

    itemsD = list(csv.reader(items, delimiter=';')) #Guarda en la variable itemsD la lectura del archivo con csv.reader utilizando ; como separador y lo convierte en una lista

    Ingresos = {} #Crea un diccionario vacio
    for item in itemsD: #Recorre itemsD y guarda en item
        IdProducto = item[1] #Guarda en IdProducto el segundo dato de item
        Cantidad = int(item[2]) #Guarda en Cantidad el tercer dato de item convertido en int
        Precio = InfoProductos[IdProducto]["precio"] #Busca el producto por la ID, extrae el "precio" y lo guarda en Precio
        Ingresos[IdProducto] = Ingresos.get(IdProducto, 0) + Cantidad * Precio #Busca por ID, con .get busca una clave en el diccionario si existe da el valor si no existe da 0, a eso le suma la multiplicacion de la cantidad por el precio

    IdMPro = max(Ingresos, key=Ingresos.get) #Max da la clave del diccionario con mayor valor, key=ingresos.get indica que se ocupa los ingresos de cada producto para la comparacion
    return InfoProductos[IdMPro]["nombre"] #Busca por el valor mas grande y devuelve el nombre

with open('productos.csv', 'r') as productos:
  with open('items.csv', 'r') as items:
   print(productoConMasIngresos(items, productos))

import csv #Importa la libreria csv
from datetime import datetime #importa datetime para las fechas

def totalVentasDelMes(año, mes, items, productos, ventas): #Crea la funcion totalVentasDelMes con los parametros año, mes, items, productos y ventas
    produD = list(csv.reader(productos, delimiter=',')) #Guarda en ProduD la lectura de productos separada por ,

    InfoProductos = {} #Crea un diccionario vacio
    for p in produD: #Recorred produD y guarda en p
            IdProducto = p[0] #Guarda en IdProducto el primer dato de p
            precio = float(p[2]) #Guarda en Precio el tercer dato de p y lo convierte en float
            InfoProductos[IdProducto] = {"precio": precio} #Crea una entrada al diccionario con la ID como clave

    ventasD = list(csv.reader(ventas, delimiter=';')) #Guarda en ventasD la lectura de ventas separad por ;

    VentasMen = set() #Crea un conjunto vacio
    for venta in ventasD:  #Recorre cada venta de ventasD
            Nboleta = venta[0] #Guarda el primer dato(Numero de boleta) en Nboleta
            Fechastr = venta[1] #Guarda como string el segundo dato(fecha) en Fechastr
            fecha = datetime.strptime(Fechastr, '%d-%m-%Y') #Convierte el string a un objeto datetime

            if fecha.year == año and fecha.month == mes: #Verifica si la venta es de la fecha que buscamos
                VentasMen.add(Nboleta)  #Agrega el numero de boleta al conjunto

    ItemsD = list(csv.reader(items, delimiter=';')) #Lee el archivo items, separado por ;

    VTotalV = 0  #Establece la variable VTotalV, que representa el total de ventas, en 0
    for item in ItemsD:  #Recorre cada item de ItemsD
            Nboleta2 = item[0] #Guarda el primer dato de item(Numero de boleta) en Nboleta2

            if Nboleta2 in VentasMen: #Verifica si la boleta es del mes que buscamos
                IdProducto = item[1] #Guarda el segundo dato(Id del producto) en IdProducto
                cantidad = int(item[2]) #Guarda el tercer dato(Cantidad) en Cantidad

                precio = InfoProductos[IdProducto]["precio"]  #Guarda en precio el precio del producto obtenido a traves de la clave
                VTotalV += cantidad * precio #Suma a la variable VTotalV el valor de cantidad multiplicado por precio

    return int(VTotalV) #Devuelve VTotalV

with open('productos.csv', 'r') as productos:
  with open('items.csv', 'r') as items:
    with open('ventas.csv', 'r') as ventas:
      print(totalVentasDelMes(2010, 10, items, productos, ventas))
