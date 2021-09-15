from app.models import cliente_model
from app import db


def listar_clientes():
    """TODO: Docstring for listar_clientes.
    :returns: TODO

    """
    clientes = cliente_model.Cliente.query.all()
    return clientes


def listar_cliente(id):
    """TODO: Docstring for listar_cliente.
    :returns: TODO

    """
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente


def casdastrar_cliente(cliente):
    """TODO: Docstring for casdastrar_cliente.
    :returns: TODO

    """
    db.session.add(cliente)
    db.session.commit()

    def editar_cliente(cliente_bd, cliente_novo):
        """TODO: Docstring for editar_cliente.
        :returns: TODO

        """
        cliente.nome = cliente_novo.nome
        cliente.email = cliente_novo.email
        cliente.data_nascimento = cliente_novo.data_nascimento
        cliente.profissao = cliente_novo.profissao
        cliente.sexo = cliente_novo.sexo
        db.session.commit()
