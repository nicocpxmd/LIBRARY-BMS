from datetime import datetime, date
from book import Libro
from user import Usuario
from loan import Prestamo

class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    # ----- Métodos auxiliares de búsqueda -----
    def buscar_libro_por_codigo(self, codigo):
        for libro in self.__libros:
            if libro.get_codigo() == codigo:
                return libro
        return None

    def buscar_usuario_por_id(self, identificador):
        for usuario in self.__usuarios:
            if usuario.get_id() == identificador:
                return usuario
        return None

    # ----- Agregar -----
    def agregar_libro(self, libro: Libro):
        if self.buscar_libro_por_codigo(libro.get_codigo()):
            print("El libro ya existe")
            return
        self.__libros.append(libro)
        print(f"Libro -{libro.get_titulo()}- agregado correctamente.")

    def agregar_usuario(self, usuario: Usuario):
        if self.buscar_usuario_por_id(usuario.get_id()):
            print("Este usuario ya existe")
            return
        self.__usuarios.append(usuario)
        print(f"Usuario -{usuario.get_nombre()}- agregado correctamente.")


#JuanDavidOcampo
    # ----- Listar -----
    def listar_libros(self):
        if not self.__libros:
            print("No hay libros registrados en la biblioteca.")
            return
        print("==== Listado de libros disponibles en la biblioteca ====")
        for libro in self.__libros:
            libro.mostrar_todo()


#JuanDavidOcampo
    # ----- Consultar (ahora recibe criterio y valor) -----
    def consultar_libros(self, criterio: str, valor: str): #Cambie el input por darle los dos parametros (criterio y valor) para en caso que requiera reutilizar se pueda hacer y no se corte con el input - Nico
        """
        criterio: 'titulo' | 'autor' | 'area'
        valor: texto a buscar (subcadena, case-insensitive)
        """
        if not self.__libros:
            print("No hay libros registrados en la biblioteca.")
            return

        criterio = criterio.lower()
        valor = valor.lower().strip()
        resultados = []

        for libro in self.__libros:
            if criterio == "titulo" and valor in libro.get_titulo().lower():
                resultados.append(libro)
            elif criterio == "autor" and valor in libro.get_autor().lower():
                resultados.append(libro)
            elif criterio == "area" and valor in libro.get_area().lower():
                resultados.append(libro)

        if resultados:
            print(f"Se encontraron {len(resultados)} libro(s):")
            for l in resultados:
                l.mostrar_todo()
        else:
            print("No se encontraron libros con ese criterio.")

    # ----- Realizar préstamo -----
    def realizar_prestamo(self, id_usuario: str, codigo_libro: str, fecha_str: str, dias: int):
        """
        fecha_str: 'YYYY-MM-DD' (string). dias: int
        """
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            print("Usuario no encontrado.")
            return

        libro = self.buscar_libro_por_codigo(codigo_libro)
        if not libro:
            print("Libro no encontrado.")
            return

        # Validaciones de negocio
        if libro.get_disponibles() <= 0:
            print("No hay copias disponibles del libro.")
            return

        if len(usuario.get_prestamos()) >= 3:
            print("El usuario ya tiene el máximo de préstamos activos (3).")
            return

        # Validar y parsear fecha
        try:
            fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de fecha inválido. Use YYYY-MM-DD.")
            return

        # Validar días
        if not isinstance(dias, int) or dias <= 0: #Isistance verifica que sea un entero - Nico
            print("La cantidad de días debe ser un entero positivo.")
            return

        # Crear préstamo (no tocar el libro hasta confirmar que el préstamo fue creado sin excepción)
        try:
            nuevo_prestamo = Prestamo(usuario, libro, fecha_obj, dias)
        except Exception as e:
            print(f"Error al crear el préstamo: {e}")
            return

        # Intentar actualizar stock del libro (prestar)
        if libro.prestar():
            # Registrar préstamo
            usuario.agregar_prestamo(nuevo_prestamo)
            self.__prestamos.append(nuevo_prestamo)
            print(f"Préstamo realizado: '{libro.get_titulo()}' para {usuario.get_nombre()} desde {fecha_str} por {dias} días.")
        else:
            # Aunque ya validamos disponibilidad, chequeo por seguridad
            print("No fue posible realizar el préstamo: no hay unidades disponibles.")

    # ----- Devolver libro -----
    def devolver_libro(self, id_usuario: str, codigo_libro: str):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            print("Usuario no encontrado.")
            return

        # Buscar préstamo activo del usuario para ese libro
        prestamo = None
        for p in usuario.get_prestamos():
            if p.get_libro().get_codigo() == codigo_libro:
                prestamo = p
                break

        if not prestamo:
            print("No se encontró un préstamo activo de ese libro para este usuario.")
            return

        libro = prestamo.get_libro()
        fecha_devolucion = prestamo.get_fecha_devolucion()
        hoy = date.today()
        if hoy > fecha_devolucion:
            dias_retraso = (hoy - fecha_devolucion).days
            print(f"Atención: la devolución está fuera de plazo por {dias_retraso} día(s).")
            # Aquí podrías calcular multa si tu política lo requiere.

        # Actualizar stock y registros
        if libro.devolver():
            usuario.devolver_prestamo(prestamo)
            if prestamo in self.__prestamos:
                self.__prestamos.remove(prestamo)
            print(f"Libro '{libro.get_titulo()}' devuelto correctamente por {usuario.get_nombre()}.")
        else:
            # Caso no esperado: intentar devolver más de las unidades totales
            print("Error al devolver: las unidades en biblioteca ya están al máximo.")

    # ----- Consultar préstamos por usuario -----
    def consultar_prestamos_usuario(self, id_usuario: str):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            print("Usuario no encontrado.")
            return

        prestamos = usuario.get_prestamos()
        if not prestamos:
            print("El usuario no tiene préstamos activos.")
            return

        print(f"Préstamos activos del usuario {usuario.get_nombre()}:")
        for p in prestamos:
            libro = p.get_libro()
            fecha_dev = p.get_fecha_devolucion()
            print(f"- {libro.get_titulo()} (Código: {libro.get_codigo()}) - Devolver antes de: {fecha_dev}")
