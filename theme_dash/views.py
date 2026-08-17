from django.shortcuts import render

app_name = 'theme_dash'

def dashboard_view(request):
    """Main SaaS Dashboard Page with KPIs, charts, and transaction list."""
    context = {
        'page_title': 'Dashboard SaaS',
        'active_menu': 'dashboard',
    }
    return render(request, 'theme_dash/pages/dashboard.html', context)

def analytics_view(request):
    """Analytics & Metrics Page."""
    context = {
        'page_title': 'Analíticas de Rendimiento',
        'active_menu': 'analytics',
    }
    return render(request, 'theme_dash/pages/analytics.html', context)

def superadmin_users_view(request):
    """Super Admin Panel - User & Role Management with Modals."""
    context = {
        'page_title': 'Gestión de Usuarios & Roles',
        'active_menu': 'superadmin_users',
    }
    return render(request, 'theme_dash/pages/superadmin_users.html', context)

def superadmin_logs_view(request):
    """Super Admin Panel - Security Audit Logs."""
    context = {
        'page_title': 'Auditoría de Logs del Sistema',
        'active_menu': 'superadmin_logs',
    }
    return render(request, 'theme_dash/pages/superadmin_logs.html', context)

def projects_view(request):
    """Projects & SaaS Subscriptions Management Page."""
    context = {
        'page_title': 'Gestión de Proyectos',
        'active_menu': 'projects',
    }
    return render(request, 'theme_dash/pages/projects.html', context)

def forms_view(request):
    """Rich UI Form Elements Page."""
    context = {
        'page_title': 'Elementos de Formulario',
        'active_menu': 'forms',
    }
    return render(request, 'theme_dash/pages/forms.html', context)

def tables_view(request):
    """Interactive Data Tables Page."""
    context = {
        'page_title': 'Tablas de Datos',
        'active_menu': 'tables',
    }
    return render(request, 'theme_dash/pages/tables.html', context)

def login_view(request):
    """Split-screen Auth Login Page."""
    context = {
        'page_title': 'Iniciar Sesión',
        'active_menu': 'login',
    }
    return render(request, 'theme_dash/pages/auth_login.html', context)

def register_view(request):
    """Split-screen Auth Register Page."""
    context = {
        'page_title': 'Crear Cuenta',
        'active_menu': 'register',
    }
    return render(request, 'theme_dash/pages/auth_register.html', context)

def starter_view(request):
    """Blank Starter Page for new Django views."""
    context = {
        'page_title': 'Página en Blanco (Starter)',
        'active_menu': 'starter',
    }
    return render(request, 'theme_dash/pages/starter.html', context)
