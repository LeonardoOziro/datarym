from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def pesquisarBanda(banda):

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()

    driver.get('https://en.wikipedia.org/wiki/Main_Page')

    search_box = driver.find_element(By.NAME, "search")
    botao = driver.find_element(By.XPATH, '//button[text()="Search"]')

    search_box.click()
    search_box.send_keys(banda)

    botao.click()

    listaGeneros = []

    generos = driver.find_element(By.XPATH, '//th[text()="Genres"]')

    td_element = generos.find_element(By.XPATH, './following-sibling::td')

    div = td_element.find_element(By.XPATH, './div')

    ul = div.find_element(By.XPATH, './ul')

    li = ul.find_elements(By.XPATH, './li')

    for li in li:
        listaGeneros.append(li.text)

    driver.quit()

    return listaGeneros
