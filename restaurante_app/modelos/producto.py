"""
Este módulo contiene la clase Producto.

La clase Producto representa la información general
de un producto registrado en el restaurante.
"""


class Producto:
    """
    Representa un producto del restaurante.

    La clase administra la información correspondiente
    a cada producto y su stock disponible.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int,
        disponible: bool = True,
    ) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    @property
    def codigo(self) -> str:
        """Devuelve el código del producto."""
        return self._codigo

    @codigo.setter
    def codigo(self, nuevo_codigo: str) -> None:
        """Establece y valida el código del producto."""

        if not nuevo_codigo.strip():
            raise ValueError(
                "El código no puede estar vacío."
            )

        self._codigo = nuevo_codigo.strip()

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Establece y valida el nombre del producto."""

        if not nuevo_nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self._nombre = nuevo_nombre.strip()

    @property
    def categoria(self) -> str:
        """Devuelve la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(
        self,
        nueva_categoria: str,
    ) -> None:
        """Establece y valida la categoría del producto."""

        if not nueva_categoria.strip():
            raise ValueError(
                "La categoría no puede estar vacía."
            )

        self._categoria = nueva_categoria.strip()

    @property
    def precio(self) -> float:
        """Devuelve el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        """Establece y valida el precio del producto."""

        if nuevo_precio <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        self._precio = nuevo_precio

    @property
    def stock(self) -> int:
        """Devuelve el stock disponible del producto."""
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock: int) -> None:
        """Establece y valida el stock del producto."""

        if not isinstance(nuevo_stock, int):
            raise ValueError(
                "El stock debe ser un número entero."
            )

        if nuevo_stock < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        self._stock = nuevo_stock

    @property
    def disponible(self) -> bool:
        """Devuelve el estado de disponibilidad."""
        return self._disponible

    @disponible.setter
    def disponible(self, estado: bool) -> None:
        """Establece el estado de disponibilidad."""
        self._disponible = estado

    def vender(self, cantidad: int) -> None:
        """
        Disminuye el stock del producto después de
        una venta válida.
        """

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        if cantidad > self.stock:
            raise ValueError(
                "No existe stock suficiente."
            )

        self.stock -= cantidad

        if self.stock == 0:
            self.disponible = False

    def mostrar_informacion(self) -> str:
        """
        Devuelve una representación del producto
        para mostrarlo en la consola.
        """

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock} | "
            f"Estado: {estado}"
        )

    def a_diccionario(self) -> dict[str, object]:
        """
        Convierte el objeto Producto en un diccionario
        compatible con formato JSON.
        """

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
            "disponible": self.disponible,
        }