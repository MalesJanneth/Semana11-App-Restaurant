# Restaurante App - Semana 10

## Manejo de archivos, excepciones y persistencia JSON

**Estudiante:** Jannneth Talía Males Conejo
---

## 1. Descripción del sistema

`restaurante_app` es un sistema de consola desarrollado en Python para administrar productos y usuarios de un restaurante.

Este proyecto corresponde a la evolución del trabajo realizado durante las semanas anteriores. Para la Semana 10 se incorporó la **persistencia de productos mediante un archivo JSON**, además del manejo de excepciones relacionadas con la lectura, escritura y validación de los datos almacenados.

El sistema permite:

- Registrar productos.
- Buscar productos por código.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Mostrar categorías.
- Registrar usuarios.
- Listar usuarios.
- Guardar productos en un archivo JSON.
- Cargar automáticamente los productos al iniciar la aplicación.
- Reconstruir los registros almacenados como objetos `Producto`.

La persistencia se aplica únicamente a los productos, de acuerdo con los requerimientos de la Semana 10.

---

## 2. Objetivo de la Semana 10

El objetivo principal de esta semana es incorporar persistencia de datos al proyecto `restaurante_app`, permitiendo que los productos registrados permanezcan disponibles aunque la aplicación sea cerrada.

Para esto se implementó:

- Manejo de archivos.
- Persistencia mediante JSON.
- Uso de `json.dump()`.
- Uso de `json.load()`.
- Uso de `with open()`.
- Codificación `UTF-8`.
- Reconstrucción de objetos `Producto`.
- Validación de los datos recuperados.
- Manejo específico de excepciones.

---

## 3. Estructura del proyecto

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
└── main.py

README.md
```

---

## 4. Responsabilidad de los componentes

### 4.1. `modelos/producto.py`

Contiene la clase `Producto`, que representa cada producto del restaurante.

La clase conserva las validaciones desarrolladas durante las semanas anteriores:

- El código no puede estar vacío.
- El nombre no puede estar vacío.
- La categoría no puede estar vacía.
- El precio debe ser mayor que cero.
- Se controla la disponibilidad del producto.

Además, la clase dispone del método:

```python
a_diccionario()
```

Este método permite convertir un objeto `Producto` en un diccionario compatible con JSON.

Los productos continúan siendo objetos de la clase `Producto` durante la ejecución del programa.

---

### 4.2. `modelos/usuario.py`

Contiene la clase `Usuario`.

Esta clase conserva las funcionalidades desarrolladas anteriormente para representar usuarios registrados en el sistema.

La información de los usuarios permanece únicamente en memoria durante la ejecución.

En esta semana no se implementó persistencia para usuarios, ya que la actividad solicita aplicar la persistencia únicamente a los productos.

---

### 4.3. `servicios/restaurante.py`

Contiene la clase `Restaurante`.

Es el servicio encargado de administrar las colecciones y las operaciones relacionadas con productos y usuarios.

Sus principales responsabilidades son:

- Registrar productos.
- Buscar productos.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Listar usuarios.
- Obtener categorías.
- Evitar códigos de productos duplicados.
- Evitar identificaciones de usuarios duplicadas.

La colección de productos permanece administrada dentro de `Restaurante`.

`main.py` no modifica directamente las colecciones internas del servicio.

---

### 4.4. `servicios/archivo_servicio.py`

Contiene la clase `ArchivoServicio`.

Este servicio concentra exclusivamente las operaciones de lectura y escritura del archivo:

```text
datos/productos.json
```

Utiliza:

- `json.load()` para cargar los productos.
- `json.dump()` para guardar los productos.
- `with open()` para trabajar con el archivo.
- `encoding="utf-8"` para la codificación de los datos.

También controla las excepciones relacionadas con:

- Archivos inexistentes.
- Archivos JSON inválidos.
- Permisos insuficientes.
- Registros incompletos.
- Datos inválidos.
- Tipos de datos incorrectos.

---

### 4.5. `datos/productos.json`

Es el archivo utilizado para almacenar de manera persistente los productos registrados.

La carpeta `datos/` se utiliza únicamente como ubicación del archivo JSON y **no representa una nueva capa de la arquitectura del sistema**.

Los productos se almacenan en forma de una lista de diccionarios compatible con JSON.

Ejemplo:

```json
[
    {
        "codigo": "01",
        "nombre": "Sopa",
        "categoria": "Comida",
        "precio": 2.5,
        "disponible": true
    }
]
```

Aunque la información se almacena como diccionarios dentro del archivo, durante la ejecución los registros son reconstruidos nuevamente como objetos `Producto`.

---

### 4.6. `main.py`

Es el punto de entrada de la aplicación.

Sus responsabilidades principales son:

- Crear el servicio `Restaurante`.
- Crear el servicio `ArchivoServicio`.
- Cargar los productos almacenados al iniciar.
- Coordinar el menú.
- Solicitar los datos mediante `input()`.
- Ejecutar las operaciones solicitadas por el usuario.
- Solicitar el guardado después de registrar un producto.
- Solicitar el guardado después de actualizar un producto.
- Solicitar el guardado después de eliminar un producto.

`main.py` coordina el flujo de la aplicación, pero no administra directamente las colecciones internas de `Restaurante`.

---

## 5. Persistencia de productos

La persistencia permite conservar los productos registrados aunque el programa sea cerrado.

El archivo utilizado para esta finalidad es:

```text
datos/productos.json
```

La persistencia se realiza únicamente para la entidad `Producto`.

---

## 6. Guardado de productos

Cuando el usuario registra correctamente un producto, se sigue el siguiente flujo:

```text
Usuario
   ↓
