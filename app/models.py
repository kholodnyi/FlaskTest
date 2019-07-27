from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='todo', lazy=True)

    def serialize(self):
        """
        Method used to serialize database objects into JSON

        :return: dict of ToDo object data
        """
        return {
            'id': self.id,
            'name': self.name,
            'date_created': self.date_created
        }

    def __repr__(self):
        return f'<TODO {self.id}>'


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.String(100), nullable=False)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'), nullable=False)

    def serialize(self):
        """
        Method used to serialize database objects into JSON

        :return: dict of Task object data
        """
        return {
            'id': self.id,
            'text': self.text,
            'date_created': self.date_created,
            'completed': self.completed,
            'todo_id': self.todo_id
        }

    def __repr__(self):
        return f'<Task {self.id}>'
