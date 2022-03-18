repetir=input("Ingrese la cantidad de números a ingresar: ")

while(repetir.isdigit() == False):
    print("El numero no es un entero por favor intentelo de nuevo")
    repetir=input("Ingrese la cantidad de números a ingresar: ")

repetir = int(repetir)
contadorMultiplo2=0
contadorMultiplo3=0
contadorMultiplo6=0

for i in range(repetir):
    numeroaEvualar=int(input("ingrese el numero a evaluar: "))

    if(numeroaEvualar%2 == 0 and numeroaEvualar%3 == 0):
        contadorMultiplo6+=1
    elif(numeroaEvualar%2 == 0):
        contadorMultiplo2+=1    
    elif(numeroaEvualar%3 == 0):
        contadorMultiplo3+=1

print(f"los numeros que son multiplos solo de 2 son {contadorMultiplo2}, los numeros que son solo multiplos de 3 son {contadorMultiplo3} y los numeros que son multiplos de 2 y de 3 son {contadorMultiplo6}")