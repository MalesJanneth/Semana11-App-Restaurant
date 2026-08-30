"""
Este módulo contiene la clase Usuario.

La clase Usuario representa de manera general
a una persona registrada en el sistema.
"""


class Usuario:
    """
    Representa un usuario registrado en el restaurante.

    La clase administra únicamente la información
    general correspondiente al usuario.
    """

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
    ) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self) -> str:
        """Devuelve la identificación del usuario."""
        return self._identificacion

    @identificacion.setter
    def identificacion(
        self,
        nueva_identificacion: str,
    ) -> None:
        """Establece y valida la identificación."""

        if not nueva_identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        self._identificacion = nueva_identificacion.strip()

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del usuario."""
        return self._nombre

    @nombre.setter
    def nombre(
        self,
        nuevo_nombre: str,
    ) -> None:
        """Establece y valida el nombre."""

        if not nuevo_nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self._nombre = nuevo_nombre.strip()

    @property
    def correo(self) -> str:
        """Devuelve el correo del usuario."""
        return self._correo

    @correo.setter
    def correo(
        self,
        nuevo_correo: str,
    ) -> None:
        """Establece y valida el correo."""

        if not nuevo_correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

        if "@" not in nuevo_correo:
            raise ValueError(
                "El correo debe contener el símbolo @."
            )

        self._correo = nuevo_correo.strip()

    def mostrar_informacion(self) -> str:
        """Devuelve la información del usuario."""

        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def a_diccionario(self) -> dict[str, str]:
        """
        Convierte el objeto Usuario en un diccionario
        compatible con formato JSON.
        """

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }