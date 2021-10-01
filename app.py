from flask import Flask
from flask_cors import CORS
from route_aluno import app_bp_alunos
from route_professor import app_bp_professor
from route_endereco import app_bp_endereco
from route_projeto import app_bp_projeto

app = Flask(__name__)
CORS(app)

app.register_blueprint(app_bp_alunos, url_prefix='/alunos')
app.register_blueprint(app_bp_professor, url_prefix='/professor')
app.register_blueprint(app_bp_endereco, url_prefix='/endereco')
app.register_blueprint(app_bp_projeto, url_prefix='/projeto')
