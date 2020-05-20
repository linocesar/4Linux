from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pathDriver = '/home/linocesar/Downloads/chromedriver'
url = 'https://www.covid-19.pa.gov.br'
xpathNovosCasos = '//*[@id="q-app"]/div/div/div[2]/div[2]/div/div/div[1]'
xpathNovosObitos = '//*[@id="q-app"]/div/div/div[2]/div[2]/div/div/div[2]'

chrome = webdriver.Chrome(pathDriver)
chrome.get(url)

esperaCarregamento = WebDriverWait(chrome, 10)

novosCasosElement = esperaCarregamento.until(EC.presence_of_element_located((By.XPATH,xpathNovosCasos)))
novosObitosElement = esperaCarregamento.until(EC.presence_of_element_located((By.XPATH,xpathNovosObitos)))

with open('novosCasos.txt', 'w') as arquivo:
    arquivo.write(novosCasosElement.text)

with open('novosObitos.txt', 'w') as arquivo:
    arquivo.write(novosObitosElement.text)

chrome.quit()