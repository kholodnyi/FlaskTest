from flask import jsonify, request, abort

from ..models import db, ToDo, Task
from . import api


@api.route('/todo/<int:id>', methods=['GET'])
def get_todo(id):
    id = request.view_args.get('id')
    todo = ToDo.query.get_or_404(id)
    return jsonify(todo=[todo.serialize()])


@api.route('/task/<int:id>', methods=['GET'])
def get_task(id):
    id = request.view_args.get('id')
    task = Task.query.get_or_404(id)
    return jsonify(task=[task.serialize()])


@api.route('/task/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        id = request.view_args.get('id')
        task = Task.query.get_or_404(id)
        task.text = request.json.get('text')
        print(task.test)
        db.session.commit()
        # updated_task = Task.query.get_or_404(id)
        updated_task = Task.query.filter_by(text=task.text).first()
        return jsonify(user=updated_task.serialize())
    except:
        return abort(400)


@api.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    id = request.view_args.get('id')
    Task.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({}), 204


@api.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    id = request.view_args.get('id')
    ToDo.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({}), 204
