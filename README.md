# Javi-kl - Web Personal
> Portfolio web personal desarrollado con Django,
> sección de proyectos con comentarios y sistema de contacto.
## Stack Tecnológico
| Capa | Tecnología |
|------|------------|
| Framework | Django 6.0.2 |
| Lenguaje | Python 3.14 |
| Base de datos | SQLite3 |
| Rich Text | CKEditor 6.7 |
| Imágenes | Django Thumbnails + Pillow |
| Plantillas | HTML5 · CSS vanilla |
## Features
- Editor Rich Text con CKEditor
### Portfolio de Proyectos
- Showcase de proyectos y repositorios
- Enlaces a GitHub y demos
- Descripción y tecnologías utilizadas
- Gestión de imágenes con thumbnails automáticos
- Editor Rich Text con CKEditor

### Sistema de comentarios (usuarios registrados)
- Registro y autenticación (requerido para comentar)
  
### Sistema de Contacto
- Formulario con validación
- Mensajes guardados en base de datos

## Arquitectura
```
web_personal/
├── core/          # Home, About, Contacto, Auth
├── projects/      # Portfolio de proyectos 
└── templates/     # Plantillas reutilizables
```
## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## Roadmap
- [x] Sistema de contacto
- [x] App de proyectos/portfolio
- [x] Comentarios
- [ ] Tests unitarios
- [ ] Despliegue en producción
---