main.py
   ↓
Restaurante
   ↓
Objeto Producto
   ↓
ArchivoServicio
   ↓
Producto convertido a diccionario
   ↓
json.dump()
   ↓
datos/productos.json
```

Los objetos `Producto` se convierten a diccionarios mediante el método:

```python
a_diccionario()
```

Posteriormente, `ArchivoServicio` utiliza `json.dump()` para escribir la información en el archivo JSON.

El archivo se actualiza después de realizar correctamente las siguientes operaciones:

1. Registrar un producto.
2. Actualizar un producto.
3. Eliminar un producto.

---

## 7. Carga de productos

Cuando se inicia nuevamente la aplicación, se ejecuta el siguiente flujo:

```text
Inicio de la aplicación
        ↓
main.py crea ArchivoServicio
        ↓
Se intenta leer datos/productos.json
        ↓
json.load()
        ↓
Se valida la información recuperada
        ↓
Se revisa cada registro
        ↓
Se crea Producto(...)
        ↓
Se reconstruyen objetos Producto
        ↓
Los objetos se entregan a Restaurante
        ↓
El menú continúa funcionando normalmente
```

Cada registro válido recuperado desde JSON se convierte nuevamente en un objeto de la clase `Producto`.

Por lo tanto, el sistema no reemplaza la clase `Producto` por diccionarios.

Durante la ejecución, las operaciones continúan trabajando con objetos.

---

## 8. Estructura de los datos JSON

El archivo `productos.json` utiliza una lista de diccionarios.

Ejemplo:

```json
[
    {
        "codigo": "01",
        "nombre": "Sopa",
        "categoria": "Comida",
        "precio": 2.5,
        "disponible": true
    },
    {
        "codigo": "02",
        "nombre": "Jugo",
        "categoria": "Bebida",
        "precio": 1.5,
        "disponible": true
    }
]
```

Cada producto contiene las siguientes propiedades:

| Propiedad | Tipo | Descripción |
|---|---|---|
| `codigo` | `str` | Código identificador del producto |
| `nombre` | `str` | Nombre del producto |
| `categoria` | `str` | Categoría del producto |
| `precio` | `float` | Precio del producto |
| `disponible` | `bool` | Estado de disponibilidad |

---

## 9. Manejo de excepciones

El programa utiliza excepciones específicas para evitar que situaciones esperadas provoquen el cierre abrupto de la aplicación.

---

### 9.1. `FileNotFoundError`

Se controla cuando el archivo:

```text
datos/productos.json
```

todavía no existe.

En este caso, el programa inicia normalmente con una colección de productos vacía.

Esto permite realizar el primer inicio de la aplicación sin tener que crear manualmente información previa.

---

### 9.2. `json.JSONDecodeError`

Se controla cuando el archivo existe, pero su contenido no corresponde a un JSON válido.

El programa muestra un mensaje indicando que el archivo no tiene un formato JSON válido y continúa funcionando sin detener toda la aplicación.

---

### 9.3. `PermissionError`

Se controla cuando el sistema no dispone de permisos suficientes para leer o escribir el archivo `productos.json`.

Se muestra un mensaje comprensible indicando el problema.

---

### 9.4. `KeyError`

Se controla durante la reconstrucción de los objetos `Producto`.

Si un registro almacenado no contiene alguna de las claves esperadas, el registro se considera incompleto y se omite.

Por ejemplo, un registro que no contenga:

```text
codigo
nombre
categoria
precio
disponible
```

no se incorpora a la colección.

Los demás registros válidos pueden continuar cargándose.

---

### 9.5. `ValueError`

Se utiliza para las validaciones propias de la clase `Producto`.

Por ejemplo:

- Código vacío.
- Nombre vacío.
- Categoría vacía.
- Precio menor o igual a cero.

Cuando se detecta un valor inválido, se muestra un mensaje de error y se evita que el problema detenga innecesariamente la aplicación.

---

### 9.6. `TypeError`

Se contempla durante la reconstrucción de productos cuando un registro almacenado contiene tipos de datos incompatibles con los esperados.

El registro que presenta el problema puede ser omitido mientras los demás registros válidos continúan procesándose.

---

## 10. Validaciones de la clase `Producto`

La clase `Producto` conserva las validaciones desarrolladas durante las semanas anteriores.

### Código

El código no puede estar vacío.

### Nombre

El nombre no puede estar vacío.

### Categoría

La categoría no puede estar vacía.

### Precio

El precio debe ser mayor que cero.

### Disponibilidad

La disponibilidad se almacena mediante un valor booleano:

```python
True
```

o:

```python
False
```

Estas validaciones también se aplican cuando los productos son reconstruidos desde el archivo JSON.

---

## 11. Operaciones disponibles

El programa mantiene las funcionalidades desarrolladas anteriormente.

```text
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Listar usuarios
8. Mostrar categorías
9. Salir
========================================
```

### Registrar producto

Permite ingresar un nuevo producto mediante `input()`.

Los datos solicitados son:

```text
Código
Nombre
Categoría
Precio
```

Una vez validado y registrado correctamente, el producto se guarda en `productos.json`.

---

### Buscar producto

Permite buscar un producto mediante su código.

El sistema devuelve la información del producto encontrado.

---

### Actualizar producto

Permite modificar:

- Código.
- Nombre.
- Categoría.
- Precio.
- Disponibilidad.

Después de una actualización correcta, el archivo JSON se actualiza.

---

### Eliminar producto

Permite eliminar un producto mediante su código.

La operación solicita confirmación al usuario.

Después de eliminar correctamente el producto, se actualiza el archivo JSON.

---

### Listar productos

Muestra todos los productos registrados actualmente en el sistema.

Los productos cargados desde JSON aparecen nuevamente como objetos `Producto`.

---

### Registrar usuario

Permite registrar usuarios durante la ejecución de la aplicación.

Los usuarios no se almacenan en el archivo JSON porque la persistencia de esta semana corresponde únicamente a los productos.

---

### Listar usuarios

Muestra los usuarios registrados durante la ejecución actual.

---

### Mostrar categorías

Muestra las categorías únicas de los productos registrados.

---

## 12. Instrucciones para ejecutar el programa

### Paso 1: Abrir una terminal

Ubicarse en la carpeta principal donde se encuentra el proyecto.

Ejemplo:

```powershell
cd "C:\Users\TALIA MALES\Desktop\Semana10_POO"
```

### Paso 2: Ejecutar el programa

Utilizar:

```powershell
python restaurante_app/main.py
```

También puede utilizarse:

```powershell
py restaurante_app/main.py
```

### Paso 3: Utilizar el menú

Después de ejecutar el programa aparecerá el menú principal.

Por ejemplo:

```text
Seleccione una opción: 1
```

Para registrar un producto se ingresan los datos solicitados.

---

## 13. Comprobación de la persistencia

Se realizó una prueba para comprobar que los productos permanecen disponibles después de cerrar y volver a iniciar la aplicación.

### Prueba 1: Inicio sin archivo

Se ejecutó:

```powershell
python restaurante_app/main.py
```

Como el archivo todavía no existía, el sistema inició normalmente y mostró un mensaje indicando que se trabajaría con una colección vacía.

Esto permitió comprobar el manejo de:

```python
FileNotFoundError
```

---

### Prueba 2: Registrar un producto

Se seleccionó:

```text
1. Registrar producto
```

Se ingresaron los siguientes datos:

```text
Código: 01
Nombre: Sopa
Categoría: Comida
Precio: 2.5
```

El sistema mostró:

```text
El producto "Sopa" fue registrado correctamente.
```

---

### Prueba 3: Verificar `productos.json`

Después del registro se comprobó que se generara:

```text
datos/productos.json
```

El archivo almacenó la información del producto en formato JSON.

---

### Prueba 4: Cerrar la aplicación

Se seleccionó:

```text
9. Salir
```

La aplicación se cerró completamente.

---

### Prueba 5: Ejecutar nuevamente

Se volvió a ejecutar:

```powershell
python restaurante_app/main.py
```

---

### Prueba 6: Listar los productos

Se seleccionó:

```text
5. Listar productos
```

El producto registrado anteriormente volvió a aparecer.

Esto permitió comprobar que la información no dependía únicamente de la memoria temporal del programa.

---

### Prueba 7: Actualizar un producto

Se seleccionó:

```text
3. Actualizar producto
```

Se modificó la información de un producto.

Después de la actualización, el archivo:

```text
datos/productos.json
```

fue actualizado.

---

### Prueba 8: Reiniciar después de actualizar

Se cerró y volvió a ejecutar la aplicación.

Posteriormente se listaron nuevamente los productos y se comprobó que la información actualizada permanecía almacenada.

---

### Prueba 9: Eliminar un producto

Se seleccionó:

```text
4. Eliminar producto
```

Después de confirmar la eliminación, el archivo JSON fue actualizado.

Al reiniciar la aplicación se comprobó que el producto eliminado ya no aparecía.

---

## 14. Resultado de las pruebas

| Prueba | Resultado |
|---|---|
| Inicio sin `productos.json` | Correcto |
| Registro de producto | Correcto |
| Creación/actualización de `productos.json` | Correcto |
| Cierre de la aplicación | Correcto |
| Reinicio de la aplicación | Correcto |
| Recuperación de productos | Correcto |
| Búsqueda de productos | Correcto |
| Actualización de productos | Correcto |
| Persistencia de actualización | Correcto |
| Eliminación de productos | Correcto |
| Persistencia de eliminación | Correcto |
| Manejo de archivo inexistente | Correcto |
| Reconstrucción como objetos `Producto` | Correcto |

---

## 15. Flujo general del sistema

```text
                         INICIO
                           │
                           ▼
                 Crear Restaurante
                           │
                           ▼
                Crear ArchivoServicio
                           │
                           ▼
                Cargar productos.json
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
          Archivo encontrado   Archivo no encontrado
                  │                 │
                  ▼                 ▼
              json.load()    Colección vacía
                  │
                  ▼
         Validar estructura JSON
                  │
                  ▼
         Validar cada registro
                  │
                  ▼
          Crear objetos Producto
                  │
                  ▼
        Registrar en Restaurante
                  │
                  ▼
              Mostrar menú
                  │
                  ▼
        Operación seleccionada
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
    Registrar  Actualizar  Eliminar
        │         │         │
        └─────────┼─────────┘
                  │
                  ▼
       ArchivoServicio guarda
                  │
                  ▼
             json.dump()
                  │
                  ▼
        productos.json actualizado
