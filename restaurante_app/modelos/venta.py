"""
Este módulo contiene la clase Venta.

La clase Venta representa la relación entre
un usuario y un producto vendido.
"""


class Venta:
    """
    Representa una venta realizada por un usuario.
    """

    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int,
    ) -> None:
        if not usuario_id.strip():
            raise ValueError(
                "La identificación del usuario no puede estar vacía."
            )

        if not producto_codigo.strip():
            raise ValueError(
                "El código del producto no puede estar vacío."
            )

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.cantidad = cantidad

    def a_diccionario(self) -> dict[str, object]:
        """
        Convierte la venta en un diccionario
        compatible con formato JSON.
        """

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }