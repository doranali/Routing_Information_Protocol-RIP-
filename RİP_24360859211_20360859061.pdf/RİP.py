class Grafik:
    def __init__(self, dugum_sayisi):
        self.dugum_sayisi = dugum_sayisi
        self.kenarlar = []

    def kenar_ekle(self, baslangic, bitis, agirlik):
        """
        Kenar ekleme: başlangıç -> bitiş (ağırlık)
        """
        self.kenarlar.append((baslangic, bitis, agirlik))

    def bellman_ford(self, kaynak):
        """
        Bellman-Ford algoritması ile en kısa yolları hesaplar.
        :param kaynak: Başlangıç düğümü
        """
        mesafeler = [float('inf')] * self.dugum_sayisi
        mesafeler[kaynak] = 0
        onceki_dugumler = [-1] * self.dugum_sayisi

        for _ in range(self.dugum_sayisi - 1):
            for baslangic, bitis, agirlik in self.kenarlar:
                if mesafeler[baslangic] != float('inf') and \
                   mesafeler[baslangic] + agirlik < mesafeler[bitis]:
                    mesafeler[bitis] = mesafeler[baslangic] + agirlik
                    onceki_dugumler[bitis] = baslangic

        for baslangic, bitis, agirlik in self.kenarlar:
            if mesafeler[baslangic] != float('inf') and \
               mesafeler[baslangic] + agirlik < mesafeler[bitis]:
                raise ValueError("Grafik negatif ağırlıklı döngü içeriyor!")

        return mesafeler, onceki_dugumler

    def en_kisa_yolu_yazdir(self, kaynak, mesafeler, onceki_dugumler):
        """
        En kısa yolları ve mesafeleri yazdırır.
        :param kaynak: Başlangıç düğümü
        :param mesafeler: Her düğüm için minimum mesafeler
        :param onceki_dugumler: Her düğüm için önceki düğümleri tutar
        """
        print(f"Kaynak Düğüm: {kaynak}")
        print("Düğüm   Mesafe   Yol")
        for hedef in range(self.dugum_sayisi):
            if mesafeler[hedef] == float('inf'):
                print(f"{hedef}\t\tUlaşılamaz")
            else:
                yol = []
                temp = hedef
                while temp != -1:
                    yol.append(temp)
                    temp = onceki_dugumler[temp]
                yol.reverse()
                print(f"{hedef}\t\t{mesafeler[hedef]}\t\t{' -> '.join(map(str, yol))}")

# Örnek kullanım
if __name__ == "__main__":
    # Negatif döngü içermeyen bir grafik tanımla
    grafik = Grafik(5)  # 5 düğümlü bir grafik
    grafik.kenar_ekle(0, 1, 6)
    grafik.kenar_ekle(0, 2, 7)
    grafik.kenar_ekle(1, 2, 8)
    grafik.kenar_ekle(1, 3, 5)
    grafik.kenar_ekle(1, 4, -4)
    grafik.kenar_ekle(2, 3, -3)
    grafik.kenar_ekle(2, 4, 9)
    grafik.kenar_ekle(3, 1, -2)
    grafik.kenar_ekle(4, 3, 7)

    # Kaynak düğüm 0
    try:
        mesafeler, onceki_dugumler = grafik.bellman_ford(0)
        grafik.en_kisa_yolu_yazdir(0, mesafeler, onceki_dugumler)
    except ValueError as e:
        print(e)
