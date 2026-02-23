from datetime import datetime

import data.dao as dao
import controllers.controller as controller
from models.model import Produtos, Vendas

# dao.DaoCategoria.salvar('Verduras')
# dao.DaoCategoria.salvar('Frutas')
# dao.DaoCategoria.salvar('Legumes')
# print(dao.DaoCategoria.ler())
# dao.DaoVendas.salvar(
#     Vendas(Produtos("Detergente", "5.00", "Limpeza"), "Juliano", "Maria", 2, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
# )
# print(dao.DaoVendas.ler()[-1].itemVendido.nome)

# controller.ControllerCategoria().cadastrar_categoria('Limpeza')
controller.ControllerCategoria().remover_categoria('limpeza')
