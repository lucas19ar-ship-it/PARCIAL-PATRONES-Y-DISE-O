from app.extensions import db

class Filial(db.Model):
    __tablename__ = "filiales"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(60), nullable=False)
    moneda = db.Column(db.String(3), nullable=False)

    inventarios = db.relationship("Inventario", back_populates="filial")
    ventas = db.relationship("Venta", back_populates="filial")
     
