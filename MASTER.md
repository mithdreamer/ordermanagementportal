Supply Chain Platform is a long-term product vision designed to manage procurement, logistics, warehousing and supply chain operations.

# The goal of this project:
 Not to build another order management application. The goal is to build a modular, scalable and commercial Supply Chain Platform that can evolve with business needs while remaining simple for end users.

# Master Vision

Order Management Portal, işletmelerin sipariş süreçlerini merkezi bir panel üzerinden yönetebilmesi için geliştirilen uzun vadeli bir ürün vizyonudur.

## Product Vision

Uygulama, ilk aşamada ürün, tedarikçi, mağaza ve sipariş yönetimini sade bir arayüzle sunar. Kullanıcılar temel operasyon verilerini tek yerde görebilmeli, sipariş durumlarını takip edebilmeli ve zamanla raporlama, sevkiyat ve doküman süreçlerini de aynı sistem içinde yönetebilmelidir.

## Long-Term Goal

Uzun vadeli hedef, Order Management Portal uygulamasını yalnızca tek bir işletme için çalışan bir panel olmaktan çıkarıp, farklı şirketlerin kullanabileceği güvenli ve ölçeklenebilir bir SaaS ürününe dönüştürmektir.

## SaaS Goal

SaaS yapısında her şirket kendi ürünlerini, tedarikçilerini, mağazalarını, siparişlerini ve kullanıcılarını yönetebilmelidir. Bu nedenle sistem mimarisinde `company_id` temelli veri ayrımı önemli bir prensip olacaktır.

## Core Modules

- Dashboard: Genel özet, sayısal göstergeler ve hızlı erişim alanı.
- Products: Ürün kayıtları, ürün detayları ve ürün durumu yönetimi.
- Suppliers: Tedarikçi kayıtları ve iletişim bilgileri.
- Stores: Mağaza veya satış noktası kayıtları.
- Orders: Sipariş oluşturma, sipariş kalemleri ve durum takibi.
- Shipments: Gelecekte sevkiyat süreçlerinin yönetimi.
- Documents: Sipariş, sevkiyat ve ithalat/ihracat dokümanları.
- Reports: Satış, sipariş, ürün ve tedarikçi raporları.
- Users: Kullanıcı hesapları ve erişim yetkileri.
- Settings: Şirket, sistem ve kullanıcı ayarları.

## Development Principles

- Start simple, design for growth.
- Keep code names in English.
- Keep the first UI language Turkish.
- Prefer reusable components and shared styles.
- Separate business logic from presentation logic over time.
- Avoid permanent hardcoded business data.
- Prepare the structure for multi-company SaaS usage.
- Build features in clear phases instead of adding everything at once.
