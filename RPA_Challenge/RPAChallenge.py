# Importa as bibliotecas necessárias
from selenium import webdriver  # Para controlar o navegador
from selenium.webdriver.common.by import By  # Para localizar elementos na página
from selenium.webdriver.chrome.options import Options  # Para configurar o navegador Chrome
import time  # Para adicionar delays no código
import pandas as pd  # Para manipular arquivos Excel
import os  # Para verificar a existência de arquivos no sistema
from openpyxl import load_workbook # Para trabalhar com arquivos Excel no formato .xlsx
# RPA Challenge Automation


# URL da página que será acessada
url = 'https://www.rpachallenge.com/'

# Configuração do navegador
options = Options()  # Cria uma instância de opções para o navegador
options.add_experimental_option("detach", True)  # Mantém o navegador aberto após a execução do script

# Inicializa o navegador Chrome com as opções configuradas
brow = webdriver.Chrome(options=options)
brow.get(url)  # Abre a URL especificada no navegador

# Pequeno delay para garantir que a página carregue corretamente
time.sleep(3)

# Caminho do arquivo Excel que contém os dados
exel_path = r'C:\Users\SE189129\Documents\_VEXIA\PYTHON\Selenium\Projetos\_RPACH_arthur_CERTO\docs\challenge.xlsx'

# Verifica se o arquivo Excel existe no exel_path especificado
if not os.path.exists(exel_path):
    print(f"Erro: O arquivo Excel não foi encontrado no caminho especificado: {exel_path}")
    brow.quit()  # Fecha o navegador
    exit()  # Encerra o programa

# Tenta ler o arquivo Excel
try:
    # Lê o arquivo Excel em um dataframe do pandas
    dataframe = pd.read_excel(exel_path)  
     # Converte os dados do DataFrame para uma lista de dicionários
    datalist = dataframe.to_dict(orient='records') 
    #Cria uma excessão de erro caso o arquivo não seja lido corretamente
except Exception as error:
    print(f"Erro ao ler o arquivo Excel: {error}")
    # Registra o erro em um arquivo de log
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"Erro ao ler o arquivo Excel: {error}\n")
    brow.quit()  # Fecha o brow
    exit()  # Encerra o programa

try:
    # Localiza e clica no botão "Start" para iniciar o desafio
    start_btn = brow.find_element(By.XPATH, '//button[text()="Start"]')
    start_btn.click()

    # Pequeno delay para garantir que os fields sejam carregados
    time.sleep(2)

    # Itera sobre os dados do Excel (adiciona)
    for index, data in enumerate(datalist):
        # Adiciona um delay apenas no primeiro formulário para evitar problemas de carregamento
        if index == 0:
            time.sleep(1)
        # Preenche os fields dinamicamente para cada linha do Excel
        for field, value in data.items():
            try:
                # Localiza o field de entrada com base no texto do rótulo
              start_field = brow.find_element(By.XPATH, f'//label[contains(normalize-space(text()), "{field}")]/following-sibling::input')
              start_field.send_keys(str(value))  # Insere o value no field
            except Exception as error:
                print(f"Error ao preencher o field '{field}': {error}")
                 # Registra o erro em um arquivo de log
                with open('field_erro_log.txt', 'a') as log_file:
                    log_file.write(f"Erro ao ler o field: {error}\n")
            
        # Localiza e clica no botão de envio para o próximo formulário
        try:
            submit_button = brow.find_element(By.XPATH, '//input[@type="submit"]')
            submit_button.click()
            time.sleep(1)  # Pequeno delay para garantir que o próximo formulário carregue
        except Exception as e:
            print(f"Erro ao enviar o formulário: {e}")
            break

    print("Dados enviados com sucesso!")  # Mensagem de sucesso após enviar todos os dados
except Exception as e:
    print(f"Erro ao interagir com os elementos: {e}")
finally:
    # Aguarda 10 segundos antes de fechar o brow
    time.sleep(10)
    brow.quit()  # Fecha o navegador
