from flask import Flask

from app.extensions import db
from app.models import Filial


def create_app():
    app = Flask(__name__)
    # TEMPORAL: en la Parte 4 esto pasará a la configuración Singleton
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///serf.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        if Filial.query.count() == 0:
            db.session.add_all([
                Filial(nombre="FinanCorp Peru", pais="Peru", moneda="PEN"),
                Filial(nombre="FinanCorp Espana", pais="Espana", moneda="EUR"),
            ])
            db.session.commit()

    @app.route("/")
    def home():
        return "SERF funcionando"

    # TEMPORAL: solo para probar la base de datos
    @app.route("/filiales")
    def filiales():
        return ", ".join(f.nombre for f in Filial.query.all())

    return app