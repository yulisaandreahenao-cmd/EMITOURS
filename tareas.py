# Seguimiento Proyecto Turismo

pendientes = [
    "Implementar módulo de pagos",
    "Generar reportes",
    "Realizar pruebas finales"
]

completadas = [
    "Diseño de base de datos",
    "Registro de usuarios",
    "Diseño de pantallas"
]

en_progreso = [
    "CRUD de reservas",
    "Conexión con MySQL"
]

print("=" * 40)
print("SEGUIMIENTO DEL PROYECTO")
print("=" * 40)

print("\n✅ COMPLETADAS:")
for t in completadas:
    print(f"   ✅ {t}")

print("\n🔧 EN PROGRESO:")
for t in en_progreso:
    print(f"   🔧 {t}")

print("\n⬜ PENDIENTES:")
for t in pendientes:
    print(f"   ⬜ {t}")

print("\n" + "=" * 40)
print(f"Total tareas: {len(completadas) + len(en_progreso) + len(pendientes)}")
print(f"Completadas: {len(completadas)}")
print(f"Pendientes: {len(pendientes)}")
