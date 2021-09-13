from app import app


@app.route('/home')
def home():
    """TODO: Docstring for home.
    :returns: TODO

    """
    return 'Feliz em te ver por aqui...'


@app.route('/opcional', defaults={'nome': None})
@app.route('/opcional/<string:nome>')
def opcional(nome):
    """TODO: Docstring for opcional.
    :returns: TODO

    """
    if nome:
        return f'Seu nome é: {nome}'
    else:
        return 'Olá, tudo bem???'
