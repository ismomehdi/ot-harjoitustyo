import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(400)

    def test_kassan_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
    
    def test_kateismaksu_rahamaara_kasvaa_ja_vaihtorahat_oikein_edulliset(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kateismaksu_rahamaara_kasvaa_ja_vaihtorahat_oikein_maukkaat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(460), 60)

    def test_kateismaksu_myytyjen_lounaiden_maara_kasvaa_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateismaksu_myytyjen_lounaiden_maara_kasvaa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateismaksu_rahamaara_ei_muutu_jos_maksu_ei_riittava_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(10)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateismaksu_rahamaara_ei_muutu_jos_maksu_ei_riittava_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateismaksu_rahat_palautetaan_jos_maksu_ei_riittava_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(10), 10)

    def test_kateismaksu_rahat_palautetaan_jos_maksu_ei_riittava_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(10), 10)
    
    def test_kateismaksu_myytyjen_lounaiden_maara_ei_kasva_jos_ei_riittava_maksu_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(10)

        self.assertEqual(self.kassapaate.edulliset, 0)    

    def test_kateismaksu_myytyjen_lounaiden_maara_ei_kasva_jos_ei_riittava_maksu_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_veloitetaan_jos_tarpeeksi_rahaa_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 160)

    def test_kortti_veloitetaan_jos_tarpeeksi_rahaa_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 0)

    def test_kortti_palauttaa_true_jos_rahaa_edullisesti(self):
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_kortti_palauttaa_true_jos_rahaa_maukkaasti(self):
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
    
    def test_kortti_myytyjen_lounaiden_maara_kasvaa_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.edulliset, 1)    
    
    def test_kortti_myytyjen_lounaiden_maara_kasvaa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)  

    def test_kortin_rahamaara_ei_muutu_jos_ei_tarpeeksi_rahaa_edullisesti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(kortti.saldo, 100)

    def test_kortin_rahamaara_ei_muutu_jos_ei_tarpeeksi_rahaa_maukkaasti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(kortti.saldo, 100)
    
    def test_lounaiden_maara_ei_muutu_jos_kortilla_ei_rahaa_edullisesti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lounaiden_maara_ei_muutu_jos_kortilla_ei_rahaa_maukkaasti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_jos_ei_rahaa_kortti_palauttaa_false_edullisesti(self):
        kortti = Maksukortti(100)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_jos_ei_rahaa_kortti_palauttaa_false_maukkaasti(self):
        kortti = Maksukortti(100)
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_kassan_raha_ei_muutu_jos_kortilla_ei_rahaa_edullisesti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_raha_ei_muutu_jos_kortilla_ei_rahaa_maukkaasti(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldo_muuttuu_kun_lataa_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1)
        self.assertEqual(self.kortti.saldo, 401)
    
    def test_kassan_saldo_muuttuu_kun_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100001)
