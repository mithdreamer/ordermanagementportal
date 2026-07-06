# Roadmap

Bu yol haritası, Order Management Portal projesinin statik arayüzden SaaS ürüne doğru gelişimini fazlara ayırır.

## Phase 1 Static UI

- Create base HTML pages.
- Build dashboard layout.
- Add pages for products, suppliers, stores and orders.
- Create basic forms for new records.
- Define initial CSS structure.
- Keep UI text in Turkish.

## Phase 2 JavaScript + LocalStorage

- Add client-side data handling with JavaScript.
- Store temporary data in `localStorage`.
- Create, list and edit basic records.
- Add form validation.
- Add shared navigation behavior.
- Improve table and detail page interactions.

## Phase 3 Backend API

- Add Node.js and Express backend.
- Create REST API endpoints.
- Move business logic from frontend to backend.
- Add request validation.
- Add consistent API response formats.
- Prepare error handling structure.

## Phase 4 PostgreSQL Database

- Create PostgreSQL schema.
- Add tables for companies, users, products, suppliers, stores and orders.
- Add `company_id` to business tables for SaaS readiness.
- Create order and order item relationships.
- Add database migrations or schema scripts.

## Phase 5 Authentication and Authorization

- Add user login and logout.
- Add password hashing.
- Add role-based access control.
- Define roles such as owner, admin, manager and staff.
- Restrict data access by `company_id`.

## Phase 6 Deployment

- Deploy frontend and backend.
- Configure environment variables.
- Connect production database.
- Add basic logging and monitoring.
- Prepare staging and production environments.

## Phase 7 SaaS Features

- Add company registration.
- Add subscription and plan structure.
- Add company-level settings.
- Add multi-language support.
- Add document management.
- Add reports and exports.
- Add shipment and import/export workflows.
