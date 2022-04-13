class Toko():
    def __init__(self,nama, jenis, alamat):
        self.nama = nama
        self.jenis = jenis
        self.alamat = alamat

    def cek_id_toko(self):
        print('nama:',self.nama, 'jenis:',self.jenis, 'alamat:',self.alamat)

class Tokopedia(Toko):
    def cek_id_toko(self):
        print('Selamat Berkunjung di Tokopedia')

toko1 = Toko('Bambang','Buku','Makassar')
toko2 = Tokopedia('Budi','Baju','Majene')

toko1.cek_id_toko()
toko2.cek_id_toko()

