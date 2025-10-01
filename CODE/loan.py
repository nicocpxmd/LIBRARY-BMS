# ================================
# Clase Prestamo
# ================================
class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, dias_prestamo):
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__dias_prestamo = dias_prestamo
        # Fecha de devolución se calcula
        self.__fecha_devolucion = None

    def get_libro(self):
        return self.__libro

    def get_usuario(self):
        return self.__usuario
