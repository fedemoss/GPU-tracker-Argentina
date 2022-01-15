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

A futuro:

  -Automatizar una funcion para mandar mails al usuario cuando se haya encontrado el precio que el usuario queria
  
  -Graficar en vivo los valores de las placas según cada sitio
  


*Hecho con amor by mossney.*
