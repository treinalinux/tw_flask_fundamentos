from flask import render_template
from app import app


@app.route('/home')
def home():
    """TODO: Docstring for home.
    :returns: TODO

    """
    return 'Feliz em te ver por aqui...'


@app.route('/opcional', defaults={'nome': None}, methods={'GET'})
@app.route('/opcional/<string:nome>')
def opcional(nome):
    """TODO: Docstring for opcional.
    :returns: TODO

    """
    if nome:
        return f'Seu nome é: {nome}'
    else:
        return 'Olá, tudo bem???'


@app.route('/teste', defaults={'nome': None}, methods={'GET'})
@app.route('/teste/<string:nome>')
def teste(nome):
    """TODO: Docstring for teste.

    :nome: TODO
    :returns: TODO

    """
    return render_template('/clientes/teste.html', nome_usuario=nome)