```

---

## 16. Separación de responsabilidades

El proyecto mantiene una arquitectura modular.

| Componente | Responsabilidad |
|---|---|
| `Producto` | Representar productos y validar sus datos |
| `Usuario` | Representar usuarios y validar sus datos |
| `Restaurante` | Administrar las colecciones y operaciones |
| `ArchivoServicio` | Leer y guardar productos en JSON |
| `main.py` | Coordinar el menú y la interacción con el usuario |
| `productos.json` | Almacenar persistentemente los productos |

La carpeta:

```text
datos/
```

se utiliza únicamente como ubicación del archivo JSON y no constituye una nueva capa de la arquitectura.

---

## 17. Tecnologías utilizadas

- **Python 3**
- **Programación Orientada a Objetos**
- **Módulo `json`**
- **Manejo de archivos**
- **Excepciones de Python**
- **Persistencia mediante JSON**
- **Anotaciones de tipos**
- **Estructuras de datos de Python**

No se utilizaron:

- Bases de datos.
- Interfaces gráficas.
- Frameworks.
- Persistencia de usuarios.
- Funcionalidades correspondientes a semanas posteriores.

---

## 18. Mejoras incorporadas en la Semana 10

En comparación con la versión anterior del proyecto, se incorporaron las siguientes mejoras:

- Se creó la carpeta `datos/`.
- Se incorporó `datos/productos.json`.
- Se creó `servicios/archivo_servicio.py`.
- Se implementó la persistencia de productos.
- Se implementó `json.dump()`.
- Se implementó `json.load()`.
- Se utilizó `with open()`.
- Se utilizó codificación `UTF-8`.
- Se implementó la carga automática de productos.
- Se reconstruyeron los registros JSON como objetos `Producto`.
- Se mantuvieron las validaciones de `Producto`.
- Se actualiza el JSON después de registrar productos.
- Se actualiza el JSON después de actualizar productos.
- Se actualiza el JSON después de eliminar productos.
- Se implementó el manejo de `FileNotFoundError`.
- Se implementó el manejo de `json.JSONDecodeError`.
- Se implementó el manejo de `PermissionError`.
- Se implementó el manejo de `KeyError`.
- Se mantuvo el manejo de `ValueError`.
- Se contempló `TypeError` para datos incompatibles.
- Se mantuvo la administración de productos dentro de `Restaurante`.
- Se mantuvo la interacción mediante consola en `main.py`.
- Se conservaron las funcionalidades desarrolladas en semanas anteriores.

---

## 19. Consideraciones sobre el archivo JSON

El archivo `productos.json` funciona como medio de persistencia.

No reemplaza a la clase `Producto`.

El funcionamiento del sistema sigue siendo orientado a objetos:

```text
JSON
 ↓
