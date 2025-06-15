import time
import json
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicia o navegador
navegador = webdriver.Chrome()

# Acessa o site da Tabela Fipe
navegador.get("https://veiculos.fipe.org.br/")
navegador.maximize_window()

time.sleep(1)  # espera curta para o DOM atualizar

# Primeiro: clicar em consulta de carros e utilitários pequenos 
elemento = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[2]'))).click()

time.sleep(1)

# Segundo: clicar e selecionar o mês de pesquisa
navegador.find_element(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/a/div/b').click()
options_mes_ano = navegador.find_elements(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/div/ul')
lista_mes_ano = options_mes_ano[0].find_elements(By.CSS_SELECTOR, 'li')
lista_mes_ano[0].click()

time.sleep(0.5)

# Terceiro: clicar e selecionar a marca
navegador.find_element(By.XPATH, '//*[@id="selectMarcacarro_chosen"]/a/div/b').click()
options_marca = navegador.find_elements(By.XPATH, '//*[@id="selectMarcacarro_chosen"]/div/ul')
lista_marca = options_marca[0].find_elements(By.CSS_SELECTOR, 'li')
lista_marca[0].click() #indice[1] --->Marca: ACURA

time.sleep(0.5)

# Quarto: clicar e selecionar o modelo
navegador.find_element(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/a/div/b').click()
options_modelo = navegador.find_elements(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/div/ul')
lista_modelo = options_modelo[0].find_elements(By.CSS_SELECTOR, 'li')
lista_modelo[0].click() #indice[0] ---> Modelo: Integral 1.8

time.sleep(0.5)

# Quinto: clicar e selecionar o ano/modelo
navegador.find_element(By.XPATH, '//*[@id="selectAnocarro_chosen"]/a/div/b').click()
options_ano_modelo = navegador.find_elements(By.XPATH, '//*[@id="selectAnocarro_chosen"]/div/ul')
lista_ano_modelo = options_ano_modelo[0].find_elements(By.CSS_SELECTOR, 'li')
lista_ano_modelo[1].click() #indice[1] ---> Ano: 1991

time.sleep(0.5)

# Sexto: clicar em pesquisar
navegador.find_element(By.LINK_TEXT, 'Pesquisar').click()

time.sleep(0.5)

# Sétimo: salvar os dados da tabela em um dicionário
tabela = navegador.find_elements(By.XPATH, '//*[@id="resultadoConsultacarroFiltros"]/table/tbody')
linhas = tabela[0].find_elements(By.CSS_SELECTOR, 'td')

carros = {}

for item in range(0, len(linhas) - 1, 2):
    carros[linhas[item].text] = linhas[item + 1].text

navegador.close()

# Sétimo: Salvar os dados em um arquivo JSON
object_json = json.dumps(carros, indent=2, ensure_ascii = False)
with open('carros_fipe_ACURA.json', 'w') as file:
    file.write(object_json)
