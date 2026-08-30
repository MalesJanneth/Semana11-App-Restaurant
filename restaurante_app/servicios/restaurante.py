"""
Módulo que contiene la clase Restaurante.

Restaurante administra las colecciones de productos,
usuarios y ventas.
"""

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """
    Servicio encargado de administrar productos,
    usuarios y ventas.
    """

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

    def registrar_producto(
        self,
        producto: Producto,
    ) -> str:
        """Registra un producto evitando códigos duplicados."""

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
        """Busca un producto mediante su código."""

        return self._buscar_producto_por_codigo(codigo)

    def actualizar_producto(
        self,
        codigo_actual: str,
        nuevo_codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
        nuevo_stock: int,
        nueva_disponibilidad: bool,
    ) -> str:
        """
        Actualiza la información de un producto.
        Se conserva el stock indicado.
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
                stock=nuevo_stock,
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
        """Elimina un producto mediante su código."""

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
        """Devuelve la información de todos los productos."""

        return [
            producto.mostrar_informacion()
            for producto in self._productos
        ]

    def obtener_productos(self) -> list[Producto]:
        """Devuelve una copia de la colección de productos."""

        return self._productos.copy()

    def registrar_usuario(
        self,
        usuario: Usuario,
    ) -> str:
        """Registra un usuario evitando identificaciones duplicadas."""

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
        """Devuelve la información de todos los usuarios."""

        return [
            usuario.mostrar_informacion()
            for usuario in self._usuarios
        ]

    def obtener_usuarios(self) -> list[Usuario]:
        """Devuelve una copia de la colección de usuarios."""

        return self._usuarios.copy()

    def obtener_categorias(self) -> set[str]:
        """
        Devuelve las categorías únicas de los productos.
        """

        return {
            producto.categoria
            for producto in self._productos
        }

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int,
    ) -> bool:
        """
        Registra una venta si el usuario y producto existen,
        la cantidad es válida y existe stock suficiente.
        """

        usuario = self._buscar_usuario_por_identificacion(
            identificacion_usuario
        )

        producto = self._buscar_producto_por_codigo(
            codigo_producto
        )

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(
            usuario_id=usuario.identificacion,
            producto_codigo=producto.codigo,
            cantidad=cantidad,
        )

        self._ventas.append(venta)
        producto.vender(cantidad)

        return True

    def obtener_ventas(self) -> list[Venta]:
        """Devuelve una copia de la colección de ventas."""

        return self._ventas.copy()

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str,
    ) -> list[Venta]:
        """
        Devuelve las ventas asociadas a un usuario
        utilizando recorrido y filtrado de la colección.
        """

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def _buscar_producto_por_codigo(
        self,
        codigo: str,
    ) -> Producto | None:
        """Realiza una búsqueda interna de productos."""

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def _buscar_usuario_por_identificacion(
        self,
        identificacion: str,
    ) -> Usuario | None:
        """Realiza una búsqueda interna de usuarios."""

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def cargar_productos(
        self,
        productos: list[Producto],
    ) -> None:
        """Carga productos en la colección interna."""

        self._productos = productos.copy()

    def cargar_usuarios(
        self,
        usuarios: list[Usuario],
    ) -> None:
        """Carga usuarios en la colección interna."""

        self._usuarios = usuarios.copy()

    def cargar_ventas(
        self,
        ventas: list[Venta],
    ) -> None:
        """Carga ventas en la colección interna."""

        self._ventas = ventas.copy()