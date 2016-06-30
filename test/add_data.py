import sys
import os

# Obtenha o diretório do arquivo atual (onde add_data.py está localizado)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtenha o diretório raiz do projeto (subindo um nível)
project_dir = os.path.dirname(current_dir)

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(project_dir)


def start_db():
    from alayatodo import db, app
    from alayatodo.models import Users, Todos

    with app.app_context():
        users = [
            Users(username='user1', password='user1'),
            Users(username='user2', password='user2'),
            Users(username='user3', password='user3')
        ]

        for u in users:
            db.session.add(u)
            db.session.commit()

        todos = [
            Todos(user_id=1, description='Vivamus tempus'),
            Todos(user_id=1, description='lorem ac odio'),
            Todos(user_id=1, description='Ut congue odio'),
            Todos(user_id=1, description='Sodales finibus'),
            Todos(user_id=1, description='Accumsan nunc vitae'),
            Todos(user_id=2, description='Lorem ipsum'),
            Todos(user_id=2, description='In lacinia est'),
            Todos(user_id=2, description='Odio varius gravida')
        ]

        for t in todos:
            db.session.add(t)
            db.session.commit()
