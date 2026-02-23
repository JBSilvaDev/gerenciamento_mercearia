from data.dao import *
from models.model import *
from datetime import datetime


class ControllerCategoria:

  def cadastrar_categoria(self, categoria):
    existe=False
    categorias = DaoCategoria.ler()
    for cat in categorias:
      if cat.categoria.lower() == categoria.lower():
        existe=True
    if not existe:
      DaoCategoria.salvar(categoria)
      print("Categoria cadastrada com sucesso!")
    else:
      print("Categoria já cadastrada")

  def remover_categoria(self, categoria):
    x = [i.categoria.lower() for i in DaoCategoria.ler()]
    cat = list(filter(lambda c: c.lower() == categoria.lower(), x))
    if len(cat) == 0:
      print("A Categoria que busca nao existe ou ja foi removida")
    else:
      for i in range(len(x)):
        print(x[i])
        if x[i] == categoria:
          del x[i]
          break
      with open(os.path.join(path_data, "categorias.txt"), "w") as arq:
        for i in x:
          arq.writelines(f"{i}\n")
      print("Categoria removida com sucesso!")
    

    # for cat in categorias:
    #   if cat.categoria.lower() == categoria.lower():
    #     categorias.remove(cat)
    #     with open(os.path.join(path_data, "categorias.txt"), "w") as arq:
    #       for cat in categorias:
    #         arq.writelines(f"{cat.categoria}\n")
    #     print("Categoria removida com sucesso!")
    #     return
    # print("Categoria não encontrada")