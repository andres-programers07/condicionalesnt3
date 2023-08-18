nombreusuario = input("ingrese su nombre: ")
usuarioedad = int(input("ingrese su edad: "))

if usuarioedad <= 15:
    print(f"querido {nombreusuario}, usted es un menor")
elif usuarioedad > 15 and usuarioedad <= 28:
    print(f"querido {nombreusuario}, usted es un joven")
elif usuarioedad > 28 and usuarioedad <= 60:
    print(f"querido {nombreusuario}, usted es un adulto")
else:
    print(f"querido {nombreusuario}, usted es un adulto mayor")