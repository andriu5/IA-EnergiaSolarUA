import pvutils
import datetime

lat = 37.7749
long = -122.4194
date_time = datetime.datetime(2023, 4, 25, 12, 0, 0)
tsi = 1412.9
irradiancia_global = 1000

sza = pvutils.angulo_cenital(lat, long, date_time)
cos_sza = pvutils.cos_angulo_cenital(sza)
kt = pvutils.indice_claridad_cielo(irradiancia_global, tsi, cos_sza)


print("Ángulo cenital: ", sza)
print("Coseno del ángulo cenital: ", cos_sza)
print("Indice de claridad del cielo: ", kt)