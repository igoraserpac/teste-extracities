import csv
import xlrd
from core.wsgi import *

from catalog.models import RegTer, Repasses

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import threading

def xls_para_csv(file_path, csv_name):
    sheet = xlrd.open_workbook(file_path).sheet_by_index(0)

    col = csv.writer(open(csv_name, 'w', newline="")) 
    for row in range(sheet.nrows): 
        col.writerow(sheet.row_values(row)) 


class TestBaixar():
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
    
    def teardown_method(self):
        self.driver.quit()
    
    def test_baixar(self):
        self.driver.get("https://consultafns.saude.gov.br/#/detalhada")
        wait = WebDriverWait(self.driver, 120)
        self.driver.set_window_size(1920, 1040)

        for i in range(1, 101):
            wait.until(expected_conditions.visibility_of_all_elements_located((By.ID, "estado")))
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "overlayLoading")))
            wait.until(expected_conditions.element_to_be_clickable((By.ID, "estado")))
            self.driver.find_element(By.ID, "estado").click()
            dropdown = self.driver.find_element(By.ID, "estado")
            dropdown.find_element(By.XPATH, "//option[. = 'MINAS GERAIS']").click()

            wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, "#estado > option:nth-child(14)")))
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "overlayLoading")))
            wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#estado > option:nth-child(14)")))
            self.driver.find_element(By.CSS_SELECTOR, "#estado > option:nth-child(14)").click()

            wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, ".margin-top-15 > .btn-primary")))
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "overlayLoading")))
            wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".margin-top-15 > .btn-primary")))
            self.driver.find_element(By.CSS_SELECTOR, ".margin-top-15 > .btn-primary").click()

            wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, ".btn:nth-child(4)")))
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "overlayLoading")))
            wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".btn:nth-child(4)")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()

            wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .btn-table .app-icone-ver")))
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "overlayLoading")))
            wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .btn-table .app-icone-ver")))
            self.driver.find_element(By.CSS_SELECTOR, f".ng-scope:nth-child({i}) > .btn-table .app-icone-ver").click()
            self.driver.execute_script("window.scrollTo(0,25)")

            wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, ".btn-primary:nth-child(3)")))
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "overlayLoading")))
            wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary:nth-child(3)")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(3)").click()
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "overlayLoading")))
            self.driver.find_element(By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding > .ng-scope").click()


teste = TestBaixar()
teste.setup_method()
teste.test_baixar()
teste.teardown_method()



for i in range(1, 101):
    xls_file = f'/home/igor/Downloads/PlanilhaDetalhada({i}).xls'
    csv_file = f'/home/igor/planilhas/detalhada({i}).csv'
    xls_para_csv(xls_file, csv_file)
    


for i in range(1, 101):
    file = f'/home/igor/planilhas/detalhada({i}).csv'
    colunas = [1, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    with open(file, 'r') as original:
        reader = csv.reader(original, delimiter=',')
        planilha = list(reader)
        codigo = [planilha[3][7]]
        repasses = []
        for linha in planilha[8:-1]:
            tem_dados = 0
            for celula in linha:
                if celula:
                    tem_dados = 1
            if tem_dados:
                repasses.append([linha[c] for c in colunas])
        with open(f'planilhas/detalhada({i}).csv', 'w') as nova:
            writer = csv.writer(nova)
            writer.writerow(codigo)
            for r in repasses:
                writer.writerow(r)
            
            
                
with open('relatorio.csv', 'r', encoding='ISO-8859-1') as file:
    reader = csv.reader(file, delimiter=';')
    cidades = list(reader)
    for cidade in cidades:
        if cidade[0] == '31':
            municipio = RegTer(uf = cidade[0],
                               nome_uf = cidade[1],
                               regiao_geografica_intermediaria = cidade[2],
                               nome_regiao_geografica_intermediaria = cidade[3],
                               regiao_geografica_imediata = cidade[4],
                               nome_regiao_geografica_imediata = cidade[5],
                               mesorregiao_geografica = cidade[6],
                               nome_mesorregiao = cidade[7],
                               microrregiao_geografica = cidade[8],
                               nome_microrregiao = cidade[9],
                               municipio = cidade[10],
                               codigo_municipio_completo = cidade[11],
                               nome_municipio = cidade[12],
                               codigo_ibge = cidade[13])
            municipio.save()


for i in range(1, 101):
    file = f'planilhas/detalhada({i}).csv'
    with open(file, 'r') as planilha:
        reader = csv.reader(planilha)
        repasses = list(reader)
        for r in repasses[1::]:
            repasse = Repasses(
                codigo_ibge = RegTer.objects.get(codigo_ibge=repasses[0][0]),
                bloco = r[0],
                grupo = r[1],
                acao_detalhada = r[2],
                competencia_parcela = r[3],
                n_ob = r[4],
                data_ob = r[5],
                banco_ob = r[6],
                agencia_ob = r[7],
                conta_ob = r[8],
                valor_total = float(r[9].replace('.', '').replace(',', '.')),
                desconto = float(r[10].replace('.', '').replace(',', '.')),
                valor_liquido = float(r[11].replace('.', '').replace(',', '.')),
                observacao = r[12],
                processo = r[13],
                tipo = r[14],
                n_proposta = r[15]
            )
            repasse.save()


