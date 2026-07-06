# Database Design Draft

Bu dosya Order Management Portal için ilk veritabanı modeli taslağını açıklar. Gelecekte PostgreSQL kullanılması hedeflenmektedir.

SaaS yapısı için `company_id` alanı kritik öneme sahiptir. Birden fazla şirket aynı sistemi kullandığında, iş verileri `company_id` ile birbirinden ayrılacaktır.

## companies

Şirket veya müşteri hesaplarını tutar.

- id
- name
- legal_name
- tax_number
- email
- phone
- address
- status
- created_at
- updated_at

## users

Sistem kullanıcılarını tutar.

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

## products

Ürün kayıtlarını tutar.

- id
- company_id
- name
- sku
- barcode
- category
- unit
- price
- currency
- status
- created_at
- updated_at

## suppliers

Tedarikçi kayıtlarını tutar.

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

## stores

Mağaza veya satış noktası kayıtlarını tutar.

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

## orders

Sipariş ana kayıtlarını tutar.

- id
- company_id
- order_number
- store_id
- supplier_id
- order_date
- expected_delivery_date
- status
- total_amount
- currency
- notes
- created_at
- updated_at

## order_items

Sipariş kalemlerini tutar.

- id
- company_id
- order_id
- product_id
- quantity
- unit_price
- total_price
- created_at
- updated_at

## shipments

Gelecekte sevkiyat kayıtlarını tutar.

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

## documents

Sipariş, sevkiyat, ithalat/ihracat veya şirket dokümanlarını tutar.

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

## Notes

- All primary keys should use a stable unique identifier.
- Foreign keys should be added between related tables.
- Business tables should include `company_id` for tenant isolation.
- Date fields should use consistent timestamp types.
- Sensitive fields should never be stored as plain text.
