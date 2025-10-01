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
