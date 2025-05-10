
# Ransomware Mitigation System

## Deskripsi
Skrip ini dirancang untuk mendeteksi dan memitigasi serangan **ransomware** dengan memantau aktivitas sistem secara **real-time**. Skrip ini akan memantau perubahan file yang mencurigakan, memeriksa proses yang mencurigakan, serta mencegah enkripsi file penting oleh ransomware.

Program ini dapat dijalankan di berbagai sistem operasi, termasuk **Linux**, **macOS**, dan **Windows**.

## Fitur
- Memantau **perubahan file** di direktori tertentu.
- Memantau **proses** yang mencurigakan yang dapat terkait dengan ransomware.
- **Menghentikan proses ransomware** yang terdeteksi secara otomatis.
- **Pemberitahuan** jika file penting diubah atau hilang.
- **Input interaktif** untuk memasukkan direktori yang dipantau dan file penting yang ingin dilindungi.

## Prasyarat
Skrip ini memerlukan **Python 3** dan dua modul Python eksternal:
- **watchdog**: Untuk memantau perubahan file.
- **psutil**: Untuk memantau proses yang berjalan di sistem.

## Instalasi dan Penggunaan

### 1. Clone Repository
Pertama, clone repository ini ke mesin lokal Anda:
```bash
git clone https://github.com/acongkuy/ransomware-detection-mitigation
cd mitigation
````

### 2. Membuat Virtual Environment (Opsional, tapi disarankan)

Untuk menjaga proyek tetap terisolasi, Anda dapat membuat **virtual environment**. Jika Anda belum menginstalnya, jalankan perintah berikut untuk membuat environment baru:

#### a. **Linux / macOS / Windows (Git Bash)**

```bash
python3 -m venv venv
```

#### b. **Windows (Command Prompt)**

```bash
python -m venv venv
```

### 3. Mengaktifkan Virtual Environment

Setelah virtual environment dibuat, aktifkan dengan perintah berikut:

#### a. **Linux / macOS**

```bash
source venv/bin/activate
```

#### b. **Windows**

```bash
.\venv\Scripts\activate
```

### 4. Menginstal Dependensi

Dengan virtual environment aktif, instal modul yang diperlukan (`watchdog` dan `psutil`) dengan menggunakan `pip`:

```bash
pip install -r requirements.txt
```

Jika Anda tidak memiliki `requirements.txt`, Anda bisa menginstalnya secara manual:

```bash
pip install watchdog psutil
```

### 5. Menjalankan Skrip

Setelah dependensi terinstal, Anda dapat menjalankan skrip dengan perintah berikut:

```bash
python3 mitigation.py
```

Skrip akan meminta Anda untuk memasukkan **path folder** yang ingin dipantau dan **file-file penting** yang ingin dilindungi secara interaktif.

### 6. Menonaktifkan Virtual Environment

Setelah selesai, Anda dapat keluar dari virtual environment dengan perintah:

```bash
deactivate
```

## Konfigurasi

Pada saat menjalankan skrip, Anda akan diminta untuk memasukkan:

1. **Path direktori** yang ingin dipantau untuk mendeteksi ransomware.
2. **Path file penting** yang ingin Anda lindungi. Anda dapat memasukkan beberapa file penting dengan mengetikkan path file satu per satu.

Contoh penggunaan input interaktif:

```
Enter the path to monitor (e.g., /home/user): /home/user
Please enter the paths to the important files you want to protect:
Enter an important file path (or type 'done' to finish): /home/user/Documents/important_file.txt
Enter an important file path (or type 'done' to finish): /home/user/important_data.xlsx
Enter an important file path (or type 'done' to finish): done
```

### Sistem yang Didukung

* **Linux**: Ubuntu, Fedora, Debian, dll.
* **macOS**: Semua versi yang mendukung Python 3.
* **Windows**: Windows 10 dan versi yang lebih baru.

### Catatan

* Skrip ini berjalan **secara real-time** dan akan memantau perubahan file serta proses yang mencurigakan tanpa henti. Pastikan untuk memonitor output yang dihasilkan agar Anda dapat mengidentifikasi potensi ancaman secara lebih cepat.
* Jika Anda menggunakan sistem Linux atau macOS, pastikan Anda memiliki hak akses yang diperlukan untuk memonitor file dan menghentikan proses.

## Troubleshooting

### Masalah 1: `ModuleNotFoundError: No module named 'psutil'`

Jika Anda mendapatkan pesan kesalahan ini, pastikan Anda telah menginstal semua dependensi dengan benar. Cobalah menjalankan:

```bash
pip install psutil
```

### Masalah 2: Skrip Tidak Berjalan Setelah Menutup Terminal

Jika terminal ditutup, Anda bisa menjalankan skrip menggunakan `nohup` atau alat lainnya seperti **screen** atau **tmux** untuk menjaga skrip tetap berjalan di latar belakang.

#### Menggunakan `nohup`:

```bash
nohup python3 mitigation.py &
```

#### Menggunakan `screen` atau `tmux`:

```bash
screen
python3 mitigation.py
```

### Masalah 3: Error `ModuleNotFoundError: No module named 'watchdog'`

Jika Anda mendapatkan error ini, pastikan Anda menginstal **watchdog**:

```bash
pip install watchdog
```

---

## Lisensi

Skrip ini dilisensikan di bawah lisensi MIT. Anda bebas menggunakan dan memodifikasi kode ini, tetapi tanpa jaminan dari pengembang.

---

**Terima kasih telah menggunakan skrip ini untuk membantu mencegah serangan ransomware!**

```

### Penjelasan:
1. **Instalasi dan Penggunaan**: Langkah-langkah terperinci untuk menginstal dependensi, menjalankan skrip, dan menggunakan virtual environment.
2. **Konfigurasi**: Menyediakan penjelasan mengenai bagaimana cara mengonfigurasi skrip agar sesuai dengan kebutuhan spesifik Anda (seperti memilih folder yang dipantau).
3. **Troubleshooting**: Panduan untuk menangani beberapa masalah umum, seperti kesalahan modul yang tidak ditemukan atau skrip yang berhenti saat terminal ditutup.
4. **Sistem yang Didukung**: Memberikan gambaran tentang platform yang kompatibel dengan skrip ini.
5. **Lisensi**: Memberikan lisensi yang sesuai (MIT) untuk penggunaan skrip.

### Cara Menggunakan File `README.md`:
1. Salin file `README.md` ini ke direktori root repository GitHub Anda.
2. Pastikan untuk mengganti bagian `https://github.com/username/repo-name.git` dengan URL repositori Anda yang benar.
3. Upload ke repository GitHub Anda untuk memberikan informasi lengkap kepada pengguna lain yang mengunjungi repo Anda.

Dengan file ini, pengguna akan mendapatkan instruksi yang jelas tentang cara menginstal, mengonfigurasi, dan menjalankan skrip Anda di berbagai platform.
```
