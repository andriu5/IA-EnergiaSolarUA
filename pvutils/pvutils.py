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
import datetime
import pytz # Para convertir a UTC

# def excentricidad():
#     return 1.00011+0.034221*math.cos(M12)+0.00128*math.sin(M12)+0.000719*math.cos(2*M12)+0.000077*math.sin(2*M12)

irradiancia_extra_cte = 1367 # W/m2

#funcion para calcular el dia del año
# def dia_del_ano(fecha) -> int:
#     """
#     Calcula el día del año para una fecha dada.

#     Args:
#         fecha: fecha en formato datetime
#     Returns:
#         dia_del_ano: día del año (1-365)
#     """
#     tz = pytz.timezone('Chile/Continental')
#     fecha_hora = datetime.datetime(fecha.year, fecha.month, fecha.day, fecha.hour, fecha.minute, fecha.second, tzinfo=tz)
#     dia_del_ano = fecha_hora.timetuple().tm_yday
#     return dia_del_ano

def dia_del_ano(fecha_hora) -> int:
    return datetime.datetime(fecha_hora.year, fecha_hora.month, fecha_hora.day, fecha_hora.hour, fecha_hora.minute, fecha_hora.second, tzinfo=pytz.timezone('Chile/Continental')).timetuple().tm_yday


def angulo_diario(fecha, unit='rad') -> float:
    """
    Calcula el ángulo diario (\Gamma) para una fecha dada.

    Args:
        fecha: fecha en formato datetime
        unit: unidades del ángulo ('deg' para grados o 'rad' para radianes)
    Returns:
        angulo_diario: ángulo diario (grados o radianes)
    """

    angulo_diario = 2*math.pi*(dia_del_ano(fecha)-1)/365
    if unit == 'deg':
        angulo_diario = math.degrees(angulo_diario)
    return angulo_diario

def ecc_del_tiempo(angulo_diario: float, unit='rad') -> float:
    """
    Calcula la ecuación del tiempo (Et) para un angulo diario dado.

    Args:
        angulo_diario: ángulo diario (grados o radianes)
        unit: unidades del ángulo ('deg' para grados o 'rad' para radianes)
    Returns:
        ecc_del_tiempo: ecuación del tiempo (minutos)
    """
    if unit == 'deg':
        angulo_diario = math.degrees(angulo_diario)

    Et = 229.18*(0.000075+0.001868*math.cos(angulo_diario)-0.032077*math.sin(angulo_diario)-0.014615*math.cos(2*angulo_diario)-0.040849*math.sin(2*angulo_diario))
    return Et

def tiempo_solar_verdadero(hora_local_std: datetime, utc: str, ecc_del_tiempo: float, long_meridian: float, long_ubicacion: float) -> float:
    """
    Calcula el tiempo solar verdadero (TSV) para una hora local dada.

    Args:
        hora_local: hora local (datetime)
        utc: zona horaria, valor por defecto 'UTC'
        ecc_del_tiempo: ecuación del tiempo (minutos)
        long_meridian: longitud del meridiano (grados o radianes)
        long_ubicacion: longitud de la ubicación (grados o radianes)
        unit: unidades del ángulo ('deg' para grados o 'rad' para radianes)
    Returns:
        tiempo_solar_verdadero: tiempo solar verdadero (datetime)
    """
    hora_local_std = hora_local_std.replace(tzinfo=pytz.timezone(utc))

    return hora_local_std + ecc_del_tiempo/60 + 4*(long_meridian-long_ubicacion)/24/60 + 4*(long_meridian-long_ubicacion)

def angulo_horario(tsv: datetime, unit='rad') -> float:
    """
    Calcula el ángulo horario (HRA) para un tiempo solar verdadero dado.

    Args:
        tsv: tiempo solar verdadero (datetime)
        unit: unidades del ángulo ('deg' para grados o 'rad' para radianes)
    Returns:
        angulo_horario: ángulo horario (grados o radianes)
    """
    angulo_horario = 15*(12 - tsv.hour + tsv.minute/60 + tsv.second/3600)
    if unit == 'deg':
        angulo_horario = math.degrees(angulo_horario)
    return angulo_horario

