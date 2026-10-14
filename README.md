# G�r�nt� Veri Art�rma

Pillow ve NumPy ile bir klas�rdeki g�r�nt�lerden farkl� d�n���mler �retir. Her script girdileri kendi konumuna g�re `images/` klas�r�nden okur ve sonu�lar� ayr� bir klas�re yazar.

## Kurulum ve kullan�m

Depo k�k�nden:

```powershell
python -m pip install -r requirements.txt
New-Item -ItemType Directory -Force images
# G�rsellerinizi �nce images/ i�ine koyun.
python augmentation_rotation.py
python augmentation_brightness.py
```

## D�n���mler

| Script | Ayar | ��kt� klas�r� |
|---|---|---|
| `augmentation_blur.py` | Gaussian blur yar��aplar�: 2, 3, 4, 5 | `blur/` |
| `augmentation_brightness.py` | Parlakl�k katsay�lar�: 1.5 ve 0.2 | `brightness/` |
| `augmentation_contrsat.py` | Kontrast katsay�lar�: 1.5 ve 0.5 | `contrast/` |
| `augmentation_greyscale.py` | Tek kanall� gri tonlama | `greyscale/` |
| `augmentation_noise.py` | Gaussian g�r�lt�, standart sapma 25 | `noise/` |
| `augmentation_rightFlip.py` | Yatay yans�tma | `flip/` |
| `augmentation_rotation.py` | 30�-330�, 30� aral�klarla; geni�leyen tuval | `rotation/` |

Dosya ad�ndaki `contrsat` yaz�m� mevcut script ad�yla uyumluluk i�in korunmu�tur. Ayarlar scriptlerin ba��ndaki de�i�kenlerden d�zenlenir.

## Kullan�m notlar�

Girdi klas�r�ne yaln�zca Pillow'un okuyabildi�i g�r�nt�ler koyun; kod uzant� filtresi veya bozuk dosya y�netimi i�ermez. ��kt� klas�rleri otomatik olu�turulur, ayn� adla �retilen dosyalar�n �zerine yaz�l�r. G�r�lt� �retiminde sabit rastgelelik tohumu yoktur.

Bu scriptler yaln�zca g�r�nt�leri d�n��t�r�r; nesne kutular� ve segmentasyon etiketlerini d�n��t�rmez. Etiketli e�itim verisinde d�nd�rme/yans�tma uygulamak etiketlerin ayr�ca g�ncellenmesini gerektirir. E�itim ve do�rulama ayr�m�n� veri art�rmadan �nce yaparak ayn� g�r�nt�n�n t�revlerinin iki b�l�me da��lmas�n� �nleyin.
