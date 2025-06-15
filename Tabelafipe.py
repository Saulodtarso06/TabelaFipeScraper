from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import datetime
import json

# Inicia o navegador
navegador = webdriver.Chrome()

# Acessa o site da Tabela Fipe
navegador.get("https://veiculos.fipe.org.br/")
navegador.maximize_window()

"""
# Aguarda o carregamento do botão "Carros e utilitários pequenos" e clica
carros_btn = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[2]')
    )
)
carros_btn.click()
"""
# Primeiro: clicar em consulta de carros e utilitários pequenos 
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="front"]/div[1]/div[2]/ul/li[1]/a/div[2]'))
).click()

carros = {} # Agora fora do loop para acumular todos os dados
numero_carro = 0

time.sleep(1) # espera curta para o DOM atualizar

def seleciona_mes_ano():
    navegador.find_element(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/a/div/b').click()
    options = navegador.find_elements(By.XPATH, '//*[@id="selectTabelaReferenciacarro_chosen"]/div/ul')
    return options[0].find_elements(By.CSS_SELECTOR, 'li')

def seleciona_marca(indice):
    WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="selectMarcacarro_chosen"]/a/div/b'))
    ).click()
    options = navegador.find_elements(By.XPATH, '//*[@id="selectMarcacarro_chosen"]/div/ul')
    marcas = options[0].find_elements(By.CSS_SELECTOR, 'li')
    marcas[indice].click() #indice[1] --->Marca: ACURA

def seleciona_modelo():
    navegador.find_element(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/a/div/b').click()
    options = navegador.find_elements(By.XPATH, '//*[@id="selectAnoModelocarro_chosen"]/div/ul')
    return options[0].find_elements(By.CSS_SELECTOR, 'li') #indice[0] ---> Modelo: Integral 1.8

def seleciona_ano_modelo():
    navegador.find_element(By.XPATH, '//*[@id="selectAnocarro_chosen"]/a/div/b').click()
    options = navegador.find_elements(By.XPATH, '//*[@id="selectAnocarro_chosen"]/div/ul')
    return options[0].find_elements(By.CSS_SELECTOR, 'li') #indice[1] ---> Ano: 1991

def move_telas(times):
    for _ in range(times):
        navegador.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)

########################################################################################################

try:
    start = datetime.now()
    print(f"Início: {start}")

# Segundo: Clicar e Selecionar o mês de referência da pesquisa

    lista_mes_ano = seleciona_mes_ano()
    for mes_ano in range(0, 1):
        lista_mes_ano[mes_ano].click()

        seleciona_marca(0)  # ACURA, por exemplo // FIAT cógido 28 // ACURA código 0
        
        # terceiro: clicar e selecionar a marca
        lista_modelos = seleciona_modelo()
        print(f'Quantidade de modelos = {len(lista_modelos)}\n')

        # quarto: clicar e selecionar o modelo
        for modelo in range(len(lista_modelos)):
            print(f'*************** Modelo: {modelo} ***************')

            lista_modelos[modelo].click()

            lista_ano_modelo = seleciona_ano_modelo() # FIAT cógido 28. ACURA codigo 0

            # quinto: clicar em ano_modelo e pesquisar
            for ano_modelo in range(len(lista_ano_modelo)):
                lista_ano_modelo[ano_modelo].click()

                time.sleep(0.5)
                navegador.find_element(By.LINK_TEXT, 'Pesquisar').click()

                # Sexto: salvar os dados da tabela em um dicionario
                tabela = navegador.find_elements(By.XPATH, '//*[@id="resultadoConsultacarroFiltros"]/table/tbody')
                linhas = tabela[0].find_elements(By.CSS_SELECTOR, 'td')

                carro = {}

                for i in range(0, len(linhas) - 1, 2):
                    chave = linhas[i].text.strip()
                    valor = linhas[i + 1].text.strip()
                    carro[chave] = valor

                    #carro = {}
                    #numero_carro = 0
                    # chave = linhas[item].text.strip()
                    # valor = linhas[item + 1].text.strip()

                carros[numero_carro] = carro
                print(f'Carro {numero_carro}: {carro}')
                print(15 * '-')
                numero_carro += 1
                time.sleep(0.5)

                move_telas(3)
                time.sleep(0.5)
                lista_ano_modelo = seleciona_ano_modelo()

            move_telas(7)

            seleciona_marca(1)#reset no campo marca, esse indice precisa ser diferente
                            #da marca que estamos coletando os dados
            time.sleep(0.5)

            seleciona_marca(0)

            lista_modelos = seleciona_modelo()

        move_telas(7)
        seleciona_marca(1)
        lista_mes_ano = seleciona_mes_ano()

    end = datetime.now()
    print(f"Fim: {end}")

    # Sétimo: Salvar os dados em um arquivo JSON
    object_json = json.dumps(carros, indent=2, ensure_ascii=False)
    with open('carros_fipe.json', 'w') as file:
        file.write(object_json)

finally:
    navegador.quit()
