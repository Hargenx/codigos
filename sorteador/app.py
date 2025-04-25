from flask import Flask, request, jsonify, render_template
import sqlite3
import random
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
DB_PATH = 'banco.db'

# Inicializa o banco
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS turmas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT UNIQUE NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS grupos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        turma_id INTEGER,
                        nome TEXT,
                        alunos TEXT,
                        tema TEXT,
                        FOREIGN KEY(turma_id) REFERENCES turmas(id))''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT nome FROM turmas")
        turmas = [row[0] for row in c.fetchall()]
    return jsonify(turmas)

@app.route('/criar_turma', methods=['POST'])
def criar_turma():
    nome = request.json.get('nome')
    try:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO turmas (nome) VALUES (?)", (nome,))
            conn.commit()
        return jsonify({'mensagem': f'Turma {nome} criada com sucesso'})
    except sqlite3.IntegrityError:
        return jsonify({'erro': 'Turma já existe'}), 400

@app.route('/adicionar_grupo', methods=['POST'])
def adicionar_grupo():
    turma_nome = request.json.get('turma')
    alunos = request.json.get('alunos')

    if not (1 <= len(alunos) <= 5):
        return jsonify({'erro': 'Um grupo deve conter entre 1 e 5 alunos'}), 400

    TEMAS_COMPLETOS = [
        "Sistema de Gerenciamento de Clientes de Barbearia",
        "Sistema de Controle de Agendamentos de Clínica Estética",
        "Sistema de Gerenciamento de Produtos em uma Papelaria",
        "Sistema de Controle de Serviços de um Mecânico",
        "Sistema de Gestão de Reservas de uma Pousada",
        "Sistema de Controle de Aluguéis de Equipamentos de Som",
        "Sistema de Cadastro e Controle de Eventos Corporativos",
        "Sistema de Gestão de Pacientes de um Consultório de Fisioterapia",
        "Sistema de Controle de Pedidos em uma Loja de Roupas",
        "Sistema de Agendamento de Aulas Particulares",
        "Sistema de Gerenciamento de Alunos de um Curso Livre",
        "Sistema de Cadastro de Trabalhos Acadêmicos de uma Faculdade",
        "Sistema de Controle de Empréstimo de Materiais em um Laboratório Escolar",
        "Sistema de Cadastro de Professores Substitutos",
        "Sistema de Gestão de Certificados de Participação em Palestras",
        "Sistema de Avaliação de Cursos por Alunos",
        "Sistema de Gerenciamento de Visitas Técnicas de uma Escola Técnica",
        "Sistema de Controle de Monitorias Universitárias",
        "Sistema de Gestão de Frequência em Cursos Extracurriculares",
        "Sistema de Controle de Projetos de Extensão Universitária",
        "Sistema de Controle de Pedidos de uma Lanchonete",
        "Sistema de Gerenciamento de Cardápios de uma Cantina Escolar",
        "Sistema de Cadastro de Fornecedores de uma Cozinha Industrial",
        "Sistema de Controle de Estoque de Ingredientes em um Food Truck",
        "Sistema de Gestão de Reservas em um Restaurante Temático",
        "Sistema de Cadastro de Clientes de uma Pet Shop",
        "Sistema de Controle de Consultas de um Terapeuta Holístico",
        "Sistema de Agendamento de Serviços de um Salão de Beleza",
        "Sistema de Controle de Clientes de uma Empresa de Limpeza",
        "Sistema de Controle de Orçamentos de uma Marcenaria",
        "Sistema de Cadastro de Membros de uma Associação de Bairro",
        "Sistema de Controle de Doações de uma ONG",
        "Sistema de Gerenciamento de Atividades de um Projeto Social",
        "Sistema de Emissão de Carteirinhas para Clube de Vizinhança",
        "Sistema de Gerenciamento de Atendimentos de um CRAS Simulado",
        "Sistema de Controle de Documentos de um Arquivo Pessoal",
        "Sistema de Gestão de Processos Administrativos Internos",
        "Sistema de Cadastro de Obras de Autores Independentes",
        "Sistema de Controle de Currículos em uma Agência de Empregos",
        "Sistema de Registro de Ocorrências em um Condomínio"
    ]

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM turmas WHERE nome = ?", (turma_nome,))
        turma = c.fetchone()
        if not turma:
            return jsonify({'erro': 'Turma não encontrada'}), 404

        turma_id = turma[0]
        c.execute("SELECT tema FROM grupos WHERE turma_id = ?", (turma_id,))
        temas_sorteados = [row[0] for row in c.fetchall()]
        temas_restantes = list(set(TEMAS_COMPLETOS) - set(temas_sorteados))

        if not temas_restantes:
            return jsonify({'erro': 'Todos os temas já foram sorteados para essa turma'}), 400

        tema_sorteado = random.choice(temas_restantes)
        grupo_nome = f"Grupo {len(temas_sorteados) + 1}"
        alunos_str = ", ".join(alunos)
        c.execute("INSERT INTO grupos (turma_id, nome, alunos, tema) VALUES (?, ?, ?, ?)",
                  (turma_id, grupo_nome, alunos_str, tema_sorteado))
        conn.commit()

    return jsonify({'mensagem': f'{grupo_nome} criado com sucesso!', 'tema': tema_sorteado})

@app.route('/turma/<nome>', methods=['GET'])
def ver_grupos(nome):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM turmas WHERE nome = ?", (nome,))
        turma = c.fetchone()
        if not turma:
            return jsonify({'erro': 'Turma não encontrada'}), 404
        turma_id = turma[0]
        c.execute("SELECT nome, alunos, tema FROM grupos WHERE turma_id = ?", (turma_id,))
        grupos = [
            {'nome': row[0], 'alunos': row[1].split(", "), 'tema': row[2]}
            for row in c.fetchall()
        ]
    return jsonify({'grupos': grupos})

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    init_db()
    app.run(debug=True)