from datetime import datetime

import data.dao as dao
import controllers.controller as controller
from models.model import Produtos, Vendas

# dao.DaoCategoria.salvar('Verduras')
# dao.DaoCategoria.salvar('Frutas')
# dao.DaoCategoria.salvar('legumes')
# print(dao.DaoCategoria.ler())
# dao.DaoVendas.salvar(
#     Vendas(Produtos("Detergente", "5.00", "Limpeza"), "Juliano", "Maria", 2, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
# )
# print(dao.DaoVendas.ler()[-1].itemVendido.nome)

# controller.ControllerCategoria().cadastrar_categoria('Verduras')
# controller.ControllerCategoria().remover_categoria('vegerais')
# controller.ControllerCategoria().alterar_categoria('drinksx', 'bebidas')
# controller.ControllerCategoria().mostrar_categorias()
# controller.ControllerEstoque().cadastrar_produto('Sabao em barra', '5.00', 'Limpeza', 30)
# controller.ControllerEstoque().remover_produto('Sabao em barra')
controller.ControllerEstoque().alterar_produto('Sabao em barras', 'Batata', '3', 'Verduras', 15)
