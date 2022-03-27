# iber2cnmc
UPDATE: Este script ya no es necesario. I-de actualmente genera CSV's de consumo por periodo 100% compatibles con el simulador de la CNMC.
  
Script en Python para convertir el CSV de las estidísticas de consumo del contador inteligente obtenidas de https://www.i-de.es/ en un CSV compatible con el simulador de facturación de tarifas PVPC de la CNMC (https://facturaluz2.cnmc.es/facturaluz2.html).   

La web i-de posee dos modos de presentar consumos en fomato CSV: El primero es generar un CSV asociado a una factura. El segundo, es la selección entre una fecha inicial y una final de un periodo de días. El primer tipo de CSV no requiere ningún tipo de conversión para ser reconocido en la web de la CNMC. Los segundos sí, y este script python los convierte en CSV's compatibles.
  
Uso:  
Iber2cnmc.py -i input.csv -o output.csv
