#!/home/lta/projects/driver_fatigue_detection/.venv/bin/python3
"""
Script para convertir documentos Markdown a PDF
Requiere: markdown, weasyprint o reportlab
"""

import os
import sys
import markdown
from pathlib import Path

try:
    from weasyprint import HTML, CSS
    HAS_WEASYPRINT = True
except ImportError:
    HAS_WEASYPRINT = False
    print("WeasyPrint no está instalado. Instalando...")
    os.system("pip install weasyprint")
    try:
        from weasyprint import HTML, CSS
        HAS_WEASYPRINT = True
    except ImportError:
        print("Error: No se pudo instalar WeasyPrint.")
        print("Instale manualmente: pip install weasyprint")
        sys.exit(1)

def markdown_to_html(md_content, title=""):
    """Convierte Markdown a HTML"""
    html_body = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'tables'])
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-family: 'DejaVu Sans', Arial, sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                font-size: 24pt;
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                margin-top: 30px;
            }}
            h2 {{
                font-size: 20pt;
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 8px;
                margin-top: 25px;
            }}
            h3 {{
                font-size: 16pt;
                color: #555;
                margin-top: 20px;
            }}
            h4 {{
                font-size: 14pt;
                color: #666;
                margin-top: 15px;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 10pt;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
                border-left: 4px solid #3498db;
            }}
            pre code {{
                background-color: transparent;
                padding: 0;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            ul, ol {{
                margin: 15px 0;
                padding-left: 30px;
            }}
            li {{
                margin: 8px 0;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                margin: 20px 0;
                padding-left: 20px;
                color: #666;
                font-style: italic;
            }}
            .page-break {{
                page-break-after: always;
            }}
            p {{
                margin: 10px 0;
                text-align: justify;
            }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    return html

def convert_md_to_pdf(md_file, pdf_file=None):
    """Convierte un archivo Markdown a PDF"""
    if pdf_file is None:
        pdf_file = md_file.replace('.md', '.pdf')
    
    print(f"Convirtiendo {md_file} a {pdf_file}...")
    
    # Leer archivo Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Obtener título del documento
    title = Path(md_file).stem.replace('_', ' ').title()
    
    # Convertir a HTML
    html_content = markdown_to_html(md_content, title)
    
    # Convertir HTML a PDF
    HTML(string=html_content).write_pdf(pdf_file)
    
    print(f"✓ PDF creado: {pdf_file}")

def main():
    """Convierte todos los documentos Markdown en docs/ a PDF"""
    docs_dir = Path("docs")
    
    if not docs_dir.exists():
        print(f"Error: El directorio {docs_dir} no existe.")
        sys.exit(1)
    
    # Archivos a convertir
    md_files = [
        "docs/manual_usuario.md",
        "docs/manual_aplicacion_codigo.md",
        "docs/memoria_descriptiva_software.md",
        "docs/descripcion_invento.md",
    ]
    
    print("==========================================")
    print("Conversión de Markdown a PDF")
    print("==========================================")
    print()
    
    for md_file in md_files:
        if os.path.exists(md_file):
            try:
                convert_md_to_pdf(md_file)
            except Exception as e:
                print(f"Error al convertir {md_file}: {e}")
        else:
            print(f"Advertencia: {md_file} no existe, omitiendo...")
    
    print()
    print("==========================================")
    print("Conversión completada!")
    print("==========================================")

if __name__ == "__main__":
    main()

