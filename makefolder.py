from pathlib import Path

# Ana proje dizini
base_path = Path(r"C:\Users\korhan.ors\Desktop\Flashdisk Korhan\GitHub\arsiv\Projeler\OrderManagementPortal")

# Klasörler
folders = [
    base_path / "css",
    base_path / "js",
    base_path / "pages"
]

# Dosyalar
files = [
    base_path / "index.html",
    base_path / "css" / "style.css",
    base_path / "js" / "app.js",
    base_path / "pages" / "orders.html",
    base_path / "pages" / "new-order.html",
    base_path / "pages" / "order-detail.html"
]

# Klasörleri oluştur
for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Dosyaları oluştur
for file in files:
    file.touch(exist_ok=True)

print("Proje yapısı başarıyla oluşturuldu.")