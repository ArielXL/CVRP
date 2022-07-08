# Problema de Enrutamiento de Vehı́culos con Capacidad, Ventana de Tiempo e Ida y Recogida Utilizando Algoritmos Genéticos

## Autores

| **Nombre y Apellidos** |                          **Coreo**                           | **Grupo** |
| :--------------------: | :----------------------------------------------------------: | :-------: |
| Thalia Blanco Figueras | [lia.blanco98@gmail.com](mailto:lia.blanco98@gmail.com)         |   C-512   |
|  Ariel Plasencia Díaz  | [arielplasencia00@gmail.com](mailto:arielplasencia00@gmail.com) |   C-512   |

## Implementación y Ejecución

### Implementación

La parte computacional del proyecto está implementada completamente en [python 3](https://es.wikipedia.org/wiki/Python). Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, pues soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma. Nos apoyamos en varias librerías provistas por dicho lenguaje de programación para una mejor y mayor comprensión en el código.

Para la instalación de las librerías ejecutamos el siguiente comando:

```bash
pip3 install -r requirements.txt
```

### Ejecución

Para ejecutar nuestro proyecto es necesario correr los siguientes comandos desde una terminal, con la ruta asociada a la carpeta [src](..\Codigo\src):

```bash
cd src/
python3 main.py
```

Además, proveemos un `makefile` con las siguientes funcionalidades:

```text
run                            Run the project
simulation                     Simulate the project
info                           Display project description
version                        Show the project version
clean                          Remove temporary files
help                           Show this help
```

Cabe mencionar que los ficheros de entrada para el algoritmo se encuentran en la carpeta [data](./src/data/).

## Informe Escrito

Para una mejor explicación agregamos un informe escrito, el cual podemos encontrar [aquí](./doc/Enrutamiento de Vehiculos.pdf).