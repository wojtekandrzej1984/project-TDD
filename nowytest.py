import unittest
import kalkulator
class testy_kalkulator(unittest.TestCase):
    def test_dodawanie(self):
        wynik = kalkulator.dodaj(2,3)
        self.assertEqual(wynik, 5)
        self.assertNotEqual(wynik, 2)
    def test_odejmij(self):
        wynik = kalkulator.odejmij(5,4)
        self.assertEqual(wynik, 1)
        self.assertNotEqual(wynik,2)
    def test_mnozenie(self):
        wynik = kalkulator.mnozenie(2,3)
        self.assertEqual(wynik, 6)
        self.assertNotEqual(wynik, 1)
    def test_dzielenie(self):
        wynik = kalkulator.dzielenie(4,2)
        self.assertEqual(wynik, 2)
        self.assertNotEqual(wynik, 5)
if __name__=='__main__':
    unittest.main()
