"""Fungsi statistik dan status ketuntasan."""

KKM = 75


def hitung_statistik(data):
    """Menghitung jumlah, rata-rata, minimum, dan maksimum."""
    if not data:
        return None

    jumlah = len(data)
    total = 0
    nilai_minimum = data[0]["nilai"]
    nilai_maksimum = data[0]["nilai"]

    for siswa in data:
        nilai = siswa["nilai"]
        total += nilai

        if nilai < nilai_minimum:
            nilai_minimum = nilai
        if nilai > nilai_maksimum:
            nilai_maksimum = nilai

    return {
        "jumlah_data": jumlah,
        "rata_rata": total / jumlah,
        "minimum": nilai_minimum,
        "maksimum": nilai_maksimum,
    }


def tentukan_status(nilai, kkm=KKM):
    """Mengembalikan status tuntas berdasarkan KKM."""
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