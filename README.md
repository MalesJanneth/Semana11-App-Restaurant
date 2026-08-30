# Restaurante App - Semana 11

## Manejo de archivos, excepciones y persistencia JSON

**Estudiante:** Jannneth Talía Males Conejo
---
## Descripción

Aplicación de restaurante desarrollada en Python con Programación Orientada a Objetos.

En la Semana 11 se incorporaron:

- Manejo de stock.
- Clase `Venta`.
- Relación entre `Usuario` y `Producto`.
- Consulta de ventas por usuario.
- Persistencia de productos, usuarios y ventas mediante JSON.
- Validaciones y manejo de excepciones.

## Estructura del proyecto

    restaurante_app/
    ├── datos/
    │   ├── productos.json
    │   ├── usuarios.json
    │   └── ventas.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   ├── usuario.py
    │   └── venta.py
    ├── servicios/
    │   ├── __init__.py
    │   ├── archivo_servicio.py
    │   └── restaurante.py
    ├── main.py
    └── README.md

## Responsabilidad de los componentes

- **Producto:** administra los datos del producto, incluyendo precio, disponibilidad y stock.
- **Usuario:** representa a los usuarios registrados.
- **Venta:** relaciona un usuario con un producto y registra la cantidad vendida.
- **Restaurante:** administra las colecciones y las reglas de negocio.
- **ArchivoServicio:** guarda y recupera productos, usuarios y ventas mediante JSON.
- **main.py:** controla el menú y la interacción mediante `input()`.

## Funcionamiento del stock

Antes de vender se verifica que:

- El usuario exista.
- El producto exista.
- La cantidad sea mayor que cero.
- Exista stock suficiente.

Si la venta es válida, se registra la `Venta` y se disminuye el stock.

El stock nunca puede ser negativo.

## Relación Usuario - Producto

La venta representa la relación:

    Usuario + Producto → Venta

Cada `Venta` contiene:

- `usuario_id`
- `producto_codigo`
- `cantidad`

Las ventas se almacenan en una colección de objetos `Venta`.

## Venta de productos

La operación `vender_producto()`:

1. Busca el usuario.
2. Busca el producto.
3. Valida la cantidad.
4. Valida el stock.
5. Crea la venta.
6. Agrega la venta a la colección.
7. Disminuye el stock.
8. Guarda `ventas.json` y `productos.json`.

## Consulta de ventas

El sistema permite consultar las ventas de un usuario recorriendo y filtrando la colección de objetos `Venta`.

Solo se muestran las ventas cuya identificación corresponde al usuario consultado.

## Persistencia JSON

Se utilizan tres archivos:

    productos.json
    usuarios.json
    ventas.json

Los objetos se convierten a diccionarios para guardarlos con `json.dump()`.

Al iniciar el programa se utiliza `json.load()` para recuperar los datos y reconstruir los objetos.

## Excepciones controladas

Se controlan las siguientes excepciones:

- `FileNotFoundError`
- `json.JSONDecodeError`
- `PermissionError`
- `KeyError`
- `ValueError`
- `TypeError`

No se utiliza `except: pass`.

## Forma de ejecución

Desde la carpeta principal del proyecto ejecutar:

    python main.py

También puede utilizarse:

    python3 main.py

## Pruebas realizadas

Se verificó:

- Registro de usuarios.
- Registro de productos con stock.
- Venta válida.
- Disminución correcta del stock.
- Registro de ventas en `ventas.json`.
- Actualización de `productos.json`.
- Consulta de ventas por usuario.
- Recuperación de productos, usuarios y ventas después de reiniciar.
- Rechazo de ventas con stock insuficiente.
- Rechazo de cantidades menores o iguales a cero.

## Conclusión

La Semana 11 amplía `restaurante_app` incorporando ventas relacionadas con usuarios y productos, control de stock, consulta de ventas y persistencia completa mediante archivos JSON.

Se mantiene la Programación Orientada a Objetos, el uso de colecciones y la separación de responsabilidades entre modelos, servicios y `main.py`.