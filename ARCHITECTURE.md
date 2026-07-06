# Architecture

Order Management Portal, başlangıçta statik frontend olarak geliştirilen ve ilerleyen fazlarda backend, database, authentication ve SaaS desteği kazanacak şekilde planlanan bir web uygulamasıdır.

## Frontend Architecture

Frontend ilk aşamada HTML, CSS ve JavaScript ile oluşturulur.

- HTML files define page structure.
- CSS files define layout, colors, spacing and reusable UI classes.
- JavaScript files handle client-side interactions.
- UI text can be Turkish.
- Code names such as files, variables and classes must be English.

Current frontend structure:

```text
index.html
css/style.css
js/app.js
pages/
```

## Backend Architecture

Backend gelecek fazlarda Node.js ve Express ile geliştirilecektir.

Planlanan backend sorumlulukları:

- REST API endpoints
- Business logic
- Authentication and authorization
- Request validation
- Error handling
- Database access
- Company-based data isolation

## Database Architecture

Veritabanı için PostgreSQL hedeflenmektedir. Veri modeli SaaS yapısına uygun tasarlanmalıdır. Bu nedenle iş verilerinin çoğunda `company_id` alanı bulunmalıdır.

Temel yaklaşım:

- `companies` table stores tenant companies.
- `users` table stores system users.
- Business tables are connected to `companies` through `company_id`.
- Orders are connected to order items.
- Documents and shipments can be connected to orders.

## SaaS Multi-Company Structure

SaaS modelinde aynı uygulama birden fazla şirket tarafından kullanılabilir. Her şirketin verisi diğer şirketlerden ayrılmalıdır.

Bu ayrım için:

- Her şirket `companies` tablosunda tutulur.
- Kullanıcılar bir şirkete bağlı olur.
- Ürün, tedarikçi, mağaza, sipariş, sevkiyat ve doküman kayıtları `company_id` ile ayrılır.
- API isteklerinde kullanıcı yalnızca kendi şirketinin verilerine erişebilmelidir.

## User Roles

İlk rol yapısı aşağıdaki gibi planlanabilir:

- owner: Şirket sahibi, tüm yetkilere sahiptir.
- admin: Şirket içi yönetici, çoğu yönetim işlemini yapabilir.
- manager: Operasyon süreçlerini yönetebilir.
- staff: Kayıt görüntüleme ve sınırlı işlem yapabilir.

Rol yapısı backend ve database fazlarında netleştirilecektir.

## Deployment Architecture

Gelecekte deployment için aşağıdaki servisler değerlendirilebilir:

- Frontend: Vercel
- Backend: Render
- Database: Supabase or Neon

Ortam değişkenleri, database bağlantı bilgileri ve güvenlik anahtarları kod içine yazılmamalı, environment variables üzerinden yönetilmelidir.
