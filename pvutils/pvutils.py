'''
pvutils es una librería de Python que contiene una colección de funciones para calcular variables astronómicas
relevantes para el forecasting de la potencia de salida de una planta fotovoltaica. 
Estas funciones se enfocan en el cálculo de:

1) Irradiancia Extraterrestre (Io)
2) Ángulo cenital (Sza)
3) Coseno Ángulo cenital (cos(Sza))
4) Indice de claridad del cielo (Kt)
'''

import math

def tsi(dia_juliano):
    """
    La función `tsi(dia_juliano)` calcula la irradiancia solar total extraterrestre (TSI) para un día juliano dado, donde el día juliano se encuentra en un rango de 1 a 365. El resultado de esta función es la irradiancia extraterrestre, medida en W/m2. 
    La fórmula utilizada para el cálculo de la irradiancia extraterrestre se basa en la ecuación de la ley de Lambert, que toma en cuenta la distancia entre la Tierra y el Sol y la inclinación del eje terrestre. 
    En este caso, se utiliza la fórmula simplificada que considera la distancia promedio entre la Tierra y el Sol y la variación anual de la inclinación del eje terrestre. 
    En resumen, la función `tsi(dia_juliano)` es útil para calcular la irradiancia solar total extraterrestre para un día juliano específico y puede ser utilizada en aplicaciones relacionadas con la energía solar y el clima.

    args:
        dia_juliano: día juliano (1-365)
    returns:
        Io: irradiancia extraterrestre (W/m2)
    """
    # Cálculo de la irradiancia extraterrestre
    Io = 1367 * (1 + 0.033 * math.cos(math.radians(360 / 365 * dia_juliano)))
    return Io

def angulo_cenital(latitud, longitud, fecha_hora):
    """
    Calcula el ángulo cenital para una ubicación y fecha/hora dadas.
    """
    # Cálculo del ángulo horario
    longitud_hora = 15 * (fecha_hora.hour + fecha_hora.minute / 60 + fecha_hora.second / 3600 - 12)
    angulo_horario = math.radians(longitud_hora) 
    # Cálculo de la declinación solar
    dia_juliano = fecha_hora.timetuple().tm_yday
    delta = math.radians(23.45) * math.sin(math.radians(360 / 365 * (284 + dia_juliano)))
    # Cálculo de la altura solar
    sin_altura_solar = math.sin(math.radians(latitud)) * math.sin(delta) + math.cos(math.radians(latitud)) * math.cos(delta) * math.cos(angulo_horario)
    altura_solar = math.degrees(math.asin(sin_altura_solar))
    # Cálculo del ángulo cenital
    angulo_cenital = 90 - altura_solar
    return angulo_cenital

def cos_angulo_cenital(angulo_cenital):
    """
    Calcula el coseno del ángulo cenital.
    """
    cos_cenital = math.cos(math.radians(angulo_cenital))
    return cos_cenital

def indice_claridad_cielo(irradiancia_global, tsi, cos_cenital):
    """
    Calcula el índice de claridad del cielo.
    """
    kt = irradiancia_global / (tsi * cos_cenital)
    return kt