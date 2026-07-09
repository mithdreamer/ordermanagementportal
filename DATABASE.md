# Database Design

**Version:** 1.1  
**Status:** Draft

This document defines the logical database model of the Supply Chain Platform.

The first implementation will use PostgreSQL.

The system is designed for multi-company SaaS architecture. Every business record belongs to a company through the `company_id` field.

---

# Database Principles

- Every business table must contain `company_id`.
- Primary keys should use UUID.
- Foreign keys should always enforce data integrity.
- Business logic should not be duplicated across tables.
- Many-to-many relationships should use bridge tables.
- Tables should be normalized unless a justified optimization is required.

---

# companies

## Purpose

Stores company / tenant information.

A company represents a business account using the platform.

## Fields

- id
- name
- legal_name
- tax_number
- tax_office
- email
- phone
- website
- country
- city
- address
- default_language
- default_currency
- timezone
- status
- created_at
- updated_at

## Relationships

```
Company (1) -------- (N) Users

Company (1) -------- (N) Products

Company (1) -------- (N) Suppliers

Company (1) -------- (N) Locations

Company (1) -------- (N) Orders

Company (1) -------- (N) Shipments

Company (1) -------- (N) Documents

Company (1) -------- (N) Audit Logs

Company (1) -------- (N) Company Modules
```

## Business Notes

A company is the main tenant of the SaaS platform.

All business data must belong to a company.

Company-level defaults such as language, currency and timezone are stored in this table.

---

# users

## Purpose

Stores platform users.

## Fields

- id
- company_id
- name
- email
- password_hash
- role
- status
- last_login_at
- created_at
- updated_at

## Relationships

```
Company (1) -------- (N) Users

Users (1) -------- (N) Product Suppliers
```

## Business Notes

Purchase responsible users are assigned through Product Suppliers.

---

# products

## Purpose

Stores product master data.

## Fields

- id
- company_id
- sku
- name
- description
- barcode
- category_id
- brand_id
- base_unit_id
- sales_unit_id
- purchase_unit_id
- hs_code
- country_of_origin
- status
- created_at
- updated_at

## Relationships

Company (1) -------- (N) Products

Product Categories (1) -------- (N) Products

Brands (1) -------- (N) Products

Units (1) -------- (N) Products

Products (1) -------- (N) Product Suppliers

Products (1) -------- (N) Order Items

Products (1) -------- (N) Product Documents (Future)

Products (1) -------- (N) Inventory Transactions (Future)

## Business Notes

Products contain only master data.

Commercial purchasing information belongs to Product Suppliers.

## Future Improvements

- Product Variants
- Product Images
- Product Documents

---
# product_categories

## Purpose

Stores product category definitions.

Categories may be organized in a hierarchical structure.

## Fields

- id
- company_id
- parent_category_id
- category_code
- category_name
- description
- status
- created_at
- updated_at

## Relationships

Company (1) -------- (N) Product Categories

Product Categories (1) -------- (N) Products

Product Categories (1) -------- (N) Product Categories

## Business Notes

Categories are company-specific.

A category may have a parent category.
---

# units

## Purpose

Stores measurement units used by products.

## Fields

- id
- company_id
- unit_code
- unit_name
- symbol
- unit_type
- decimal_precision
- status
- created_at
- updated_at

## Relationships

Company (1) -------- (N) Units

Units (1) -------- (N) Products

Units (1) -------- (N) Product Unit Conversions

## Business Notes

Units are shared across all products within a company.

Examples:

- PCS
- KG
- LITER
- BOX
- PALLET
---

# product_unit_conversions

## Purpose

Stores product-specific unit conversion rules.

## Fields

- id
- company_id
- product_id
- from_unit_id
- to_unit_id
- conversion_rate
- status
- created_at
- updated_at

## Relationships

Products (1) -------- (N) Product Unit Conversions

Units (1) -------- (N) Product Unit Conversions

## Business Notes

Conversions are product-specific.

Example:

1 BOX = 24 PCS

1 PALLET = 48 BOX

---

# suppliers

## Purpose

Stores supplier information.

## Fields

- id
- company_id
- name
- contact_name
- email
- phone
- address
- country
- status
- created_at
- updated_at

## Relationships

```
Company (1) -------- (N) Suppliers

Suppliers (1) ------ (N) Product Suppliers

Suppliers (1) ------ (N) Orders
```

---

# product_suppliers

## Purpose

Stores commercial relationships between products and suppliers.

One product may have multiple suppliers.

One supplier may provide multiple products.

## Fields

- id
- company_id
- product_id
- supplier_id
- is_primary_supplier
- incoterm
- transport_mode
- purchase_responsible_user_id
- lead_time_days
- minimum_order_quantity
- currency
- status
- created_at
- updated_at

## Relationships

```
Products (1) -------- (N) Product Suppliers

Suppliers (1) ------- (N) Product Suppliers

Users (1) ----------- (N) Product Suppliers

Product Suppliers (1) ---- (N) Order Items
```

## Business Notes

Commercial information depends on the supplier.

Different suppliers may have different:

- Incoterms
- Transport Modes
- Purchase Responsible
- Lead Times
- Minimum Order Quantities

## Future Improvements

- Supplier Product Codes
- Supplier Product Name
- Supplier Packaging
- Last Purchase Price
- Preferred Supplier Ranking

---

# brands

## Purpose

Stores product brand definitions.

## Fields

- id
- company_id
- brand_code
- brand_name
- description
- website
- country_of_origin
- status
- created_at
- updated_at

