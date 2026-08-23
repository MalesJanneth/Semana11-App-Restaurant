"""
Servicio encargado de la persistencia de productos
mediante archivos JSON.
"""

import json

from modelos.producto import Producto


class ArchivoServicio:
    """
    Gestiona la lectura y escritura de productos
    en el archivo productos.json.
    """

    def __init__(self, ruta_archivo: str) -> None:
        self._ruta_archivo = ruta_archivo

    def guardar_productos(
        self,
        productos: list[Producto],
    ) -> bool:
        """
        Guarda los productos en formato JSON.
        """

        datos_productos = [
            producto.a_diccionario()
            for producto in productos
        ]

        try:
            with open(
                self._ruta_archivo,
                "w",
                encoding="utf-8",
            ) as archivo:

                json.dump(
                    datos_productos,
                    archivo,
                    ensure_ascii=False,
                    indent=4,
                )

            return True

        except PermissionError:
            print(
                "\nError: no existen permisos suficientes "
                "para escribir el archivo de productos."
            )
            return False

        except FileNotFoundError:
            print(
                "\nError: no se encontró la carpeta "
                "destinada al archivo de productos."
            )
            return False

    def cargar_productos(self) -> list[Producto]:
        """
        Carga los productos desde el archivo JSON y
        reconstruye objetos Producto a partir de los
        registros válidos.
        """

        try:
            with open(
                self._ruta_archivo,
                "r",
                encoding="utf-8",
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            print(
                "\nAviso: todavía no existe el archivo "
                "productos.json. Se iniciará con una "
                "colección de productos vacía."
            )
            return []

        except json.JSONDecodeError:
            print(
                "\nError: el archivo productos.json "
                "no contiene un formato JSON válido."
            )
            return []

        except PermissionError:
            print(
                "\nError: no existen permisos suficientes "
                "para leer el archivo de productos."
            )
            return []

        if not isinstance(datos, list):
            print(
                "\nError: la estructura de productos.json "
                "debe ser una lista de productos."
            )
            return []

        productos: list[Producto] = []

        for numero_registro, registro in enumerate(
            datos,
            start=1,
        ):
            try:
                if not isinstance(registro, dict):
                    raise ValueError(
                        "El registro no tiene formato "
                        "de diccionario."
                    )

                producto = Producto(
                    codigo=registro["codigo"],
                    nombre=registro["nombre"],
                    categoria=registro["categoria"],
                    precio=registro["precio"],
                    disponible=registro["disponible"],
                )

                productos.append(producto)

            except KeyError as error:
                print(
                    f"\nAviso: se omitió el registro "
                    f"{numero_registro} porque falta la clave "
                    f"{error}."
                )

            except ValueError as error:
                print(
                    f"\nAviso: se omitió el registro "
                    f"{numero_registro} por contener datos "
                    f"inválidos: {error}"
                )

            except TypeError as error:
                print(
                    f"\nAviso: se omitió el registro "
                    f"{numero_registro} por contener tipos "
                    f"de datos inválidos: {error}"
                )

        return productos