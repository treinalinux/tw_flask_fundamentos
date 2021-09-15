from flask import render_template, redirect, url_for
from app.forms import cliente_form
from app import db

from app import app
from app.models import cliente_model


@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    """TODO: Docstring for cadastrar_cliente."""
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente = cliente_model.Cliente(
                nome=nome,
                email=email,
                data_nascimento=data_nascimento,
                profissao=profissao,
                sexo=sexo
        )

        try:
            db.session.add(cliente)
            db.session.commit()
            return redirect(url_for('listar_clientes'))
        except Exception as e:
            raise e

    return render_template('clientes/form.html', form=form)


@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    """TODO: Docstring for listar_clientes.
    :returns: TODO

    """
    clientes = cliente_model.Cliente.query.all()
    return render_template('clientes/lista_clientes.html', clientes=clientes)


@app.route('/listar_cliente/<int:id>')
def listar_cliente(id):
    """TODO: Docstring for listar_cliente.

    :id: TODO
    :returns: TODO

    """
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    
    return render_template('clientes/lista_cliente.html', cliente=cliente)
