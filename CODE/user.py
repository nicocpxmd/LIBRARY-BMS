# ================================
# Clase Usuario
# ================================
from loan import Prestamo

class Usuario:
    def __init__(self, nombre, identificador, tipo):
        self.__nombre = nombre
        self.__identificador = identificador
        self.__tipo = tipo  # estudiante o profesor
        self.__prestamos = []  # libros prestados
        self.__historial = []  # libros prestados lifetime
        
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
        self.__historial.append(prestamo)

    def devolver_prestamo(self, prestamo):
        if prestamo in self.__prestamos:
            self.__prestamos.remove(prestamo)

    def mostrar_todo(self):
        print(f"ID: {self.__identificador}")
        print(f"Nombre: {self.__nombre}")
        print(f"Tipo: {self.__tipo}")
        print("---- Libros prestados actualmente ----")
        if self.__prestamos:
            for p in self.__prestamos:
                libro = p.get_libro()
                print(f"- {libro.get_titulo()} (Código: {libro.get_codigo()})")
        else:
            print("Ninguno")

        print("---- Historial de préstamos ----")
        if self.__historial:
            for p in self.__historial:
                libro = p.get_libro()
                print(f"- {libro.get_titulo()} (Código: {libro.get_codigo()})")
        else:
            print("No tiene historial")
        print("-" * 30)    
    

