# API para Gestión de Campañas Publicitarias

Esta solución implementa la arquitectura de clases básica para gestionar campañas publicitarias, permitiendo instanciar y manipular campañas con distintos tipos de anuncios. Se han implementado las clases necesarias siguiendo las especificaciones proporcionadas, incluyendo manejo de excepciones y validaciones.

## Descripción

Esta solución es parte del desarrollo de una API para una plataforma de marketing digital que gestiona campañas publicitarias en diversas plataformas. Las clases están diseñadas para facilitar la creación y manipulación de campañas y anuncios, respetando las reglas de negocio definidas.

## Estructura del Proyecto

- `error.py`: Define las excepciones personalizadas para manejar errores específicos.
- `anuncio.py`: Contiene las clases `Anuncio`, `Video`, `Display` y `Social` con sus respectivas validaciones y métodos.
- `campania.py`: Define la clase `Campania` que encapsula la lógica para manejar campañas y anuncios.
- `demo.py`: Script de demostración que permite interactuar con una campaña, modificando sus atributos y manejando excepciones.

## Clases y Funcionalidades

### error.py

Define las excepciones personalizadas:
- `Error`: Clase base para todas las excepciones.
- `LargoExcedidoError`: Excepción lanzada cuando el nombre de una campaña excede los 250 caracteres.
- `SubTipoInvalidoError`: Excepción lanzada cuando el subtipo de un anuncio no es válido.

### anuncio.py

Contiene las clases para manejar los diferentes tipos de anuncios:
- `Anuncio`: Clase base para anuncios con validaciones para ancho, alto, url_archivo, url_clic y sub_tipo.
- `Video`: Hereda de `Anuncio` y añade la validación de duración y métodos específicos.
- `Display`: Hereda de `Anuncio` y añade métodos específicos.
- `Social`: Hereda de `Anuncio` y añade métodos específicos.

### campania.py

Define la clase `Campania` que encapsula una colección de anuncios:
- Validaciones para el nombre de la campaña.
- Método para crear anuncios basados en datos proporcionados.
- Método `__str__` para obtener una representación de la campaña y sus anuncios.

### demo.py

Script de demostración que:
- Crea una instancia de `Campania` con un anuncio de tipo `Video`.
- Permite modificar el nombre de la campaña y el subtipo del anuncio mediante inputs del usuario.
- Maneja excepciones y las registra en un archivo de log.

## Uso

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Navega al directorio del proyecto y ejecuta el script `demo.py`.

```bash
python demo.py
```

El script solicitará al usuario ingresar un nuevo nombre para la campaña y un nuevo subtipo para el anuncio. Si se producen errores, se registrarán en un archivo de log en el directorio `logs`.

## Ejemplo de Ejecución

```plaintext
Ingrese el nuevo nombre para la campaña:
Nueva Campaña
Nombre de la campaña: Nueva Campaña
Anuncios: 1 Video, 0 Display, 0 Social
Ingrese el nuevo subtipo para el anuncio:
outstream
```

## Autor

Este proyecto fue desarrollado por [GabrielRecabarren](https://github.com/GabrielRecabarren).
