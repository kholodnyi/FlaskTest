from flask import render_template, url_for, redirect, request

from . import site
from ..models import db, ToDo, Task


@site.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        if 'name' in request.form.keys():
            todo_name = request.form['name']
            new_todo = ToDo(name=todo_name)

            try:
                db.session.add(new_todo)
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue adding new TODO'

        elif 'text' in request.form.keys():
            task_text = request.form['text']
            todo_id = request.form['todo_id']
            completed = request.form['completed']
            new_task = Task(text=task_text, todo_id=todo_id, completed=completed)

            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue adding your task'

    else:
        todos = ToDo.query.order_by(ToDo.date_created).all()
        tasks = Task.query.order_by(Task.date_created).all()
        return render_template('site/index.html', todos=todos, tasks=tasks)


@site.route("/delete_todo/<int:id>", methods=['POST'])
def delete_todo(id):
    ToDo.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/')


@site.route("/delete_task/<int:id>", methods=['POST'])
def delete_task(id):
    Task.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/')


@site.route("/update_task/<int:id>", methods=['GET'])
def update_task(id):
    task = Task.query.get_or_404(id)
    db.session.commit()
    return render_template('site/task.html', task=task)


@site.route("/update_selected_task/<int:id>", methods=['POST'])
def update_selected_task(id):
    text = request.form['text']
    Task.query.filter_by(id=id).update(dict(text=text))
    db.session.commit()
    return redirect('/')


@site.route("/complete_task/<int:id>", methods=['POST'])
def complete_task(id):
    completed = request.form['completed']
    Task.query.filter_by(id=id).update(dict(completed=completed))
    db.session.commit()
    return redirect('/')


@site.route("/uncomplete_task/<int:id>", methods=['POST'])
def uncomplete_task(id):
    completed = request.form['completed']
    Task.query.filter_by(id=id).update(dict(completed=completed))
    db.session.commit()
    return redirect('/')


