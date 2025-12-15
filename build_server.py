"""
Script para construir ejecutable del servidor
Usa PyInstaller para crear un ejecutable standalone
"""

import PyInstaller.__main__
import os

# Configuración
APP_NAME = "DrowsinessDetectionServer"
MAIN_SCRIPT = "app.py"
ICON_PATH = None

# Archivos y carpetas a incluir
ADDITIONAL_DATA = [
    ("drowsiness_processor", "drowsiness_processor"),
]

# Archivos ocultos a incluir
HIDDEN_IMPORTS = [
    "fastapi",
    "uvicorn",
    "websockets",
    "cv2",
    "numpy",
    "mediapipe",
    "base64",
    "json",
]

def build_executable():
    """Construye el ejecutable del servidor"""
    
    # Intentar usar archivo .spec si existe
    spec_file = "pyinstaller_server.spec"
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
            "--console",  # Con consola (para ver logs del servidor)
            "--clean",
            "--noconfirm",
        ]
        
        # Agregar datos adicionales
        for src, dst in ADDITIONAL_DATA:
            pyinstaller_args.extend(["--add-data", f"{src}{os.pathsep}{dst}"])
        
        # Agregar imports ocultos
        for module in HIDDEN_IMPORTS:
            pyinstaller_args.extend(["--hidden-import", module])
    
    # Ejecutar PyInstaller
    print("Construyendo ejecutable del servidor...")
    print(f"Comando: pyinstaller {' '.join(pyinstaller_args)}")
    PyInstaller.__main__.run(pyinstaller_args)
    
    print(f"\n✓ Ejecutable creado en: dist/{APP_NAME}")
    print("Para ejecutar: ./dist/DrowsinessDetectionServer")

if __name__ == "__main__":
    build_executable()

