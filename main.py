import pandas as pd
from selenium_tools.selenium_driver import SeleniumDriver


from pages.pages import LogarRedeSocial, Login, Endereco, Pedido, GastosIfood

driver = SeleniumDriver(log=False)

page_rede_social = LogarRedeSocial(driver)
page_endereco = Endereco(driver)
page_pedido = Pedido(driver)
page_gastos_ifood = GastosIfood(driver)


URL = "https://www.ifood.com.br/"

with Login(driver, url=URL) as login_page:
    login_page.logar.logar()
    page_rede_social.facebook.abrir_facebook()
    page_rede_social.facebook.logar_facebook()
    page_endereco.selecionar_endereco.primeiro_endereco()
    page_pedido.pedidos.abrir_menu_pedidos()
    page_pedido.pedidos.abrir_pedidos()
    links = page_pedido.pedidos.pegar_links()
    dados = page_gastos_ifood.pegar_dados.dados(links)
pd.DataFrame(dados).to_csv("result.csv", sep=";", index=False)