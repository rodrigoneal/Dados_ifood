from time import sleep
from typing import List
from selenium_tools import Element
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

from result import Result

load_dotenv()

class Logar(Element):
    btn_login = (By.XPATH, "//section[1]/header/button[2]")

    def logar(self):
        self.find_element(self.btn_login).click()


class Facebook(Element):
    btn_facebook = (By.XPATH, "//div/div[2]/div/div[1]/div/button[1]")
    input_email = (By.ID, "email")
    input_pass = (By.ID, "pass")
    btn_entrar = (By.NAME, "login")

    def abrir_facebook(self):
        self.find_element(self.btn_facebook).click()

    def logar_facebook(self):
        self.change_window()
        dados_login = (
            (self.input_email, os.getenv("usuario")),
            (self.input_pass,  os.getenv("senha")),
        )
        for dado_login in dados_login:
            self.find_element(dado_login[0]).send_keys(dado_login[1])
        self.find_element(self.btn_entrar).click()


class SelecionarEndereco(Element):
    bnt_endereco = (By.XPATH, "//div[2]/div[2]/div[1]/button[1]")

    def primeiro_endereco(self):
        self.change_window(0)
        self.find_element(self.bnt_endereco).click()


class Pedidos(Element):
    btn_menu = (By.XPATH, "/html/body/div[1]/div[1]/header/div[3]/div/button")
    btn_pedidos = (By.PARTIAL_LINK_TEXT, "Pedidos")
    btn_todos_pedidos = (By.XPATH, "//div[1]/main/div/div[2]/div[2]/button")
    card_pedido = (By.CLASS_NAME, "order-card-finished__link")

    def abrir_menu_pedidos(self):
        elementos = (self.btn_menu, self.btn_pedidos)
        for elemento in elementos:
            self.find_element(elemento).click()

    def abrir_pedidos(self):
        while True:
            try:
                sleep(2)
                self.find_element(self.btn_todos_pedidos, time=1).click()
            except:
                break

    def pegar_links(self):
        links = [
            link.get_attribute("href") for link in self.find_elements(self.card_pedido)
        ]
        return links


class PegarDados(Element):
    valor_total = (By.XPATH, "//div[2]/div/section[1]/div[2]/p[3]/span[2]")
    valor_entrega = (By.XPATH, "//div/section[1]/div[2]/p[2]/span[2]")
    valor_pedido = (By.XPATH, "//div[2]/div/section[1]/div[2]/p[1]/span[2]")
    lanche_pedido = (By.XPATH, "//div[2]/div/section[1]/ul/li/div[1]/span[1]")
    restaurante = (By.XPATH, "//div[2]/div/section[1]/div[1]/h2")
    local_entrega = (By.XPATH, "//div[2]/div/section[2]/div[2]/p[1]")
    data_pedido = (By.XPATH, "//div[2]/div/section[3]/p[2]/span[2]")
    status_pedido = (By.XPATH, "//div[2]/div/section[3]/p[4]/span[2]")

    dados_list = []

    def _pegar_dados(self):
        valor_total = self.find_element(self.valor_total)
        valor_entrega = self.find_element(self.valor_entrega)
        valor_pedido = self.find_element(self.valor_pedido)
        lanche_pedido = self.find_element(self.lanche_pedido)
        restaurante = self.find_element(self.restaurante)
        local_entrega = self.find_element(self.local_entrega)
        data_pedido = self.find_element(self.data_pedido)
        status_pedido = self.find_element(self.status_pedido)
        return Result.selenium_to_result(
            valor_total,
            valor_entrega,
            valor_pedido,
            lanche_pedido,
            restaurante,
            local_entrega,
            data_pedido,
            status_pedido
        )

    def dados(self, links: List):
        links = set(links)
        for link in links:
            self.driver.get(link)
            dados = self._pegar_dados()
            print(dados)
            self.dados_list.append(dados)
        return self.dados_list
