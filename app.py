from BD.conexion import DataAccessObject
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("=== MENÚ PRINCIPAL ===")
            print("1.- Listar cursos")
            print("2.- Registrar curso")
            print("3.- Actualizar curso")
            print("4.- Eliminar curso")
            print("5.- Salir")
            print("=======================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")  
                break  
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dataAccessObject = DataAccessObject()

    if opcion == 1:
        try:
            cursos = dataAccessObject.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            dataAccessObject.registrarCurso(curso)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            cursos = dataAccessObject.listarCursos()
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dataAccessObject.actualizarCurso(curso)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            cursos = dataAccessObject.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    DataAccessObject.eliminarCurso(codigoEliminar)
                else:
                    print("Código de curso no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

menuPrincipal()