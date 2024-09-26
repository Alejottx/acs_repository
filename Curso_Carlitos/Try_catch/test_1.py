#programa que captura la edad del usuario para verificar su mayoria de edad#
#capturar edad
edad = int(input("ingrese su edad: "))
print(f"la edad ingresada por el usuario es {edad} años")
# procedemos a validar mediante el condicional "if" si el usuario es mayor de edad.
if(edad >= 18):
    print(f"usted es mayor de edad, bienvenido")
else:
    print(f"lo lamentamos,no cumple con la edad requerida")