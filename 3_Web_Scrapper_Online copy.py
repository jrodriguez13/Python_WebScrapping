# Scrapper ONLINE. Se accede a la web de ML, automatizando la búsqueda del término 'teclado' y 
# seleccionando mediante Selenium uno de los filtros de precio
# Luego, mediante BeautifulSoup se realiza un muestreo por consola de la lista de productos obtenidos

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.get('https://mercadolibre.com.ar')

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.nav-search-input'))).send_keys('teclado')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/aside/section/div[12]/ul/li[1]/a')))

url = driver.find_element_by_xpath('/html/body/main/div/div[2]/aside/section/div[12]/ul/li[1]/a').get_attribute("href")

driver.get(url)
time.sleep(5)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/section/ol')))
html_list = driver.find_element_by_css_selector("ol.ui-search-layout.ui-search-layout--stack")
items = html_list.find_elements_by_tag_name("li")

for item in items:
    text = item.get_attribute('innerHTML')
    soup = BeautifulSoup(text, 'html.parser')
    titulo = soup.find_all("h2")[0].string
    print('Producto: ', titulo)
    precio = soup.select("span.price-tag-fraction")[0].text
    print('Precio: $', precio)
    for link in soup.select('a.ui-search-item__group__element.ui-search-link'):
        print('Link: ', link.get("href"))
    print('*' * 5)