# Proyecto MiCV — Django

## 1. Descripción del proyecto

MiCV es una aplicación web desarrollada con Django que permite visualizar un currículum vitae profesional de forma dinámica.

El sistema obtiene la información desde una base de datos y la presenta en una interfaz moderna, estructurada en dos columnas, incluyendo experiencia laboral, educación, habilidades, idiomas y datos de contacto.

---

## 2. ¿Cómo instalar y ejecutar el proyecto?

### Requisitos

* Python 3.x
* pip

### Pasos

1. Clonar el repositorio:

```
git clone https://github.com/TU_USUARIO/micv_project.git
cd micv_project
```

2. Crear entorno virtual:

```
python -m venv venv
```

3. Activar entorno:

```
venv\Scripts\activate
```

4. Instalar dependencias:

```
pip install -r requirements.txt
```

5. Ejecutar migraciones:

```
python manage.py migrate
```

6. Crear superusuario (opcional):

```
python manage.py createsuperuser
```

7. Ejecutar servidor:

```
python manage.py runserver
```

8. Abrir en navegador:

```
http://127.0.0.1:8000/
```

---

## 3. Estructura del proyecto

```
micv_project/
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
│   └── static/
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

## 4. Flujo de una petición en Django

Cuando alguien entra a la página, el navegador le pide a Django una URL. Django revisa sus rutas (`urls.py`) para ver a dónde tiene que enviar esa petición.
Después, esa URL llega a una vista (`views.py`), que es donde se decide qué hacer. La vista puede buscar información en la base de datos usando los modelos.
Con esos datos, Django arma una página HTML (`index.html`) y finalmente se la devuelve al navegador, ya con estilos, para que el usuario la vea.

---

## 5. Dificultades encontradas

Durante el desarrollo me encontré con varios desafíos. Por ejemplo, me costó ajustar el diseño para que se viera igual a la maqueta, sobre todo alinear bien los elementos del timeline y las distintas secciones.
Otro punto fue manejar correctamente las rutas de las imágenes y definir una imagen por defecto cuando no hay foto de perfil.
Además, tuve que trabajar bastante en los espacios y la jerarquía visual para que el diseño se viera más ordenado y profesional.
Todos estos problemas los fui resolviendo haciendo ajustes en el CSS, en los templates y aplicando buenas prácticas de Django.

---

## 6. Buenas prácticas aplicadas

Durante el desarrollo del proyecto se aplicaron buenas prácticas de calidad de código:

* Uso de **flake8** para análisis estático
* Eliminación de imports no utilizados
* Corrección de advertencias de estilo
* Organización clara de archivos y estructura del proyecto
* Separación correcta entre archivos estáticos (`static`) y archivos dinámicos (`media`)

Estas prácticas permiten mantener un código más limpio, legible y mantenible.

---