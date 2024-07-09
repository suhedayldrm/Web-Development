
# Synchronizing HTML Files Using `base.html`

This guide explains how to use `base.html` as a template to ensure styling and consistency across multiple templates in your application.

## Steps to Implement `base.html`

### 1. Create a Directory for the Base Template

Create a directory called `base` in your app directory and place the provided `base.html` file into this directory.

### 2. Update `settings.py` to Include the Base Template Directory

Add the path to the `base` directory in the `TEMPLATES` section of your `settings.py` file. This ensures that Django knows where to find the `base.html` template.

```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'your_app/base')],
        ...
    },
]
```

### 3. Extend `base.html` in Your Templates

To ensure that your templates use the styles and structure defined in `base.html`, add the following line at the beginning of each of your HTML files:

```html
{% extends "base.html" %}
```

By extending `base.html`, you ensure that all your templates inherit the base structure, allowing for consistent styling and layout across your application.

---