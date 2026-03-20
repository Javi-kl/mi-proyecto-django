# AGENTS.md - ConquerBlocks Development Guide

AI agent guidelines for this Django project.

---

## Project Overview

- **Framework**: Django 6.0.2
- **Python**: 3.14
- **Database**: SQLite3 (db.sqlite3)
- **Apps**: blog, core
- **Language**: Spanish (es-es) for user-facing content

---

## Commands

### Development Server
```bash
python manage.py runserver
python manage.py runserver 8000
```

### Database
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py showmigrations
```

### Create Superuser
```bash
python manage.py createsuperuser
```

---

## Testing

This project uses Django's built-in test framework (`tests.py` files).

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test blog
python manage.py test core


# Run single test class
python manage.py test blog.tests.PostModelTest

# Run single test method
python manage.py test blog.tests.PostModelTest.test_post_creation

# Verbose output
python manage.py test -v 2
```

---

## Code Style

### General
- **Line length**: Max 119 characters (Django default)
- **Indentation**: 4 spaces
- **File encoding**: UTF-8

### Imports Order
```python
# 1. Standard library
from pathlib import Path
# 2. Third-party
from django.db import models
from ckeditor.fields import RichTextField
# 3. Local application (relative)
from .models import Post
```

### Naming Conventions
| Element | Convention | Example |
|---------|------------|---------|
| Models | PascalCase | `class Post(models.Model):` |
| Functions | snake_case | `def get_post_by_id(id):` |
| Variables | snake_case | `all_posts = Post.objects.all()` |
| Constants | UPPER_SNAKE_CASE | `MAX_UPLOAD_SIZE = 10485760` |

### Type Hints
```python
from typing import Optional

def get_post(pk: int) -> Optional[Post]:
    return Post.objects.filter(pk=pk).first()

def __str__(self) -> str:
    return self.title
```

### Model Pattern
```python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación",
        default=timezone.now,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self) -> str:
        return self.title
```

### Admin Pattern
```python
from django.contrib import admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
```

### Views Pattern
```python
from django.shortcuts import render, redirect
from django.http import JsonResponse

def blog_list(request):
    all_posts = Post.objects.all()
    context = {"posts": all_posts}
    return render(request, "blog/blog_list.html", context)

def blog_create(request):
    if request.method == "POST":
        form = PostModelFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:blog_list")
        return render(request, "blog/blog_create.html", {"form": form, "error": True})
    return render(request, "blog/blog_create.html", {"form": PostModelFormCreate()})
```

### Error Handling
- Always validate forms with `form.is_valid()`
- Use try/except for database operations
- Return proper HTTP responses (JsonResponse, render, redirect)
- Never expose sensitive data in error messages

---

## Recommended Tools

Add to improve code quality:
- **black**: Code formatter (`--line-length=119`)
- **isort**: Import sorter
- **ruff**: Fast Python linter
- **mypy + django-stubs**: Type checking
- **pytest-django**: Enhanced testing

---

## Quick Reference

| Task | Command |
|------|---------|
| Run server | `python manage.py runserver` |
| Run tests | `python manage.py test` |
| Specific test | `python manage.py test blog.tests.PostModelTest.test_create` |
| Create migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Check config | `python manage.py check` |
