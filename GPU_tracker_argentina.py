# -*- coding: utf-8 -*-
"""
@author: mossney



Las siguientes funciones scrapean los sitios de Mercadolibre, Compragamer y Libreopcion.

Estos son los 3 sitios mas grandes de compra/venta de (en particular) gpus de Argentina. 

La idea de este codigo es poder automatizar la búsqueda de GPUs (cuyo stock y cuyos precios 
son sumamante volátiles)

INICIALIZACION:
    1) pip install selenium
    2) Instalar drivers con el navegador que quieras (https://selenium-python.readthedocs.io/installation.html#drivers)
    3) definir el path al driver. En caso de chrome, por ejemplo: path = 'C:/Users/.../chromedriver.exe'
    4) Correr las funciones de aca abajo
    5) Correr x ejemplo:  price_tracker('3060 ti', thres = 150000 , product_info = False, PATH = path, interval = 3600)
       Esto hace busquedas de la placa 3060 ti, que se que esta mas cara que 150 mil pesos. no me muestra detalles
       de cada producto (product_info = False), utiliza el path al navegador que elegí en el paso 2 y corre el script de busqueda 
       cada un intervalo de 3600 seg = 1hs
    6) Se genera un csv 'gpu.csv' con los datos relevantes de la busqueda
"""
#MERCADOLIBRE scraper
#El gpu_type es la placa que queremos buscar, 
#El product_info es por si queremos detalles 
#tecnicos de cada placa. 
#Recomiendo product_info = False pues es mucho mas rapido, 
#de otra forma, el codugo scrapea publicacion por publicacion

def meli_gpu_tracker(gpu_type, product_info):

  #import things
  import numpy as np
  import pandas as pd
  from bs4 import BeautifulSoup as BS
  import requests
  #init
  gpu_type_ml = gpu_type.replace(' ','-')
  list_products = []
  url = 'https://computacion.mercadolibre.com.ar/componentes-pc-placas-video/{}_Desde_{}'.format(gpu_type_ml, len(list_products))
  response = requests.get(url)
  soup = BS(response.content, 'html.parser')
  paginas = int(soup.find(name = 'li', attrs = {'class' : 'andes-pagination__page-count'}).text.replace('de ',''))

  #iterate pages
  url_site = []
  prices = []
  links = []
  sites = []
  conditions = []
  brands = []
  versions = []
  editions = []
  titles = []
  for i in range(paginas):
    try:  
      url_site.append('https://computacion.mercadolibre.com.ar/componentes-pc-placas-video/{}_Desde_{}'.format(gpu_type_ml, len(list_products)))
      response = requests.get(url_site[i])
      soup = BS(response.content, 'html.parser')
      list_products = soup.findAll(name = 'li', attrs = {'class' : 'ui-search-layout__item'})

      title_ml = []
      price_ml = []
      link_ml = []
      site = []
      condition = []

      for product in list_products:
        site.append('Mercadolibre')
        title_ml.append(product.find(name = 'h2', attrs = {'class' : 'ui-search-item__title'}).text)
        price_ml.append(int(product.find(name = 'span', attrs = {'class' : 'price-tag-amount'}).text.replace('$','').replace('.','')))
        link_ml.append(product.find('a')['href'])
        try:
          condition.append(product.find(attrs = {'class' : 'ui-search-item__group__element ui-search-item__details'}).text)
        except:
          condition.append('Nuevo')

      prices.append(price_ml)
      links.append(link_ml)
      titles.append(title_ml)
      sites.append(site)
      conditions.append(condition)

      #iterate articles (if product_info == True)
      brand = []
      version = []
      edition = []
      for url in link_ml:
        if product_info == True:
          response = requests.get(url)
          soup = BS(response.content, 'html.parser')
          specs = soup.find_all(attrs = {'class' : 'andes-table__column--value'})
          try:
            brand.append(specs[1].text)
          except: 
            brand.append(np.nan)
          try:
            version.append(specs[5].text)
          except: 
            version.append(np.nan)
          try:
            edition.append(specs[6].text)
          except:
            edition.append(np.nan)
        else:
          brand.append(np.nan)
          version.append(np.nan)
          edition.append(np.nan)



      brands.append(brand)
      versions.append(version)
      editions.append(edition)
    except:
      pass
  #merge list of lists
  prices = sum(prices, [])
  links = sum(links, [])
  titles = sum(titles, [])
  sites = sum(sites, [])
  conditions = sum(conditions, [])

  brands = sum(brands, [])
  versions = sum(versions, [])
  editions = sum(editions, [])

  #create dataframe
  dict_ml = {'Site':sites, 'Store':sites, 'Price':prices, 'Condition':conditions, 'Title':titles, 'Brand':brands, 'Edition':editions, 'Version':versions, 'Link':links }
  df = pd.DataFrame(dict_ml)
  return df

