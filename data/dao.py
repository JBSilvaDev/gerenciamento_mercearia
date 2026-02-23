from models.model import *
import os

path_data = os.getcwd() + "/data/bd"
os.makedirs(path_data, exist_ok=True)


class DaoCategoria:

    @classmethod
    def salvar(cls, categoria):
        with open(os.path.join(path_data, "categorias.txt"), "a") as arq:
            arq.writelines(f"{categoria}\n")

    @classmethod
    def ler(cls):
        with open(os.path.join(path_data, "categorias.txt"), "r") as arq:
            cls.categoria = arq.readlines()
        # cls.categoria = [cat.strip('\n') for cat in cls.categoria]
        categoria = []
        for i in cls.categoria:
            i = i.replace(
                "\n", ""
            )  # Remove o caractere de nova linha, sem isso fica ['Bebidas\n', 'Verduras\n', 'Frutas\n', 'Legumes\n']
            categoria.append(Categorias(i))
        return categoria


class DaoVendas:

    @classmethod
    def salvar(cls, venda: Vendas):
        with open(os.path.join(path_data, "vendas.txt"), "a") as arq:
            arq.writelines(
                f"{venda.itemVendido.nome};{venda.itemVendido.preco};{venda.itemVendido.categoria};{venda.vendedor};{venda.comprador};{venda.data}\n"
            )

    @classmethod
    def ler(cls):
        with open(os.path.join(path_data, "vendas.txt"), "r") as arq:
            cls.venda = arq.readlines()
        cls.venda = [venda.strip("\n") for venda in cls.venda]  # Remove o \n
        cls.venda = [
            venda.split(";") for venda in cls.venda
        ]  # Separa os dados por ';' criando uma lista de listas
        venda = []
        for i in cls.venda:
            venda.append(Vendas(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5]))

        return venda


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantiddade):
        with open(os.path.join(path_data, "estoque.txt"), "a") as arq:
            arq.writelines(
                f"{produto.nome};{produto.preco};{produto.categoria};{quantiddade}\n"
            )

    @classmethod
    def ler(cls):
        with open(os.path.join(path_data, "estoque.txt"), "r") as arq:
            cls.estoque = arq.readlines()
        cls.estoque = [estoque.strip("\n") for estoque in cls.estoque]  # Remove o \n
        cls.estoque = [estoque.split(";") for estoque in cls.estoque]
        estoque = []
        if len(cls.estoque)>0:
          for i in cls.estoque:
              estoque.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return estoque
    
class DaoFornecedores:
    @classmethod
    def salvar(cls, fornecedor: Fornecedores):
        with open(os.path.join(path_data, "fornecedores.txt"), "a") as arq:
            arq.writelines(f"{fornecedor.nome};{fornecedor.cnpj};{fornecedor.contato};{fornecedor.categoria}\n")

    @classmethod
    def ler(cls):
        with open(os.path.join(path_data, "fornecedores.txt"), "r") as arq:
            cls.fornecedores = arq.readlines()
        cls.fornecedores = [fornecedor.strip("\n") for fornecedor in cls.fornecedores]  # Remove o \n
        cls.fornecedores = [fornecedor.split(";") for fornecedor in cls.fornecedores]
        fornecedores = []
        for i in cls.fornecedores:
            fornecedores.append(Fornecedores(i[0], i[1], i[2], i[3]))
        return fornecedores
    

class DaoPCliente:
    @classmethod
    def salvar(cls, p_cliente: Pessoa):
        with open(os.path.join(path_data, "p_cliente.txt"), "a") as arq:
            arq.writelines(f"{p_cliente.nome};{p_cliente.contato};{p_cliente.cpf};{p_cliente.email};{p_cliente.endereco}\n")

    @classmethod
    def ler(cls):
        with open(os.path.join(path_data, "p_cliente.txt"), "r") as arq:
            cls.p_cliente = arq.readlines()
        cls.p_cliente = [p_cliente.strip("\n") for p_cliente in cls.p_cliente]  # Remove o \n
        cls.p_cliente = [p_cliente.split(";") for p_cliente in cls.p_cliente]
        p_cliente = []
        for i in cls.p_cliente:
            p_cliente.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return p_cliente

class DaoPFuncionario:
    @classmethod
    def salvar(cls, p_funcionario: Funcionario):
        with open(os.path.join(path_data, "p_funcionario.txt"), "a") as arq:
            arq.writelines(f"{p_funcionario.id_func};{p_funcionario.nome};{p_funcionario.contato};{p_funcionario.cpf};{p_funcionario.email};{p_funcionario.endereco}\n")

    @classmethod
    def ler(cls):
        with open(os.path.join(path_data, "p_funcionario.txt"), "r") as arq:
            cls.p_funcionario = arq.readlines()
        cls.p_funcionario = [p_funcionario.strip("\n") for p_funcionario in cls.p_funcionario]  # Remove o \n
        cls.p_funcionario = [p_funcionario.split(";") for p_funcionario in cls.p_funcionario]
        p_funcionario = []
        for i in cls.p_funcionario:
            p_funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return p_funcionario

