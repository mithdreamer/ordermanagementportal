# UI Guide

Bu dosya Order Management Portal için mevcut UI standartlarını ve tekrar kullanılacak temel sınıfları açıklar.

## General UI Direction

- UI text can be Turkish.
- CSS class names must be English.
- Layout should be clean, readable and consistent.
- Reusable classes should be preferred.
- Pages should use similar spacing, headers and button styles.

## header

Sayfanın üst bölümünü temsil eder. Uygulama adı, kısa başlık veya ana navigasyon bu alanda yer alabilir.

Usage:

```html
<header class="header"></header>
```

## navbar

Ana sayfa bağlantıları ve modül geçişleri için kullanılır. Dashboard, Products, Suppliers, Stores and Orders gibi ana bölümlere erişim sağlamalıdır.

Usage:

```html
<nav class="navbar"></nav>
```

## main-content

Sayfanın ana içerik alanıdır. Liste, form, detay veya dashboard içerikleri bu alan içinde gösterilmelidir.

Usage:

```html
<main class="main-content"></main>
```

## page-header

Her sayfanın başlık alanıdır. Sayfa başlığı, kısa açıklama ve varsa ana aksiyon butonu bu bölümde yer alabilir.

Usage:

```html
<section class="page-header"></section>
```

## dashboard-card

Dashboard üzerinde özet bilgi kartları için kullanılır. Örneğin toplam ürün, toplam tedarikçi veya bekleyen sipariş sayısı gösterilebilir.

Usage:

```html
<div class="dashboard-card"></div>
```

## data-table

Listeleme sayfalarında tablo görünümü için kullanılır. Products, Suppliers, Stores and Orders sayfalarında ortak tablo yapısı tercih edilmelidir.

Usage:

```html
<table class="data-table"></table>
```

## form-card

Yeni kayıt veya düzenleme formlarını çevreleyen form alanıdır. Form başlığı, input alanları ve aksiyon butonları bu yapı içinde tutulabilir.

Usage:

```html
<section class="form-card"></section>
```

## primary-button

Ana aksiyon butonları için kullanılır. Yeni kayıt oluşturma, kaydetme veya onaylama gibi işlemlerde tercih edilmelidir.

Usage:

```html
<button class="primary-button">Kaydet</button>
```

## UI Notes

- Keep buttons visually consistent.
- Keep tables readable on smaller screens.
- Use clear page titles.
- Avoid unnecessary visual complexity.
- Use consistent spacing between sections.
