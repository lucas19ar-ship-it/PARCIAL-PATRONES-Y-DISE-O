from app.extensions import db

class Inventario(db.Model):
    __tablename__="inventarios"

    id = db.Column(db.Integer, primary_key=True)
    filial_id = db.Column(db.Integer, db.ForeignKey("filiales.id"), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)

    filial = db.relationship("Filial", back_populates="inventarios")
    producto = db.relationship("Producto", back_populates="inventarios")
    