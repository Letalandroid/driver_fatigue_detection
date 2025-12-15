#!/bin/bash
# Script para construir todos los ejecutables

echo "=========================================="
echo "Build System - Driver Fatigue Detection"
echo "=========================================="
echo ""

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    echo "Activando entorno virtual..."
    source venv/bin/activate
fi

# Verificar que PyInstaller está instalado
echo "Verificando PyInstaller..."
pip install pyinstaller > /dev/null 2>&1

# Limpiar builds anteriores
echo "Limpiando builds anteriores..."
rm -rf build dist __pycache__ *.spec

# Construir servidor
echo ""
echo "=========================================="
echo "Construyendo servidor..."
echo "=========================================="
python build_server.py

# Construir cliente
echo ""
echo "=========================================="
echo "Construyendo cliente..."
echo "=========================================="
python build_client.py

echo ""
echo "=========================================="
echo "Build completado!"
echo "=========================================="
echo "Ejecutables disponibles en:"
echo "  - Servidor: dist/DrowsinessDetectionServer"
echo "  - Cliente: dist/DrowsinessDetectionClient"
echo ""

