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