Diccionario
 ↓
Producto
 ↓
Restaurante
 ↓
Operaciones del sistema
```

De esta manera, los datos almacenados externamente vuelven a convertirse en objetos del dominio cuando la aplicación inicia.

---

## 20. Conclusión

La implementación realizada en la Semana 10 permite que el sistema `restaurante_app` conserve los productos registrados entre diferentes ejecuciones de la aplicación.

La incorporación del archivo:

```text
datos/productos.json
```

permite almacenar los productos de manera persistente utilizando una estructura compatible con JSON.

El proyecto mantiene la separación de responsabilidades:

- `Producto` representa y valida los productos.
- `Usuario` representa y valida los usuarios.
- `Restaurante` administra las colecciones y operaciones.
- `ArchivoServicio` administra exclusivamente la lectura y escritura del archivo JSON.
- `main.py` coordina la interacción con el usuario y el flujo de carga y guardado.

Además, se incorporó el manejo específico de excepciones para situaciones como archivos inexistentes, JSON inválido, permisos insuficientes, registros incompletos y datos inválidos.

La prueba de cierre y reinicio de la aplicación permitió comprobar que los productos registrados permanecen disponibles posteriormente y que las modificaciones y eliminaciones también se conservan correctamente.

Por lo tanto, el proyecto mantiene las funcionalidades desarrolladas anteriormente y agrega una persistencia funcional de productos mediante JSON, cumpliendo con los requerimientos establecidos para la Semana 10.