"""Fungsi untuk menyusun dan menyimpan laporan."""

from .proses import tentukan_status


def tampilkan_header():
    """Menampilkan judul program."""
    print("=" * 52)
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS")
    print("=" * 52)


def format_laporan(statistik, ketuntasan, data):
    """Menyusun ringkasan statistik dan detail status siswa."""
    garis = "=" * 52
    baris = [
        garis,
        "LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA",
        garis,
    ]

    if statistik is None:
        baris.extend([
            "Tidak ada data siswa valid untuk dianalisis.",
            f"KKM               : {ketuntasan['kkm']}",
            f"Jumlah tuntas     : {ketuntasan['tuntas']}",
            f"Belum tuntas      : {ketuntasan['belum_tuntas']}",
            garis,
        ])
        return "\n".join(baris) + "\n"

    baris.extend([
        f"Jumlah data valid : {statistik['jumlah_data']}",
        f"Rata-rata         : {statistik['rata_rata']:.2f}",
        f"Nilai minimum     : {statistik['minimum']:.2f}",
        f"Nilai maksimum    : {statistik['maksimum']:.2f}",
        f"KKM               : {ketuntasan['kkm']}",
        f"Jumlah tuntas     : {ketuntasan['tuntas']}",
        f"Belum tuntas      : {ketuntasan['belum_tuntas']}",
        "",
        "DETAIL STATUS SISWA",
        "-" * 52,
    ])

    for siswa in data:
        status = tentukan_status(siswa["nilai"], ketuntasan["kkm"])
        baris.append(
            f"{siswa['nama']:<20} {siswa['nilai']:>6.2f}  {status}"
        )

    baris.append(garis)
    return "\n".join(baris) + "\n"


def simpan_laporan(teks_laporan, file_output):
    """Menyimpan laporan dalam format teks UTF-8."""
    with open(file_output, "w", encoding="utf-8") as file:
        file.write(teks_laporan)