#COMPRAGAMER scraper
#Java Script generated content. 
#Cuando hacemos el request, 
#no carga el JS en donde esta 
#toda la info que quiero. 
#Debo usar Selenium.   
def compragamer_gpu_tracker(gpu_type, product_info, PATH = 'chromedriver'):
    #import things
    import pandas as pd
    import numpy as np
    from bs4 import BeautifulSoup as BS
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
  
    #What to scrap
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
  
    gpu_type = gpu_type.replace(' ','%20')
    url = 'https://compragamer.com/?seccion=3&criterio={}'.format(gpu_type)
    driver.get(url)
    time.sleep(2)
  
    #BS
    html = driver.page_source
    soup = BS(html, 'html.parser')
  
    #Products
    list_products = soup.find_all(attrs={'class':'mat-card card-product col-12 col-md-12 ng-star-inserted'})

    #General info
    compragamer_url_base = 'https://compragamer.com'
    condition = []
    site = []
    link = []
    price = []
    title = []
    for product in list_products:
        condition.append('Nuevo')
        site.append('CompraGamer')
        price.append(int(product.find(attrs={'class': 'theme_precio'}).text.replace('$','').replace('.','')))
        title.append(product.find(attrs={'class':'theme_nombreProducto title aself vert-center mat-h2'}).text)
        link.append(compragamer_url_base + product.find('a')['href'])
    
    #Detailed info
    brand = []
    edition = []
    version = []
    for url in link:
        if product_info == True:
            time.sleep(np.random.uniform(0.5, 1)) #acting as a normal user
            driver.get(url)
            time.sleep(2)
            soup = BS(driver.page_source, 'html.parser')
            brand.append(soup.find(attrs={'class':'brand-name ng-star-inserted'}).text)
            version.append(soup.find(attrs={'class':'mat-chip mat-focus-indicator mat-primary mat-standard-chip ng-star-inserted'}).text.replace('SKU: ',''))
            edition.append(np.nan)
        else:
            brand.append(np.nan)
            edition.append(np.nan)
            version.append(np.nan)
    
    dict_compragamer = {'Site':site, 'Store':site, 'Price':price, 'Condition':condition, 'Title':title, 'Brand':brand, 'Edition':edition, 'Version':version, 'Link':link }
    df = pd.DataFrame(dict_compragamer)

    return df

