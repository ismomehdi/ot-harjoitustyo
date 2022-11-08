import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
    
    def test_saldo_vahenee_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_true_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_false_jos_rahat_eivat_riittaneet(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)
