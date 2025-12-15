@echo off
REM Script para construir todos los ejecutables (Windows)

echo ==========================================
echo Build System - Driver Fatigue Detection
echo ==========================================
echo.

REM Activar entorno virtual si existe
if exist venv\Scripts\activate.bat (
    echo Activando entorno virtual...
    call venv\Scripts\activate.bat
)

REM Verificar que PyInstaller esta instalado
echo Verificando PyInstaller...
pip install pyinstaller > nul 2>&1

REM Limpiar builds anteriores
echo Limpiando builds anteriores...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
del /q *.spec 2>nul

REM Construir servidor
echo.
echo ==========================================
echo Construyendo servidor...
echo ==========================================
python build_server.py

REM Construir cliente
echo.
echo ==========================================
echo Construyendo cliente...
echo ==========================================
python build_client.py

echo.
echo ==========================================
echo Build completado!
echo ==========================================
echo Ejecutables disponibles en:
echo   - Servidor: dist\DrowsinessDetectionServer.exe
echo   - Cliente: dist\DrowsinessDetectionClient.exe
echo.
pause

