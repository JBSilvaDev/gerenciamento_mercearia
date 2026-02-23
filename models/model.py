from datetime import date, datetime

class Categorias:
  def __initi__(self, categoria):
    self.categoria = categoria

class Produtos:
  def __init__(self, nome, preco, categoria:Categorias):
    self.nome = nome
    self.preco = preco
    self.categoria = categoria

class Estoque:
  def __init__(self, produto:Produtos, quantidade):
    self.produto = produto
    self.quantidade = quantidade

class Vendas:
  def __init__(self, itemVendido:Produtos, vendedor, comprador, quantidade):
    self.produto = itemVendido
    self.quantidade = quantidade
    self.vendedor = vendedor
    self.comprador = comprador
    self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class Fornecedores:
  def __init__(self, nome, cnpj, contato, categoria:Categorias):
    self.nome = nome
    self.cnpj = cnpj
    self.contato = contato
    self.categoria = categoria


class Pessoa:
  def __init__(self, nome, contato, cpf, email, endereco):
    self.nome = nome
    self.contato = contato
    self.cpf = cpf
    self.email = email
    self.endereco = endereco

class Funcionario(Pessoa):
  def __init__(self, id_func, nome, contato, cpf, email, endereco):
    self.id_func = id_func
    super().__init__(nome, contato, cpf, email, endereco)