
# Javi-kl - Web Personal
> Portfolio web personal desarrollado con Django — blog,
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
### Blog
- Editor Rich Text con CKEditor
- Gestión de imágenes con thumbnails automáticos
- Publicación selectiva en homepage
- **Sistema de comentarios** (usuarios registrados)
### Portfolio de Proyectos
- Showcase de proyectos y repositorios
- Enlaces a GitHub y demos
- Descripción y tecnologías utilizadas
- **Sistema de comentarios** (usuarios registrados)
### Sistema de Contacto
- Formulario con validación
- Mensajes guardados en base de datos
- Notificaciones por email
### Usuarios
- Registro y autenticación (requerido para comentar)
- Gestión de perfil básico
## Arquitectura
```
web_personal/
├── core/          # Home, About, Contacto, Auth
├── blog/          # Blog con sistema de comentarios
├── projects/      # Portfolio de proyectos (próximamente)
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
Roadmap
- [x] Blog con comentarios
- [x] Sistema de contacto
- [ ] App de proyectos/portfolio
- [ ] Tests unitarios
- [ ] Despliegue en producción
---
