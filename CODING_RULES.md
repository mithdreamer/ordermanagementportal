# Coding Rules

Bu dosya Order Management Portal projesinde uygulanacak temel kod standartlarını açıklar.

## Language Rules

- Code must be in English.
- UI text can be Turkish.
- File names must be in English.
- Variables must be in English.
- Database tables and fields must be in English.
- API endpoints must be in English.
- CSS class names must be in English.

## HTML Rules

- Use semantic HTML.
- Prefer elements such as `header`, `nav`, `main`, `section`, `article`, `table` and `form`.
- Keep page structure readable.
- Use descriptive class names.
- Do not duplicate large HTML blocks when a shared structure becomes possible.

## CSS Rules

- Use reusable CSS classes.
- Prefer descriptive class names.
- Keep indentation clean.
- Avoid unnecessary overrides.
- Group related styles together.
- Keep responsive design in mind.

## JavaScript Rules

- Use descriptive variable and function names.
- Keep business logic readable.
- Avoid permanently hardcoded business data.
- Prefer reusable helper functions when logic repeats.
- Validate form data before saving or sending.

## File Naming Rules

- Use lowercase file names.
- Use hyphenated names for multi-word files.
- Keep names clear and related to the feature.

Examples:

```text
new-product.html
order-detail.html
style.css
app.js
```

## Data Rules

- Do not hardcode business data permanently.
- Temporary sample data can be used during early UI development.
- Future persistent data should come from API and database layers.
- SaaS-related records should be connected to `company_id` where needed.

## Formatting Rules

- Keep indentation clean and consistent.
- Remove unused code when it is no longer needed.
- Keep comments short and useful.
- Prefer simple, understandable code over complex abstractions.
