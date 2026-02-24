from data.dao import *
from models.model import *
from datetime import datetime


class ControllerCategoria:

  def cadastrar_categoria(self, categoria, acao="cadastrada"):
    categoria = categoria.lower()
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
    categoria = categoria.lower()
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
      #TODO: Alterar categoria do estoque para "sem categoria"
      if delete:
        print(f"Categoria removida com sucesso!")
    

  def alterar_categoria(self, old_categoria, new_categoria):
    old_categoria = old_categoria.lower()
    new_categoria = new_categoria.lower()
    x = [i.categoria for i in DaoCategoria.ler()]

    cat_old = list(filter(lambda c: c == old_categoria, x))
    cat_new = list(filter(lambda c: c == new_categoria, x))

    if len(cat_old) > 0:
      if len(cat_new) == 0:
        x = list(map(lambda x: Categorias(new_categoria) if(x.categoria == old_categoria) else x, DaoCategoria.ler()))
        #TODO: Alterar categoria do estoque para "sem categoria"
      else:
        print("A nova categoria já existe")
        return
    else:
      print("A Categoria que busca nao existe ou ja foi removida")
      return
    self.remover_categoria(old_categoria, False)
    self.cadastrar_categoria(new_categoria, "alterada")

  def mostrar_categorias(self):
    categorias = DaoCategoria.ler()
    if len(categorias)==0:
      print("Não há categorias cadastradas")
    else:
      for i, cat in enumerate(categorias):
        print(f"{i+1} - {cat.categoria.capitalize()}")


class ControllerEstoque:
  def cadastrar_produto(self, nome, preco, categoria, quantidade):
    nome = nome.lower()
    categoria = categoria.lower()
    e = DaoEstoque.ler()
    c = DaoCategoria.ler()
    cat = list(filter(lambda c: c.categoria == categoria, c))
    est = list(filter(lambda e: e.produto.nome == nome, e))
    if len(cat) > 0:
      if len(est) == 0:
        produto = Produtos(nome, preco, categoria)
        DaoEstoque.salvar(produto, quantidade)
        print("Produto cadastrado com sucesso!")
        return
      else:
        print(f"Produto ja existe: {nome}") 
    else:
      print(f"Categoria informada nao existe: {categoria}")  
      return
     

