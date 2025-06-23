import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QInputDialog, QMessageBox
)
from finalresep import Ui_ResepMasakanApp  # pastikan nama file ui kamu adalah finalresep.py

class ResepMasakanApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ResepMasakanApp()
        self.ui.setupUi(self)

        self.reseps = [
            {"judul": "Ayam Bakar", "kategori": "Makanan", "bahan": "10 potong paha ayam, 1 sdm asam jawa, 2 lbr daun jeruk, 2 batang sereh, geprek simpulkan, 2 sdm gula merah, 400 ml air, Secukupnya garam, Secukupnya kaldu bubuk, Secukupnya kecap manis, 2 sdm mentega, 2 sdm saos tomat, Bumbu halus :, 7 siung bawang putih, 10 siung bawang merah, 5 butir kemiri, 5 bh cabe merah/ keriting merah, 1 ruas jahe, 1 jempol lengkuas, 2 batang sereh (ambil putihnya), 1 sdm ketumbar, 1 sdm merica, 1/4 biji pala", "langkah": "Cuci bersih ayam, tiriskan. Masukkan asam jawa, secukupnya garam, kaldu bubuk dan kecap manis. Aduk rata sambil asam jawa dihancurkan dan ayam sedikit di urut-urut agar bumbu meresap. Marinasi paling cepat 3 jam, didiamkan semalaman lebih baik. Simpan di kulkas → Haluskan bumbu, tumis dengan sedikit minyak hingga matang dan harum. Masukkan jg sereh geprek dan daun jeruk, tumis. Bumbui dengan garam dan kaldu bubuk. Beri sedikit air, lalu masukkan ayam. Aduk hingga ayam rata dengan bumbu, dan biarkan selama 5 menit → Tambahkan air, lalu tes rasa. Jika kurang, bisa di sesuaikan pada tahap ini. Masukkan juga gula merah. Ungkep ayam selama 10-13 menit per sisinya. Jika ayam sudah matang dan air mulai surut, tambahkan lagi kecap manis. Masak kembali selama 2 menit hingga kecap meresap ke dalam ayam → Angkat ayam, dan biarkan bumbunya dimasak lebih lama hingga surut kuah mengental. Jika sudah, matikan kompor dan campurkan bumbu ungkep dengan margarin, saos dan kecap manis. Aduk rata, sisihkan → Panaskan pan, panggang ayam tanpa minyak. Olesi bumbu bakar, lalu balik, oleskan kembali bumbu, panggang 1 menit, lalu balik kembali dan olesi bumbu kembali. Lakukan proses ini 3-4 kali sesuai selera. Pastikan menggunakan api kecil supaya ayam tidak terlalu hangus. Jika sudah, angkat dan sajikan dengan nasi hangat, lalap dan sambalnya. "},
            {"judul": "Es Jeruk Peras", "kategori": "Minuman", "bahan": "2 buah jeruk peras, 2 sdm gula pasir, 50 ml air hangat, 50 ml air es, Secukupnya es batu", "langkah": "Campur air hangat dan gula pasir dalam gelas, aduk hingga gula larut. Potong dua jeruk peras dan peras kedalam gelas (dengan saringan) → Tuang air es, aduk rata, tambahkan es batu → Siap disajikan"}
        ]

        # Tambah kategori
        self.ui.kategori_filter.addItems(["Semua", "Makanan", "Minuman"])

        # 🔗 Connect signals
        self.ui.kategori_filter.currentIndexChanged.connect(self.tampilkan_resep)
        self.ui.input_cari.textChanged.connect(self.tampilkan_resep)
        self.ui.list_resep.itemClicked.connect(self.tampilkan_detail)
        self.ui.btn_tambah.clicked.connect(self.tambah_resep)

        # Tampilkan awal
        self.tampilkan_resep()

    def tampilkan_resep(self):
        self.ui.list_resep.clear()
        keyword = self.ui.input_cari.text().lower()
        kategori = self.ui.kategori_filter.currentText()

        for resep in self.reseps:
            if (kategori == "Semua" or resep["kategori"] == kategori) and keyword in resep["judul"].lower():
                self.ui.list_resep.addItem(resep["judul"])

    def tampilkan_detail(self, item):
        nama = item.text()
        for resep in self.reseps:
            if resep["judul"] == nama:
                detail = f"== {resep['judul']} ==\nKategori: {resep['kategori']}\n\nBahan:\n{resep['bahan']}\n\nLangkah:\n{resep['langkah']}"
                self.ui.detail_resep.setText(detail)

    def tambah_resep(self):
        judul, ok = QInputDialog.getText(self, "Tambah Resep", "Judul:")
        if not ok or not judul.strip():
            return
        kategori, ok = QInputDialog.getItem(self, "Kategori", "Pilih Kategori:", ["Makanan", "Minuman"], 0, False)
        if not ok:
            return
        bahan, ok = QInputDialog.getMultiLineText(self, "Tambah Resep", "Bahan:")
        if not ok:
            return
        langkah, ok = QInputDialog.getMultiLineText(self, "Tambah Resep", "Langkah:")
        if not ok:
            return
        self.reseps.append({
            "judul": judul.strip(),
            "kategori": kategori,
            "bahan": bahan.strip(),
            "langkah": langkah.strip()
        })
        QMessageBox.information(self, "Sukses", "Resep berhasil ditambahkan!")
        self.tampilkan_resep()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResepMasakanApp()
    window.show()
    sys.exit(app.exec())
