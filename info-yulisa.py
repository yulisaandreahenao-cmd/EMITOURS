nombre_proyecto = "EMITOURS"

descripcion = "Plataforma para consultar y gestionar destinos turisticos."

tecnologias = [
    "Node.js",
    "Express",
    "React",
    "Vite"
]

integrantes = [
    "Yulisa Andrea Henao Lopez"
]

funcionalidades = [
    "Consulta de destinos",
    "Gestion de usuarios",
    "Reservas turisticas"
]

def mostrar_info():
    print(f"Proyecto: {nombre_proyecto}")
    print(f"Descripcion: {descripcion}")

    print("\nTecnologias:")
    for t in tecnologias:
        print("-", t)

    print("\nIntegrantes:")
    for i in integrantes:
        print("-", i)

mostrar_info()