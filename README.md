# 🚀 MP-Fast-API

API REST desarrollada con **FastAPI** para la gestión de Items.  
Este proyecto forma parte de prácticas para reforzar arquitectura backend, validaciones con Pydantic, integración con base de datos y testing automatizado.

---

## 📌 Tecnologías Utilizadas

- 🐍 Python 3.10+
- ⚡ FastAPI
- 🗄 SQLAlchemy
- 🧠 Pydantic
- 🔥 Uvicorn
- 🧪 Pytest
- 🗃 SQLite

---

## 📂 Estructura del Proyecto

```
MP-Fast-API/
│
├── app/
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── models.py        # Modelos ORM (SQLAlchemy)
│   ├── schemas.py       # Esquemas de validación (Pydantic)
│   ├── database.py      # Configuración de base de datos
│   ├── routers/
│   │   └── items.py     # Endpoints del módulo Items
│   └── __init__.py
│
├── test.db              # Base de datos SQLite
├── requirements.txt     # Dependencias del proyecto
├── README.md
```

---

## ⚙️ Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/JAngelGL/MP-Fast-API.git
cd MP-Fast-API
```

### 2️⃣ Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la API

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

### 📚 Documentación automática

- Swagger UI:  
  `http://127.0.0.1:8000/docs`

---

## 📌 Endpoints Principales

### 📦 Items

| Método | Endpoint      | Descripción              |
|--------|--------------|--------------------------|
| POST   | /items/     | Crear un nuevo item      |
| GET    | /items/     | Obtener todos los items  |
| GET    | /items/{id} | Obtener item por ID      |
| PUT    | /items/{id} | Actualizar un item       |
| DELETE | /items/{id} | Eliminar un item         |

---

## 🧪 Testing

Para ejecutar las pruebas automatizadas:

```bash
pytest
```

---

## 🏗 Arquitectura

El proyecto sigue una estructura modular basada en buenas prácticas:

- Separación de responsabilidades
- Uso de Router para modularizar endpoints
- Validaciones con Pydantic
- ORM con SQLAlchemy
- Patrón CRUD
- Testing con TestClient

---

## 🎯 Objetivo del Proyecto

- Practicar desarrollo backend moderno con FastAPI
- Implementar CRUD completo
- Manejo de base de datos relacional
- Validaciones robustas
- Testing automatizado
- Preparación para entornos productivos

---

## 👨‍💻 Autor

José Ángel García López  
Ingeniería en Sistemas Digitales y Robótica  
Minor en Inteligencia Artificial para Ciencia de Datos  