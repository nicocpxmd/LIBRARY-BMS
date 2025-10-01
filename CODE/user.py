# ================================
# Clase Usuario
# ================================
class Usuario:
    def __init__(self, nombre, identificador, tipo):
        self.__nombre = nombre
        self.__identificador = identificador
        self.__tipo = tipo  # estudiante o profesor
        self.__prestamos = []  # libros prestados

    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__identificador

    def get_tipo(self):
        return self.__tipo

    def get_prestamos(self):
        return self.__prestamos

    def agregar_prestamo(self, prestamo):
        self.__prestamos.append(prestamo)

    def devolver_prestamo(self, prestamo):
        if prestamo in self.__prestamos:
            self.__prestamos.remove(prestamo)
