# Estrutura MVC (Python com Flask e SQLite/SQLAlchemy)
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sistema.db'
db = SQLAlchemy(app)

# MODEL (Modelo de Dados)
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(150), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pendente')

with app.app_context():
    db.create_all()

# CONTROLLER / ROUTES (Controlador)
@app.route('/')
def index():
    pedidos = Pedido.query.all()
    return render_template('index.html', pedidos=pedidos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form['descricao']
    valor = float(request.form['valor'])
    novo_pedido = Pedido(descricao=descricao, valor=valor)
    db.session.add(novo_pedido)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