#LIBREOPCION scraper
#Al igual que con compragamer, 
#por cuestiones de JS, debo usar
#Selenium
def libre_opcion_gpu_tracker(gpu_type, product_info, PATH='chromedriver'):
  #import things
  import pandas as pd
  import numpy as np
  from bs4 import BeautifulSoup as BS
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  import time

  #What to scrap
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

  #get
  gpu = gpu_type.replace(' ','-')
  url_base = 'https://www.libreopcion.com/'
  url = url_base + gpu + '?c=9&o=rel'
  driver.get(url)
  time.sleep(5)
  html = driver.page_source
  soup = BS(html, 'html.parser')

  #Products
  list_products = soup.find_all(attrs={'class':'productos-modulo-b'})

  #General info
  site = []
  title = []
  price = []
  brand = []
  store = []
  link = []
  for product in list_products:
    try:
      stores_available = len(product.find(attrs={'class':'lista'}))

      for i in range(stores_available):
        site.append('Libre Opción')
        brand.append(str(product.find(attrs={'class':'marca'}).find('img')).split('"')[1].replace('Logo de ',''))
        title.append(product.find(attrs={'class':'titulo'}).text.replace('          ','').replace('\n',''))
        store.append(product.find(attrs={'class':'productos-otras-opciones-compra'}).find(attrs={'class':'lista'}).find_all('a')[i].text.replace('        ','').split('\n')[1])
        price.append(int(product.find(attrs={'class':'productos-otras-opciones-compra'}).find(attrs={'class':'lista'}).find_all('a')[i].text.replace('        ','').split('\n')[2].replace('$ ','').split('.')[0]))
        link.append(url_base + product.find(attrs={'class':'productos-otras-opciones-compra'}).find(attrs={'class':'lista'}).find_all('a')[i]['href'])
    except:
      site.append('Libre Opción')
      brand.append(str(product.find(attrs={'class':'marca'}).find('img')).split('"')[1].replace('Logo de ',''))
      title.append(product.find(attrs={'class':'titulo'}).text.replace('          ','').replace('\n',''))
      store.append('Libre Opcion')
      link.append(url_base + product.find('a')['href'])
      price.append(int(product.find(attrs={'class':'con-descuento'}).text.replace('\n              $\xa0','').replace('\n              00','').replace('.','')))

  #detailed info
  version = []
  condition = []
  edition = []
  for url in link:
    if product_info == True:
      time.sleep(np.random.uniform(0.5, 1)) #acting as a normal user
      driver.get(url)
      time.sleep(2)
      html = driver.page_source
      soup = BS(html, 'html.parser')

      try:
        version.append(soup.find(attrs={'class':'producto-especificaciones'}).find_all('span')[17].text.replace('\n            ','').replace('\n          ',''))
      except:
        version.append('Unknown')
      try:
        condition.append(soup.find(attrs={'class':'producto-especificaciones'}).find_all('span')[1].text.replace('\n            ','').replace('\n          ',''))
      except:
          if (soup.find('info-ficha producto-usado')) is None:     
            condition.append('Nuevo')
          else:
            condition.append('Usado')
      try:
        edition.append(soup.find(attrs={'class':'producto-especificaciones'}).find_all('span')[12].text.replace('\n            ','').replace('\n          ',''))
      except:
        edition.append('Unknown')
    else:
        version.append(np.nan)
        condition.append(np.nan)
        edition.append(np.nan)

  dict_libre = {'Site':site, 'Store':store, 'Price':price, 'Condition':condition, 'Title':title, 'Brand':brand, 'Edition':edition, 'Version':version, 'Link':link }
  df = pd.DataFrame(dict_libre)

  return df

#Todo el scraping junto
def gpu_tracker(gpu_type, info=False, PATH='chromedriver'):
    import pandas as pd  
    df_ml = meli_gpu_tracker(gpu_type, info)
    df_compra = compragamer_gpu_tracker(gpu_type, info, PATH)
    df_libre = libre_opcion_gpu_tracker(gpu_type, info, PATH)
    
    df_total = pd.concat([df_compra, df_libre, df_ml]).sort_values(by=['Price']).reset_index(drop=True)
    return df_total

#Filtramos poniendo una threshold al precio 
def filtered_df(df_total, thres = 0):
    index_to_drop = []
    for i in range(len(df_total['Price'])):
      if df_total['Price'][i] < thres:
        index_to_drop.append(i) 
    
    df_filtered = df_total.drop(df_total.index[index_to_drop]).reset_index(drop=True)
    return df_filtered

#La funcion final
def price_tracker(gpu_type, thres, PATH, info=False, interval=21600):
    import time
    from datetime import datetime
    global df_top
    while True:
        df = gpu_tracker(gpu_type, info, PATH)
        df_filtered = filtered_df(df, thres)
        df_filtered.to_csv('gpu.csv')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print('Busqueda actualizada a las {} \n El mejor resultado fue: ${} de {}'.format(current_time, df_filtered['Price'][0], df_filtered['Site'][0]))
        time.sleep(interval)
    
#%%
#my situation
PATH = r'C:\Users\mossney\Documents\Selenium\chromedriver.exe'

price_tracker('3060 ti', 250000, PATH, False , 60)

