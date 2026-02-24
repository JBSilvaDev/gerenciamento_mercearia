from data.dao import *
from models.model import *
from datetime import datetime


class ControllerCategoria:

  def cadastrar_categoria(self, categoria, acao="cadastrada"):
    existe=False
    categorias = DaoCategoria.ler()
    for cat in categorias:
      if cat.categoria == categoria:
        existe=True
    if not existe:
      DaoCategoria.salvar(categoria)
      print(f"Categoria {acao} com sucesso!")
    else:
      print(f"Categoria já {acao}")

  def remover_categoria(self, categoria, delete=True):
    categoria_list_str = [i.categoria for i in DaoCategoria.ler()]
    cat = list(filter(lambda c: c == categoria, categoria_list_str))
    if len(cat) == 0:
      print("A Categoria que busca nao existe ou ja foi removida")
    else:
      for i in range(len(categoria_list_str)):
        if categoria_list_str[i] == categoria:
          del categoria_list_str[i]
          break
      DaoCategoria.remover(categoria_list_str)
      if delete:
        print(f"Categoria removida com sucesso!")
    

  def alterar_categoria(self, old_categoria, new_categoria):
    x = [i.categoria for i in DaoCategoria.ler()]

    cat_old = list(filter(lambda c: c == old_categoria, x))
    cat_new = list(filter(lambda c: c == new_categoria, x))

    if len(cat_old) > 0:
      if len(cat_new) == 0:
        x = list(map(lambda x: Categorias(new_categoria) if(x.categoria == old_categoria) else x, DaoCategoria.ler()))
      else:
        print("A nova categoria já existe")
        return
    else:
      print("A Categoria que busca nao existe ou ja foi removida")
      return
    self.remover_categoria(old_categoria, False)
    self.cadastrar_categoria(new_categoria, "alterada")



