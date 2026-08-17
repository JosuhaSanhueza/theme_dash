# 🚀 OrionShield SaaS Dashboard Theme for Django (`theme_dash`)

Una maqueta y plantilla de administración SaaS completa, moderna e inspirada en **Skote / OrionShield**, optimizada como una **App Reutilizable de Django** lista para producción.

Incluye sistema de diseño dinámico (Modo Claro/Oscuro), menú lateral inteligente colapsable, widgets de estadísticas (Chart.js), panel SuperAdmin para gestión de Usuarios & Roles (con modales), Auditoría de Logs de Seguridad y un **Mini-Instalador Automatizado en Python (`install.py`)**.

---

## 📖 Guía Completa de Instalación & Uso en Django

Existen 2 métodos para integrar este tema en cualquier proyecto Django nuevo o existente:

---

### ⚡ Método 1: Instalación Automatizada con `install.py` (Recomendado)

Si ya tienes un proyecto Django creado en tu computadora, puedes inyectar todo el tema en **menos de 5 segundos** ejecutando en tu terminal:

```bash
python install.py /ruta/a/tu/proyecto_django
```

#### ¿Qué realiza este script automáticamente?
1. **Copia de App**: Copia la carpeta `theme_dash/` (con todos sus CSS, JS, SVG y plantillas HTML) a la raíz de tu proyecto destino.
2. **Inyección en `settings.py`**: Localiza la configuración de tu proyecto y agrega `'theme_dash'` a `INSTALLED_APPS` sin duplicar.
3. **Verificación de salida**: Confirma en la consola con mensajes claros que la app quedó lista para usarse.

---

### 🛠️ Método 2: Instalación Manual Paso a Paso

Si prefieres realizar la integración manualmente:

#### Paso 1: Copiar la App
Copia la carpeta de la app `theme_dash/` dentro del directorio principal de tu proyecto Django.

#### Paso 2: Registrar la App en `settings.py`
Abre el archivo `settings.py` de tu proyecto y registra `'theme_dash'` en la lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # OrionShield SaaS Theme App
    'theme_dash',
]
```

#### Paso 3: Verificar la Instalación
En la terminal de tu proyecto Django, puedes verificar que la plantilla esté correctamente integrada ejecutando:

```bash
python manage.py setup_theme
```

---

## 💻 Cómo Usar la Plantilla Base en tus Vistas de Django

En cualquier vista o archivo HTML de tu proyecto, extiende la plantilla maestra `theme_dash/base.html`:

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
        <p>¡Tu contenido se renderiza dentro del layout OrionShield automáticamente!</p>
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

### Bloques de Plantilla Disponibles (`base.html`)
- `{% block title %}`: Personaliza el título de la pestaña del navegador.
- `{% block extra_css %}`: Carga archivos CSS adicionales para esa página específica.
- `{% block header %}`: Sobreescribe la barra superior si es necesario.
- `{% block sidebar %}`: Sobreescribe la barra de navegación lateral.
- `{% block content %}`: **Área principal de contenido de tu aplicación.**
- `{% block footer %}`: Sobreescribe el pie de página.
- `{% block extra_js %}`: Carga JavaScript o scripts de gráficos adicionales al final del documento.

---

## 🗺️ Vistas de Demostración Incluidas

- **Dashboard Principal**: `http://127.0.0.1:8000/`
- **Analíticas & Métricas**: `http://127.0.0.1:8000/analytics/`
- **Gestión de Usuarios & Roles (Modales)**: `http://127.0.0.1:8000/superadmin/users/`
- **Auditoría de Logs de Seguridad**: `http://127.0.0.1:8000/superadmin/logs/`
- **Proyectos & Clientes**: `http://127.0.0.1:8000/projects/`
- **Tablas de Datos**: `http://127.0.0.1:8000/tables/`
- **Formularios & Ajustes**: `http://127.0.0.1:8000/forms/`
- **Autenticación Login (Google SSO)**: `http://127.0.0.1:8000/login/`
- **Página Starter (En Blanco)**: `http://127.0.0.1:8000/starter/`

---

## ⚡ Servidor de Desarrollo Local

Para previsualizar y probar todas las vistas en este repositorio:

```bash
python manage.py runserver 8000
```