## Relationships

Company (1) -------- (N) Brands

Brands (1) -------- (N) Products

## Business Notes

Brands are company-specific.

A company may define its own brands or use manufacturer brands.

---

# product_documents

## Purpose

Stores documents related to products.

## Fields

- id
- company_id
- product_id
- document_type
- document_name
- file_url
- version
- expiry_date
- uploaded_by
- created_at
- updated_at

## Relationships

Products (1) -------- (N) Product Documents

## Business Notes

A product may contain multiple documents.

Example document types:

- Technical Datasheet
- MSDS
- Product Catalog
- Quality Certificate
- Test Report
- GTIP Determination Report
- University Report
- CE Certificate
- Declaration of Conformity

---

# product_images

## Purpose

Stores product images.

## Fields

- id
- company_id
- product_id
- image_url
- image_type
- sort_order
- created_at

## Relationships

Products (1) -------- (N) Product Images

---

# locations

## Purpose

Stores every physical location.

## Location Types

- Store
- Factory
- Warehouse
- Customer
- Bonded Warehouse

## Fields

- id
- company_id
- name
- code
- email
- phone
- address
- city
- status
- created_at
- updated_at

## Relationships

```
Company (1) -------- (N) Locations

Locations (1) ------ (N) Orders
```

---

# orders

## Purpose

Stores purchase order headers.

## Fields

- id
- company_id
- order_number
- location_id
- supplier_id
- order_date
- expected_delivery_date
- status
- total_amount
- currency
- notes
- created_at
- updated_at

## Relationships

```
Company (1) -------- (N) Orders

Suppliers (1) ------ (N) Orders

Locations (1) ------ (N) Orders

Orders (1) --------- (N) Order Items

Orders (1) --------- (N) Shipments

Orders (1) --------- (N) Documents
```

## Business Notes

One Purchase Order belongs to one supplier.

One Purchase Order may contain multiple order items.

Purchase Orders may contain products from only one supplier.

A supplier may receive multiple Purchase Orders.

---

# order_items

## Purpose

Stores purchase order lines.

## Fields

- id
- company_id
- order_id
- product_id
- product_supplier_id
- quantity
- unit
- unit_price
- total_price
- confirmed_quantity
- delivered_quantity
- remaining_quantity
- created_at
- updated_at

## Relationships

```
Orders (1) --------- (N) Order Items

Products (1) ------- (N) Order Items

Product Suppliers (1) ---- (N) Order Items
```

## Business Notes

Each order item references:

- Product
- Selected Product Supplier
- Ordered Quantity
- Purchase Unit
- Purchase Price

Commercial information is copied from Product Suppliers at the time of ordering.

---

# shipments

## Purpose

Stores shipment information.

## Fields

- id
- company_id
- order_id
- shipment_number
- carrier_name
- tracking_number
- shipment_date
- delivery_date
- status
- created_at
- updated_at

## Relationships

```
Orders (1) --------- (N) Shipments

Shipments (1) ------ (N) Documents
```

## Business Notes

One Purchase Order may be delivered in multiple shipments.

---

# documents

## Purpose

Stores business documents.

## Fields

- id
- company_id
- order_id
- shipment_id
- document_type
- file_name
- file_url
- uploaded_by
- created_at
- updated_at

## Relationships

```
Orders (1) --------- (N) Documents

Shipments (1) ------ (N) Documents
```

---

# Relationship Summary

```
Company (1) -------- (N) Users

Company (1) -------- (N) Products

Company (1) -------- (N) Suppliers

Company (1) -------- (N) Locations

Company (1) -------- (N) Orders

Products (1) ------- (N) Product Suppliers

Suppliers (1) ------ (N) Product Suppliers

Users (1) ---------- (N) Product Suppliers

Suppliers (1) ------ (N) Orders

Locations (1) ------ (N) Orders

Orders (1) --------- (N) Order Items

Products (1) ------- (N) Order Items

Product Suppliers (1) ---- (N) Order Items

Orders (1) --------- (N) Shipments

Orders (1) --------- (N) Documents

Shipments (1) ------ (N) Documents
```

---

# Future Tables

These tables are planned for future versions.

- product_brands
- warehouses
- inventory
- inventory_transactions
- customs_declarations
- customs_items
- bonded_warehouses
- invoices
- invoice_items
- payments
- exchange_rates
- audit_logs
- notification_templates
- notification_logs
- reminders
- scheduled_tasks
- reports
- report_definitions
- product_variants
- variant_attributes
- variant_attribute_values

---

# Notes

- Use UUID for all primary keys.
- All timestamps should use UTC.
- Sensitive data should never be stored in plain text.
- Foreign keys must enforce referential integrity.
- Business data must always be isolated by `company_id`.

---

# modules

## Purpose

Stores platform module definitions.

## Fields

- id
- module_key
- module_name
- description
- status
- created_at
- updated_at

## Relationships

Modules (1) -------- (N) Company Modules

## Business Notes

Modules define platform capabilities such as Import, Export, Warehouse, Finance or AI Assistant.

---

# company_modules

## Purpose

Stores enabled modules for each company.

## Fields

- id
- company_id
- module_id
- is_enabled
- enabled_at
- disabled_at
- created_at
- updated_at

## Relationships

Company (1) -------- (N) Company Modules

Modules (1) -------- (N) Company Modules

## Business Notes

A company may enable only the modules it needs.

This enables flexible SaaS capability management.