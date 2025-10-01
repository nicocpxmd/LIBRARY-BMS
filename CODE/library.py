from book import Libro
from user import Usuario
from loan import Prestamo
# ================================
# Clase Biblioteca
# ================================
class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    # Métodos de gestión (aquí SOLO la estructura con explicación):
    def agregar_libro(self,libro):
        for i in self.__libros:
            if i.get_codigo() == libro.get_codigo():
                print(f"El libro ya existe")
                return
        self.__libros.append(libro)
        print(f"Libro -{libro.get_titulo()}- agregado correctamente.")

    def agregar_usuario(self, usuario):
        for j in self.__usuarios:
            if j.get_id() == usuario.get_id():
                print(f"Este usuario ya existe")
                return
        self.__usuarios.append(usuario)
        print(f"Usuario -{usuario.get_nombre()}- agregado correctamente.") 
#JuanDavidOcampo
    def listar_libros(self):
        """
        Aquí hay que recorrer la lista de libros y mostrar
        cuáles están disponibles.
        Ejemplo de pista:
            for libro in self.__libros:
                print(libro.get_titulo(), libro.get_disponibles())
        """
        if not self.__libros:
            print("No hay libros registrados en la biblioteca.")
            return
         print("==== Listado de libros disponibles en la biblioteca ====")
        for libro in self.__libros:
            libro.mostrar_todo()
    #JuanDavidOcampo
    def consultar_libros(self, criterio):
        """
        Aquí la idea es permitir buscar libros ya sea por título o por área.
        Se puede hacer con un if que compare criterio == "titulo" o criterio == "area".
        Luego recorrer la lista y devolver los que coincidan.
        """
        if not self.__libros:
        print("No hay libros registrados en la biblioteca.")
        return

        # Pedimos el texto de búsqueda al usuario
        texto_busqueda = input(f"Ingrese el {criterio} que desea buscar: ").lower()
    
        resultados = []
    
        # Recorremos la lista de libros y verificamos coincidencias
        for libro in self.__libros:
            if criterio == "titulo" and texto_busqueda in libro.get_titulo().lower():
                resultados.append(libro)
            elif criterio == "autor" and texto_busqueda in libro.get_autor().lower():
                resultados.append(libro)
            elif criterio == "area" and texto_busqueda in libro.get_area().lower():
                resultados.append(libro)
    
        # Mostramos resultados
        if resultados:
            print(f"Se encontraron {len(resultados)} libros:")
            for l in resultados:
                l.mostrar_todo()
        else:
            print("No se encontraron libros con ese criterio.")
    def realizar_prestamo(self, id_usuario, codigo_libro, fecha, dias):
        """
        Aquí debes:
        1. Buscar al usuario en la lista de usuarios.
        2. Buscar el libro en la lista de libros.
        3. Verificar que:
            - El usuario tenga menos de 3 préstamos.
            - El libro tenga unidades disponibles.
        4. Si se cumplen, crear un objeto Prestamo y añadirlo a la lista.
        Pista: usuario.agregar_prestamo(nuevo_prestamo)
        """

    def devolver_libro(self, id_usuario, codigo_libro):
        """
        Aquí se busca el usuario y el préstamo correspondiente.
        Si existe, se devuelve el libro:
            - libro.devolver()
            - usuario.devolver_prestamo(prestamo)
            - quitar de self.__prestamos
        """

    def consultar_prestamos_usuario(self, id_usuario):
        """
        Se busca el usuario y se listan los libros que tiene en su lista de préstamos.
        """



