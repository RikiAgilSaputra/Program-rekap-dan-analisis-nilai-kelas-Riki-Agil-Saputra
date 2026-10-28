"""Fungsi untuk membaca dan memvalidasi data siswa."""


def baca_data(file_input):
    """Mengembalikan data valid dan daftar peringatan."""
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