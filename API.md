# API Draft

Bu dosya gelecekte geliştirilecek REST API yapısı için ilk endpoint taslağını içerir. Backend hedefi Node.js ve Express olarak planlanmıştır.

API endpoint names must be in English. UI text can remain Turkish.

## General Principles

- Use RESTful endpoints.
- Use JSON request and response bodies.
- Validate all incoming data.
- Return consistent success and error responses.
- Filter data by authenticated user's `company_id`.
- Do not expose data from another company.

## Products

### GET /products

Ürün listesini döndürür.

### POST /products

Yeni ürün oluşturur.

Expected body example:

```json
{
  "name": "Product Name",
  "sku": "PRD-001",
  "price": 100,
  "currency": "TRY"
}
```

## Suppliers

### GET /suppliers

Tedarikçi listesini döndürür.

### POST /suppliers

Yeni tedarikçi oluşturur.

Expected body example:

```json
{
  "name": "Supplier Name",
  "email": "supplier@example.com",
  "phone": "+90 555 000 0000"
}
```

## Stores

### GET /stores

Mağaza listesini döndürür.

### POST /stores

Yeni mağaza oluşturur.

Expected body example:

```json
{
  "name": "Store Name",
  "code": "STORE-001",
  "city": "Istanbul"
}
```

## Orders

### GET /orders

Sipariş listesini döndürür.

### POST /orders

Yeni sipariş oluşturur.

Expected body example:

```json
{
  "store_id": "store-id",
  "supplier_id": "supplier-id",
  "order_date": "2026-07-06",
  "items": [
    {
      "product_id": "product-id",
      "quantity": 10,
      "unit_price": 100
    }
  ]
}
```

### PUT /orders/:id/status

Sipariş durumunu günceller.

Expected body example:

```json
{
  "status": "approved"
}
```

## Future Endpoints

- GET /shipments
- POST /shipments
- GET /documents
- POST /documents
- GET /reports/orders
- GET /users
- POST /users
- GET /settings
- PUT /settings
