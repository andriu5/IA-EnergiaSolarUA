pvutils
========================

[![Tests](https://github.com/andriu5/IA-EnergiaSolarUA/actions/workflows/.ci.yaml/badge.svg)](https://github.com/andriu5/IA-EnergiaSolarUA/actions/workflows/.ci.yaml)

Copyright © 2023 Andrés Alvear, Mauricio Trigo. All rights reserved.

---------------------------------------------------------------------------------------------------------------------

This project provides a set of Python functions for computing astronomical variables related to photovoltaic power generation. These functions can be used in a machine learning pipeline for forecasting the power output of a photovoltaic plant.

---------------------------------------------------------------------------------------------------------------------
## 1. Implementation details:

The project consists of a single Python module `pvutils` that contains several functions for calculating important variables for photovoltaic power generation, including:

1. Irradiance Extraterrestrial (Io)
2. Solar Zenith Angle (Sza)
3. Cosine Solar Zenith Angle (cos(Sza))
4. Clear Sky Index (Kt)

> **Note:** The functions are implemented using standard astronomical formulas and are thoroughly documented with docstrings.

`pvutils` is an abbreviation of **"photovoltaic utilities"**, which refers to a set of functions and utilities designed to facilitate the calculations and analysis required for photovoltaic (PV) solar energy systems. These functions typically involve the calculation of various solar-related variables such as solar irradiance, angle of incidence, and shading effects, which are important for the accurate modeling and prediction of PV system performance.

---------------------------------------------------------------------------------------------------------------------
## 2. Testing:
### 2.1 Unit Tests:

The project has unit tests to validate that the functions and methods works as required:

```py
$ python -m unittest --verbose
```
---------------------------------------------------------------------------------------------------------------------
## 3. Running the code:

To use the pvutils module in your own machine learning pipeline, simply import the module and call the functions as needed. For example:

```py
import pvutils
import datetime

lat = 37.7749
long = -122.4194
date_time = datetime.datetime(2023, 4, 25, 12, 0, 0)

sza = pvutils.angulo_cenital(lat, long, date_time)
cos_sza = pvutils.cos_angulo_cenital(sza)
kt = pvutils.indice_claridad_cielo(lat, long, date_time)
```

---------------------------------------------------------------------------------------------------------------------
Cheers,<br>
Andrés