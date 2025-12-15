"""
Script para construir ejecutable del cliente (GUI)
Usa PyInstaller para crear un ejecutable standalone
"""

import PyInstaller.__main__
import os
import shutil

# Configuración
APP_NAME = "DrowsinessDetectionClient"
MAIN_SCRIPT = "main.py"
ICON_PATH = None  # Puedes agregar una ruta a un archivo .ico si tienes uno

# Archivos y carpetas a incluir
ADDITIONAL_DATA = [
    ("gui", "gui"),
    ("drowsiness_processor", "drowsiness_processor"),
]

# Archivos ocultos a incluir
HIDDEN_IMPORTS = [
    "flet",
    "cv2",
    "numpy",
    "websockets",
    "asyncio",
    "threading",
    "json",
    "base64",
    "PIL",
    "mediapipe",
]

def build_executable():
    """Construye el ejecutable del cliente"""
    
    # Intentar usar archivo .spec si existe
    spec_file = "pyinstaller_client.spec"
    if os.path.exists(spec_file):
        print(f"Usando archivo de especificación: {spec_file}")
        pyinstaller_args = [
            spec_file,
            "--clean",
            "--noconfirm",
        ]
    else:
        # Construir comando de PyInstaller manualmente
        pyinstaller_args = [
            MAIN_SCRIPT,
            "--name", APP_NAME,
            "--onefile",  # Crear un solo archivo ejecutable
            "--windowed",  # Sin consola (para GUI)
            "--clean",  # Limpiar archivos temporales
            "--noconfirm",  # No confirmar sobrescritura
        ]
        
        # Agregar datos adicionales
        for src, dst in ADDITIONAL_DATA:
            pyinstaller_args.extend(["--add-data", f"{src}{os.pathsep}{dst}"])
        
        # Agregar imports ocultos
        for module in HIDDEN_IMPORTS:
            pyinstaller_args.extend(["--hidden-import", module])
        
        # Agregar icono si existe
        if ICON_PATH and os.path.exists(ICON_PATH):
            pyinstaller_args.extend(["--icon", ICON_PATH])
    
    # Ejecutar PyInstaller
    print("Construyendo ejecutable del cliente...")
    print(f"Comando: pyinstaller {' '.join(pyinstaller_args)}")
    PyInstaller.__main__.run(pyinstaller_args)
    
    print(f"\n✓ Ejecutable creado en: dist/{APP_NAME}")
    print("Nota: En Windows será .exe, en Linux/macOS será sin extensión")

if __name__ == "__main__":
    build_executable()

