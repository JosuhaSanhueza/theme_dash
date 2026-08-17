# 🚀 Guía Rápida: Cómo usar `theme_dash` en cualquier Proyecto Django

Esta plantilla está construida como una **App Reutilizable de Django** que empaqueta todo el tema Skote (CSS, JS, iconos y plantillas HTML) para integrarse en **menos de 2 minutos**.

---

## ⚡ Método 1: Instalación Automatizada con `install.py` (Recomendado)

En la terminal de tu computadora, ejecuta el script `install.py` apuntando a la carpeta de tu nuevo proyecto Django:

```bash
python install.py /ruta/a/tu/proyecto_django
```

### ¿Qué hace `install.py` por ti?
1. Copia la app `theme_dash/` con todos sus recursos al directorio de tu proyecto.
2. Abre tu `settings.py` e inyecta automáticamente `'theme_dash'` en `INSTALLED_APPS`.
3. Confirma la instalación con mensajes a color en la consola.

---

## 🛠️ Método 2: Instalación Manual en 2 Pasos

Si prefieres hacerlo manualmente:

### Paso 1: Copiar la app
Copia la carpeta `theme_dash/` dentro de la raíz de tu proyecto Django.

### Paso 2: Registrar la App
Abre tu `settings.py` y agrega `'theme_dash'` a `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tema Skote SaaS Reutilizable
    'theme_dash',
]
```

---

## 💻 Cómo Usar las Plantillas en tus Vistas de Django

En cualquier vista o plantilla de tu proyecto, simplemente extiendes el layout maestro:

```html
{% extends "theme_dash/base.html" %}

{% block title %}Mi Nueva Vista SaaS{% endblock %}

{% block content %}
<div class="row">
  <div class="col-12">
    <div class="card">
      <div class="card-header">
        <h5 class="card-title">Título de tu Módulo</h5>
      </div>
      <div class="card-body">
        <p>¡Este contenido corre sobre la interfaz Skote automáticamente!</p>
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

### Bloques Disponibles en `base.html`:
- `{% block title %}`: Personaliza el título que aparece en la pestaña del navegador.
- `{% block extra_css %}`: Carga hojas de estilo CSS adicionales específicas de la página.
- `{% block header %}`: Sobreescribe la barra superior si es necesario.
- `{% block sidebar %}`: Sobreescribe el menú lateral si requieres navegación personalizada.
- `{% block content %}`: **Área principal de contenido de tu app.**
- `{% block footer %}`: Sobreescribe el pie de página.
- `{% block extra_js %}`: Agrega JavaScript o scripts personalizados al final del documento.

---

## 🔍 Comando de Verificación de Django

Una vez instalado en tu proyecto, puedes ejecutar en la terminal de tu proyecto:

```bash
python manage.py setup_theme
```

Este comando inspeccionará tu proyecto y confirmará que el tema esté listo para usarse.
