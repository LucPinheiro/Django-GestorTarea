## Gestor de Tareas - Aplicación Web y Movil con Django

Aplicación web desarrollada con Django para la gestión completa de tareas mediante operaciones CRUD, importación/exportación CSV y una interfaz moderna inspirada en herramientas tipo Trello y Odoo.

---

## Funcionalidades principales

- Crear tareas mediante formularios web.
- Visualizar tareas en:
  - Vista Kanban
  - Vista Lista
- Editar tareas existentes.
- Eliminar tareas individualmente o en lote.
- Confirmación antes de eliminar registros.
- Importación masiva de tareas mediante archivos CSV.
- Exportación de tareas a CSV.
- Sistema de autenticación:
  - Login
  - Logout
  - Protección de vistas privadas
- Diseño responsive para escritorio y móvil.
- Interfaz moderna con Bootstrap 5 y CSS personalizado.

---

## Tecnologías utilizadas

- Python 3
- Django 5
- SQLite
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- ORM de Django
- ModelForm
- CSV module de Python

---

## Características técnicas implementadas

- Arquitectura MVC/MVT de Django.
- Uso de `models.py`, `views.py`, `forms.py` y `urls.py`.
- Sistema de rutas personalizado.
- Templates reutilizables mediante `base.html`.
- Uso de mensajes dinámicos (`messages framework`).
- CRUD completo.
- Sistema de filtros y búsqueda.
- Importación y exportación de datos CSV.
- Diseño responsive y experiencia de usuario moderna.

---

## Objetivo del proyecto

El objetivo de esta aplicación es facilitar la organización y gestión de tareas personales o profesionales mediante una interfaz intuitiva y funcionalidades avanzadas de administración de datos.

## Estructura del proyecto

```bash
gestor_tareas/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
│
├── mi_proyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tareas/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── ...
│   │
│   ├── static/
│   │   └── tareas/
│   │       └── style.css
│   │
│   └── templates/
│       └── tareas/
│           ├── base.html
│           ├── lista.html
│           ├── detalle.html
│           ├── formulario.html
│           ├── confirmar_eliminar.html
│           ├── importar_csv.html
│           └── login.html
│
├── media/
│
└── venv/
```
## 🔧 Instalación y configuración

### 📋 Requisitos previos

- Python 3.10+
- pip
- Virtualenv (opcional)

---

## 🚀 Instalación del proyecto

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/usuario/gestor_tareas.git
cd gestor_tareas
```

O descargar el archivo `.zip` y descomprimirlo.

---

### 2. Crear entorno virtual

#### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

---

### 6. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

---

## 🌐 Acceso a la aplicación

Aplicación:

```bash
http://127.0.0.1:8000
```

Panel administrador:

```bash
http://127.0.0.1:8000/admin
```

---

## 📖 Funcionalidades principales

## ✅ Gestión de tareas

- Crear tareas mediante formularios.
- Editar tareas existentes.
- Eliminar tareas.
- Visualizar detalles de cada tarea.
- Cambio rápido de estados.
- Prioridades visuales mediante estrellas.

---

## 📋 Vistas disponibles

### 🗂 Vista Kanban

- Organización visual por estados:
  - Borrador
  - Pendiente
  - En proceso
  - Completada

### 📑 Vista Lista

- Tabla organizada de tareas.
- Selección múltiple.
- Acciones masivas.
- Navegación rápida.

---

## 📂 Importación y exportación CSV

### 📥 Importar CSV

Permite cargar tareas automáticamente desde un archivo CSV.

### 📤 Exportar CSV

Genera un archivo CSV con todas las tareas registradas.

---

## 🔐 Sistema de autenticación

- Login de usuarios.
- Logout.
- Protección de vistas privadas.
- Gestión de sesiones.

---

## 🎨 Interfaz y diseño

- Diseño responsive.
- Inspiración visual en Odoo y Trello.
- Bootstrap 5 + CSS personalizado.
- Experiencia moderna para escritorio y móvil.

---

# 🗄️ Modelo de datos

## Tarea

```python
titulo
descripcion
estado
prioridad
fecha_creada
fecha_limite
```

---

# ⚙️ Tecnologías utilizadas

- Python 3
- Django 5
- SQLite
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- Django ORM
- ModelForms
- CSV module

---

# 🔒 Características técnicas

- Arquitectura MVT de Django.
- CRUD completo.
- Templates reutilizables.
- Sistema de rutas.
- Formularios dinámicos.
- Validación de datos.
- Sistema de mensajes.
- Responsive Design.

---

# 🚀 Posibles mejoras futuras

- Drag & Drop en vista Kanban.
- Notificaciones.
- Adjuntos de archivos.
- Usuarios y permisos avanzados.
- Calendario de tareas.
- Dashboard estadístico.

---

# 👨‍💻 Desarrollado con

- Django
- Bootstrap
- Python
- Mucho café ☕
  ---

## 📌 Información del proyecto

**Versión:** 1.0  
**Última actualización:** Mayo 2026

---
