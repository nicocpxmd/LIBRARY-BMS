#Juan David Ocampo Gutierrez
# Nicolás Castro Pacheco
# Michell Valencia Berdugo
# Juan David Rivera Durán

from book import Libro
from user import Usuario
from library import Biblioteca
# ================================
# Programa Principal
# ================================
if __name__ == "__main__":
    biblio = Biblioteca()

    # ----- 10 libros iniciales -----
    biblio.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela", "N001", 5))
    biblio.agregar_libro(Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela", "N002", 3))
    biblio.agregar_libro(Libro("Física para la Ciencia y la Tecnología Vol. 1", "Raymond A. Serway", 2014, "Ciencia", "C001", 2))
    biblio.agregar_libro(Libro("Introducción a la Programación con Python", "John Zelle", 2017, "Programación", "P001", 4))
    biblio.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry", 1943, "Infantil", "I001", 6))
    biblio.agregar_libro(Libro("Crimen y castigo", "Fiódor Dostoyevski", 1866, "Novela", "N003", 3))
    biblio.agregar_libro(Libro("Cálculo de una variable", "James Stewart", 2015, "Matemáticas", "M001", 4))
    biblio.agregar_libro(Libro("Inteligencia Artificial: Un Enfoque Moderno", "Stuart Russell", 2010, "Tecnología", "T001", 2))
    biblio.agregar_libro(Libro("Historia de dos ciudades", "Charles Dickens", 1859, "Novela", "N004", 3))
    biblio.agregar_libro(Libro("Fundamentos de bases de datos", "Abraham Silberschatz", 2010, "Tecnología", "T002", 3))

    # ----- Cargar usuarios de inicio (3) -----
    biblio.agregar_usuario(Usuario("Juan Perez", "U001", "estudiante"))
    biblio.agregar_usuario(Usuario("Maria Garcia", "U002", "profesor"))
    biblio.agregar_usuario(Usuario("Carlos Lopez", "U003", "estudiante"))

    try:
        while True:
            print("\n--- Menú de la Biblioteca ---")
            print("1. Listar libros")
            print("2. Consultar libros")
            print("3. Realizar préstamo")
            print("4. Devolver libro")
            print("5. Consultar préstamos por usuario")
            print("6. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                biblio.listar_libros()

            elif opcion == '2':
                criterio = input("Buscar por (titulo/autor/area): ").strip().lower()
                if criterio not in ("titulo", "autor", "area"):
                    print("Criterio inválido. Use 'titulo', 'autor' o 'area'.")
                    continue
                valor = input(f"Ingrese el {criterio} a buscar: ").strip()
                if not valor:
                    print("Debe ingresar un texto para buscar.")
                    continue
                biblio.consultar_libros(criterio, valor)

            elif opcion == '3':
                id_usuario = input("Ingrese el ID del usuario: ").strip()
                codigo_libro = input("Ingrese el código del libro: ").strip()
                fecha_prestamo_str = input("Ingrese la fecha del préstamo (YYYY-MM-DD): ").strip()
                dias_input = input("Ingrese la cantidad de días del préstamo: ").strip()
                try:
                    dias_prestamo = int(dias_input)
                    if dias_prestamo <= 0:
                        print("La cantidad de días debe ser un entero positivo.")
                        continue
                except ValueError:
                    print("Por favor ingrese un número válido para los días.")
                    continue

                # La Biblioteca valida formato de fecha internamente
                biblio.realizar_prestamo(id_usuario, codigo_libro, fecha_prestamo_str, dias_prestamo)

            elif opcion == '4':
                id_usuario = input("Ingrese el ID del usuario: ").strip()
                codigo_libro = input("Ingrese el código del libro a devolver: ").strip()
                biblio.devolver_libro(id_usuario, codigo_libro)

            elif opcion == '5':
                id_usuario = input("Ingrese el ID del usuario: ").strip()
                biblio.consultar_prestamos_usuario(id_usuario)

            elif opcion == '6':
                print("Saliendo del sistema de biblioteca.")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

    except KeyboardInterrupt: #Esta parte es como un escape para salir del programa con ctrl+c - Nico
        print("\nInterrupción por teclado. Saliendo...")
