#Juan David Ocampo Gutierrez
# Nicolás Castro Pacheco
# Michell Valencia Berdugo
# Juan David Rivera Durán

# ================================
# Clase Libro
# ================================
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, area, codigo, unidades):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__area = area
        self.__codigo = codigo
        self.__unidades = unidades  # cantidad total
        self.__disponibles = unidades  # disponibles para préstamo

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_area(self):
        return self.__area

    def get_codigo(self):
        return self.__codigo

    def get_disponibles(self):
        return self.__disponibles

    # Métodos para actualizar disponibilidad
    def prestar(self):
        if self.__disponibles > 0:
            self.__disponibles -= 1
            return True
        return False

    def devolver(self):
        if self.__disponibles < self.__unidades:
            self.__disponibles += 1

    def mostrar_todo(self):
        print(f"Código: {self.__codigo}")
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Año de publicación: {self.__anio_publicacion}")
        print(f"Área: {self.__area}")
        print(f"Unidades totales: {self.__unidades}")
        print(f"Disponibles: {self.__disponibles}")
        print("-" * 30)
