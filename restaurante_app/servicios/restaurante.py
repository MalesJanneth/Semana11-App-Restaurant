"""
Módulo que contiene la clase Restaurante.
Restaurante administra las colecciones de productos
y usuarios.
"""

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """
    Servicio encargado de administrar productos y usuarios.
    Las colecciones permanecen dentro de esta clase.
    """

    def __init__(self) -> None:
        # LISTAS:
        # Se utilizan porque productos y usuarios son
        # colecciones dinámicas de objetos.
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

    def registrar_producto(
        self,
        producto: Producto,
    ) -> str:
        """
        Registra un producto evitando códigos duplicados.
        """

        if self._buscar_producto_por_codigo(
            producto.codigo
        ) is not None:
            return (
                f"Ya existe un producto con el código "
                f"{producto.codigo}."
            )

        self._productos.append(producto)

        return (
            f'El producto "{producto.nombre}" '
            "fue registrado correctamente."
        )

    def buscar_producto(
        self,
        codigo: str,
    ) -> Producto | None:
        """
        Busca y devuelve un producto mediante su código.
        """

        return self._buscar_producto_por_codigo(codigo)

    def actualizar_producto(
        self,
        codigo_actual: str,
        nuevo_codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
        nueva_disponibilidad: bool,
    ) -> str:
        """
        Actualiza la información de un producto.
        Se verifica que el nuevo código no se repita.
        """

        producto_actual = self._buscar_producto_por_codigo(
            codigo_actual
        )

        if producto_actual is None:
            return (
                f"No existe un producto con el código "
                f"{codigo_actual}."
            )

        if (
            nuevo_codigo != codigo_actual
            and self._buscar_producto_por_codigo(
                nuevo_codigo
            ) is not None
        ):
            return (
                f"Ya existe otro producto con el código "
                f"{nuevo_codigo}."
            )

        try:
            producto_actualizado = Producto(
                codigo=nuevo_codigo,
                nombre=nuevo_nombre,
                categoria=nueva_categoria,
                precio=nuevo_precio,
                disponible=nueva_disponibilidad,
            )

        except ValueError as error:
            return f"Error al actualizar el producto: {error}"

        indice = self._productos.index(producto_actual)
        self._productos[indice] = producto_actualizado

        return (
            f'El producto "{producto_actualizado.nombre}" '
            "fue actualizado correctamente."
        )

    def eliminar_producto(
        self,
        codigo: str,
    ) -> str:
        """
        Elimina un producto mediante su código.
        """

        producto = self._buscar_producto_por_codigo(codigo)

        if producto is None:
            return (
                f"No existe un producto con el código "
                f"{codigo}."
            )

        self._productos.remove(producto)

        return (
            f'El producto "{producto.nombre}" '
            "fue eliminado correctamente."
        )

    def listar_productos(self) -> list[str]:
        """
        Devuelve la información de todos los productos.
        """

        return [
            producto.mostrar_informacion()
            for producto in self._productos
        ]

    def obtener_productos(self) -> list[Producto]:
        """
        Devuelve una copia de la colección de productos.
        """

        return self._productos.copy()

    def registrar_usuario(
        self,
        usuario: Usuario,
    ) -> str:
        """
        Registra un usuario evitando identificaciones
        duplicadas.
        """

        if self._buscar_usuario_por_identificacion(
            usuario.identificacion
        ) is not None:
            return (
                "Ya existe un usuario con la "
                f"identificación {usuario.identificacion}."
            )

        self._usuarios.append(usuario)

        return (
            f'El usuario "{usuario.nombre}" '
            "fue registrado correctamente."
        )

    def listar_usuarios(self) -> list[str]:
        """
        Devuelve la información de todos los usuarios.
        """

        return [
            usuario.mostrar_informacion()
            for usuario in self._usuarios
        ]

    def obtener_categorias(self) -> set[str]:
        """
        Devuelve las categorías únicas de los productos.

        SET:
        El conjunto elimina automáticamente los valores
        repetidos, permitiendo mostrar cada categoría
        una sola vez.
        """

        return {
            producto.categoria
            for producto in self._productos
        }

    def _buscar_producto_por_codigo(
        self,
        codigo: str,
    ) -> Producto | None:
        """
        Realiza una búsqueda interna de productos.
        """

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def _buscar_usuario_por_identificacion(
        self,
        identificacion: str,
    ) -> Usuario | None:
        """
        Realiza una búsqueda interna de usuarios.
        """

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None