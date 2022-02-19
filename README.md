# GPU-tracker-Argentina
Scrapping de paginas web de compra-venta de GPUs en Argentina


El gpu_tracking_argentina.py se encarga de hacer web-scraping de las famosas paginas de compra de placas de video: Mercadolibre, Compragamer y Libreopcion. 

Tener en cuenta que se requiere de la librería Selenium

```
pip install selenium
```
y se debe instalar el driver del navegador que utilizaremos (https://selenium-python.readthedocs.io/installation.html#drivers)

NOTA: Si se corre desde un colab, no se debe instalar nada. Funciona desde ya.

Tras correr el código, todo se globaliza finalmente en una sola función: 
```
price_tracker(gpu_type, thres, PATH, product_info, interval)
```

en donde por ejemplo, 

```
gpu_type = '1660 super' #la placa que desamos comprar
thres = 80000 #valor cota inferior en pesos de la placa para evitar busquedas engañosas
PATH =  'C:/Users/.../chromedriver.exe' # El path a donde instalé el .exe de mi navegador (default PATH='chromedriver')
product_info = False #informacion detallada de cada palca (default product_info=False)
interval = 3600 #cada cuanto se repite la busqueda de la placa en segundos (default interval=21600)
```

La fución nos printea en pantalla el sitio y el valor en pesos de la placa que matchea con nuestras necesidades (el mejor precio del mercado).
Ademas, devuelve un .csv (gpu.csv) con todas las placas encontradas, ordenadas en orden ascendiente de precio. Tener en cuenta que el stock de las placas se ve reflejado en el .csv (el stock es una variable implicita).


El código se puede ampliar jugando con la función price_tracker. 

**Actualización 18/02**

Se me ocurrió que tal vez estaba bueno lanzar esto en formato web. Pensando en modo crypto, tras ir a whattomine, ver que placas caen tienen la mejor relación mh/costo, se podría hacer algo para visualzar en vivo los mejores sitios en donde comprar las placas. A modo de incio, usé Flask para crear localmente un sitio web y hacer un display del top best prices for GPUs para las 3 GPU que considero asequibles para minar ETH hoy (es febrero del 2022 y ETH 2.0 aún no salio).

Se agregaron los archivos .py:

  - GPU_tracker_run_580.py
  - GPU_tracker_run_1660.py
  - GPU_tracker_run_3070.py

Que hacen alusión a las placas rx580, 1660 super y rtx3070 y corren cada uno al archivo madre GPU_tracker_Argentina.py

y se incorporó el uso de Flask en el archivo:

  - flask_GPU.py

Para correr esto, poner todos los archivos en una misma carpeta, ejecutar los GPU_tracker_run_x.py (por default corren cada 24 hs) y luego correr el flask_GPU.py. Este último requiere de Flask por lo que *pip install flask* es necesario. Tiene por default un Debug=True, esto significa que todos los cambios que hagamos a los otros archivos se verán reflejados en la app web automáticamente.  

A futuro:

  + Webpage GPU tracker Live

  + Automatizar una funcion para mandar mails al usuario cuando se haya encontrado el precio que el usuario queria
  
  + Graficar en vivo los valores de las placas según cada sitio
  


*Hecho con amor by mossney.*
