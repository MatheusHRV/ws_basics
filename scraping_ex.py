# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:07:22 2024

@author: Matheus Vicente, @MatheusHRV
https://www.linkedin.com/in/matheushrv/
"""

import time
import pandas as pd
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

################
# Extração de dados
################

# Url do site que deseja acessar
url = "https://www.worldometers.info/world-population/brazil-population/"
option = Options()
option.headlers = True # mudar para 'False' se quiser que o navegador opere em 2º plano

# Download do driver que controla o navegador (Firefox nesse caso)
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

driver.get(url) # acessar o site desejado com o navegador

# Um tempo de 5 segundos para o site carregar por completo antes de prosseguir
time.sleep(5)

# Definir o path do elemento que queremos extrair
table = driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div/div[5]/table')

# Extraimos o atributo 'outerHTML' do elemento para selecionar toda a parte externa do HTML ou toda a tabela
html_content = table.get_attribute('outerHTML')

# O método 'html.parser' do BeautifulSoup serve para convertermos o HTML cru em um objeto manipulavel pelo Pandas
soup = bs4(html_content, 'html.parser')


################
# Processamento e manipulação de dados
################

# Localizar e armazenar a delimitação da tag 'table' do objeto soup
table = soup.find(name='table')

# O Pandas tem um atributo específico para ler html (e já transforma em dataframe), mas o html precisa estar em string
df = pd.read_html(str(table))[0] # Como o pd.read_html retorna uma lista (mesmo que de 1 elemento) usamos o [0] para selecionar apenas o primeiro
# Dica: Se vc quiser ler um arquivo CSV com o Pandas é só usar pd.read_csv('caminho'), pd.read suporta vários outros formatos também

df = df.drop(12) # Excluir uma linha do dataframe
head_data = df.head(10) # visualizar apenas os primeiros 10 registros
print(head_data)

# Renomear uma coluna do dataframe {"Antigo nome": "novo nome"}
df = df.rename(columns={"Year": "year"})


################
# Visualização de dados
################

# plt.plot para um gráfico de linha (se quiser mudar para barras > "plt.bar" e remover os dois últimos métodos)
# Por padrão, ele deve receber o eixo X e depois o Y, selecionei as colunas X(year) e Y(Population) dentro do dataframe
plt.plot(df['year'], df['Population'])
plt.title('Crescimento da população brasileira') # Legenda superior
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True) # Mostrar grades
plt.show() # Exibir o gráfico na IDE (se isso der problema tem q ver se sua IDE suporta plotar gráficos)

driver.quit() # encerrar o driver do navegador