cats = {}


def comprar_entrada():
    while True:
        nombre = input("ingrese nombre del comprador: ")
        if nombre in cats:
            print("nombre ya registrado. intente con otro")
            continue
        break

    while True:
        funcion = input("ingrese entradas para la funcion 1: cats dia viernes o funcion 2: cats dia sabado: ")
        if funcion not in ["funcion 1" , "funcion 2"]:
            print("funcion no valida, debe ser funcion 1 o funcion 2 ")
            continue
        break
def mostrar_totales():
    while True:
        maximo_entradas = input("ingrese entradas a reservar: ")
        if maximo_entradas < 150:
            contador = 0 
            contador == +1
            print("entradas funcion 1")
        elif maximo_entradas < 180:
            print("entradas funcion 2")
        else:
            print("reserva exitos")

def cambio_funcion():
    nombre = input("ingrese el nombre para cambio de funcion: ")
    if nombre in cats:
        datos = cats[nombre]
        print(f"entrada: {datos["entrada"]}, funcion {datos ["funcion"]}" )
    else:
        print("cambiar a otra funcion disponible")




def main():
    while True:
        print("\ntotem autotencion cafe con leche")
        print("1.- compra entradas a cats")
        print("2.- cambio de funcion")
        print("3.-mostrar stock de funciones")
        print("4.-salir")
        opcion = input("ingrese opcion")

        if opcion == 1:
            comprar_entrada()
        if opcion == 2:
            cambio_funcion()
        if opcion == 3:
            mostrar_totales()
        if opcion == 4:
            print("programa terminado")
            break
        else:
            print("debe ingresar opcion valida")

main()



