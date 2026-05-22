# E1 - Gestión de Pacientes y Tomas de Tensión

Aplicación de escritorio para gestionar pacientes de un centro sanitario y sus tomas de tensión arterial.

## Objetivo

El sistema permite registrar, consultar, modificar y eliminar pacientes y tomas de tensión.  
También permite realizar un pequeño estudio de las tensiones de un paciente, calculando la media y mostrando la última toma registrada.

## Arquitectura

El proyecto está organizado siguiendo una arquitectura de 3 capas:

- Presentación
- Negocio
- Datos

La capa de presentación aplica el patrón MVC.

## Estructura

- `main.py`: punto de entrada de la aplicación e inyección de dependencias.
- `view.py`: interfaz gráfica con Tkinter.
- `controllers.py`: comunica la vista con la capa de negocio.
- `services.py`: lógica de negocio y validaciones.
- `repositories.py`: acceso a los datos.
- `models.py`: modelos de dominio validados con Pydantic.
- `db.py`: conexión a la base de datos.

## Funcionalidades

### Pacientes

- Crear paciente
- Listar pacientes
- Actualizar paciente
- Eliminar paciente

### Tomas de tensión

- Crear toma de tensión
- Listar tomas
- Actualizar toma
- Eliminar toma

### Estudio de tensiones

- Media de tensiones de un paciente
- Última toma registrada

## Tecnologías utilizadas

- Python
- Tkinter
- Pydantic
- PyMongo
- MongoDB

## Principios aplicados

- Separación de responsabilidades
- MVC
- Inyección de dependencias
- Singleton para la conexión
- KISS
- DRY
- YAGNI