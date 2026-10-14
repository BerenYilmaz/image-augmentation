# Görüntü Veri Artırma

Pillow ve NumPy ile bir klasördeki görüntülerden farklı dönüşümler üretir. Her script girdileri kendi konumuna göre `images/` klasöründen okur ve sonuçları ayrı bir klasöre yazar.

## Kurulum ve kullanım

Depo kökünden:

```powershell
python -m pip install -r requirements.txt
New-Item -ItemType Directory -Force images
# Görsellerinizi önce images/ içine koyun.
python augmentation_rotation.py
python augmentation_brightness.py
```

## Dönüşümler

| Script | Ayar | Çıktı klasörü |
|---|---|---|
| `augmentation_blur.py` | Gaussian blur yarıçapları: 2, 3, 4, 5 | `blur/` |
| `augmentation_brightness.py` | Parlaklık katsayıları: 1.5 ve 0.2 | `brightness/` |
| `augmentation_contrsat.py` | Kontrast katsayıları: 1.5 ve 0.5 | `contrast/` |
| `augmentation_greyscale.py` | Tek kanallı gri tonlama | `greyscale/` |
| `augmentation_noise.py` | Gaussian gürültü, standart sapma 25 | `noise/` |
| `augmentation_rightFlip.py` | Yatay yansıtma | `flip/` |
| `augmentation_rotation.py` | 30°–330°, 30° aralıklarla; genişleyen tuval | `rotation/` |

Dosya adındaki `contrsat` yazımı mevcut script adıyla uyumluluk için korunmuştur. Ayarlar scriptlerin başındaki değişkenlerden düzenlenir.

## Kullanım notları

Girdi klasörüne yalnızca Pillow'un okuyabildiği görüntüler koyun; kod uzantı filtresi veya bozuk dosya yönetimi içermez. Çıktı klasörleri otomatik oluşturulur, aynı adla üretilen dosyaların üzerine yazılır. Gürültü üretiminde sabit rastgelelik tohumu yoktur.

Bu scriptler yalnızca görüntüleri dönüştürür; nesne kutuları ve segmentasyon etiketlerini dönüştürmez. Etiketli eğitim verisinde döndürme/yansıtma uygulamak etiketlerin ayrıca güncellenmesini gerektirir. Eğitim ve doğrulama ayrımını veri artırmadan önce yaparak aynı görüntünün türevlerinin iki bölüme dağılmasını önleyin.
