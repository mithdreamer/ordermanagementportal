# 2026-07-06

## Decision 001
**Title:** Replace Stores with Locations

**Reason:**
A physical destination can represent a Store, Factory, Warehouse, Customer or Bonded Warehouse.

**Impact:**
The system becomes more flexible and future-proof.

---

## Decision 002
**Title:** Introduce Product Suppliers Bridge Table

**Reason:**
A product may be supplied by multiple suppliers with different commercial conditions.

**Impact:**
Incoterms, transport mode, purchasing responsibility and lead times are managed per product–supplier relationship.

---

## Decision 003
**Title:** Keep Commercial Conditions in Product-Supplier Relationship

**Reason:**
Commercial terms belong to the relationship, not to the product itself.

**Impact:**
Supports multiple suppliers with different purchasing conditions for the same product.

## Decision 005

### Title

Optional Product Variant Architecture

### Decision

Product variants will be optional.

Companies that do not use variants will operate with a single default variant created automatically by the system.

Companies that require variants may define their own variant attributes such as Color, Size, Material, Model or any other business-specific characteristic.

### Reason

The platform must support multiple industries without hardcoding variant structures.

### Impact

- Supports manufacturing, retail, textile, footwear and industrial companies.
- Eliminates unnecessary complexity for companies that do not require variants.
- Provides a scalable and flexible product architecture.

## Decision 006 
## Title

Multiple Order Creation Channels

## Decision

Purchase Orders may be created from different sources.

Supported sources include:

- Manual Entry
- Excel Import
- ERP Integration
- SAP Integration
- Email Processing
- REST API
- Future AI Automation

## Reason

Companies use different operational workflows.

The platform must support both manual and automated order creation.

## Impact

A Validation Engine will verify imported data before active Purchase Orders are created.
