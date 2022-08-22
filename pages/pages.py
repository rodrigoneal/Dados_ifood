from selenium_tools import Page

from pages.elements import Facebook, Logar, SelecionarEndereco, Pedidos,PegarDados


class Login(Page):
    logar = Logar()


class LogarRedeSocial(Page):
    facebook = Facebook()


class Endereco(Page):
    selecionar_endereco = SelecionarEndereco()

class Pedido(Page):
    pedidos = Pedidos()

class GastosIfood(Page):
    pegar_dados = PegarDados()
