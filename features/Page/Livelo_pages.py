import asyncio
from features.Page.Base_page import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from unittest import *


class LiveloPage(Browser):

    def go_to_page(self):
        self.driver.get("https://www.livelo.com.br/")

    def procurar_elemento(self, name='Sanduicheira/Grill Lenoxx Cozinha Classic - 750W Antiaderente'):
        element_pesquisa = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'[id="search-container"]')))
        element_pesquisa.click()
        self.driver.find_element(By.ID, 'input-search').send_keys(name)
        self.driver.find_element(By.ID, 'span-searchIcon').click()
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, f'//div[@class="card-name"]/div[contains(text(), "{name}")]')))
        elemento = element.text
        if name.lower() == elemento.replace('"', '').lower():
            return True
        else:
            return False

    def colocar_elemento_carrinho(self, name='Sanduicheira/Grill Lenoxx Cozinha Classic - 750W Antiaderente'):
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, f'//div[@class="card-name"]/div[contains(text(), "{name}")]')))
        element.click()
        self.selecionar_opp()
        self.driver.find_element(By.ID, 'cc-prodDetails-addToCart').click()
        self.driver.find_element(By.ID, 'btn-authorizeCoookies').click()
        self.driver.find_element(By.ID, 'cc-prodDetails-refusePriceClubeDiscount').click()
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, f'ctaCheckout')))

    def selecionar_Produto(self, name):
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, f'//div[@class="card-name"]/div[contains(text(), "{name}")]')))
        element.click()

    def adicionar_elemento_ao_carrinho(self):
        try:
            addcart = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable(
                    (By.ID, 'cc-prodDetails-addToCart')))
            addcart.click()

            self.driver.find_element(By.ID, 'btn-authorizeCoookies').click()
            recusar = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable(
                    (By.ID, 'cc-prodDetails-refusePriceClubeDiscount')))
            recusar.click()

            element = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, f'ctaCheckout')))
        except:
            self.driver.find_element(By.ID, 'cc-prodDetails-refusePriceClubeDiscount').click()

            element = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, f'ctaCheckout')))

    def selecionar_opp(self, vol='220v', cor='NA'):
        volt = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, 'CC-prodDetails-sku-type_other_v_voltage')))

        volt = Select(volt)
        volt.select_by_visible_text(vol)

        if cor != 'NA':
            Cor = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, 'CC-prodDetails-sku-type_other_v_color')))
            Cor = Select(Cor)
            Cor.select_by_visible_text(cor)

    def verificar_elemento_carrinho(self, name='Grill e Sanduicheira Lenoxx Classic 750W 220V'):
        self.go_to_page()
        carrinho = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, 'a-linkCart')))
        carrinho.click()
        for produtos in name.split(','):
            element = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, f'//a[contains(text(), "{produtos}")]')))
            elemento = element.text
            if produtos.lower() == elemento.replace('"', '').lower():
                return True
            else:
                return False

    def somar_elemento(self, QTD):
        X = 1
        QTD = int(QTD)
        if QTD == 1:
            return True
        else:
            while (QTD > X):
                espera = WebDriverWait(self.driver, 60).until(
                    EC.invisibility_of_element_located((By.XPATH,
                                                        '/html/body/div[4]')))
                soma = WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/main/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/span[3]')))
                soma.click()
                espera = WebDriverWait(self.driver, 60).until(
                    EC.invisibility_of_element_located((By.XPATH,
                                                        '/html/body/div[4]')))
                print(X)
                X += 1

    def verificar_QTD(self, QTD):
        espera = WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH,
                                                '/html/body/div[4]')))
        valor = self.driver.find_element(By.CLASS_NAME, 'cart-list__value-qnt').text
        print(valor)
        if int(QTD) == int(valor):
            return True
        else:
            return False
