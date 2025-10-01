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
        
    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_dias_prestamo(self):
        return self.__dias_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha):
        self.__fecha_devolucion = fecha

    def mostrar(self):
        print(f"Libro: {self.__libro.get_titulo()}")
        print(f"Usuario: {self.__usuario.get_nombre()}")
        print(f"Fecha de préstamo: {self.__fecha_prestamo}")
        print(f"Días de préstamo: {self.__dias_prestamo}")
        if self.__fecha_devolucion is None:
            print("Fecha de devolución: No asignada aún.")
        else:
            print(f"Fecha de devolución: {self.__fecha_devolucion}")
        print("-" * 30)
