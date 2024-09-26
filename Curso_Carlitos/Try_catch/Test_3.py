#programa que captura la edad del usuario para verificar su mayoria de edad#
#capturar edad
try:
    edad = int(input("ingrese su edad: "))
except:
    print(f"valor ingresado no valido")
    exit()

print(f"la edad ingresada por el usuario es {edad} años")

if(edad >=0 and edad <150):

    # procedemos a validar mediante el condicional "if" si el usuario es mayor de edad.
    if(edad >= 18):
        print(f"usted es mayor de edad, bienvenido")
    else:
        print(f"lo lamentamos,no cumple con la edad requerida")
else:
    print(f"no cumple con el rango establecido")
