# Softwarcc

**Softwarcc** adalah sebuah program Python yang dirancang untuk mengotomatisasi 40 misi dalam upaya meningkatkan rating sebuah aplikasi di **mplus-softwarcc.com**. Program ini akan melakukan login menggunakan username dan password yang diberikan, kemudian menjalankan misi secara otomatis dengan memberikan umpan balik pada status setiap misi.

## Fitur

- Mengotomatisasi proses login dan penyelesaian misi di mplus-softwarcc.com.
- Menangani kesalahan umum seperti "You clicked too quickly" atau "Task is complete".
- Tampilan output di konsol yang interaktif menggunakan **Rich**.
- Waktu tunggu otomatis antara percobaan misi untuk mencegah pemblokiran.

## Persyaratan

- Python 3.8 atau versi lebih baru
- Koneksi internet aktif

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan **Softwarcc**:

1. **Clone repository ini**:
    ```bash
    git clone https://github.com/RozhakXD/Softwarcc.git
    cd Softwarcc
    ```
2. **Instal dependensi yang diperlukan**:
    ```bash
    pip install requests rich
    ```
3. **Jalankan program dengan perintah**:
    ```bash
    python Run.py
    ```

## Troubleshooting
- **Kesalahan login**: Jika Anda memasukkan username atau password yang salah, program akan langsung memberikan notifikasi dan menghentikan proses.
- **Misi gagal**: Jika misi tidak bisa diselesaikan karena alasan tertentu, program akan menampilkan pesan kesalahan yang relevan.
- **Klik terlalu cepat**: Jika program mendeteksi bahwa Anda melakukan klik terlalu cepat, program akan secara otomatis menunggu 5 detik sebelum mencoba kembali.

## Masalah Umum
- **Task tidak dapat diselesaikan**: Pastikan akun Anda memiliki misi yang tersedia di **mplus-softwarcc.com**.
- **Kesalahan otentikasi**: Jika mengalami masalah saat login, periksa apakah username dan password sudah benar, serta pastikan koneksi internet Anda stabil.

## Kontribusi
Kontribusi sangat diterima! Jika Anda menemukan bug atau memiliki saran fitur, silakan buat **issue** atau lakukan **pull request** di repository ini.

## Lisensi
Proyek ini dilisensikan di bawah lisensi **MIT**. Silakan lihat file [LICENSE](./LICENSE) untuk detail lebih lanjut.
