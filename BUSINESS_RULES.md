## Order Lifecycle - Initial Business Flow

The order process starts from MRP or demand planning performed by a store or factory.

After the required delivery date is determined, an order is created. The order waits for supplier confirmation. Once supplier confirmation is received, the order is approved.

The supplier may prepare the order fully or partially. After preparation, the supplier issues an invoice and dispatches the goods.

For international orders, the goods arrive at customs. After customs arrival, the goods may be directly imported or first transferred to a bonded warehouse and then imported later.

Customs declarations are created, duties and taxes are paid, and the goods are delivered by domestic transportation to the store or factory.

After physical receipt, goods receipt is posted. Then the goods may be delivered to the final customer.


Draft
Waiting Supplier Confirmation
Approved
Partially Prepared
Fully Prepared
In Transit
Arrived At Customs
In Customs Clearance
In Bonded Warehouse
Imported
In Domestic Transport
Delivered
Goods Receipt Completed
Closed

## Product Rules

- SKU must be unique within a company.
- Passive products cannot be added to new orders.
- A product may have multiple suppliers.
- A product may have one primary supplier.
- Commercial terms are stored in product_suppliers, not in products.
- HS Code is optional for domestic products but required for import/export capable products.
- Country of Origin is optional for domestic-only products but required for import/export operations.
- Products should not be physically deleted if they are used in orders.

## Product Variant Rules

- Product variant usage should be optional per company.
- Some companies may manage products directly without variants.
- Companies such as textile, footwear or fashion businesses may use variants.
- Variant attributes may differ by company.
- Example variant attributes include color, size, material, model and season.
- Each variant should be able to have its own SKU if required.

## Order Creation Rules

- Open orders must be linked to defined products.
- A purchase order item cannot be finalized without a valid product reference.
- If an imported order line contains an unknown SKU, the line must be sent to a review process.
- In simple usage mode, the system may allow draft product creation during manual order entry.
- Imported orders from Excel, SAP, email or API should be validated before becoming active purchase orders.