# Program Rekap dan Analisis Nilai Matematika Kelas

Salinan tahap implementasi Pertemuan 15 dari proyek Pertemuan 14. Tujuan program, format data, rentang nilai, KKM, dan jalur input/output mengikuti proyek acuan. Folder Pertemuan 15 terpisah dan tidak mengubah berkas pertemuan 14.

## Deskripsi

Program terminal membaca data siswa dari file teks, memvalidasi nama dan nilai pada rentang 0–100, menghitung statistik kelas, menentukan ketuntasan berdasarkan KKM 75, lalu menampilkan dan menyimpan laporan. Pada Pertemuan 15, program juga tetap membuat laporan dengan jumlah tuntas dan belum tuntas 0 ketika tidak ada data valid; ini merupakan peningkatan dari perilaku rancangan Pertemuan 14.

## Fitur

- Membaca data dengan format `Nama|Nilai`.
- Mengabaikan baris kosong dan komentar yang diawali `#`.
- Memvalidasi format, nama, nilai numerik, dan rentang nilai 0–100.
- Memberi peringatan dan melewati baris yang tidak valid.
- Menghitung jumlah data valid, rata-rata, nilai minimum, dan maksimum.
- Menentukan status `Tuntas` jika nilai mencapai KKM 75, serta menghitung jumlah tuntas dan belum tuntas.
- Menampilkan dan menyimpan laporan, termasuk saat tidak ada data valid.
- Menangani file input atau output yang tidak ditemukan dengan `FileNotFoundError`.

## Persyaratan

- Python 3.x
- Tidak memerlukan pustaka eksternal.

## Cara Menjalankan

Buka terminal pada folder utama proyek, lalu jalankan:

~~~bash
python main.py
~~~

Jalur file dihitung relatif terhadap folder utama proyek.

## Konfigurasi

- File input: `data/nilai_contoh.txt`
- File output: `output/laporan_nilai.txt`
- KKM: `75`
- Format satu baris data: `Nama|Nilai`

## Data Contoh

~~~text
Ayu  |85
Budi |78
Citra|92
Deni |65
Eka  |70
Fajar|88
Gita |55
Hana |100
Indra|0
Joko |74
~~~

Data tersebut sama dengan isi `data/nilai_contoh.txt`. Program mengabaikan spasi di sekitar nama dan nilai. Data contoh menghasilkan 10 data valid, rata-rata 70.70, minimum 0, maksimum 100, 5 siswa tuntas, dan 5 siswa belum tuntas.

## Struktur Folder

~~~text
.
├── .gitignore
├── README.md
├── proposal.md
├── main.py
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── tests/
│   └── test_case.md
├── docs/
│   ├── bug_log.md
│   └── screenshot/
│       ├── data-contoh.png
│       ├── TC01-normal.png
│       ├── TC02-boundary-nilai.png
│       ├── TC03-boundary-kkm.png
│       ├── TC04-invalid-data.png
│       ├── TC05-empty-data.png
│       ├── TC06-missing-input.png
│       └── TC07-missing-output.png
└── output/
    └── .gitkeep
~~~

Titik masuk Pertemuan 15 adalah `main.py` di folder utama dan dapat dijalankan tanpa pernyataan `import`. Fungsi dalam `src/` disimpan terpisah sebagai referensi; `main.py` tidak memanggilnya. `src/__init__.py` berisi konfigurasi paket, tetapi tidak dijalankan oleh titik masuk ini.

## Pengujian

`tests/test_case.md` berisi tujuh kasus manual dengan ID dan kondisi yang disamakan dengan rancangan Pertemuan 14: data normal, batas nilai, batas KKM, data tidak valid, data kosong, file input tidak ditemukan, dan file output tidak ditemukan. Jumlahnya lima kasus minimum ditambah dua kasus.

TC01 sampai TC07 telah dijalankan ulang dan hasilnya sesuai harapan. Status PASS dan hasil aktual tercatat di `tests/test_case.md`; bukti tersedia di `docs/screenshot/`. Untuk TC04 dan TC05, hasil Pertemuan 15 mengikuti peningkatannya: laporan tetap dibuat walaupun tidak ada data valid.

## Bug Log dan Bukti

`docs/bug_log.md` menyediakan tabel untuk mencatat bug yang benar-benar ditemukan. Saat ini belum ada temuan bug yang dikonfirmasi. Bukti terminal setiap pengujian tersedia di `docs/screenshot/`.

## Git dan GitHub

Folder Pertemuan 15 ini belum memiliki repositori Git lokal atau URL GitHub sendiri. Jika salinan ini akan dikumpulkan melalui GitHub, buat repositori untuk folder Pertemuan 15 dan tambahkan URL-nya setelah berhasil dipublikasikan.

## Anggota dan Kontribusi

Cantumkan nama anggota kelompok dan kontribusi masing-masing sebelum pengumpulan.

| Nama anggota | Kontribusi |
|---|---|
| (isi nama) | (isi kontribusi) |

## Referensi dan Bantuan

OpenAI Codex digunakan sebagai bantuan dalam penyusunan dan peninjauan kode serta dokumentasi proyek ini. Anggota kelompok perlu memahami dan memeriksa kembali seluruh kode dan hasil pengujian, serta mencantumkan sumber tambahan lain yang digunakan.
