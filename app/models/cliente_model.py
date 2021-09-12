from app import db
from sqlalchemy_utils = import ChoiceType


class Cliente(db.Model):
    """Docstring for Cliente. """
    __table__ = 'clientes'

    SEXO_CHOICES = [
            (u'F', u'Feminino'),
            (u'M', u'Masculino'),
            (u'N', u'Nenhuma das opcões')

    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(200)), unique=True)
    data_nascimento = db.Column(db.DateTime)
    profissao = db.Column(db.String(30))
    sexo = db.Column(db.ChoiceType(SEXO_CHOICES))
