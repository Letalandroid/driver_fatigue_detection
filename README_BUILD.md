# Guía de Build y Generación de Ejecutables

Esta guía explica cómo generar ejecutables del Sistema de Detección de Somnolencia del Conductor y cómo convertir los documentos a PDF.

## Requisitos Previos

1. **Python 3.10 o superior**
2. **Entorno virtual activado** (recomendado)
3. **Todas las dependencias instaladas**

## Instalación de Dependencias de Build

```bash
pip install -r requirements_build.txt
```

## Generación de Ejecutables

### Opción 1: Build Completo (Recomendado)

#### Linux/macOS:
```bash
chmod +x build_all.sh
./build_all.sh
```

#### Windows:
```cmd
build_all.bat
```

### Opción 2: Build Individual

#### Servidor:
```bash
python build_server.py
```

#### Cliente (GUI):
```bash
python build_client.py
```

### Ubicación de Ejecutables

Los ejecutables se generan en el directorio `dist/`:

- **Linux/macOS**:
  - Servidor: `dist/DrowsinessDetectionServer`
  - Cliente: `dist/DrowsinessDetectionClient`

- **Windows**:
  - Servidor: `dist/DrowsinessDetectionServer.exe`
  - Cliente: `dist/DrowsinessDetectionClient.exe`

## Ejecución de los Ejecutables

### Servidor

```bash
# Linux/macOS
./dist/DrowsinessDetectionServer

# Windows
dist\DrowsinessDetectionServer.exe
```

### Cliente

```bash
# Linux/macOS
./dist/DrowsinessDetectionClient

# Windows
dist\DrowsinessDetectionClient.exe
```

## Notas Importantes

1. **Tamaño de Ejecutables**: Los ejecutables pueden ser grandes (50-200 MB) debido a que incluyen todas las dependencias.

2. **Primera Ejecución**: La primera ejecución puede ser más lenta mientras se cargan las librerías.

3. **Dependencias del Sistema**: Algunas dependencias (como OpenCV) pueden requerir librerías del sistema. Asegúrese de que estén instaladas.

4. **Cámara**: El cliente necesita acceso a la cámara web.

5. **Servidor**: El servidor debe estar ejecutándose antes de iniciar el cliente.

## Conversión de Documentos a PDF

### Conversión Automática

```bash
python convert_to_pdf.py
```

Este script convierte automáticamente todos los documentos Markdown en `docs/` a PDF:

- `docs/manual_usuario.md` → `docs/manual_usuario.pdf`
- `docs/manual_aplicacion_codigo.md` → `docs/manual_aplicacion_codigo.pdf`
- `docs/memoria_descriptiva_software.md` → `docs/memoria_descriptiva_software.pdf`
- `docs/descripcion_invento.md` → `docs/descripcion_invento.pdf`

### Requisitos para Conversión

- **WeasyPrint**: Instalado automáticamente con `requirements_build.txt`
- **Markdown**: Instalado automáticamente con `requirements_build.txt`

### Conversión Manual

Si prefiere convertir un documento específico:

```python
from convert_to_pdf import convert_md_to_pdf

convert_md_to_pdf("docs/manual_usuario.md", "docs/manual_usuario.pdf")
```

## Solución de Problemas

### Error: "PyInstaller no encontrado"

```bash
pip install pyinstaller
```

### Error: "Módulo no encontrado durante la ejecución"

Agregue el módulo faltante a `HIDDEN_IMPORTS` en `build_client.py` o `build_server.py`.

### Error: "WeasyPrint no se puede instalar"

En algunos sistemas, WeasyPrint requiere dependencias del sistema:

#### Ubuntu/Debian:
```bash
sudo apt-get install python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
```

#### macOS:
```bash
brew install pango
```

#### Windows:
Siga las instrucciones en: https://weasyprint.org/

### Error: "Ejecutable no funciona en otro sistema"

Los ejecutables generados con PyInstaller son específicos del sistema operativo. Debe generar ejecutables en cada plataforma objetivo.

## Personalización del Build

### Agregar Icono

1. Cree o descargue un archivo `.ico` (Windows) o `.png` (Linux/macOS)
2. Modifique `ICON_PATH` en `build_client.py` o `build_server.py`:

```python
ICON_PATH = "path/to/icon.ico"
```

### Agregar Archivos Adicionales

Modifique `ADDITIONAL_DATA` en los scripts de build:

```python
ADDITIONAL_DATA = [
    ("ruta/origen", "ruta/destino"),
]
```

### Modificar Nombre del Ejecutable

Cambie `APP_NAME` en los scripts de build:

```python
APP_NAME = "MiNombrePersonalizado"
```

## Distribución

### Empaquetado para Distribución

1. **Crear carpeta de distribución**:
```bash
mkdir -p release
```

2. **Copiar ejecutables**:
```bash
cp dist/DrowsinessDetectionServer release/
cp dist/DrowsinessDetectionClient release/
```

3. **Copiar documentación**:
```bash
cp docs/*.pdf release/
cp README.md release/
```

4. **Crear archivo ZIP**:
```bash
cd release
zip -r DrowsinessDetection_v1.0.zip .
```

### Instalador (Opcional)

Para crear un instalador, considere usar:
- **Inno Setup** (Windows)
- **PackageMaker** (macOS)
- **Debian Package** (Linux)

## Contacto

Para problemas o preguntas sobre el build, consulte la documentación del proyecto o contacte al equipo de desarrollo.