def declinacion_solar(angulo_diario: float, unit='rad') -> float:
    """
    Calcula la declinación solar (delta) para un ángulo diario dado.

    Args:
        angulo_diario: ángulo diario (grados o radianes)
        unit: unidades del ángulo ('deg' para grados o 'rad' para radianes)
    Returns:
        declinacion_solar: declinación solar (grados o radianes)
    """

    # a = 0.006918
    # b = -0.399912
    # c = 0.070257
    # d = -0.006758
    # e = 0.000907
    # f = -0.002697
    # g = 0.00148
    
    # declinacion_solar = a - b * math.cos(angulo_diario) + c * math.sin(angulo_diario) - d * math.cos(2 * angulo_diario) + e * math.sin(2 * angulo_diario) - f * math.cos(3 * angulo_diario) + g * math.sin(3 * angulo_diario)
    
    declinacion_solar = 0.006918 - 0.399912 * math.cos(angulo_diario) + 0.070257 * math.sin(angulo_diario) \
                      - 0.006758 * math.cos(2 * angulo_diario) + 0.000907 * math.sin(2 * angulo_diario) \
                      - 0.002697 * math.cos(3 * angulo_diario) + 0.00148 * math.sin(3 * angulo_diario)
    
    if unit == 'deg':
        declinacion_solar = math.degrees(declinacion_solar)
    
    return declinacion_solar

def cos_sza(latitude: float, hour_angle: float, solar_declination: float, unit='rad') -> float:
    """
    Calcula el coseno del ángulo cenital (cos(SZA)) para una latitud, ángulo horario y declinación solar dados.

    Args:
        latitude: latitud de la ubicación (grados o radianes)
        hour_angle: ángulo horario (grados o radianes)
        solar_declination: declinación solar (grados o radianes)
        unit: unidades del ángulo ('deg' para grados o 'rad' para radianes)
    Returns:
        cos_sza: coseno del ángulo cenital (grados o radianes)
    """
    if unit == 'deg':
        latitude = math.radians(latitude)
        hour_angle = math.radians(hour_angle)
        solar_declination = math.radians(solar_declination)

    sin_lat = math.sin(latitude)
    sin_dec = math.sin(solar_declination)
    cos_lat = math.cos(latitude)
    cos_dec = math.cos(solar_declination)

    cos_sza = sin_lat * sin_dec + cos_lat * cos_dec * math.cos(hour_angle)

    if unit == 'deg':
        cos_sza = math.degrees(cos_sza)

    return cos_sza

def distancia_tierra_sol(angulo_diario: float, unit='rad') -> float:
    """
    Calcula la distancia Tierra-Sol (R) para un ángulo diario dado.

    Args:
        angulo_diario: ángulo diario (grados o radianes)
        unit: unidades del ángulo ('deg' para grados o 'rad' para radianes)
    Returns:
        distancia_tierra_sol: distancia Tierra-Sol (UA)
    """
    distancia_tierra_sol = 1.00011 + 0.034221 * math.cos(angulo_diario) + 0.00128 * math.sin(angulo_diario) \
                         + 0.000719 * math.cos(2 * angulo_diario) + 0.000077 * math.sin(2 * angulo_diario)
    
    if unit == 'deg':
        distancia_tierra_sol = math.degrees(distancia_tierra_sol)
    
    return distancia_tierra_sol

def irradiancia_extra_sup_horizontal(irradiacion_extraterrestre: float, distancia_tierra_sol: float, cos_zsa: float) -> float:
    """
    Calcula la irradiancia extraterrestre en la superficie horizontal de la tierra

    Args:
        irradiacion_extraterrestre: irradiancia extraterrestre (W/m2)
        distancia_tierra_sol: distancia Tierra-Sol (UA)
        cos_zsa: coseno del ángulo cenital (grados o radianes)
    Returns:
        irradiancia_extra_sup_horizontal: irradiancia extraterrestre en la superficie horizontal de la tierra (W/m2)
    """

    irradiancia_extra_sup_horizontal = irradiacion_extraterrestre * distancia_tierra_sol ** 2 * cos_zsa

    return irradiancia_extra_sup_horizontal

def indice_claridad_cielo(irradiancia_global, tsi, cos_cenital):
    """
    Calcula el índice de claridad del cielo.
    """
    kt = irradiancia_global / (tsi * cos_cenital)
    return kt