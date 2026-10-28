"""Program mandiri rekap dan analisis nilai matematika kelas."""

FILE_INPUT = "data/nilai_contoh.txt"
FILE_OUTPUT = "output/laporan_nilai.txt"
KKM = 75


def baca_data(file_input):
    """Membaca data Nama|Nilai dan mengumpulkan peringatan."""
    data = []
    peringatan = []

    with open(file_input, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue

            bagian = baris.split("|")
            if len(bagian) != 2:
                peringatan.append(
                    f"Peringatan baris {nomor_baris}: format harus Nama|Nilai."
                )
                continue

            nama = bagian[0].strip()
            teks_nilai = bagian[1].strip()
            if not nama:
                peringatan.append(
                    f"Peringatan baris {nomor_baris}: nama kosong."
                )
                continue

            try:
                nilai = float(teks_nilai)
            except ValueError:
                peringatan.append(
                    f"Peringatan baris {nomor_baris}: nilai harus angka."
                )
                continue

            if not 0 <= nilai <= 100:
                peringatan.append(
                    f"Peringatan baris {nomor_baris}: nilai harus 0-100."
                )
                continue

            data.append({"nama": nama, "nilai": nilai})

    return data, peringatan


def hitung_statistik(data):
    """Menghitung jumlah data, rata-rata, nilai minimum, dan maksimum."""
    if not data:
        return None

    jumlah_data = len(data)
    total_nilai = 0
    nilai_minimum = data[0]["nilai"]
    nilai_maksimum = data[0]["nilai"]

    for siswa in data:
        nilai = siswa["nilai"]
        total_nilai += nilai

        if nilai < nilai_minimum:
            nilai_minimum = nilai
        if nilai > nilai_maksimum:
            nilai_maksimum = nilai

    return {
        "jumlah_data": jumlah_data,
        "rata_rata": total_nilai / jumlah_data,
        "minimum": nilai_minimum,
        "maksimum": nilai_maksimum,
    }


def tentukan_status(nilai, kkm=KKM):
    """Menentukan apakah nilai siswa telah mencapai KKM."""
    if nilai >= kkm:
        return "Tuntas"
    return "Belum Tuntas"


def rekap_ketuntasan(data, kkm=KKM):
    """Menghitung jumlah siswa tuntas dan belum tuntas."""
    jumlah_tuntas = 0

    for siswa in data:
        if tentukan_status(siswa["nilai"], kkm) == "Tuntas":
            jumlah_tuntas += 1

    return {
        "kkm": kkm,
        "tuntas": jumlah_tuntas,
        "belum_tuntas": len(data) - jumlah_tuntas,
    }


def format_laporan(statistik, ketuntasan, data):
    """Menyusun ringkasan statistik dan status setiap siswa."""
    garis = "=" * 52
    baris_laporan = [
        garis,
        "LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA",
        garis,
    ]

    if statistik is None:
        baris_laporan.extend([
            "Tidak ada data siswa valid untuk dianalisis.",
            f"KKM               : {ketuntasan['kkm']}",
            f"Jumlah tuntas     : {ketuntasan['tuntas']}",
            f"Belum tuntas      : {ketuntasan['belum_tuntas']}",
            garis,
        ])
        return "\n".join(baris_laporan) + "\n"

    baris_laporan.extend([
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
        baris_laporan.append(
            f"{siswa['nama']:<20} {siswa['nilai']:>6.2f}  {status}"
        )

    baris_laporan.append(garis)
    return "\n".join(baris_laporan) + "\n"


def simpan_laporan(teks_laporan, file_output):
    """Menyimpan laporan dalam file teks."""
    with open(file_output, "w", encoding="utf-8") as file:
        file.write(teks_laporan)


def main():
    """Menjalankan alur baca, analisis, dan pembuatan laporan."""
    print("=" * 52)
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS")
    print("=" * 52)

    try:
        data, peringatan = baca_data(FILE_INPUT)
    except FileNotFoundError as error:
        print(f"File input tidak ditemukan: {error}")
        return

    for pesan in peringatan:
        print(pesan)

    statistik = hitung_statistik(data)
    ketuntasan = rekap_ketuntasan(data, KKM)
    laporan = format_laporan(statistik, ketuntasan, data)

    print(laporan, end="")

    try:
        simpan_laporan(laporan, FILE_OUTPUT)
    except FileNotFoundError as error:
        print(f"File output tidak ditemukan: {error}")
        return

    print(f"Laporan tersimpan di {FILE_OUTPUT}.")


if __name__ == "__main__":
    main()
