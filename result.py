from dataclasses import dataclass


@dataclass(init=False)
class Result:
    valor_total: str
    valor_entrega: str
    valor_pedido: str
    lanche_pedido: str
    restaurante: str
    local_entrega: str
    data_pedido: str
    pedido_concluido: bool

    @classmethod
    def selenium_to_result(
        cls,
        valor_total,
        valor_entrega,
        valor_pedido,
        lanche_pedido,
        restaurante,
        local_entrega,
        data_pedido,
        pedido_concluido
    ):
        _class = cls()
        _class.valor_total = valor_total.text.replace("R$ ", "").replace(",", ".")
        _class.valor_entrega = valor_entrega.text.replace("R$ ", "").replace(",", ".")
        _class.valor_pedido = valor_pedido.text.replace("R$ ", "").replace(",", ".")
        _class.lanche_pedido = lanche_pedido.text
        _class.restaurante = restaurante.text
        _class.local_entrega = local_entrega.text
        _class.data_pedido = data_pedido.text
        _class.pedido_concluido = True if pedido_concluido.text == "Concluído" else False

        return _class
