from alayatodo import app, db
from .models import Users, Todos
from flask import (
    g,
    redirect,
    render_template,
    request,
    session,
    jsonify,
    flash
)
from sqlalchemy import and_


@app.route('/')
def home():
    with app.open_resource('../README.md', mode='r') as f:
        readme = "".join(line for line in f)
        return render_template('index.html', readme=readme)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_POST():
    username = request.form.get('username')
    password = request.form.get('password')
    user = Users.query.filter(and_(Users.username == username, Users.password == password)).first()
    if user:
        session['user'] = user.to_dict()
        session['logged_in'] = True
        return redirect('/todo')

    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect('/')


@app.route('/todo/<id>', methods=['GET'])
def todo(id):
    _todo = Todos.query.filter(and_(Todos.id == id, Todos.user_id == session['user']['id'])).first()
    if _todo:
        return render_template('todo.html', todo=_todo)
    return redirect("/todo")


@app.route('/todo', methods=['GET'])
@app.route('/todo/', methods=['GET'])
def todos():
    if not session.get('logged_in'):
        return redirect('/login')
    _page = request.args.get("page", 1, type=int)
    _per_page = 10
    _todos_page = (Todos.query.filter(Todos.user_id == session['user']['id'])
                   .paginate(page=_page, per_page=_per_page, error_out=False))
    return render_template('todos.html', todos=_todos_page)


@app.route('/todo', methods=['POST'])
@app.route('/todo/', methods=['POST'])
def todos_POST():
    if not session.get('logged_in'):
        return redirect('/login')
    description = request.form.get('description', "").strip()

    if not description:
        return redirect('/todo')

    _todo = Todos(user_id=session['user']['id'], description=description)
    db.session.add(_todo)
    db.session.commit()
    flash(f"Todo '{_todo.description}' added successfully!", 'success')
    return redirect('/todo')


@app.route('/todo/<id>/deleted', methods=['POST'])
def todo_delete(id):
    if not session.get('logged_in'):
        return redirect('/login')
    _todo = Todos.query.filter(and_(Todos.id == id, Todos.user_id == session['user']['id'])).first()
    db.session.delete(_todo)
    db.session.commit()
    flash(f"Todo '{_todo.description}' deleted successfully!", "success")
    return redirect('/todo')


@app.route('/todo/<id>/completed', methods=['POST'])
def todo_completed(id):
    if not session.get('logged_in'):
        return redirect('/login')
    toggle_completed = 'checked'
    _todo = Todos.query.filter(and_(Todos.id == id, Todos.user_id == session['user']['id'])).first()
    if _todo.completed == "checked":
        toggle_completed = "unchecked"

    _todo.completed = toggle_completed
    db.session.commit()
    return redirect('/todo')


@app.route('/todo/<id>/json', methods=['GET'])
def todo_json(id):
    if not session.get('logged_in'):
        return redirect('/login')

    _todo = Todos.query.filter(and_(Todos.id == id, Todos.user_id == session['user']['id'])).first()
    data = {
        'error': 'Not Found!'
    }
    status_code = 404
    if _todo:
        data = {
            'id': _todo.id,
            'user_id': _todo.user_id,
            'description': _todo.description,
            'completed': _todo.completed
        }

        status_code = 200

    response = jsonify(data)
    response.status_code = status_code
    return response
