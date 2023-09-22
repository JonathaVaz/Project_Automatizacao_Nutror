'''
Relatório :  

A sua Empresa precisa estar constantemente monitorando 
alguns sites para saber onde pode comprar pelo menor
preço um determinado produto, sua responsabilidade é de 
fornecer uma planilha com os preços todos os dias, de pelo menos
3 sites para que a empresa possa decidir onde comprar aquele 
determinado produto.

O produto exemplo escolhido é o Abacate.


Automação Web (Selenium) - Permite abrir Navegadores, Através de algo chamado
de webdriver (Navegador que permite enviar comandos Python)

'''
# Passos Lógicos :

# - Abrir o Navegador 
# - Acessar o Primeiro/Segundo/Terceiro site
# - Encontrar onde esta o produto
# - Anotar o Valor
# - Colocar o Valor na Planilha

# (Executar com os 3 Sites diferentes)

# Sites : 
    # 1 - https://sitepreco1.netlify.app
    # 2 - https://sitepreco2.netlify.app
    # 3 - https://sitepreco3.netlify.app

# - Comandos Necessários entender :
# - XPATH - Caminho para chegar até um Elemento dentro do HTML
# - Exemplo de HTML (Atributo, Tag) : <div class="" id"">
# - TAG - <div> é uma Tag. Tipo de Elemento que pode ser encontrado em uma Página HTML. (Exemplo <div>, <body>, <span> são Tags)
# - ATRIBUTO da TAG - class="" id"" é um atributo. O que se encontra dentro da Tag, dando valor.
# - Para montar um XPATH voce precisa digitar "  //tag[@atributo="valor do atributo"]  "


# 1 - Qual Navegador Utilizar? (Opcional) Navegador Indicado: Google Chrome (Por ser um processo Web essa seria a melhor Escolha por Segurança, Dados Atualizados, Compatível, Simples e Universal)
# 2 - Instalar esse Navegador no computador/computador do cliente
# 3 - Instalar o Selenium no Python
# 4 - Instalar um WebDriver, através do webdriver-manager


# Passos Descritivos :

# Importar as Bibliotecas de uso para tempo de execução do programa, criação, abertura e leitura de arquivos/planilha csv, navegar entre sites e organizar arquivos por vírgula separadamente
# Abrir o Navegador e Instalação do ManagerService (Execução apenas uma vez)
# Acessar os Sites separadamente por vez 
                # 1 - (sitepreco1.netlify.app)
                # 2 - (sitepreco2.netlify.app)
                # 3 - (sitepreco3.netlify.app)
# Encontrar onde está o Produto (Abacate) no Site por Indice
# Anotar o Valor do Produto
# Copiar o Valor do Produto na Planilha CSV

# <<< CODDING!!! >>>



from mailbox import linesep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os 
from time import sleep 



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    



driver.get('https://sitepreco1.netlify.app')          
sleep(5)                               
precos_site_1 = driver.find_elements(By.XPATH,'//h6[@class="price_heading"]')    
sleep(3)    
preco_final_site_1 = precos_site_1[0].text.split(' ')[1]                                



driver.get('https://sitepreco2.netlify.app')
sleep(5)
precos_site_2 = driver.find_elements(By.XPATH,"//h5")
sleep(3)
preco_final_site_2 = precos_site_2[3].text.split('$')[1]



driver.get('https://sitepreco3.netlify.app')
sleep(5)
precos_site_3 = driver.find_elements(By.XPATH,'//div[@class="featured__item__text"]//h5')
sleep(3)
preco_final_site_3 = precos_site_3[2].text.split('$')[1]



with open('precos.csv','w',newline='',encoding='utf-8') as arquivo:
    arquivo.write(f'site,preço{os.linesep}')
    arquivo.write(f'https://sitepreco1.netlify.app,{preco_final_site_1}{os.linesep}')
    arquivo.write(f'https://sitepreco2.netlify.app,{preco_final_site_2}{os.linesep}')
    arquivo.write(f'https://sitepreco3.netlify.app,{preco_final_site_3}{os.linesep}')
