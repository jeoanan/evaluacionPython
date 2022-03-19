listaProductos=[]
print("********************************************")
print("Bienvenido a superMercados la gente de Bien!")
print("********************************************")
print("Ingresa un valor de nuestro menu para continuar")
print("Ingresa 1 para agregar un nuevo producto:")
print("Ingresa 2 para consultar nuestros productos:")
print("Ingresa 3 para editar un producto productos:")
print("Ingresa 4 para eliminar un producto:")
print("Ingresa 0 para Salir:")

menuIngresado=input("")

while(True):
    if(menuIngresado.isdigit()):
        menuIngresado=int(menuIngresado)
        if(menuIngresado<0 or menuIngresado>4):
            print("Ingresa 1 para agregar un nuevo producto:")
            print("Ingresa 2 para consultar nuestros productos:")
            print("Ingresa 3 para editar un producto productos:")
            print("Ingresa 4 para eliminar un producto:")
            print("Ingresa 0 para Salir:")
            menuIngresado=input("")
        else:
            producto={}
            if(menuIngresado == 0):
                break
            elif(menuIngresado == 1):
                codigo=input("ingrese el codigo del producto: ")
                producto['codigo']=codigo
                nombre=input("ingrese el nombre del producto: ")
                producto['nombre']=nombre
                precio=input("ingrese el precio del producto: ")
                producto['precio']=precio
                listaProductos.append(producto)          
    
            elif(menuIngresado==2):
                for producto in listaProductos:
                    print(producto)
                input("Presione enter para continuar...")
            elif(menuIngresado==3):
                buscarProducto=input("Ingrese el codigo a buscar: ")
                for producto in listaProductos:
                    for key,values in producto.items():
                        if(values == buscarProducto):
                            nuevoPrecio=int(input("Ingrese el nuevo precio: "))
                            producto['precio'] = nuevoPrecio
                            break
                        else:
                            print("El producto no existe")
                            break
                input("Presione enter para continuar...")
            else:
                buscarProducto=input("Ingrese el codigo a buscar: ")
                for producto in listaProductos:
                    for key,values in producto.items():
                        if(values == buscarProducto):
                            listaProductos.remove(producto)
                            break
                        else:
                            print("El producto no existe")
                            break
                input("Presione enter para continuar...")

            print("Ingresa 1 para agregar un nuevo producto:")
            print("Ingresa 2 para consultar nuestros productos:")
            print("Ingresa 3 para editar un producto productos:")
            print("Ingresa 4 para eliminar un producto:")
            print("Ingresa 0 para Salir:")
            menuIngresado=input("")
    else:
        print("Ingresa 1 para agregar un nuevo producto:")
        print("Ingresa 2 para consultar nuestros productos:")
        print("Ingresa 3 para editar un producto productos:")
        print("Ingresa 4 para eliminar un producto:")
        print("Ingresa 0 para Salir:")
        menuIngresado=input("")


