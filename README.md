
# MyStack_Python

**Implementación de la estructura de datos Pila en Python**

# Autores
- Ibeth Stefanny Pulido Arias
- David Fernando Cifuentes Bohórquez

## 1. Descripción:

Este proyecto implementa una estructura de datos de pila (LIFO - Last In, First Out). La pila está compuesta de nodos, donde cada nodo contiene un dato, una referencia al nodo siguiente y una referencia al nodo anterior (en caso de ser una lista doblemente enlazada).

El proyecto está desarrollado en el lenguaje de programación Python 3.12.6, y utiliza el paradigma de programación orientada a objetos (OOP) para encapsular la funcionalidad de los nodos y de la pila. Se implementan métodos como `push`, `pop`, `peek`, `is_empty`, y `size` que permiten manipular la pila de forma eficiente.

## 2. Estructura del proyecto:

- **Node**: Clase que representa un nodo de la lista doblemente enlazada, con punteros hacia el nodo anterior y siguiente, y un dato almacenado.
- **Stack**: Clase que representa la pila, con operaciones estándar como agregar (`push`), eliminar y visualizar el último elemento (`pop`), visualizar el último elemento (`peek`), verificar si está vacía (`is_empty`), y conocer su tamaño (`size`).

## 3. Requerimientos de software:

Para ejecutar este proyecto, necesitas:

- Descargar Python en una versión estable, abre un navegador web y dirígete al sitio web oficial de Python en https://www.python.org/. 
    Haz clic en el botón de descarga para Windows y descarga la última versión estable de Python, preferiblemente **Python 3.12.6**.
    Una vez descargado, haz doble clic en el archivo de instalación (.exe) para iniciar el instalador de Python.
    Asegúrate de marcar la casilla que dice "Add Python X.X to PATH" (donde "X.X" es la versión de Python que estás instalando). Esto asegurará que Python se agregue al PATH de tu sistema y puedas ejecutarlo desde la línea de comandos.
    Haz clic en "Instalar Ahora" y sigue las instrucciones en pantalla para completar la instalación de Python.
    Una vez finalizada la instalación, abre una ventana de línea de comandos (cmd) y escribe 
    **python --version** para verificar que Python se haya instalado correctamente.

- Para el editor Visual Studio Code es necesaria la instación de las extenciones requeridas.
- Para el IDE Eclipse, es necesario añadir el plugin PyDev para programar en Python
- Para programar en IntelliJ IDEA, necesitas instalar el plugin Python Plugin


## 4. Instrucciones para la ejecución del código:

1. Asegúrate de tener **Python 3.12.6** o una versión estable instalada.
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