from django.core.management.base import BaseCommand
from django.conf import settings
import os
from pathlib import Path

class Command(BaseCommand):
    help = 'Inspecciona y verifica la integración del tema Skote SaaS (theme_dash) en el proyecto Django'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n======================================================='))
        self.stdout.write(self.style.SUCCESS('   🚀 SKOTE SAAS DASHBOARD THEME - ESTADO DE INSTALACIÓN'))
        self.stdout.write(self.style.SUCCESS('=======================================================\n'))

        # 1. Verificar INSTALLED_APPS
        if 'theme_dash' in settings.INSTALLED_APPS:
            self.stdout.write(self.style.SUCCESS('  ✅ [INSTALLED_APPS] theme_dash está correctamente registrado.'))
        else:
            self.stdout.write(self.style.ERROR('  ❌ [INSTALLED_APPS] theme_dash NO está registrado en settings.py.'))

        # 2. Verificar estáticos y plantillas
        theme_dir = Path(__file__).resolve().parent.parent.parent
        templates_exist = (theme_dir / 'templates' / 'theme_dash' / 'base.html').exists()
        static_exist = (theme_dir / 'static' / 'theme_dash' / 'css' / 'main.css').exists()

        if templates_exist:
            self.stdout.write(self.style.SUCCESS('  ✅ [PLANTILLAS] Plantillas maestras localizadas en theme_dash/base.html.'))
        else:
            self.stdout.write(self.style.WARNING('  ⚠️ [PLANTILLAS] No se encontraron las plantillas base.'))

        if static_exist:
            self.stdout.write(self.style.SUCCESS('  ✅ [ESTÁTICOS] CSS y JavaScript localizados.'))
        else:
            self.stdout.write(self.style.WARNING('  ⚠️ [ESTÁTICOS] No se encontraron archivos CSS/JS.'))

        self.stdout.write('\n' + self.style.MIGRATE_HEADING('Ejemplo de uso en tus templates:'))
        self.stdout.write("  {% extends 'theme_dash/base.html' %}")
        self.stdout.write("  {% block title %}Mi Título{% endblock %}")
        self.stdout.write("  {% block content %}")
        self.stdout.write("    <!-- Tu HTML aquí -->")
        self.stdout.write("  {% endblock %}\n")

        self.stdout.write(self.style.SUCCESS('=======================================================\n'))
