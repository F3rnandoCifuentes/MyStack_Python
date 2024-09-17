
# MyStack_Python

**Implementación de la estructura de datos Pila en Python**

## 1. Descripción:

Este proyecto implementa una estructura de datos de pila (LIFO - Last In, First Out). La pila está compuesta de nodos, donde cada nodo contiene un dato, una referencia al nodo siguiente y una referencia al nodo anterior (en caso de ser una lista doblemente enlazada).

El proyecto está desarrollado en el lenguaje de programación Python 3.12.6, y utiliza el paradigma de programación orientada a objetos (OOP) para encapsular la funcionalidad de los nodos y de la pila. Se implementan métodos como `push`, `pop`, `peek`, `is_empty`, y `size` que permiten manipular la pila de forma eficiente.

## 2. Estructura del proyecto:

- **Node**: Clase que representa un nodo de la lista doblemente enlazada, con punteros hacia el nodo anterior y siguiente, y un dato almacenado.
- **Stack**: Clase que representa la pila, con operaciones estándar como agregar (`push`), eliminar el último elemento (`pop`), visualizar el último elemento (`peek`), verificar si está vacía (`is_empty`), y conocer su tamaño (`size`).

## 3. Requerimientos de software:

Para ejecutar este proyecto, necesitas:

- **Python 3.12.6** o una versión estable. Puedes descargar Python desde [python.org](https://www.python.org/).
- No se necesitan paquetes adicionales de Python, ya que el código solo utiliza librerías estándar.

## 4. Instrucciones para la ejecución del código:

1. Asegúrate de tener **Python 3.12.6** instalado.
2. Descarga o clona el proyecto en tu máquina local.
3. Ejecuta el archivo Python que contiene la implementación de la pila en un IDE o editor de texto.

Para ejecutar el programa en una terminal ingrese:

\`\`\`bash
python myStack.py
\`\`\`

## 5. Funcionalidades principales:

- **push(data)**: Agrega un nuevo nodo con el dato `data` en la parte superior de la pila.
- **pop()**: Elimina y retorna el dato del nodo en la parte superior de la pila. Si la pila está vacía, lanza una excepción.
- **peek()**: Retorna el dato del nodo en la parte superior de la pila sin eliminarlo.
- **is_empty()**: Verifica si la pila está vacía.
- **size()**: Retorna el tamaño actual de la pila.
