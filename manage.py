# from app.models import db
from app import create_app
from app.models import db


app = create_app(db)


if __name__ == '__main__':

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../todo.db'
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # host='0.0.0.0', port=8000, threaded=True
