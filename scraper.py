from selenium import webdriver
from selenium.webdriver.common.by import By
import unicodedata

def has_hindi(texto):
    caracteres_totales = 0
    caracteres_hindi = 0
    caracteres_nohindi = 0

    for caracter in texto:
        nombreunicode = unicodedata.name(caracter, 'sin nombre unicode')
        if nombreunicode.find('DEVANAGARI') >= 0:
            caracteres_hindi += 1
            caracteres_totales += 1
        else:
            caracteres_nohindi += 1
            caracteres_totales += 1
    if caracteres_totales >= 0:
        proporcion = caracteres_hindi / caracteres_totales
        if proporcion >= 0.2:
            return True
        else:
            return False
    else:
        return False

def checkweb(url):
    driver = webdriver.Firefox()
    driver.get(url)
    comprobaciones = []

    contenido = driver.find_element(By.TAG_NAME, 'body').text
    comprobaciones.append(has_hindi(contenido))

    todos_los_enlaces = driver.find_elements(By.TAG_NAME, 'a')
    enlaces = [
        todos_los_enlaces[9].get_attribute('href'),
        todos_los_enlaces[13].get_attribute('href'),
        todos_los_enlaces[19].get_attribute('href'),
        todos_los_enlaces[23].get_attribute('href'),
    ]

    for enlace in enlaces:
        driver.get(enlace)
        contenido = driver.find_element(By.TAG_NAME, 'body').text
        comprobaciones.append(has_hindi(contenido))
    
    indicador = True
    for comprobacion in comprobaciones:
        if comprobacion == False:
            indicador = False
            break
    
    if indicador == True:
        return True
    else:
        return False

tick = checkweb(input('Introduce la URL'))
if tick == True:
    print('Está en hindi')
if tick == False:
    print('No está en hindi')