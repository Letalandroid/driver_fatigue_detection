# Instrucciones para Generar Ejecutables y Documentos PDF

## Resumen Rápido

Este documento proporciona instrucciones paso a paso para:
1. Generar ejecutables del sistema (cliente y servidor)
2. Convertir documentos Markdown a PDF

## Paso 1: Preparar el Entorno

### 1.1 Activar Entorno Virtual

```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 1.2 Instalar Dependencias de Build

```bash
pip install -r requirements_build.txt
```

Esto instalará:
- PyInstaller (para generar ejecutables)
- Markdown (para convertir documentos)
- WeasyPrint (para generar PDFs)

## Paso 2: Generar Ejecutables

### Opción A: Build Automático (Recomendado)

#### Linux/macOS:
```bash
./build_all.sh
```

#### Windows:
```cmd
build_all.bat
```

### Opción B: Build Manual

#### 2.1 Generar Ejecutable del Servidor

```bash
python build_server.py
```

O usando PyInstaller directamente:
```bash
pyinstaller pyinstaller_server.spec
```

#### 2.2 Generar Ejecutable del Cliente

```bash
python build_client.py
```

O usando PyInstaller directamente:
```bash
pyinstaller pyinstaller_client.spec
```

### 2.3 Ubicación de los Ejecutables

Los ejecutables se generan en la carpeta `dist/`:

- **Servidor**: `dist/DrowsinessDetectionServer` (Linux/macOS) o `dist/DrowsinessDetectionServer.exe` (Windows)
- **Cliente**: `dist/DrowsinessDetectionClient` (Linux/macOS) o `dist/DrowsinessDetectionClient.exe` (Windows)

## Paso 3: Probar los Ejecutables

### 3.1 Ejecutar el Servidor

```bash
# Linux/macOS
./dist/DrowsinessDetectionServer

# Windows
dist\DrowsinessDetectionServer.exe
```

El servidor debería iniciar en `http://localhost:8000`

### 3.2 Ejecutar el Cliente

En una nueva terminal:

```bash
# Linux/macOS
./dist/DrowsinessDetectionClient

# Windows
dist\DrowsinessDetectionClient.exe
```

La interfaz gráfica debería abrirse.

## Paso 4: Convertir Documentos a PDF

### 4.1 Conversión Automática

```bash
python convert_to_pdf.py
```

Esto convertirá todos los documentos Markdown en `docs/` a PDF:
- `docs/manual_usuario.md` → `docs/manual_usuario.pdf`
- `docs/manual_aplicacion_codigo.md` → `docs/manual_aplicacion_codigo.pdf`
- `docs/memoria_descriptiva_software.md` → `docs/memoria_descriptiva_software.pdf`
- `docs/descripcion_invento.md` → `docs/descripcion_invento.pdf`

### 4.2 Conversión Manual (Opcional)

Si necesita convertir un documento específico, puede modificar `convert_to_pdf.py` o usar:

```python
from convert_to_pdf import convert_md_to_pdf

convert_md_to_pdf("docs/manual_usuario.md", "docs/manual_usuario.pdf")
```

## Solución de Problemas Comunes

### Problema: PyInstaller no se instala

**Solución**:
```bash
pip install --upgrade pip
pip install pyinstaller
```

### Problema: Error "Module not found" durante la ejecución

**Solución**: Agregue el módulo faltante a `HIDDEN_IMPORTS` en `build_client.py` o `build_server.py`.

### Problema: WeasyPrint no se instala (dependencias del sistema)

**Linux (Ubuntu/Debian)**:
```bash
sudo apt-get update
sudo apt-get install python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
pip install weasyprint
```

**macOS**:
```bash
brew install pango
pip install weasyprint
```

**Windows**: Siga las instrucciones en https://weasyprint.org/

### Problema: El ejecutable es muy grande

**Solución**: Esto es normal. PyInstaller incluye todas las dependencias (Python, librerías, etc.). El tamaño típico es de 50-200 MB.

### Problema: El ejecutable no funciona en otro sistema

**Solución**: Los ejecutables generados con PyInstaller son específicos del sistema operativo. Debe generar ejecutables en cada plataforma objetivo (Windows, Linux, macOS).

### Problema: Error al ejecutar el servidor

**Solución**: 
1. Verifique que el puerto 8000 no esté en uso
2. Asegúrese de que todas las dependencias estén incluidas
3. Revise los logs de error

### Problema: Error al ejecutar el cliente

**Solución**:
1. Asegúrese de que el servidor esté ejecutándose
2. Verifique que la cámara web esté disponible
3. Revise los permisos de la cámara

## Personalización

### Agregar un Icono

1. Cree o descargue un archivo de icono:
   - Windows: `.ico`
   - Linux/macOS: `.png` o `.icns`

2. Modifique `build_client.py` o `build_server.py`:
```python
ICON_PATH = "path/to/icon.ico"  # o .png
```

### Cambiar el Nombre del Ejecutable

Modifique `APP_NAME` en `build_client.py` o `build_server.py`:
```python
APP_NAME = "MiNombrePersonalizado"
```

### Agregar Archivos Adicionales

Modifique `ADDITIONAL_DATA` en los scripts de build:
```python
ADDITIONAL_DATA = [
    ("ruta/origen", "ruta/destino"),
    ("otros/archivos", "destino"),
]
```

## Distribución

### Empaquetado para Distribución

1. Cree una carpeta de release:
```bash
mkdir -p release
```

2. Copie los ejecutables:
```bash
cp dist/* release/
```

3. Copie la documentación PDF:
```bash
cp docs/*.pdf release/
```

4. Copie el README:
```bash
cp README.md release/
```

5. Cree un archivo ZIP:
```bash
cd release
zip -r DrowsinessDetection_v1.0.zip .
```

## Verificación Final

Antes de distribuir, verifique:

- [ ] Los ejecutables se generan correctamente
- [ ] El servidor inicia sin errores
- [ ] El cliente se conecta al servidor
- [ ] La detección funciona correctamente
- [ ] Los documentos PDF se generan correctamente
- [ ] Los PDFs tienen formato correcto
- [ ] Todos los archivos necesarios están incluidos

## Contacto

Si tiene problemas o preguntas:
1. Revise la documentación en `README_BUILD.md`
2. Consulte los logs de error
3. Verifique que todas las dependencias estén instaladas
4. Contacte al equipo de desarrollo

---

**Nota**: Estos ejecutables son para distribución local. Para despliegue en producción, considere usar Docker o sistemas de despliegue en la nube.

