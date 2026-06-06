# WhatsApp Spam Bot (Auto Message)

> **⚠️ Peringatan:** Proyek ini dibuat untuk tujuan edukasi dan pembelajaran otomatisasi.  
> Penggunaan untuk spam, pelecehan, atau pelanggaran kebijakan WhatsApp **tidak diperbolehkan**.  
> Gunakan dengan bijak dan hanya pada perangkat/chat milik sendiri.

## 📋 Deskripsi

Script Python sederhana untuk mengirim pesan berulang secara otomatis ke chat WhatsApp Web yang sedang aktif.  
Script ini akan mengklik area tertentu di layar (berdasarkan koordinat) lalu mengetik pesan "hari" secara berulang hingga tombol `C` ditekan.

## 🛠 Prasyarat

- Python 3.x
- WhatsApp Web terbuka di browser
- Pustaka Python:
  - `pyautogui`
  - `keyboard`
    
## Langkah menentukan koordinat

- ```bash
  python -m pyautogui
  ```
  jalankan perintah diatas di terminal vs code
- Akan muncul jendela kecil dengan informasi koordinat
- Arahkan mouse ke kolom chat WhatsApp Web atau yang lainnya
- Catat nilai X dan Y yang muncul (contoh: X=850, Y=650)
- Tekan Ctrl+C untuk keluar

## 🚀 Menjalankan Script

- Buka WhatsApp Web di browser
- Pilih chat target (teman/grup)
- Pastikan chat terbuka (kolom chat terlihat)
- Buka terminal/CMD di folder tempat ```spam-wa.py``` berada
- Jalankan perintah ```python spam-wa.py``` di terminal/CMD
- Anda memiliki 5 detik untuk memastikan WhatsApp Web aktif
- Script akan mulai mengirim pesan secara berulang-ulang
