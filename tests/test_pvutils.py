import unittest
from datetime import datetime
from pvutils import tsi, angulo_cenital, cos_angulo_cenital, indice_claridad_cielo

class TestPVUtils(unittest.TestCase):
    def test_tsi(self):
        Io = tsi(1)
        self.assertAlmostEqual(Io, 1412.9, 1)
        Io = tsi(100)
        self.assertAlmostEqual(Io, 1413.0, 1)
        Io = tsi(200)
        self.assertAlmostEqual(Io, 1412.9, 1)
        Io = tsi(300)
        self.assertAlmostEqual(Io, 1412.8, 1)
        Io = tsi(365)
        self.assertAlmostEqual(Io, 1412.9, 1)
    
    def test_angulo_cenital(self):
        Sza = angulo_cenital(0, 0, datetime(2019, 1, 1, 12, 0, 0))
        self.assertAlmostEqual(Sza, 90, 1)
        Sza = angulo_cenital(0, 0, datetime(2019, 3, 21, 12, 0, 0))
        self.assertAlmostEqual(Sza, 41.8, 1)
        Sza = angulo_cenital(0, 0, datetime(2019, 6, 21, 12, 0, 0))
        self.assertAlmostEqual(Sza, 0, 1)
        Sza = angulo_cenital(0, 0, datetime(2019, 9, 23, 12, 0, 0))
        self.assertAlmostEqual(Sza, 41.8, 1)
        Sza = angulo_cenital(0, 0, datetime(2019, 12, 21, 12, 0, 0))
        self.assertAlmostEqual(Sza, 90, 1)

    def test_cos_angulo_cenital(self):
        cos_Sza = cos_angulo_cenital(0)
        self.assertAlmostEqual(cos_Sza, 1, 1)
        cos_Sza = cos_angulo_cenital(45)
        self.assertAlmostEqual(cos_Sza, 0.707, 3)
        cos_Sza = cos_angulo_cenital(90)
        self.assertAlmostEqual(cos_Sza, 0, 1)

    def test_indice_claridad_cielo(self):
        Kt = indice_claridad_cielo(0, 0, datetime(2019, 1, 1, 12, 0, 0))
        self.assertAlmostEqual(Kt, 0.0, 1)
        Kt = indice_claridad_cielo(0, 0, datetime(2019, 3, 21, 12, 0, 0))
        self.assertAlmostEqual(Kt, 0.4, 1)
        Kt = indice_claridad_cielo(0, 0, datetime(2019, 6, 21, 12, 0, 0))
        self.assertAlmostEqual(Kt, 0.7, 1)
        Kt = indice_claridad_cielo(0, 0, datetime(2019, 9, 23, 12, 0, 0))
        self.assertAlmostEqual(Kt, 0.4, 1)
        Kt = indice_claridad_cielo(0, 0, datetime(2019, 12, 21, 12, 0, 0))
        self.assertAlmostEqual(Kt, 0.0, 1)

if __name__ == '__main__':
    unittest.main()
