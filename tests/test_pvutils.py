from datetime import datetime
from pvutils import pvutils as pvu

class TestPVUtils:
    def test_angulo_diario(self):
        fecha1 = datetime(2023, 1, 1, 12, 0, 0)
        fecha2 = datetime(2023, 7, 1, 12, 0, 0)
        fecha3 = datetime(2023, 12, 31, 23, 59, 59)
        angulo_diario = pvu.angulo_diario(fecha1)
        assert angulo_diario == 0.0
        angulo_diario = pvu.angulo_diario(fecha2)
        assert angulo_diario == 3.115771344108233
        angulo_diario = pvu.angulo_diario(fecha3)
        assert angulo_diario == 6.265971100858546
    def test_ecc_del_tiempo(self):
        angulo_diario1 = 0.0
        angulo_diario2 = 3.115771344108233
        angulo_diario3 = 6.265971100858546
        ecc_del_tiempo = pvu.ecc_del_tiempo(angulo_diario1)
        assert ecc_del_tiempo == -2.90416896
        ecc_del_tiempo = pvu.ecc_del_tiempo(angulo_diario2)
        assert ecc_del_tiempo == -3.4623274857594577
        ecc_del_tiempo = pvu.ecc_del_tiempo(angulo_diario3)
        assert ecc_del_tiempo == -2.453457770899547
    # def test_indice_claridad_cielo(self):
    #     Kt = indice_claridad_cielo(0, 0, datetime(2019, 1, 1, 12, 0, 0))
    #     assert Kt == 0.0
    #     Kt = indice_claridad_cielo(0, 0, datetime(2019, 3, 21, 12, 0, 0))
    #     assert Kt == 0.4
    #     Kt = indice_claridad_cielo(0, 0, datetime(2019, 6, 21, 12, 0, 0))
    #     assert Kt == 0.7
    #     Kt = indice_claridad_cielo(0, 0, datetime(2019, 9, 23, 12, 0, 0))
    #     assert Kt == 0.4
    #     Kt = indice_claridad_cielo(0, 0, datetime(2019, 12, 21, 12, 0, 0))
    #     assert Kt == 0.
