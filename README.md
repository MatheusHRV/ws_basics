####################
##### LER PELO README OU RAW #####
####################

Projeto de análise de dados para iniciantes.

Descrição: 
Projeto end-to-end de análise de dados para iniciantes, da extração á visualização dos dados.

O que será aprendido: 
Extração, processamento, visualização de dados.
Geralmente um projeto de análise ou ciência de dados em empresas seguem um workflow padrão (1º extração dos dados > 2º processamento > 3º visualização), os dados podem ser extraídos de diversas fontes, web-scraping é quando extraímos da WEB, muito comum.
Esse projeto é símples mas percorre por todas estas etapas, primeiro fazemos a extração dos dados de um website de maneira automatizada, processamos e manipulamos os dados, e para a visualização criamos um gráfico.
Geralmente projetos de análise de dados em grandes empresas seguem este mesmo escopo, só muito mais complexos.

Task-list:
# Análise exploratória
1 - Acessar o website: https://www.worldometers.info/world-population/brazil-population/
2 - Entender a estrutura do site, tentar inspecionar o HTML, principalmente da tabela 'Population of Brazil (2024 and historical)' que é a que vamos extrair.

# Extração de dados
3 - No Python, utilize o Selenium para automatizar o navegador e acessar o site pela URL anterior (e de um tempo para o site carregar)
4 - Use as ferramentas do Selenium para automaticamente localizar a tabela 'Population of Brazil (2024 and historical)' pelo HTML, pode passar como parâmetro do Selenium o XPATH da tabela, nome da Classe da tabela, etc.
(O XPATH costuma funcionar bem, um truque é inspecionar a tabela pelo Opera GX, clicar com o botão direito e selecionar a opção de copiar o XPATH inteiro, sempre funciona)
5 - Utilize o BeautifulSoup para converter o HTML crú em um objeto mais familiar para o Python.

# Processamento dos dados
6 - Use o Pandas para ler o objeto do BeautifulSoup.
7 - Crie um Pandas DataFrame á partir deste objeto.
8 - Um dataframe é uma tabela (como a do excel) onde você pode manipular do jeito que você quiser, teste excluir uma linha ou coluna, adicionar mais dados, filtrar ou visualizar de outras formas.
9 - Renomear uma coluna do dataframe

# Visualização de Dados
10 - Usando matplotlib, crie um gráfico de linha mostrando o crescimento da população brasileira ao decorrer do tempo.
11 - Exiba o gráfico (pode exibir na própria IDE ou salvar o gráfico em .png)
12 - Tente exibir outros tipos de gráfico, mudar cores, tamanho, etc.


Pré requisitos de conhecimento: 
Básico de Python (não usa loops, OOP nem nada, só listas)
Básico de web-scraping com Selenium. --> https://www.youtube.com/watch?v=Vxl5jUltHBo <-- Esse video vai te ajudar mt, só a sintaxe da lib q mudou um pouco: https://www.selenium.dev/pt-br/documentation/webdriver/elements/locators/
Quase nada de BeautifulSoup (Parsear objetos HTML) --> mesmo video acima, https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/
Básico de Pandas (leitura de objetos, criação de Dataframe, manipulação de linhas e colunas) --> https://www.youtube.com/watch?v=F6kmIpWWEdU
Básico de Matplotlib (Plotar um gráfico de linha com legenda --> https://www.youtube.com/watch?v=tpNzggVtwhM

Pré requisitos técnicos:
pip install beautifulsoup4
pip install selenium
pip install pandas
pip install matplotlib
pip install webdriver_manager

Declaração de bibliotecas:
import time
import pandas as pd
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

Neste repositório tem o meu código pronto scraping_ex.py, hyper mega comentado, consulte se achar necessário
