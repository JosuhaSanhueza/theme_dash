#!/usr/bin/env python3
"""
install.py - Mini-Instalador Automatizado para theme_dash

Uso:
    python install.py /ruta/a/tu/proyecto_django

Este script automatiza la integración de la app 'theme_dash' en cualquier proyecto de Django:
1. Copia la app 'theme_dash' con todos sus estáticos y plantillas al proyecto destino.
2. Inyecta automáticamente 'theme_dash' en INSTALLED_APPS dentro del settings.py de tu proyecto.
3. Genera una vista de prueba starter si lo deseas.
"""

import os
import sys
import shutil
import re
from pathlib import Path

# Colores para la terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_banner():
    print(f"{CYAN}{BOLD}")
    print("=" * 65)
    print("      🚀 SKOTE SAAS DASHBOARD THEME - INSTALADOR EN PYTHON")
    print("=" * 65)
    print(f"{RESET}")

def find_settings_file(target_dir: Path):
    """Busca el archivo settings.py dentro del proyecto Django destino."""
    # Buscar en primer nivel y subdirectorios de primer nivel
    candidates = list(target_dir.glob("**/settings.py"))
    # Excluir virtuales como venv o env
    candidates = [c for c in candidates if not any(part in c.parts for part in ['.venv', 'venv', 'env', '.env'])]
    
    if not candidates:
        return None
    return candidates[0]

def inject_installed_apps(settings_path: Path):
    """Agrega 'theme_dash' a INSTALLED_APPS en settings.py sin duplicarlo."""
    with open(settings_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "'theme_dash'" in content or '"theme_dash"' in content:
        print(f"  {YELLOW}ℹ️  'theme_dash' ya está presente en INSTALLED_APPS de {settings_path.name}{RESET}")
        return True

    match = re.search(r'INSTALLED_APPS\s*=\s*\[', content)
    if match:
        insert_pos = match.end()
        new_content = content[:insert_pos] + "\n    'theme_dash',  # Instalado automáticamente por install.py" + content[insert_pos:]
        with open(settings_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  {GREEN}✅ 'theme_dash' agregado exitosamente a INSTALLED_APPS en {settings_path}{RESET}")
        return True
    else:
        print(f"  {RED}⚠️ No se pudo localizar la lista INSTALLED_APPS en {settings_path}. Por favor agrégala manualmente.{RESET}")
        return False

def install_theme(target_path_str: str):
    print_banner()
    source_dir = Path(__file__).resolve().parent / "theme_dash"
    
    if not source_dir.exists():
        print(f"{RED}❌ Error: No se encontró la carpeta 'theme_dash' en el origen ({source_dir}).{RESET}")
        sys.exit(1)

    target_dir = Path(target_path_str).resolve()
    if not target_dir.exists():
        print(f"{RED}❌ Error: El directorio destino '{target_dir}' no existe.{RESET}")
        sys.exit(1)

    dest_theme_dir = target_dir / "theme_dash"

    print(f"{BOLD}📂 Proyecto destino:{RESET} {target_dir}")
    print(f"{BOLD}📦 App a instalar:{RESET} {source_dir} -> {dest_theme_dir}")

    # Copiar o actualizar la app
    if dest_theme_dir.exists():
        print(f"  {YELLOW}⚠️  La carpeta 'theme_dash' ya existía en el destino. Actualizando archivos...{RESET}")
        shutil.rmtree(dest_theme_dir)
    
    shutil.copytree(source_dir, dest_theme_dir)
    print(f"  {GREEN}✅ App 'theme_dash' copiada exitosamente a {dest_theme_dir}{RESET}")

    # Inyectar en settings.py
    settings_path = find_settings_file(target_dir)
    if settings_path:
        print(f"  {CYAN}🔍 Archivo settings.py localizado:{RESET} {settings_path}")
        inject_installed_apps(settings_path)
    else:
        print(f"  {YELLOW}⚠️ No se encontró settings.py automáticamente. Recuerda agregar 'theme_dash' a INSTALLED_APPS.{RESET}")

    # Generar demo de ejemplo en el proyecto destino si tiene carpeta de templates o views
    print("\n" + f"{CYAN}{BOLD}🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!{RESET}\n")
    print(f"{BOLD}Para usar el tema en tu proyecto Django:{RESET}")
    print(f" 1. En cualquier vista/template de tu proyecto, simplemente extienda el base:{RESET}")
    print(f"    {GREEN}{{% extends \"theme_dash/base.html\" %}}{RESET}")
    print(" 2. Agrega bloques de contenido:")
    print(f"    {GREEN}{{% block title %}} Mi Vista SaaS {{% endblock %}}{RESET}")
    print(f"    {GREEN}{{% block content %}}{RESET}")
    print("        <h1>¡Bienvenido a mi App SaaS!</h1>")
    print(f"    {GREEN}{{% endblock %}}{RESET}")
    print("\n" + "=" * 65 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_banner()
        print(f"{BOLD}Uso de este script:{RESET}")
        print(f"  python install.py <ruta_del_proyecto_django>\n")
        print(f"{BOLD}Ejemplo:{RESET}")
        print(f"  python install.py /home/usuario/Proyectos/mi_saas_django\n")
        sys.exit(0)

    install_theme(sys.argv[1])
