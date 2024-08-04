from dominio.dominio import Estudiante
from servicio.estudianteService import EstudianteService


def mostrar_estudiante(estudiantes):
    for est in estudiantes:
        print(vars(est))


def main():
    estudiante_service = EstudianteService()

    while True:
        print("\n--- MENU ---")
        print("1. Crear estudiante")
        print("2. Consultar todos los estudiante")
        print("3. Consultar estudiante por ID")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            mail = input("Ingrese el correo electrónico: ")
            matricula = input("Ingrese la matricula: ")
            carrera = input("Ingrese la carrera: ")
            #en la creacion no se envia el ID xq la tabla crea automaticamente un secuencial
            #entonces para el parametro id se envia null o None que significa nada
            nuevo_estudiante = Estudiante(None, nombre, apellido, edad, mail, matricula, carrera)
            estudiante_service.crear_estudiante(nuevo_estudiante)

        elif opcion == "2":
            estudiante = estudiante_service.obtener_estudiantes()
            mostrar_estudiante(estudiante)

        elif opcion == "3":
            print("HACER una consulta de estudiante por id, es similar a la consulta de todos solo aumentar el where id")
        
        elif opcion == "4":
            id_persona = int(input("Ingrese el ID de la persona que desea actualizar: "))
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            edad = int(input("Ingrese la nueva edad: "))
            mail = input("Ingrese el nuevo correo electrónico: ")
            matricula = input("Ingrese la matricula: ")
            carrera = input("Ingrese la carrera: ")
            estudiante_actualizada = Estudiante(id_persona, nombre, apellido, edad, mail, matricula, carrera)
            estudiante_service.actualizar_estudiante(estudiante_actualizada)

        elif opcion == "5":
            estudianteId = int(input("Ingrese el ID de la persona que desea eliminar: "))
            estudiante_service.eliminar_estudiante(estudianteId)

        elif opcion == "6":
            estudiante_service.cerrar_conexion()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")



if __name__ == "__main__":
    main()