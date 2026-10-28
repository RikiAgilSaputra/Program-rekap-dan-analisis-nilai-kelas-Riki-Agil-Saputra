# Rencana Implementasi Proyek - Pertemuan 15
## Program Rekap dan Analisis Nilai Matematika Kelas

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa  (UNTIRTA)
**Acuan:** Proposal proyek Pertemuan 14  
**Tahap:** Implementasi, pengujian, dokumentasi, dan persiapan demonstrasi  
**Tahun Ajaran:** 2026/2027 Ganjil

## 1. Acuan dan Ruang Lingkup

Pertemuan 15 melanjutkan proyek Pertemuan 14 dengan tujuan dan fitur inti yang sama: membaca data siswa dari `data/nilai_contoh.txt` dalam format `Nama|Nilai`, memvalidasi nilai 0–100, memakai KKM 75, menghitung statistik dan ketuntasan, serta menampilkan dan menyimpan laporan ke `output/laporan_nilai.txt`.

Tahap ini menambahkan implementasi, pengujian, dokumentasi, dan bukti uji. Salah satu peningkatan perilaku adalah program tetap menyusun serta menyimpan laporan saat tidak ada data valid; pada rancangan Pertemuan 14, program berhenti setelah memberi tahu bahwa data valid tidak tersedia. Titik masuk proyek Pertemuan 15 berada di `main.py` pada folder utama dan berjalan tanpa `import`, sesuai batasan materi. Berkas di `src/` tetap tersedia sebagai modul referensi terpisah dan tidak dipanggil oleh titik masuk tersebut.

## 2. Kebutuhan Fungsional

| ID | Kebutuhan | Kriteria |
|---|---|---|
| F01 | Membaca data | Membaca `data/nilai_contoh.txt` dengan format `Nama\|Nilai` |
| F02 | Mengabaikan baris | Baris kosong dan komentar yang diawali `#` dilewati |
| F03 | Memvalidasi data | Format benar, nama tidak kosong, nilai numerik dalam rentang 0–100; data tidak valid diberi peringatan dan dilewati |
| F04 | Menghitung statistik | Jumlah data valid, rata-rata, nilai minimum, dan maksimum dihitung dari data valid |
| F05 | Menentukan status | Nilai >= KKM 75 berstatus `Tuntas`; nilai di bawah 75 berstatus `Belum Tuntas` |
| F06 | Menghitung ketuntasan | Menghitung jumlah siswa tuntas dan belum tuntas |
| F07 | Membuat laporan | Menampilkan dan menyimpan ringkasan serta detail status ke `output/laporan_nilai.txt`, termasuk ketika data valid berjumlah 0 |

## 3. Alur Program

1. Baca file input; jika file tidak ditemukan, tampilkan pesan `FileNotFoundError` dan hentikan program dengan aman.
2. Abaikan baris kosong dan komentar, lalu validasi format, nama, dan nilai setiap baris; tampilkan peringatan untuk baris yang dilewati.
3. Hitung statistik serta status dan jumlah ketuntasan dari data valid.
4. Susun dan tampilkan laporan. Jika tidak ada data valid, tampilkan jumlah data valid 0, KKM 75, serta jumlah tuntas dan belum tuntas 0 tanpa menghitung rata-rata, minimum, atau maksimum.
5. Simpan laporan; jika file atau folder output tidak ditemukan, tampilkan pesan `FileNotFoundError`.

## 4. Struktur File dan Tanggung Jawab

- `main.py`: titik masuk mandiri di folder utama; memuat alur baca, validasi, analisis, format, dan simpan laporan tanpa `import`.
- `src/__init__.py`: berisi konfigurasi `FILE_INPUT`, `FILE_OUTPUT`, dan `KKM`; tidak dijalankan oleh `main.py` karena tidak ada import paket.
- `src/input_data.py`: versi terpisah fungsi baca dan validasi data.
- `src/proses.py`: versi terpisah fungsi statistik dan ketuntasan.
- `src/output.py`: versi terpisah fungsi format dan penyimpanan laporan.
- `data/nilai_contoh.txt`: data contoh yang sama dengan proyek Pertemuan 14.
- `tests/test_case.md`: tujuh skenario, hasil aktual, dan status pengujian.
- `docs/bug_log.md`: tabel untuk mencatat bug yang benar-benar ditemukan.
- `docs/screenshot/`: bukti tampilan program dan pengujian.
- `output/`: lokasi penyimpanan laporan; `.gitkeep` menjaga folder tetap ada pada salinan proyek.

Modul di `src/` belum dipanggil oleh `main.py`. Pemisahan ini menjaga batasan tanpa import yang diminta untuk program utama.

## 5. Rencana Pengujian dan Debugging

Pertemuan 15 memakai tujuh ID dan kondisi kasus yang sama dengan rancangan Pertemuan 14: TC01 data normal; TC02 nilai batas 0 dan 100; TC03 batas KKM 74 dan 75; TC04 gabungan data invalid (format salah, nama kosong, nilai bukan angka, nilai -1 dan 101); TC05 file kosong/komentar; TC06 file input tidak ditemukan; TC07 folder output tidak tersedia. Tujuh kasus terdiri atas lima kasus minimum dan dua kasus tambahan.

Hasil aktual dan status dicatat di `tests/test_case.md` setelah dijalankan. TC01–TC07 telah diperiksa ulang dan tercatat PASS. Perbedaan yang direncanakan dari tahap 14 terdapat pada kondisi TC04 dan TC05: program Pertemuan 15 tetap menyimpan laporan saat tidak ada data valid. Jika ada bug yang dapat direproduksi, catat gejala, penyebab, perbaikan, kasus regresi, dan statusnya di `docs/bug_log.md`.

## 6. Kriteria Siap Demonstrasi

- Program dapat dijalankan dari folder utama dengan `python main.py`.
- Kebutuhan F01–F07 bekerja sesuai uraian.
- Hasil aktual dan status tujuh test case tercatat di `tests/test_case.md`.
- Bug yang benar-benar ditemukan diperbaiki atau dicatat di bug log.
- README menjelaskan cara menjalankan, konfigurasi, struktur, fitur, dan hasil pengujian.
- Bukti terminal tersimpan di `docs/screenshot/`.
- Setiap anggota dapat menjelaskan kontribusi dan logika program.

## 7. Integritas Akademik

Setiap anggota bertanggung jawab memahami kode, hasil uji, perbaikan, dan kontribusinya. Ai codex dipergunakan sebagai alat bantu untuk menyusun proyek ini.
