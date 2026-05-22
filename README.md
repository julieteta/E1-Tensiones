# E1 - Gestión de Tensiones

Aplicación de escritorio desarrollada en Python para la gestión de pacientes y tomas de tensión arterial.

## Tecnologías utilizadas

- Python
- Tkinter
- MongoDB
- PyMongo
- Pydantic

## Arquitectura

El proyecto sigue una arquitectura de 3 capas:

- Presentación
- Negocio
- Datos

La capa de presentación utiliza el patrón MVC.

## Estructura del proyecto

```text
project/
│
├── main.py
├── db.py
├── models.py
├── repositories.py
├── services.py
├── controllers.py
└── view.py