# Test case - Pertemuan 15

Jumlah test case: 7. Bare minimum pada bahan ajar adalah 5; dua kasus tambahan menjadikan jumlahnya 7. Jalankan setiap kasus dari terminal pada folder utama proyek. Isi kolom Aktual dan Status hanya setelah kasus dijalankan.

| ID | Kategori | Input/kondisi | Hasil yang diharapkan | Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Jumlah 3; rata-rata 80.00; minimum 70; maksimum 90 | Jumlah 3; rata-rata 80.00; minimum 70; maksimum 90; tuntas 2; belum tuntas 1 | PASS |
| TC02 | Boundary | Nilai 0 dan 100 | Keduanya diterima sebagai nilai valid | Jumlah 2; rata-rata 50.00; minimum 0; maksimum 100; nilai 0 dan 100 diterima sebagai data valid | PASS |
| TC03 | Boundary KKM | Nilai 75 dan 74 dengan KKM 75 | Nilai 75 Tuntas; nilai 74 Belum Tuntas | Jumlah 2; rata-rata 74.50; minimum 74; maksimum 75; tuntas 1; belum tuntas 1; nilai 74 Belum Tuntas dan nilai 75 Tuntas | PASS |
| TC04 | Invalid | Baris format salah, nama kosong, nilai abc, -1, dan 101 | Setiap baris tidak valid dilewati dan mendapat peringatan yang sesuai | Lima peringatan tampil; tidak ada data valid untuk dianalisis; jumlah tuntas dan belum tuntas 0; laporan tersimpan | PASS |
| TC05 | Empty | File hanya berisi komentar dan baris kosong | Pesan data kosong; tidak terjadi pembagian nol; laporan tersimpan | Tidak ada data siswa valid untuk dianalisis; tuntas 0; belum tuntas 0; laporan tersimpan | PASS |
| TC06 | File input | File input tidak ditemukan | Pesan FileNotFoundError yang jelas; program berhenti dengan aman | Pesan “File input tidak ditemukan” tampil untuk data/nilai_contoh.txt; program berhenti dengan aman | PASS |
| TC07 | File output | Folder output tidak tersedia | Pesan FileNotFoundError yang jelas saat menyimpan laporan | Analisis 10 data selesai; pesan “File output tidak ditemukan” tampil untuk output/laporan_nilai.txt | PASS |

## Prosedur pencatatan

1. Jalankan program dari folder utama proyek.
2. Untuk kondisi khusus, siapkan input sementara dan pulihkan data/nilai_contoh.txt sesudahnya.
3. Bandingkan keluaran aktual dengan hasil yang diharapkan.
4. Isi kolom Aktual dan ubah Status menjadi PASS atau FAIL.
5. Jika kasus gagal, catat gejala dan perbaikannya di docs/bug_log.md, lalu ulangi kasus gagal dan kasus terkait.

## Hasil yang diharapkan untuk data contoh

Data di data/nilai_contoh.txt seharusnya menghasilkan 10 data valid, rata-rata 70.70, minimum 0, maksimum 100, 5 siswa tuntas, dan 5 siswa belum tuntas. Angka tersebut merupakan hasil perhitungan yang diharapkan, bukan hasil eksekusi test case.





