class AgendaContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, correo):
        self.contactos[nombre] = {'Teléfono': telefono, 'Correo': correo}
        print(f"Contacto {nombre} agregado correctamente.\n")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {self.contactos[nombre]['Teléfono']}")
            print(f"Correo: {self.contactos[nombre]['Correo']}\n")
        else:
            print("Contacto no encontrado.\n")
    
    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for nombre, info in self.contactos.items():
                print(f"Nombre: {nombre}, Teléfono: {info['Teléfono']}, Correo: {info['Correo']}")
            print()
        else:
            print("No hay contactos en la agenda.\n")


def menu():
    agenda = AgendaContactos()
    while True:
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            agenda.agregar_contacto(nombre, telefono, correo)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == "3":
            agenda.mostrar_contactos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")


if __name__ == "__main__":
    menu()
