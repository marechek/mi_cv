# MiCV — Aplicación Django

## 📌 Descripción

MiCV es una aplicación web desarrollada con Django que permite visualizar un currículum vitae de forma dinámica, obteniendo la información desde una base de datos y presentándola en una interfaz moderna y profesional.

El sistema incluye secciones de perfil, resumen profesional, experiencia laboral, educación, habilidades e idiomas, organizadas en un diseño de dos columnas similar a plantillas reales de CV.

---

## 🚀 Tecnologías utilizadas

* Python 3
* Django
* Bootstrap 5
* CSS personalizado
* SQLite

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/marechek/mi_cv.git
cd mi_cv
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno

```bash
venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor

```bash
python manage.py runserver
```

### 8. Acceder a la aplicación

* CV: http://127.0.0.1:8000/
* Admin: http://127.0.0.1:8000/admin/

---

## 🧱 Estructura del proyecto

```
mi_cv/
│
├── manage.py
├── requirements.txt
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── cv/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/cv/index.html
│
├── templates/
│   └── base.html
│
├── static/
│   └── css/style.css
│
└── media/
    └── profile/
```

---

## 🔄 Flujo de funcionamiento en Django

Cuando alguien entra a la página, el navegador le pide a Django una URL. Django revisa sus rutas (`urls.py`) para ver a dónde tiene que enviar esa petición.
Después, esa URL llega a una vista (`views.py`), que es donde se decide qué hacer. La vista puede buscar información en la base de datos usando los modelos.
Con esos datos, Django arma una página HTML (`index.html`) y finalmente se la devuelve al navegador, ya con estilos, para que el usuario la vea.

---

## ⚠️ Dificultades encontradas

Durante el desarrollo me encontré con varios desafíos. Por ejemplo, entender bien la diferencia entre los archivos estáticos (static) y los archivos dinámicos (media).
También me costó ajustar el diseño para que se viera igual a la maqueta, sobre todo alinear bien los elementos del timeline y las distintas secciones.
Otro punto fue manejar correctamente las rutas de las imágenes y definir una imagen por defecto cuando no hay foto de perfil.
Además, tuve que trabajar bastante en los espacios y la jerarquía visual para que el diseño se viera más ordenado y profesional.
Todos estos problemas los fui resolviendo haciendo ajustes en el CSS, en los templates y aplicando buenas prácticas de Django.

---

## ✨ Características principales

* Renderizado dinámico del CV desde base de datos
* Panel de administración para gestionar contenido
* Diseño profesional con Bootstrap + CSS personalizado
* Timeline para experiencia laboral
* Navegación interna entre secciones
* Uso correcto de archivos `static` y `media`
* Código limpio validado con flake8

---

## 🧪 Buenas prácticas aplicadas

* Análisis estático con **flake8**
* Eliminación de imports no utilizados
* Separación adecuada entre `static` y `media`
* Estructura clara y mantenible del proyecto
* Uso de templates reutilizables (`base.html`)

---

## 📝 Consideraciones

* Las imágenes de perfil se almacenan en `media/`
* En caso de no existir imagen, se utiliza un placeholder desde `static/`

---

## 📸 Capturas

### Vista principal
![Vista principal](static\img\CV_navegador.png "Vista Principal")

### Panel admin
![Panel admin](static\img\Admin.png "Panel Admin")

### Código
![Código](static\img\Codigo.png "Código")

---

## 👤 Autor

Proyecto desarrollado por **Marcos Elias**
